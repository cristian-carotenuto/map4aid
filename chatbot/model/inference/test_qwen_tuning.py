"""
Script di test completo per Aidano (Qwen 2.5-3B Fine-tuned).
Verifica: inferenza, memoria, tempo e conoscenza del progetto.
"""

from qwen_client import QwenClient
import time

def test_aidano_capabilities():
    """Test approfondito delle capacità di Aidano."""
    
    print("=" * 60)
    print(">> TEST AIDANO - Modello Fine-tuned & Memory Ready")
    print("=" * 60)
    
    # Inizializza il client
    client = QwenClient()
    client.load_model()
    
    # Test 1: Consapevolezza temporale
    print("\n>> Test 1: Consapevolezza temporale")
    prompt1 = "Che ore sono e che giorno è oggi? Salutami in modo appropriato."
    response1 = client.generate_response(prompt1, max_length=100)
    print(f"Prompt: {prompt1}")
    print(f"Risposta: {response1}")
    
    # Test 2: Conoscenza specifica del Progetto (Fine-tuning check)
    print("\n>> Test 2: Conoscenza Map4Aid (Fine-tuning)")
    prompt2 = "Che tipo di donazioni posso effettuare su Map4Aid?"
    response2 = client.generate_response(prompt2, max_length=200)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}")
    
    # Test 3: Altra domanda specifica
    print("\n>> Test 3: Gestione scorte (Fine-tuning)")
    prompt3 = "Come posso aggiornare le scorte se sono un ente?"
    response3 = client.generate_response(prompt3, max_length=200)
    print(f"Prompt: {prompt3}")
    print(f"Risposta: {response3}")

    # Test 4: Memoria della conversazione
    print("\n>> Test 4: Memoria")
    prompt4 = "Qual era la mia primissima domanda in questa chat? Rispondi in modo breve."
    response4 = client.generate_response(prompt4, max_length=100)
    print(f"Prompt: {prompt4}")
    print(f"Risposta: {response4}")
    
    print("\n" + "=" * 60)
    print("[OK] Tutti i test di Aidano completati!")
    print("=" * 60)

if __name__ == "__main__":
    test_aidano_capabilities()
