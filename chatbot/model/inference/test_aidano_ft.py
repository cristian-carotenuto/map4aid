"""
Script di test completo per Aidano (Qwen 2.5-3B Fine-tuned).
Verifica: inferenza, personalità e fallback anti-allucinazione + Notifiche.
"""

from qwen_client import QwenClient
import time

def test_aidano_capabilities():
    """Test approfondito delle capacità di Aidano."""
    
    print("=" * 60)
    print(">> TEST AIDANO - Modello Fine-tuned (Run #5.1 - Stability)")
    print("=" * 60)
    
    # Inizializza il client
    client = QwenClient()
    client.load_model()
    
    # Test 1: Saluti e Personalità
    print("\n>> Test 1: Saluti e Personalità")
    prompt1 = "Ciao Aidano, come ti senti oggi?"
    response1 = client.generate_response(prompt1, max_length=100)
    print(f"Prompt: {prompt1}")
    print(f"Risposta: {response1}")
    
    # Test 2: Nuova Conoscenza (Notifiche)
    print("\n>> Test 2: Notifiche (Email/SMS)")
    prompt2 = "Ho ricevuto un messaggio OTP sul telefono senza aver fatto nulla, è normale?"
    response2 = client.generate_response(prompt2, max_length=200)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}")
    
    # Test 3: Conoscenza Progetto
    print("\n>> Test 3: Gestione Map4Aid")
    prompt3 = "Come posso iscrivermi come ente beneficiario?"
    response3 = client.generate_response(prompt3, max_length=200)
    print(f"Prompt: {prompt3}")
    print(f"Risposta: {response3}")
    
    # Test 4: Fallback
    print("\n>> Test 4: Fallback Anti-Allucinazione")
    prompt4 = "Mi consigli una ricetta per la pizza?"
    response4 = client.generate_response(prompt4, max_length=150)
    print(f"Prompt: {prompt4}")
    print(f"Risposta: {response4}")
    
    print("\n" + "=" * 60)
    print("[OK] Tutti i test di Aidano (Run #5.1) completati!")
    print("=" * 60)

if __name__ == "__main__":
    test_aidano_capabilities()
