"""
Fine-tuning Qwen 2.5-3B con QLoRA "a tranche" SENZA resume dei checkpoint Trainer.

Obiettivo: evitare il resume (optimizer/scheduler .pt) che richiede torch>=2.6 (CVE torch.load).
Strategia:
- Ogni run fa +STEP_PER_RUN step.
- A fine run salva SOLO l'adapter LoRA in una cartella incrementale (stage-00025, stage-00050, ...).
- Alla run successiva, carica base model + ultimo adapter e continua (optimizer reset, ma i pesi LoRA restano).
- Logging ogni LOG_EVERY_STEPS step.
- Riduce warning principali dove possibile.
"""

import os
import re
import warnings
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    PeftModel,
)
from trl import SFTTrainer
from datasets import load_dataset


# =========================
# CONFIG
# =========================
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

# Tranche
STEP_PER_RUN = 25          # 25 step per run
TARGET_TOTAL_STEPS = 100   # obiettivo totale
LOG_EVERY_STEPS = 5

# Salvataggi adapter
ADAPTERS_DIR = "./qwen-aidano-adapters"   # stage-00025, stage-00050, ...
FINAL_DIR = "./qwen-aidano-final"         # ultimo adapter “finale”

# Training
MAX_SEQ_LEN = 320
BATCH_SIZE = 1
GRAD_ACCUM = 4
LR = 2e-4


def _find_last_stage_steps(adapters_dir: str) -> int:
    """
    Cerca la cartella stage-XXXXX più recente e restituisce XXXXX come int.
    Se non esiste, ritorna 0.
    """
    if not os.path.isdir(adapters_dir):
        return 0

    pat = re.compile(r"^stage-(\d{5})$")
    last = 0
    for name in os.listdir(adapters_dir):
        m = pat.match(name)
        if m:
            steps = int(m.group(1))
            last = max(last, steps)
    return last


def _stage_path(adapters_dir: str, steps: int) -> str:
    return os.path.join(adapters_dir, f"stage-{steps:05d}")


def train():
    # Riduci warning verbosi non utili (non nasconde errori reali)
    warnings.filterwarnings("ignore", message="`tokenizer` is deprecated")
    warnings.filterwarnings("ignore", message="`torch_dtype` is deprecated")
    warnings.filterwarnings("ignore", message="The tokenizer has new PAD/BOS/EOS tokens")

    # Percorso dataset robusto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, "../../data/training_data_expanded.jsonl")

    if not os.path.exists(dataset_path):
        print(f"!! [ERRORE] Dataset non trovato: {dataset_path}")
        print("!! Lancia prima: python ../../data/dataset_generator.py")
        return

    os.makedirs(ADAPTERS_DIR, exist_ok=True)

    # Calcola da dove ripartire (in termini di "step totali" target)
    last_total_steps = _find_last_stage_steps(ADAPTERS_DIR)

    if last_total_steps >= TARGET_TOTAL_STEPS:
        print(f">> Hai già raggiunto {last_total_steps} step (>= {TARGET_TOTAL_STEPS}).")
        print(f">> Ultimo adapter: {_stage_path(ADAPTERS_DIR, last_total_steps)}")
        print(f">> Se vuoi, copia quello in {FINAL_DIR} oppure usa direttamente lo stage.")
        return

    next_total_steps = min(last_total_steps + STEP_PER_RUN, TARGET_TOTAL_STEPS)
    steps_this_run = next_total_steps - last_total_steps

    print(f">> Dataset utilizzato: {dataset_path}")
    if last_total_steps == 0:
        print(f">> Nessun adapter precedente. Avvio da base model e farò {steps_this_run} step (totale {next_total_steps}).")
    else:
        print(f">> Trovato adapter: {_stage_path(ADAPTERS_DIR, last_total_steps)}")
        print(f">> Carico base+adapter e farò altri {steps_this_run} step (totale {next_total_steps}).")

    # =========================
    # Quantizzazione 4-bit
    # =========================
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Modello base (usa dtype invece di torch_dtype)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        dtype=torch.float16,
    )

    # Evita warning/use_cache incompatibile con gradient checkpointing
    model.config.use_cache = False

    # Preparazione QLoRA
    model = prepare_model_for_kbit_training(model)

    # Config LoRA
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # =========================
    # Adapter: crea o carica
    # =========================
    stage_path = _stage_path(ADAPTERS_DIR, last_total_steps)

    if last_total_steps == 0:
        # Prima tranche: crea adapter
        model = get_peft_model(model, lora_config)
    else:
        # Tranche successive: carica adapter ESISTENTE (evita "multiple adapters")
        model = PeftModel.from_pretrained(model, stage_path, is_trainable=True)

    # =========================
    # Dataset
    # =========================
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    def formatting_prompts_func(example):
        output_texts = []
        for i in range(len(example["messages"])):
            messages = example["messages"][i]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
            output_texts.append(text)
        return output_texts

    # =========================
    # TrainingArguments
    # =========================
    training_args = TrainingArguments(
        output_dir="./tmp-trainer-output",     # non usato per resume
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        max_steps=steps_this_run,              # step SOLO di questa run
        logging_steps=LOG_EVERY_STEPS,
        fp16=True,
        save_strategy="no",                    # niente checkpoint trainer (evita torch.load al resume)
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        # peft_config qui va bene anche se model è già PeftModel: non crea adapter nuovi
        peft_config=lora_config,
        max_seq_length=MAX_SEQ_LEN,
        tokenizer=tokenizer,
        args=training_args,
        formatting_func=formatting_prompts_func,
    )

    print(">> Avvio addestramento...")
    trainer.train()

    # =========================
    # Salvataggio adapter "stage-XXXXX"
    # =========================
    stage_out = _stage_path(ADAPTERS_DIR, next_total_steps)
    os.makedirs(stage_out, exist_ok=True)
    model.save_pretrained(stage_out)
    print(f"[OK] Tranche completata. Adapter salvato in: {stage_out}")

    # Se abbiamo raggiunto il target, salva anche in FINAL_DIR
    if next_total_steps >= TARGET_TOTAL_STEPS:
        os.makedirs(FINAL_DIR, exist_ok=True)
        model.save_pretrained(FINAL_DIR)
        print(f"[OK] Target raggiunto ({next_total_steps} step). Adapter finale salvato in: {FINAL_DIR}")
    else:
        print(f">> Quando vuoi continuare, rilancia lo script: farà altri {STEP_PER_RUN} step (fino a {TARGET_TOTAL_STEPS}).")


if __name__ == "__main__":
    train()
