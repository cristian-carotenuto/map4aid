import json

def generate_variations():
    """Genera variazioni di domande e risposte basate sui template dei casi d'uso raffinati."""
    
    templates = [
        {
            "intent": "registrazione",
            "questions": [
                "Come mi registro?",
                "Qual è la procedura di iscrizione?",
                "Cosa serve per creare un account?",
                "Come posso iscrivermi a Map4Aid?",
                "Mi spieghi come fare la registrazione?"
            ],
            "answer": "Per registrarti su Map4Aid, vai alla pagina di registrazione e inserisci i tuoi dati (nome, cognome, Codice Fiscale, email e password). Se sei un donatore, puoi aggiungere la Partita IVA. Indica anche eventuali esigenze alimentari se sei un beneficiario."
        },
        {
            "intent": "tipi_donazione",
            "questions": [
                "Che tipo di donazioni posso effettuare?",
                "Quali sono le modalità di donazione?",
                "Cosa posso donare su Map4Aid?",
                "In che modo posso aiutare tramite donazioni?",
                "Che opzioni di donazione ci sono?"
            ],
            "answer": "Su Map4Aid puoi effettuare due tipi di donazioni: donazioni monetarie (fondi destinati agli enti erogatori) e donazioni di beni materiali (oggetti o viveri che vengono poi convalidati e ritirati dall'ente). Puoi scegliere la modalità più adatta a te direttamente dall'interfaccia principale."
        },
        {
            "intent": "donazione_monetaria",
            "questions": [
                "Come faccio a donare soldi?",
                "Voglio fare una donazione in denaro.",
                "Come funzionano le donazioni monetarie?",
                "Dove posso donare fondi agli enti?",
                "Mi aiuti a fare una donazione economica?"
            ],
            "answer": "Puoi fare una donazione monetaria selezionando l'opzione apposita nell'interfaccia. Scegli l'ente destinatario, inserisci l'importo e i dati del metodo di pagamento. Il sistema verificherà la transazione e ti invierà una conferma."
        },
        {
            "intent": "gestione_scorte",
            "questions": [
                "Come aggiorno le scorte dei beni?",
                "Come si caricano i nuovi beni in inventario?",
                "In che modo posso modificare le quantità dei prodotti?",
                "Come funziona l'aggiornamento dell'inventario?",
                "Dove gestisco la disponibilità dei beni?"
            ],
            "answer": "La gestione delle scorte è riservata agli enti erogatori tramite la dashboard dedicata. Le quantità si aggiornano automaticamente in caso di donazioni ricevute o prenotazioni effettuate. È inoltre possibile aggiungere manualmente nuovi beni o incrementare le scorte esistenti, mentre la riduzione manuale non è consentita per garantire la coerenza dei dati."
        },
        {
            "intent": "prenotazione_beni",
            "questions": [
                "Come prenoto un pacco?",
                "Voglio ritirare dei beni, come faccio?",
                "Come funziona la prenotazione degli slot?",
                "Posso scegliere quando andare a ritirare gli aiuti?",
                "Come si prenota un ritiro sulla mappa?"
            ],
            "answer": "Sulla mappa di Map4Aid trovi i punti di ritiro. Selezionane uno, scegli i beni che ti servono e prenota uno slot orario disponibile. Riceverai una conferma della prenotazione per il ritiro."
        }
    ]

    output_file = "training_data_expanded.jsonl"
    system_prompt = "Sei Aidano, l'assistente virtuale di Map4Aid, un sistema di gestione donazioni e aiuti."

    with open(output_file, "w", encoding="utf-8") as f:
        for item in templates:
            for q in item["questions"]:
                entry = {
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": q},
                        {"role": "assistant", "content": item["answer"]}
                    ]
                }
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f">> Dataset espanso generato con successo in {output_file}")

if __name__ == "__main__":
    generate_variations()
