"""
Script di test base per verificare il funzionamento di QWEN senza fine-tuning.
"""

from qwen_client import QwenClient

def test_basic_inference():
    """Test di base per l'inferenza con QWEN 2.5-3B."""
    
    print("=" * 60)
    print(">> TEST QWEN 2.5-3B - Inferenza Base")
    print("=" * 60)
    
    # Inizializza il client
    client = QwenClient()
    client.load_model()
    
    # Test 1: Saluto semplice
    print("\n>> Test 1: Saluto semplice")
    prompt1 = "Ciao, come stai?"
    response1 = client.generate_response(prompt1, max_length=100)
    print(f"Prompt: {prompt1}")
    print(f"Risposta: {response1}\n")
    
    # Test 2: Domanda generica
    print(">> Test 2: Domanda generica")
    prompt2 = "Quali sono i vantaggi dell'intelligenza artificiale?"
    response2 = client.generate_response(prompt2, max_length=150)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}\n")
    
    print("=" * 60)
    print("[OK] Test base completati!")
    print("=" * 60)

if __name__ == "__main__":
    test_basic_inference()
