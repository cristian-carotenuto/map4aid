import os
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
from rich.console import Console

console = Console()

def train():
    model_id = "Qwen/Qwen2.5-3B-Instruct"
    dataset_path = "chatbot/data/training_data.jsonl"
    output_dir = "chatbot/model/training/qwen-aidano-final"

    console.print(f"[bold blue]>> Inizio Fine-Tuning di {model_id}[/bold blue]")

    # 1. Carica Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # 2. Configurazione Quantizzazione (4-bit)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # 3. Carica Modello
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )
    model = prepare_model_for_kbit_training(model)

    # 4. Configurazione LoRA
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)

    # 5. Carica Dataset
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    def formatting_func(example):
        """Formatta i messaggi usando il template di Qwen."""
        text = tokenizer.apply_chat_template(example["messages"], tokenize=False, add_generation_prompt=False)
        return {"text": text}

    formatted_dataset = dataset.map(formatting_func)

    # 6. Argomenti di Training
    training_args = TrainingArguments(
        output_dir="chatbot/model/training/qwen-aidano-checkpoints",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        max_steps=100, # Per test rapido
        logging_steps=10,
        save_strategy="no",
        fp16=True,
        push_to_hub=False,
        report_to="none"
    )

    # 7. Trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=formatted_dataset,
        dataset_text_field="text",
        max_seq_length=512,
        args=training_args,
        peft_config=peft_config,
    )

    # 8. Avvio Training
    console.print("[bold green]>> Training in corso...[/bold green]")
    trainer.train()

    # 9. Salvataggio
    console.print(f"[bold blue]>> Salvataggio modello in {output_dir}[/bold blue]")
    trainer.model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    console.print("[bold green]>> Fine-Tuning completato![/bold green]")

if __name__ == "__main__":
    train()
