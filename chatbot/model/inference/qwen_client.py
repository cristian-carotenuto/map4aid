"""
Client per l'inferenza con Qwen 2.5-3B (Aidano / Map4Aid).

Versione "fixed output":
- LLM usato SOLO per:
  1) classificazione intent
  2) gate ANSWERABLE come COERENZA (domanda + risposta candidata)
- L'output NON viene generato dal modello: viene scelto da un set di risposte canoniche
  (round-robin per intent), così si evitano allucinazioni e dettagli inventati.
"""

import json
import os
from typing import Dict, List, Optional, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class QwenClient:
    """Client per interagire con il modello QWEN come classificatore + gating."""

    BASE_SYSTEM_PROMPT = (
        "Sei Aidano, l’assistente virtuale ufficiale di Map4Aid.\n\n"
        "Map4Aid è una piattaforma di aiuti che consente sia di ricevere beni di prima necessità "
        "sia di contribuire aiutando altre persone tramite donazioni monetarie o materiali.\n\n"
        "Il tuo compito è rispondere alle domande degli utenti in modo chiaro, diretto e conciso, "
        "utilizzando esclusivamente informazioni ufficiali relative al funzionamento di Map4Aid.\n\n"
        "Non fare supposizioni, non inventare funzionalità e non fornire informazioni esterne al progetto.\n"
        "Se una domanda non riguarda Map4Aid o se non disponi di informazioni certe, rispondi esclusivamente con:\n"
        "\"Mi dispiace, non dispongo delle conoscenze per rispondere a questa domanda.\""
    )

    FALLBACK_REPLY = "Mi dispiace, non dispongo delle conoscenze per rispondere a questa domanda."

    NOT_SUPPORTED_REPLY = (
        "Non ho informazioni ufficiali su questa funzionalità in Map4Aid. "
        "Posso aiutarti con registrazione, login, donazioni, utilizzo della mappa e prenotazione dei beni."
    )

    FEEDBACK_REPLY_TEMPLATE = (
        "Non ho informazioni ufficiali sufficienti per rispondere a questa richiesta in modo affidabile.\n\n"
        "Per aiutarci a migliorare Aidano, puoi inviare un feedback con:\n"
        "- la domanda che hai scritto\n"
        "- cosa stavi cercando di fare / qual è la problematica\n"
        "- (se possibile) la pagina o schermata in cui ti trovi\n\n"
        "Domanda: \"{user_question}\""
    )

    # Default fallback (se non trovi il JSON runtime)
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
        "problemi_login",
        "non_disponibile",
        "NONE",
    ]

    FIXED_ANSWERS: Dict[str, List[str]] = {
        "non_disponibile": [NOT_SUPPORTED_REPLY],
    }

    # Intent comuni usati come padding per arrivare a 3 opzioni in two-stage
    TWO_STAGE_DEFAULTS = [
        "descrizione_progetto",
        "registrazione",
        "problemi_login",
        "password_dimenticata",
        "email_dimenticata",
        "tipi_donazione",
        "donazione_di_beni",
        "donazione_monetaria",
        "prenotazione_beni",
        "mappa_utilita",
        "filtri_mappa",
        "categorie_beni",
        "accesso_profilo",
    ]

    def __init__(self, model_name: str = "Qwen/Qwen2.5-3B-Instruct"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.history = []
        self._rr_counter: Dict[str, int] = {}

        # Runtime-config (overridable via JSON)
        self.INTENT_LABELS = list(self.INTENT_LABELS)
        self.FIXED_ANSWERS = dict(self.FIXED_ANSWERS)
        self.FALLBACK_INTENT = "NONE"
        self.NOT_SUPPORTED_INTENT = "non_disponibile"
        self.CONFUSABLE: Dict[str, List[str]] = {}
        self.INTENT_DISPLAY_NAMES: Dict[str, str] = {}

        # Stato per disambiguazione numerica (testo_originale, [intent1,intent2,intent3])
        self.pending_disambiguation: Optional[Tuple[str, List[str]]] = None

    def load_runtime_config(self, config_path: str) -> None:
        """Carica intent_labels, fixed_answers, confusable e display names da JSON generato dal dataset_generator."""
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        intent_labels = cfg.get("intent_labels", [])
        fixed_answers = cfg.get("fixed_answers", {})

        if not isinstance(intent_labels, list) or not intent_labels:
            raise ValueError("runtime_config: 'intent_labels' mancante o non valido")

        if not isinstance(fixed_answers, dict) or not fixed_answers:
            raise ValueError("runtime_config: 'fixed_answers' mancante o non valido")

        self.INTENT_LABELS = [str(x).strip().lower() for x in intent_labels if str(x).strip()]
        self.FIXED_ANSWERS = {str(k).strip().lower(): v for k, v in fixed_answers.items()}

        self.FALLBACK_INTENT = str(cfg.get("fallback_intent", "NONE")).strip().lower()
        self.NOT_SUPPORTED_INTENT = str(cfg.get("not_supported_intent", "non_disponibile")).strip().lower()

        conf = cfg.get("confusable", {})
        if isinstance(conf, dict):
            norm_conf: Dict[str, List[str]] = {}
            for k, v in conf.items():
                kk = str(k).strip().lower()
                if not kk:
                    continue
                if isinstance(v, list):
                    vv = [str(x).strip().lower() for x in v if str(x).strip()]
                else:
                    vv = []
                norm_conf[kk] = vv
            self.CONFUSABLE = norm_conf
        else:
            self.CONFUSABLE = {}

        disp = cfg.get("intent_display_names", {})
        if isinstance(disp, dict):
            self.INTENT_DISPLAY_NAMES = {
                str(k).strip().lower(): str(v).strip()
                for k, v in disp.items()
                if str(k).strip() and str(v).strip()
            }

        if "none" not in self.INTENT_LABELS:
            self.INTENT_LABELS.append("none")

    def _build_system_prompt(self) -> str:
        return self.BASE_SYSTEM_PROMPT

    def load_model(self) -> None:
        print(f">> Caricamento modello {self.model_name}...")
        print(f">> Device: {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        if self.tokenizer.pad_token_id is None:
            if self.tokenizer.eos_token_id is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                self.tokenizer.add_special_tokens({"pad_token": "[PAD]"})

        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=True,
        )

        try:
            self.model.resize_token_embeddings(len(self.tokenizer))
        except Exception:
            pass

        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Runtime config in /data
        runtime_cfg_path = os.path.join(script_dir, "../../data/aidano_runtime_config.json")
        if os.path.exists(runtime_cfg_path):
            print(f">> Caricamento runtime config da: {runtime_cfg_path}")
            self.load_runtime_config(runtime_cfg_path)
        else:
            print(">> Nessuna runtime config trovata. Uso fallback hardcoded nel client.")

        # Caricamento adapter (Fine-tuning)
        adapter_path = os.path.join(script_dir, "../training/qwen-aidano-final")
        if os.path.exists(adapter_path):
            from peft import PeftModel
            print(f">> Caricamento adapter personalizzati Aidano da: {adapter_path}")
            self.model = PeftModel.from_pretrained(self.model, adapter_path)
        else:
            print(">> Nessun adapter personalizzato trovato. Utilizzo modello base.")

        self.model.eval()
        print("[OK] Modello pronto!")

    def clear_history(self) -> None:
        self.history = []
        self._rr_counter = {}
        self.pending_disambiguation = None

    def _inputs_to_device(self, inputs):
        try:
            return inputs.to(self.model.device)
        except Exception:
            return inputs.to(self.device)

    @staticmethod
    def _normalize_label(label: str) -> str:
        if not label:
            return "none"
        x = label.strip()
        x = x.splitlines()[0].strip()
        x = x.split()[0].strip()
        x = x.strip("\"'.,:;!?()[]{}")
        x_low = x.lower()
        return x_low

    def _intent_name(self, intent: str) -> str:
        intent = str(intent).strip().lower()
        if intent in self.INTENT_DISPLAY_NAMES:
            return self.INTENT_DISPLAY_NAMES[intent]
        return intent.replace("_", " ").strip()

    def _label_logprob(self, prompt_text: str, label: str) -> float:
        """Log-probabilità che il modello generi `label` dopo `prompt_text` (label può essere multi-token)."""
        device = self.model.device
        enc = self.tokenizer([prompt_text], return_tensors="pt").to(device)
        input_ids = enc["input_ids"]

        label_ids = self.tokenizer(" " + label, add_special_tokens=False)["input_ids"]
        if not label_ids:
            return float("-inf")
        label_ids = torch.tensor(label_ids, device=device).unsqueeze(0)

        total = 0.0
        cur = input_ids
        with torch.inference_mode():
            for i in range(label_ids.size(1)):
                out = self.model(input_ids=cur)
                logits = out.logits[:, -1, :]
                log_probs = torch.nn.functional.log_softmax(logits, dim=-1)
                tok = label_ids[:, i]
                total += log_probs.gather(1, tok.unsqueeze(1)).item()
                cur = torch.cat([cur, tok.unsqueeze(1)], dim=1)
        return total

    def topk_intents_restricted(self, user_text: str, candidates: List[str], k: int = 3):
        """Top-k intent su un sottoinsieme di label (più veloce di topk_intents su tutte le label)."""
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")

        valid = set([x.lower() for x in self.INTENT_LABELS if x])
        uniq: List[str] = []
        seen = set()
        for c in candidates:
            cc = str(c).strip().lower()
            if not cc or cc == "none":
                continue
            if cc in seen:
                continue
            if cc not in valid:
                continue
            uniq.append(cc)
            seen.add(cc)

        if not uniq:
            return []

        classifier_system = (
            "Sei un classificatore di intent per Map4Aid.\n"
            "Rispondi con UNA SOLA etichetta, senza testo aggiuntivo.\n"
            f"Etichette possibili: {', '.join(uniq)}, NONE.\n"
            "Regole:\n"
            "- Se la domanda non rientra chiaramente in una delle etichette, rispondi: NONE\n"
            "- Non aggiungere spiegazioni.\n"
        )

        msgs = [
            {"role": "system", "content": classifier_system},
            {"role": "user", "content": user_text},
        ]

        prompt_text = self.tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True
        )

        scored = [(lab, self._label_logprob(prompt_text, lab)) for lab in uniq]
        lps = torch.tensor([s[1] for s in scored], device=self.model.device)
        probs = torch.softmax(lps, dim=0).tolist()

        ranked = sorted(
            [(scored[i][0], probs[i]) for i in range(len(scored))],
            key=lambda x: x[1],
            reverse=True,
        )
        return ranked[: max(1, k)]

    # (Debug) molto costosa se hai tante label: usala solo in test mirati
    def topk_intents(self, user_text: str, k: int = 3):
        labels = [x for x in self.INTENT_LABELS if x != "none"]
        return self.topk_intents_restricted(user_text, labels, k=k)

    def _should_disambiguate(self, topk, min_p1: float = 0.55, min_margin: float = 0.12) -> bool:
        if not topk or len(topk) < 2:
            return False
        p1 = float(topk[0][1])
        p2 = float(topk[1][1])
        return (p1 < min_p1) or ((p1 - p2) < min_margin)

    def _build_disambiguation_prompt(self, topk) -> str:
        top3 = topk[:3]
        lines = ["Ho capito più possibili richieste. Seleziona il numero corretto:"]
        for i, (intent, _) in enumerate(top3, start=1):
            lines.append(f"{i}) {self._intent_name(intent)}")
        lines.append("Rispondi con 1, 2 oppure 3.")
        return "\n".join(lines)

    def _pick_fixed_answer_round_robin(self, intent: str) -> str:
        options = self.FIXED_ANSWERS.get(intent)
        if not options:
            return self.NOT_SUPPORTED_REPLY
        idx = self._rr_counter.get(intent, 0)
        chosen = options[idx % len(options)]
        self._rr_counter[intent] = idx + 1
        return chosen

    def classify_intent(self, user_text: str, max_new_tokens: int = 10) -> str:
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")

        labels = [x for x in self.INTENT_LABELS if x != "none"]

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
            add_generation_prompt=True,
        )

        inputs = self._inputs_to_device(self.tokenizer([text], return_tensors="pt"))

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                repetition_penalty=1.05,
                pad_token_id=self.tokenizer.pad_token_id,
            )

        raw = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True,
        ).strip()

        label = self._normalize_label(raw)
        if label not in [x.lower() for x in self.INTENT_LABELS]:
            return "none"
        return label

    def is_answerable(self, user_text: str, intent: str, candidate_answer: str, max_new_tokens: int = 4) -> bool:
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")

        classifier_system = (
            "Valuta se la RISPOSTA CANDIDATA è pertinente alla DOMANDA dell’utente.\n"
            "Rispondi SOLO con una parola:\n"
            "ANSWERABLE oppure NOT_ANSWERABLE\n\n"
            "ANSWERABLE: la risposta candidata risponde correttamente alla domanda.\n"
            "NOT_ANSWERABLE: la risposta candidata non è coerente con la domanda.\n"
        )

        payload = (
            f"Domanda: {user_text}\n"
            f"Intent stimato: {intent}\n"
            f"Risposta candidata: {candidate_answer}"
        )

        msgs = [
            {"role": "system", "content": classifier_system},
            {"role": "user", "content": payload},
        ]

        text = self.tokenizer.apply_chat_template(
            msgs,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = self._inputs_to_device(self.tokenizer([text], return_tensors="pt"))

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                repetition_penalty=1.05,
                pad_token_id=self.tokenizer.pad_token_id,
            )

        raw = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True,
        ).strip()

        label = raw.splitlines()[0].strip().split()[0].strip().strip("\"'.,:;!?()[]{}")
        label = label.upper()
        return label == "ANSWERABLE"

    def _respond_with_intent(self, text: str, intent: str, force_answerable: bool = False) -> str:
        lower = text.lower()

        if intent == self.FALLBACK_INTENT or intent == "none":
            return self.FALLBACK_REPLY

        if intent == self.NOT_SUPPORTED_INTENT:
            return self.NOT_SUPPORTED_REPLY

        if intent not in self.FIXED_ANSWERS:
            return self.NOT_SUPPORTED_REPLY

        candidate = self._pick_fixed_answer_round_robin(intent)

        # PRE-GATE
        words = [w for w in lower.split() if w]
        word_count = len(words)

        strong_keywords = {
            "registrazione", "registrarmi", "sign", "signup", "account",
            "login", "loggarmi", "password", "email", "map4aid",
            "donazione", "donare", "monetaria", "beni", "materiali", "donazioni",
            "mappa", "punti", "distribuzione", "filtri",
            "prenotare", "prenotazione", "ritiro", "slot",
            "profilo", "storico"
        }

        off_topic_markers = {"tostapane", "mare", "calcio", "bitcoin", "rubare", "truffa", "anziani"}

        has_strong = any(k in lower for k in strong_keywords)
        has_off_topic = any(m in lower for m in off_topic_markers)

        should_check_answerable = False
        if force_answerable:
            should_check_answerable = False
        elif has_off_topic:
            should_check_answerable = True
        elif word_count >= 8 or len(lower) >= 45:
            should_check_answerable = True
        elif not has_strong:
            should_check_answerable = True

        if should_check_answerable:
            if not self.is_answerable(text, intent=intent, candidate_answer=candidate):
                return self.FEEDBACK_REPLY_TEMPLATE.format(user_question=text)

        return candidate

    def _two_stage_candidates(self, intent_pred: str, user_text: str) -> List[str]:
        """Costruisce un set piccolo di candidati: predetto + confusable + padding."""
        intent_pred = str(intent_pred).strip().lower()
        base: List[str] = []
        if intent_pred and intent_pred != "none":
            base.append(intent_pred)
            base.extend(self.CONFUSABLE.get(intent_pred, []))

        # se NONE o nessun confusable, usa alcuni intent comuni come fallback
        if not base:
            base = []

        # padding per arrivare a >=3 (senza duplicati)
        seen = set()
        out: List[str] = []
        for x in base + self.TWO_STAGE_DEFAULTS:
            xx = str(x).strip().lower()
            if not xx or xx == "none":
                continue
            if xx in seen:
                continue
            out.append(xx)
            seen.add(xx)
            if len(out) >= 8:  # keep small to stay fast
                break

        return out

    def respond_fixed_gated(self, prompt: str) -> str:
        text = prompt.strip()
        lower = text.lower()

        # 1) Se siamo in disambiguazione, accetta 1/2/3 e usa la domanda originale
        if self.pending_disambiguation is not None:
            original_text, intents = self.pending_disambiguation
            choice = lower.strip()
            if choice in ("1", "2", "3") and len(intents) >= int(choice):
                idx = int(choice) - 1
                chosen_intent = intents[idx]
                self.pending_disambiguation = None
                return self._respond_with_intent(original_text, chosen_intent)
            menu_topk = [(i, 0.0) for i in intents[:3]]
            return self._build_disambiguation_prompt(menu_topk)

        force_answerable = False

        # Shortcut: domande generiche su Map4Aid -> descrizione progetto
        if "map4aid" in lower:
            if any(x in lower for x in ["cos'è", "che cos'è", "cosa è", "chi è", "a cosa serve", "come funziona", "spiegami", "parlami"]):
                intent = "descrizione_progetto"
                force_answerable = True
                return self._respond_with_intent(text, intent, force_answerable=force_answerable)
            if len(lower) < 25 and not any(k in lower for k in ["registra", "login", "password", "email", "donaz", "prenot", "mappa"]):
                intent = "descrizione_progetto"
                force_answerable = True
                return self._respond_with_intent(text, intent, force_answerable=force_answerable)

        # ----------------------------
        # TWO-STAGE CLASSIFICATION
        # ----------------------------
        # Stage 1: classify veloce (generate)
        intent_pred = self.classify_intent(text)

        # Stage 2: scoring solo su candidati piccoli (predetto + confusable + padding)
        candidates = self._two_stage_candidates(intent_pred, text)
        ranked = self.topk_intents_restricted(text, candidates, k=3)

        if ranked:
            top3 = ranked
            # Disambiguazione solo se serve (bassa confidenza / margine piccolo)
            if self._should_disambiguate(top3):
                intents = [x[0] for x in top3]
                self.pending_disambiguation = (text, intents)
                return self._build_disambiguation_prompt(top3)
            intent = top3[0][0]
            return self._respond_with_intent(text, intent, force_answerable=force_answerable)

        # Fallback: se per qualche motivo non abbiamo ranking, usa predizione stage1
        return self._respond_with_intent(text, intent_pred, force_answerable=force_answerable)


if __name__ == "__main__":
    client = QwenClient()
    client.load_model()
    print(client.respond_fixed_gated("Ciao, chi sei?"))
