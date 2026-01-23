"""
Script di test per verificare le conoscenze acquisite con il fine-tuning.
"""

from qwen_client import QwenClient

def test_tuning_knowledge():
    print("=" * 60)
    print(">> TEST AIDANO - Verifica Fine-Tuning (Map4Aid)")
    print("=" * 60)
    
    # Carichiamo il client (tenterà di caricare gli adapter se presenti)
    client = QwenClient()
    client.load_model()
    
    # Test 1: Conoscenza specifica RAD/Use Cases
    print("\n>> Test 1: Conoscenza specifica (Stock)")
    prompt1 = "Come funziona il modulo di gestione dello Stock?"
    response1 = client.generate_response(prompt1)
    print(f"User: {prompt1}")
    print(f"Aidano: {response1}")

    # Test 2: Conoscenza specifica (Donazioni)
    print("\n>> Test 2: Conoscenza specifica (Donazioni Monetarie)")
    prompt2 = "Chi può fare donazioni monetarie e come?"
    response2 = client.generate_response(prompt2)
    print(f"User: {prompt2}")
    print(f"Aidano: {response2}")

    # Test 3: Memoria specifica
    print("\n>> Test 3: Memoria e Contesto Progetto")
    prompt3 = "Oltre alle donazioni monetarie, quali altri tipi di donazioni esistono per Map4Aid?"
    response3 = client.generate_response(prompt3)
    print(f"User: {prompt3}")
    print(f"Aidano: {response3}")

    print("\n" + "=" * 60)
    print("[FINE] Test tuning completati.")
    print("=" * 60)

if __name__ == "__main__":
    test_tuning_knowledge()
