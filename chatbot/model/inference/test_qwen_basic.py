"""
Script di test per verificare le capacità base di Aidano (senza fine-tuning).
Verifica: Consapevolezza temporale, Memoria a breve termine, Lingua italiana.
"""

from qwen_client import QwenClient
import time

def test_basic_capabilities():
    print("=" * 60)
    print(">> TEST AIDANO - Capacità Base (Modello Base)")
    print("=" * 60)
    
    # Inizializziamo senza usare gli adapter per testare il modello base
    client = QwenClient()
    client.load_model() # use_adapters=False è il default ora nel caricamento
    
    # Test 1: Consapevolezza Temporale
    print("\n>> Test 1: Consapevolezza Temporale")
    prompt1 = "Che giorno è oggi e che ore sono?"
    response1 = client.generate_response(prompt1)
    print(f"User: {prompt1}")
    print(f"Aidano: {response1}")

    # Test 2: Cortesia e Lingua
    print("\n>> Test 2: Cortesia e Lingua")
    prompt2 = "Quali sono le tue funzioni principali come assistente di beneficenza?"
    response2 = client.generate_response(prompt2, max_length=200)
    print(f"User: {prompt2}")
    print(f"Aidano: {response2}")

    # Test 3: Memoria della conversazione
    print("\n>> Test 3: Memoria della conversazione")
    prompt3 = "Di cosa abbiamo parlato nel messaggio precedente?"
    response3 = client.generate_response(prompt3)
    print(f"User: {prompt3}")
    print(f"Aidano: {response3}")

    print("\n" + "=" * 60)
    print("[OK] Test base completati.")
    print("=" * 60)

if __name__ == "__main__":
    test_basic_capabilities()
