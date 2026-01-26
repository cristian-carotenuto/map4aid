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
                "Mi spieghi come fare la registrazione?",
                "Voglio registrarmi sul sito, cosa devo fare?",
                "Passaggi per la creazione account?",
                "Dove trovo il modulo di registrazione?",
                "Posso creare un profilo nuovo?",
                "Istruzioni per l'iscrizione a Map4Aid."
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
                "Che opzioni di donazione ci sono?",
                "Potete dirmi come donare?",
                "Cosa accettate come donazione?",
                "Posso donare sia soldi che cibo?",
                "Quali tipi di aiuti posso inviare?",
                "Elenco delle modalità di aiuto disponibili."
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
                "Mi aiuti a fare una donazione economica?",
                "Passaggi per la donazione monetaria.",
                "Posso donare con carta di credito?",
                "Come invio un contributo in denaro?",
                "Metodi di pagamento per le donazioni.",
                "Vorrei supportare economicamente un ente."
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
                "Dove gestisco la disponibilità dei beni?",
                "Un ente come aggiorna il magazzino?",
                "Procedura per inserire nuovi beni materiali.",
                "Come vedo cosa è disponibile in magazzino?",
                "Posso diminuire le scorte manualmente?",
                "Gestione inventario per gli enti erogatori."
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
                "Come si prenota un ritiro sulla mappa?",
                "Ho bisogno di cibo, come prenoto?",
                "Punti di ritiro sulla mappa, come scelgo?",
                "Voglio prenotare un orario per il ritiro.",
                "Cosa devo fare per ricevere un pacco aiuti?",
                "Prenotazione dei beni di prima necessità."
            ],
            "answer": "Sulla mappa di Map4Aid trovi i punti di ritiro. Selezionane uno, scegli i beni che ti servono e prenota uno slot orario disponibile. Riceverai una conferma della prenotazione per il ritiro."
        },
        {
            "intent": "mappa_utilita",
            "questions": [
                "A cosa serve la mappa?",
                "Perché c'è una mappa nella home?",
                "Cosa posso vedere sulla mappa?",
                "Mi spieghi la funzione della mappa?",
                "Come uso la mappa del sito?",
                "Qual è lo scopo della mappa in homepage?",
                "Cosa indicano i punti sulla mappa?",
                "Posso navigare sulla mappa?",
                "La mappa mostra i centri di aiuto?",
                "Utilità della mappa per l'utente."
            ],
            "answer": "La mappa presente nella homepage serve per mostrarti i punti di distribuzione, se vuoi puoi prenotare il ritiro di beni cliccando su uno dei punti."
        },
        {
            "intent": "mappa_problemi_geo",
            "questions": [
                "Perché la mappa non mostra i punti vicino a me?",
                "Non vedo la mia posizione sulla mappa.",
                "La geolocalizzazione non funziona.",
                "Perché la mappa è vuota intorno a me?",
                "Problemi con la posizione sulla mappa.",
                "Come attivo la posizione sulla mappa?",
                "Ho negato i permessi di posizione, come risolvo?",
                "La mappa non mi trova.",
                "Perché non vedo i punti di ritiro vicini?",
                "Mappa e permessi di geolocalizzazione."
            ],
            "answer": "Se la mappa non mostra i punti di ritiro vicino alla tua posizione probabilmente è perché hai negato al sito l'autorizzazione per conoscere la tua posizione; senza quell'autorizzazione non possiamo sapere dove ti trovi. Per risolvere facilmente il problema ti basterà ricaricare la pagina e consentire alla richiesta che ti apparirà in alto a sinistra."
        },
        {
            "intent": "descrizione_progetto",
            "questions": [
                "che cos'è Map4Aid?",
                "Di cosa si occupa questo sito?",
                "Qual è lo scopo di Map4Aid?",
                "Mi parli del progetto Map4Aid?",
                "Chi ha creato Map4Aid e perché?",
                "Quali servizi offre Map4Aid?",
                "Map4Aid spiegazione breve.",
                "A chi è rivolto Map4Aid?",
                "Cosa posso fare su questo portale?",
                "Missione di Map4Aid."
            ],
            "answer": "Map4Aid è un sito che nasce con lo scopo di aiutare coloro in difficoltà fornendo loro servizi semplici per prenotare il ritiro di beni di prima necessità. Allo stesso tempo ha lo scopo di fornire a coloro che desiderano aiutarci un interfaccia semplice sia per organizzare la donazione dei beni sia per partecipare attivamente alle donazioni, sia dei beni materiali che di denaro."
        },
        {
            "intent": "identita_bot",
            "questions": [
                "Chi sei tu?",
                "Come ti chiami?",
                "Sei un'intelligenza artificiale?",
                "Qual è il tuo compito?",
                "Mi spieghi chi sei?",
                "Chi è Aidano?",
                "Sei un assistente virtuale?",
                "Con chi sto parlando?",
                "Presentati Aidano.",
                "Cosa puoi fare per me?"
            ],
            "answer": "Io sono Aidano sono un chatbot con il quale puoi interagire liberamente, sono stato programmato per rispondere alle tue domande e ai tuoi dubbi. Sentiti libero di scrivere per qualsiasi quesito o problematica tu possa incontrare sul nostro sito."
        },
        {
            "intent": "stato_animo",
            "questions": [
                "Come stai?",
                "Tutto bene?",
                "Come va?",
                "Aidano, come ti senti oggi?",
                "Sei in forma?",
                "Come procede il tuo lavoro?",
                "Stai bene Aidano?",
                "Ciao Aidano, come stai?",
                "Ehi, come te la passi?",
                "Tutto a posto?"
            ],
            "answer": "Benone sono felice di aiutare i miei utenti :) Fammi sapere se hai qualsiasi domanda sul nostro sito"
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
