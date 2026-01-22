"""
Script per scaricare il modello QWEN 2.5-3B da Hugging Face.
Questo script scarica il modello nella cache locale (~3.5GB).
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def download_qwen_model():
    """Scarica il modello QWEN 2.5-3B e il tokenizer."""
    
    model_name = "Qwen/Qwen2.5-3B-Instruct"
    
    print(f">> Inizio download del modello: {model_name}")
    print(f">> Dimensione approssimativa: ~3.5GB")
    print(f">> Verra salvato in: C:\\Users\\luciano_corvino\\.cache\\huggingface\\hub\\")
    print("\n>> Questo potrebbe richiedere 5-10 minuti...\n")
    
    try:
        # Download del tokenizer
        print("1/2 Download tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("[OK] Tokenizer scaricato con successo!\n")
        
        # Download del modello
        print("2/2 Download modello...")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,  # Usa float16 per risparmiare memoria
            device_map="auto"  # Carica automaticamente su GPU se disponibile
        )
        print("[OK] Modello scaricato con successo!\n")
        
        print(">> Download completato!")
        print(f">> Parametri del modello: {model.num_parameters() / 1e9:.2f}B")
        
        # Test veloce
        print("\n>> Test rapido del modello...")
        test_prompt = "Ciao, come stai?"
        inputs = tokenizer(test_prompt, return_tensors="pt")
        
        print(f"[OK] Modello pronto all'uso!")
        
    except Exception as e:
        print(f"[ERROR] Errore durante il download: {e}")
        raise

if __name__ == "__main__":
    download_qwen_model()
