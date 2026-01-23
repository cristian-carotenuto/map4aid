"""
Script per il fine-tuning di Qwen 2.5-3B usando QLoRA.
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
from datasets import load_dataset
import os

def train():
    model_name = "Qwen/Qwen2.5-3B-Instruct"
    
    # Percorso robusto relativo alla posizione dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, "../../data/training_data_expanded.jsonl")
    
    # Se il file espanso non esiste, usa quello base
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join(script_dir, "../../data/training_data.jsonl")
    
    print(f">> Dataset utilizzato: {dataset_path}")
    print(f">> Inizio preparazione per il fine-tuning di {model_name}")

    # 1. Configurazione Quantizzazione (4-bit per risparmiare VRAM)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # 2. Caricamento Modello e Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.float16,
    )

    # 3. Preparazione per PEFT (QLoRA)
    model = prepare_model_for_kbit_training(model)
    
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"], # Layer Qwen specifici
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = get_peft_model(model, lora_config)

    # 4. Caricamento Dataset
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    # 5. Argomenti di Addestramento
    training_args = TrainingArguments(
        output_dir="./qwen-aidano-checkpoints",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        max_steps=100, # Numero di step per un test veloce
        logging_steps=10,
        fp16=True,
        save_strategy="steps",
        save_steps=50,
        report_to="none", # Disabilita wandb/tensorboard per semplicità
    )

    # 6. Funzione di Formattazione (per convertire i messaggi in stringhe tramite chat template)
    def formatting_prompts_func(example):
        output_texts = []
        for i in range(len(example['messages'])):
            messages = example['messages'][i]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
            output_texts.append(text)
        return output_texts

    # 7. Trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        max_seq_length=512,
        tokenizer=tokenizer,
        args=training_args,
        formatting_func=formatting_prompts_func,
    )

    print(">> Avvio addestramento...")
    trainer.train()

    # 8. Salvataggio
    model.save_pretrained("./qwen-aidano-final")
    print("[OK] Fine-tuning completato e modello salvato!")

if __name__ == "__main__":
    train()
