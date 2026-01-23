"""
Client per l'inferenza con QWEN 2.5-3B.
Questo modulo gestisce il caricamento del modello, la memoria della conversazione
e la consapevolezza temporale.
"""

import os
import torch
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class QwenClient:
    """Client per interagire con il modello QWEN."""
    
    def __init__(self, model_name="Qwen/Qwen2.5-3B-Instruct", use_adapters=True):
        """
        Inizializza il client QWEN.
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.history = []
        self.use_adapters = use_adapters
        
    def _get_system_info(self):
        # ... (stesso codice di prima)
        now = datetime.now()
        data = now.strftime("%d/%m/%Y")
        ora = now.strftime("%H:%M:%S")
        giorni = {
            "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
            "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
        }
        giorno_settimana = giorni.get(now.strftime("%A"), now.strftime("%A"))
        return f"Oggi è {giorno_settimana}, {data}. L'ora attuale è {ora}."

    def load_model(self):
        """Carica il modello e opzionalmente gli adapter."""
        print(f">> Caricamento modello {self.model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        
        # Sincronizzazione pad token come fatto nel training
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=True
        )
        
        if self.use_adapters:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            adapter_path = os.path.join(script_dir, "../training/qwen-aidano-final")
            if os.path.exists(adapter_path):
                from peft import PeftModel
                print(f">> Caricamento adapter personalizzati Aidano da: {adapter_path}")
                self.model = PeftModel.from_pretrained(self.model, adapter_path)
            else:
                print(">> Nessun adapter trovato.")
        else:
            print(">> Utilizzo modello base (adapter disabilitati).")
            
        print("[OK] Modello pronto!")

    def generate_response(self, prompt, max_length=512, temperature=0.7):
        if self.model is None:
            raise RuntimeError("Modello non caricato.")
        
        # 1. System Prompt più bilanciato (Conversazionale + Esperto)
        system_info = self._get_system_info()
        system_prompt = (
            "Sei Aidano, l'assistente virtuale di Map4Aid. Sei un assistente gentile, utile e preparato. "
            "Il tuo compito è rispondere alle domande degli utenti sulla piattaforma Map4Aid utilizzando la tua conoscenza specifica, "
            "ma sei anche un assistente conversazionale: tieni traccia di quanto detto in chat per rispondere in modo coerente. "
            f"Informazioni attuali: {system_info}"
        )
        
        # 2. Gestione History
        if not self.history:
            self.history.append({"role": "system", "content": system_prompt})
        else:
            self.history[0] = {"role": "system", "content": system_prompt}
            
        self.history.append({"role": "user", "content": prompt})
        if len(self.history) > 11:
            self.history = [self.history[0]] + self.history[-10:]
        
        # DEBUG: Decommenta per vedere cosa stiamo inviando al modello
        # print(f"DEBUG: Numero messaggi in history: {len(self.history)}")
        
        # 3. Generazione
        text = self.tokenizer.apply_chat_template(self.history, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                do_sample=True,
                top_p=0.9,
                pad_token_id=self.tokenizer.pad_token_id
            )
        
        response = self.tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True).strip()
        self.history.append({"role": "assistant", "content": response})
        return response

if __name__ == "__main__":
    client = QwenClient()
    client.load_model()
    print(client.generate_response("Ciao, chi sei?"))
