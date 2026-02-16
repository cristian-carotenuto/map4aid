"""
Test interattivo per Aidano (Qwen 2.5-3B + eventuale adapter fine-tuned).
Questo script è allineato al QwenClient: carica il modello una sola volta e
ti permette di fare domande in modalità REPL (solo input manuale, nessun test statico).
"""

from qwen_client import QwenClient


def main():
    print("=" * 60)
    print(">> AIDANO - MODALITÀ INTERATTIVA")
    print("Scrivi una domanda e premi Invio.")
    print("Comandi: /esci  /reset  /help")
    print("=" * 60)

    client = QwenClient()
    client.load_model()

    while True:
        user_input = input("\nTu: ").strip()

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ["/esci", "esci", "exit", "quit"]:
            print("Chiusura. A presto!")
            break

        if cmd in ["/reset", "reset"]:
            client.clear_history()
            print("Memoria conversazione resettata.")
            continue

        if cmd in ["/help", "help", "?"]:
            print("Comandi disponibili:")
            print("  /reset  -> resetta la memoria conversazione")
            print("  /esci   -> termina il programma")
            continue

        # Genera risposta (il client usa max_new_tokens=160 e do_sample=False internamente)
        response = client.generate_response_gated(user_input)
        print(f"Aidano: {response}")


if __name__ == "__main__":
    main()
