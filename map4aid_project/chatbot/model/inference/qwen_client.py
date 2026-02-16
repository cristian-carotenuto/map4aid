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

    # System prompt canonico (da usare identico anche nei dataset)
    BASE_SYSTEM_PROMPT = (
        "Sei Aidano, l’assistente virtuale ufficiale di Map4Aid.\n\n"
        "Map4Aid è una piattaforma di aiuti che consente sia di ricevere beni di prima necessità "
        "sia di contribuire aiutando altre persone tramite donazioni monetarie o materiali.\n\n"
        "Il tuo compito è rispondere alle domande degli utenti in modo chiaro, diretto e conciso, "
        "utilizzando esclusivamente informazioni ufficiali relative al funzionamento di Map4Aid.\n\n"
        "Non fare supposizioni, non inventare funzionalità e non fornire informazioni esterne al progetto.\n"
        "Non usare emoji.\n\n"
        "Se una domanda non riguarda Map4Aid o se non disponi di informazioni certe, rispondi esclusivamente con:\n"
        "\"Mi dispiace, non dispongo delle conoscenze per rispondere a questa domanda.\""
    )

    FALLBACK_REPLY = "Mi dispiace, non dispongo delle conoscenze per rispondere a questa domanda."

    # Intent supportati (devono riflettere quelli del dataset)
    INTENT_LABELS = [
        "registrazione",
        "password_dimenticata",
        "email_dimenticata",
        "tipi_donazione",
        "donazione_monetaria",
        "donazione_di_beni",
        "prenotazione_beni",
        "mappa_utilita",
        "mappa_problemi",
        "descrizione_progetto",
        "identita_bot",
        "stato_animo",
        "filtri_mappa",
        "categorie_beni",
        "accesso_profilo",
        "storico_donazioni",
        "storico_prenotazioni",
        "Problemi_login",  # mantieni il case uguale al dataset
        "fallback",
        "NONE",
    ]

    def __init__(self, model_name="Qwen/Qwen2.5-3B-Instruct"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.history = []  # Memoria della conversazione

    def _get_system_info(self):
        """Recupera informazioni di sistema (data e ora) in italiano."""
        now = datetime.now().replace(tzinfo=None)
        data = now.strftime("%d/%m/%Y")
        ora = now.strftime("%H:%M:%S")
        giorni = {
            "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
            "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
        }
        giorno_settimana = giorni.get(now.strftime("%A"), now.strftime("%A"))
        return f"Informazioni di sistema: Oggi è {giorno_settimana}, {data}. L'ora attuale è {ora}."

    def _build_system_prompt(self):
        """Costruisce il system prompt finale (canonico + info temporali)."""
        system_info = self._get_system_info()
        return f"{self.BASE_SYSTEM_PROMPT}\n\n{system_info}"

    def load_model(self):
        """Carica il modello base e gli eventuali adapter del fine-tuning."""
        print(f">> Caricamento modello {self.model_name}...")
        print(f">> Device: {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # Fix: se il tokenizer non ha pad_token, lo impostiamo (utile con generate)
        if self.tokenizer.pad_token_id is None:
            if self.tokenizer.eos_token_id is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                self.tokenizer.add_special_tokens({"pad_token": "[PAD]"})

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

        # Se abbiamo aggiunto token speciali (es. PAD), riallineiamo embeddings
        try:
            self.model.resize_token_embeddings(len(self.tokenizer))
        except Exception:
            pass

        # Tentativo di caricamento degli adapter (Fine-tuning)
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

    def classify_intent(self, user_text: str, max_new_tokens: int = 8) -> str:
        """
        Classifica l'intent della domanda in una delle etichette note.
        Ritorna una label tra INTENT_LABELS. Se output non valido -> NONE.
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")

        labels = [x for x in self.INTENT_LABELS if x != "NONE"]

        classifier_system = (
            "Sei un classificatore di intent per Map4Aid.\n"
            "Rispondi con UNA SOLA etichetta, senza testo aggiuntivo.\n"
            f"Etichette possibili: {', '.join(labels)}, NONE.\n"
            "Regole:\n"
            "- Se la domanda non rientra chiaramente in una delle etichette, rispondi: NONE\n"
            "- Non aggiungere spiegazioni.\n"
        )

        msgs = [
            {"role": "system", "content": classifier_system},
            {"role": "user", "content": user_text},
        ]

        text = self.tokenizer.apply_chat_template(
            msgs,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer([text], return_tensors="pt")
        # Evita mismatch con device_map="auto": metti gli input su un device valido
        try:
            inputs = inputs.to(self.model.device)
        except Exception:
            inputs = inputs.to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                repetition_penalty=1.05,
                pad_token_id=self.tokenizer.pad_token_id
            )

        raw = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True
        ).strip()

        # Prendi solo la prima "parola/riga" e ripulisci
        label = raw.splitlines()[0].strip()
        label = label.split()[0].strip().strip('",.:')

        if label not in self.INTENT_LABELS:
            return "NONE"
        return label

    def generate_response_gated(self, prompt: str, max_new_tokens: int = 160) -> str:
        """
        Applica intent gate:
        - se NONE -> fallback (senza contaminare la history)
        - altrimenti -> risposta normale
        """
        intent = self.classify_intent(prompt)

        if intent == "NONE":
            return self.FALLBACK_REPLY

        return self.generate_response(prompt, max_new_tokens=max_new_tokens)

    def generate_response(self, prompt: str, max_new_tokens: int = 160) -> str:
        """
        Genera una risposta gestendo la memoria e il contesto temporale.
        Nota: max_length rinominato in max_new_tokens per chiarezza.
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")

        # 1) System prompt canonico + info temporali
        system_prompt = self._build_system_prompt()

        # 2) Gestione history (system + ultimi 10 messaggi)
        if not self.history:
            self.history.append({"role": "system", "content": system_prompt})
        else:
            self.history[0] = {"role": "system", "content": system_prompt}

        self.history.append({"role": "user", "content": prompt})

        # Mantiene: system + ultimi 10 messaggi totali (user/assistant)
        if len(self.history) > 11:
            self.history = [self.history[0]] + self.history[-10:]

        # 3) Chat template
        text = self.tokenizer.apply_chat_template(
            self.history,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer([text], return_tensors="pt")
        try:
            inputs = inputs.to(self.model.device)
        except Exception:
            inputs = inputs.to(self.device)

        # 4) Generazione deterministica (KB-style)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                repetition_penalty=1.1,
                pad_token_id=self.tokenizer.pad_token_id
            )

        response = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True
        ).strip()

        # 5) Hardening leggero: se il modello “sfora” con fallback + extra testo, taglia al fallback
        if response.startswith(self.FALLBACK_REPLY):
            response = self.FALLBACK_REPLY

        # Salva nella memoria
        self.history.append({"role": "assistant", "content": response})

        return response


if __name__ == "__main__":
    client = QwenClient()
    client.load_model()
    print(client.generate_response_gated("Ciao, chi sei?"))
