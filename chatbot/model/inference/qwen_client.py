"""
Client per l'inferenza con QWEN 2.5-3B.
Questo modulo gestisce il caricamento del modello e la generazione di risposte.
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

class QwenClient:
    """Client per interagire con il modello QWEN."""
    
    def __init__(self, model_name="Qwen/Qwen2.5-3B-Instruct"):
        """
        Inizializza il client QWEN.
        
        Args:
            model_name: Nome del modello su Hugging Face
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def load_model(self):
        """Carica il modello e il tokenizer."""
        print(f">> Caricamento modello {self.model_name}...")
        print(f">> Device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        # Configurazione per quantizzazione a 4-bit
        # Questo riduce drasticamente l'uso della VRAM (<2GB per il modello 3B)
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=quantization_config,
            device_map="auto"
        )
        
        print("[OK] Modello caricato con successo!")
        
    def generate_response(self, prompt, max_length=512, temperature=0.7):
        """
        Genera una risposta dato un prompt.
        
        Args:
            prompt: Testo di input
            max_length: Lunghezza massima della risposta
            temperature: Creatività della risposta (0.0-1.0)
            
        Returns:
            Risposta generata dal modello
        """
        if self.model is None:
            raise RuntimeError("Modello non caricato. Chiama load_model() prima.")
        
        # Prepara il prompt con il formato chat
        messages = [
            {"role": "system", "content": "Sei un assistente utile che risponde in italiano."},
            {"role": "user", "content": prompt}
        ]
        
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        # Tokenizza
        inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
        
        # Genera risposta
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                do_sample=True,
                top_p=0.9
            )
        
        # Decodifica
        response = self.tokenizer.decode(
            outputs[0][len(inputs.input_ids[0]):],
            skip_special_tokens=True
        )
        
        return response.strip()

if __name__ == "__main__":
    # Test del client
    client = QwenClient()
    client.load_model()
    
    test_prompt = "Ciao! Puoi presentarti brevemente?"
    print(f"\n>> Prompt: {test_prompt}")
    response = client.generate_response(test_prompt)
    print(f">> Risposta: {response}")
