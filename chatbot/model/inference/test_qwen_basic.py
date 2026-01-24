"""
Script di test per verificare le capacità base di Aidano:
Consapevolezza temporale e Memoria della conversazione.
"""

from qwen_client import QwenClient

def test_basic_capabilities():
    """Test delle funzionalità base (tempo e memoria)."""
    
    print("=" * 60)
    print(">> TEST AIDANO - Capacità Base (Tempo & Memoria)")
    print("=" * 60)
    
    # Inizializza il client senza adapter per testare la base
    client = QwenClient(use_adapters=False)
    client.load_model()
    
    # Test 1: Consapevolezza temporale
    print("\n>> Test 1: Consapevolezza temporale")
    prompt1 = "Che ore sono e che giorno è oggi? Salutami in modo appropriato."
    response1 = client.generate_response(prompt1, max_length=200)
    print(f"Prompt: {prompt1}")
    print(f"Risposta: {response1}")
    
    # Test 2: Conoscenza della lingua italiana
    print("\n>> Test 2: Conoscenza della lingua italiana")
    prompt2 = "Secondo te cosa deve fare un buon sito che intende lavorare per aiutare le persone?"
    response2 = client.generate_response(prompt2, max_length=200)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}")
    
    # Test 3: Memoria della conversazione
    print("\n>> Test 3: Memoria")
    prompt3 = "Qual era la mia primissima domanda che ti ho fatto?"
    response3 = client.generate_response(prompt3, max_length=100)
    print(f"Prompt: {prompt3}")
    print(f"Risposta: {response3}")
    
    print("\n" + "=" * 60)
    print("[OK] Test capacità base completati!")
    print("=" * 60)

if __name__ == "__main__":
    test_basic_capabilities()
