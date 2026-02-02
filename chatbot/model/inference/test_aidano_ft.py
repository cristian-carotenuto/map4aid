"""
Script di test completo per Aidano (Qwen 2.5-3B Fine-tuned).
Verifica: inferenza, personalità e fallback anti-allucinazione.
NOTE: Le domande sono diverse da quelle presenti nel dataset di training per testare la generalizzazione.
"""

from qwen_client import QwenClient
import time

def test_aidano_capabilities():
    """Test approfondito delle capacità di Aidano."""
    
    print("=" * 60)
    print(">> TEST AIDANO - Modello Fine-tuned (Run #6 - Clean)")
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
    
    # Test 2: Conoscenza Progetto (Donazioni)
    print("\n>> Test 2: Conoscenza Map4Aid (Donazioni)")
    prompt2 = "Quali modi ci sono per donare sul vostro sito?"
    response2 = client.generate_response(prompt2, max_length=200)
    print(f"Prompt: {prompt2}")
    print(f"Risposta: {response2}")
    
    # Test 3: Gestione scorte (Ente)
    print("\n>> Test 3: Gestione scorte (Ente)")
    prompt3 = "In che modo un'organizzazione può inserire nuovi prodotti in magazzino?"
    response3 = client.generate_response(prompt3, max_length=200)
    print(f"Prompt: {prompt3}")
    print(f"Risposta: {response3}")

    # Test 4: Registrazione (Sign Up Check)
    print("\n>> Test 4: Registrazione (Procedura)")
    prompt4 = "Come posso iscrivermi come nuovo utente?"
    response4 = client.generate_response(prompt4, max_length=200)
    print(f"Prompt: {prompt4}")
    print(f"Risposta: {response4}")
    
    # Test 5: Fallback Anti-Allucinazione
    print("\n>> Test 5: Fallback Anti-Allucinazione")
    prompt5 = "Chi ha vinto l'ultimo Festival di Sanremo?"
    response5 = client.generate_response(prompt5, max_length=100)
    print(f"Prompt: {prompt5}")
    print(f"Risposta: {response5}")
    
    print("\n" + "=" * 60)
    print("[OK] Test statici completati!")
    print("=" * 60)
    
    # --- NUOVA MODALITÀ INTERATTIVA ---
    print("\n>> MODALITÀ INTERATTIVA ATTIVATA")
    print("Puoi scrivere una domanda ad Aidano (scrivi 'esci' per terminare):")
    
    while True:
        user_input = input("\nTu: ")
        if user_input.lower() in ["esci", "exit", "quit"]:
            print("Chiusura test interattivo. A presto!")
            break
            
        if not user_input.strip():
            continue
            
        # Genera risposta
        response = client.generate_response(user_input, max_length=200)
        print(f"Aidano: {response}")
    # ---------------------------------

if __name__ == "__main__":
    test_aidano_capabilities()
