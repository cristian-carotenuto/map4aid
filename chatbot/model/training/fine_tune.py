"""
Fine-tuning Qwen 2.5-3B con QLoRA "a tranche" (25 step per run),
MA con 2 fasi nello stesso run:
1) Intent classification (label-only)
2) Answerable classification (label-only)

Obiettivo:
- Addestrare SOLO il riconoscimento (etichette), non la generazione di risposte.
- Salvare un SOLO adapter per run (stage-00025, stage-00050, ...).
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
STEP_PER_RUN = 26
TARGET_TOTAL_STEPS = 104
LOG_EVERY_STEPS = 4

# Split per run: devono sommare a STEP_PER_RUN
INTENT_STEPS = 13
ANSWERABLE_STEPS = 13

# Salvataggi adapter
ADAPTERS_DIR = "./qwen-aidano-adapters"   # stage-00025, stage-00050, ...
FINAL_DIR = "./qwen-aidano-final"

# Dataset (devono essere generati dal tuo dataset_generator)
INTENT_DATASET_NAME = "training_intent.jsonl"
ANSWERABLE_DATASET_NAME = "training_answerable.jsonl"

# Training
MAX_SEQ_LEN = 256
BATCH_SIZE = 1
GRAD_ACCUM = 4
LR = 2e-4


def _find_last_stage_steps(adapters_dir: str) -> int:
    if not os.path.isdir(adapters_dir):
        return 0
    pat = re.compile(r"^stage-(\d{5})$")
    last = 0
    for name in os.listdir(adapters_dir):
        m = pat.match(name)
        if m:
            last = max(last, int(m.group(1)))
    return last


def _stage_path(adapters_dir: str, steps: int) -> str:
    return os.path.join(adapters_dir, f"stage-{steps:05d}")


def _load_jsonl_dataset(dataset_path: str):
    return load_dataset("json", data_files=dataset_path, split="train")


def train_phase(model, tokenizer, dataset, max_steps: int):
    """
    Esegue una fase di training (max_steps) sul dataset passato.
    Ritorna il modello aggiornato (stesso oggetto, ma per chiarezza lo ritorniamo).
    """
    def formatting_prompts_func(example):
        output_texts = []
        for i in range(len(example["messages"])):
            messages = example["messages"][i]
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            output_texts.append(text)
        return output_texts

    training_args = TrainingArguments(
        output_dir="./tmp-trainer-output",
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        max_steps=max_steps,
        logging_steps=LOG_EVERY_STEPS,
        fp16=True,
        save_strategy="no",
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        # ok anche se model è già PeftModel
        peft_config=None,
        max_seq_length=MAX_SEQ_LEN,
        tokenizer=tokenizer,
        args=training_args,
        formatting_func=formatting_prompts_func,
    )

    trainer.train()
    return model


def train():
    if INTENT_STEPS + ANSWERABLE_STEPS != STEP_PER_RUN:
        print("!! [ERRORE] INTENT_STEPS + ANSWERABLE_STEPS deve essere = STEP_PER_RUN")
        return

    warnings.filterwarnings("ignore", message="`tokenizer` is deprecated")
    warnings.filterwarnings("ignore", message="`torch_dtype` is deprecated")
    warnings.filterwarnings("ignore", message="The tokenizer has new PAD/BOS/EOS tokens")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "../../data")

    intent_path = os.path.join(data_dir, INTENT_DATASET_NAME)
    answerable_path = os.path.join(data_dir, ANSWERABLE_DATASET_NAME)

    if not os.path.exists(intent_path):
        print(f"!! [ERRORE] Dataset intent non trovato: {intent_path}")
        print("!! Assicurati che dataset_generator produca training_intent.jsonl")
        return

    if not os.path.exists(answerable_path):
        print(f"!! [ERRORE] Dataset answerable non trovato: {answerable_path}")
        print("!! Assicurati che dataset_generator produca training_answerable.jsonl")
        return

    os.makedirs(ADAPTERS_DIR, exist_ok=True)

    last_total_steps = _find_last_stage_steps(ADAPTERS_DIR)
    if last_total_steps >= TARGET_TOTAL_STEPS:
        print(f">> Hai già raggiunto {last_total_steps} step (>= {TARGET_TOTAL_STEPS}).")
        print(f">> Ultimo adapter: {_stage_path(ADAPTERS_DIR, last_total_steps)}")
        return

    next_total_steps = min(last_total_steps + STEP_PER_RUN, TARGET_TOTAL_STEPS)
    steps_this_run = next_total_steps - last_total_steps

    # se l’ultimo run è “parziale” (quando TARGET_TOTAL_STEPS non è multiplo di STEP_PER_RUN)
    # ridistribuiamo mantenendo priorità su intent
    intent_steps = min(INTENT_STEPS, steps_this_run)
    answerable_steps = max(0, steps_this_run - intent_steps)

    print(f">> Dataset intent:      {intent_path}")
    print(f">> Dataset answerable:  {answerable_path}")
    if last_total_steps == 0:
        print(f">> Nessun adapter precedente. Avvio da base model e farò {steps_this_run} step (Intent {intent_steps} + Answerable {answerable_steps}) (totale {next_total_steps}).")
    else:
        print(f">> Trovato adapter: {_stage_path(ADAPTERS_DIR, last_total_steps)}")
        print(f">> Carico base+adapter e farò altri {steps_this_run} step (Intent {intent_steps} + Answerable {answerable_steps}) (totale {next_total_steps}).")

    # =========================
    # Quantizzazione 4-bit
    # =========================
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.float16
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    stage_path = _stage_path(ADAPTERS_DIR, last_total_steps)
    if last_total_steps == 0:
        model = get_peft_model(model, lora_config)
    else:
        model = PeftModel.from_pretrained(model, stage_path, is_trainable=True)

    # =========================
    # Dataset load
    # =========================
    intent_ds = _load_jsonl_dataset(intent_path)
    answerable_ds = _load_jsonl_dataset(answerable_path)

    # =========================
    # Phase 1: intent
    # =========================
    if intent_steps > 0:
        print(f">> Phase 1/2: Intent training ({intent_steps} step)...")
        model = train_phase(model, tokenizer, intent_ds, intent_steps)

    # =========================
    # Phase 2: answerable
    # =========================
    if answerable_steps > 0:
        print(f">> Phase 2/2: Answerable training ({answerable_steps} step)...")
        model = train_phase(model, tokenizer, answerable_ds, answerable_steps)

    # =========================
    # Salvataggio adapter "stage-XXXXX"
    # =========================
    stage_out = _stage_path(ADAPTERS_DIR, next_total_steps)
    os.makedirs(stage_out, exist_ok=True)
    model.save_pretrained(stage_out)
    print(f"[OK] Run completata. Adapter salvato in: {stage_out}")

    if next_total_steps >= TARGET_TOTAL_STEPS:
        os.makedirs(FINAL_DIR, exist_ok=True)
        model.save_pretrained(FINAL_DIR)
        print(f"[OK] Target raggiunto ({next_total_steps} step). Adapter finale salvato in: {FINAL_DIR}")
    else:
        print(f">> Rilancia lo script quando vuoi: farà altri {STEP_PER_RUN} step (fino a {TARGET_TOTAL_STEPS}).")


if __name__ == "__main__":
    train()
