"""
Script di test per verificare il funzionamento di QWEN.
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
    
    # Test 2: Domanda sul chatbot
    print(">> Test 2: Domanda sul chatbot")
    prompt2 = "Sei un chatbot per un sito di beneficenza. Puoi aiutarmi a fare una donazione?"
    response2 = client.generate_response(prompt2, max_length=150)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}\n")
    
    # Test 3: Domanda in italiano
    print(">> Test 3: Comprensione italiano")
    prompt3 = "Quali sono le funzionalita principali di un sito di beneficenza?"
    response3 = client.generate_response(prompt3, max_length=200)
    print(f"Prompt: {prompt3}")
    print(f"Risposta: {response3}\n")
    
    print("=" * 60)
    print("[OK] Test completati con successo!")
    print("=" * 60)

if __name__ == "__main__":
    test_basic_inference()
