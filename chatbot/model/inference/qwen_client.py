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
        self.history = [] # Memoria della conversazione
        
    def _get_system_info(self):
        """Recupera informazioni di sistema (data e ora) in italiano."""
        now = datetime.now()
        data = now.strftime("%d/%m/%Y")
        ora = now.strftime("%H:%M:%S")
        giorni = {
            "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
            "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
        }
        giorno_settimana = giorni.get(now.strftime("%A"), now.strftime("%A"))
        return f"Informazioni di sistema: Oggi è {giorno_settimana}, {data}. L'ora attuale è {ora}."

    def load_model(self):
        """Carica il modello base e gli eventuali adapter del fine-tuning."""
        print(f">> Caricamento modello {self.model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        )

        # Carica il modello base
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=True
        )
        
        # Tentativo di caricamento degli adapter (Fine-tuning)
        # Cerchiamo la cartella qwen-aidano-final nella cartella di training
        script_dir = os.path.dirname(os.path.abspath(__file__))
        adapter_path = os.path.join(script_dir, "../training/qwen-aidano-final")
        
        if os.path.exists(adapter_path):
            from peft import PeftModel
            print(f">> Caricamento adapter personalizzati Aidano da: {adapter_path}")
            self.model = PeftModel.from_pretrained(self.model, adapter_path)
        else:
            print(">> Nessun adapter personalizzato trovato. Utilizzo modello base.")
            
        print("[OK] Modello pronto!")
        
    def clear_history(self):
        """Resetta la memoria della conversazione."""
        self.history = []

    def generate_response(self, prompt, max_length=512, temperature=0.5):
        """
        Genera una risposta gestendo la memoria e il contesto temporale.
        """
        if self.model is None:
            raise RuntimeError("Modello non caricato.")
        
        # 1. Recupera info temporali aggiornate
        system_info = self._get_system_info()
        # Allineato esattamente al prompt usato nel dataset generator
        # System Prompt restrittivo (Anti-Allucinazione) con eccezione per saluti/personalità
        system_prompt = (
            f"Sei Aidano, l'assistente virtuale ufficiale di Map4Aid. {system_info} "
            "Il tuo compito è rispondere a domande sul progetto Map4Aid usando solo informazioni ufficiali. "
            "Sii gentile, amichevole e rispondi normalmente ai saluti o a brevi domande sulla tua personalità. "
            "IMPORTANTE: Non inventare mai indirizzi email di supporto. Ad oggi non esiste una mail di supporto ufficiale, Aidano è l'unico assistente. "
            "Per qualsiasi richiesta su argomenti esterni complessi (storia, cucina, scienza, ecc.) "
            "o se non sei sicuro della risposta tecnica, rispondi categoricamente con: "
            "'Mi dispiace non dispongo delle conoscenze per rispondere a questa domanda'."
        )
        
        # 2. Gestione History (Sliding Window: sistema + ultimi 10 messaggi)
        if not self.history:
            self.history.append({"role": "system", "content": system_prompt})
        else:
            # Aggiorna il system prompt con l'orario attuale se è già presente
            self.history[0] = {"role": "system", "content": system_prompt}
            
        self.history.append({"role": "user", "content": prompt})
        
        # Limita la memoria (mantiene il system prompt + gli ultimi 10 scambi)
        if len(self.history) > 11:
            self.history = [self.history[0]] + self.history[-10:]
        
        # 3. Prepara il testo per il modello
        text = self.tokenizer.apply_chat_template(
            self.history,
            tokenize=False,
            add_generation_prompt=True
        )
        
        inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
        
        # 4. Generazione
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                do_sample=True,
                top_p=0.9,
                repetition_penalty=1.1,
                pad_token_id=self.tokenizer.pad_token_id
            )
        
        response = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True
        ).strip()
        
        # 5. Salva la risposta nella memoria
        self.history.append({"role": "assistant", "content": response})
        
        return response

if __name__ == "__main__":
    client = QwenClient()
    client.load_model()
    print(client.generate_response("Ciao, chi sei?"))
