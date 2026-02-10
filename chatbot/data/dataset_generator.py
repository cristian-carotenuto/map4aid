import json
import os
import random
from typing import Dict, List


def generate_variations(seed: int = 42):
    """
    Genera 3 dataset JSONL a partire dai template:

    1) training_data_expanded.jsonl
       - Formato: system/user/assistant (risposta testuale)
       - Se "answers" è una lista: genera una riga per ogni (domanda, variante risposta)

    2) training_intent.jsonl
       - Formato: system/user/assistant (label intent)
       - Una riga per ogni domanda

    3) training_answerable.jsonl  (COERENZA)
       - Formato: system/user/assistant (ANSWERABLE / NOT_ANSWERABLE)
       - Input include: Domanda + Intent + Risposta candidata
       - Per ogni domanda:
           * 1 esempio positivo (ANSWERABLE) con risposta del proprio intent
           * N esempi negativi (NOT_ANSWERABLE) con risposte prese da intent "confondibili"

    + (NUOVO) aidano_runtime_config.json
       - intent_labels, fixed_answers, confusable, ecc.
    """

    random.seed(seed)

    templates = [
        # --- START (tuoi template invariati) ---
        {
            "intent": "registrazione",
            "questions": [
                "Come mi registro?",
                "Come faccio a registrarmi?",
                "Cosa devo fare per registrarmi?",
                "Come posso registrarmi a Map4Aid?",
                "Mi spieghi come fare la registrazione?",
                "Voglio registrarmi sul sito, cosa devo fare?",
                "Quali sono i passaggi per creare un account?",
                "Dove trovo il modulo di registrazione?",
                "Posso creare un nuovo profilo?",
                "Registrazione.",
                "Come posso registrarmi come beneficiario?",
                "Come faccio a registrarmi come donatore?",
                "Come ci si registra come ente erogatore?",
                "Devo registrarmi, come faccio?",
                "Come posso effettuare la registrazione al sito?"
            ],
            "answers": [
                "Per registrarti su Map4Aid clicca su Sign Up, seleziona il ruolo (Beneficiario, Donatore o Ente erogatore) e compila il modulo con i dati richiesti.",
                "Per registrarti su Map4Aid clicca su Sign Up, scegli uno dei ruoli disponibili (Beneficiario, Donatore, Ente erogatore) e completa il modulo di registrazione.",
                "Se vuoi creare un account su Map4Aid, premi Sign Up, seleziona il ruolo con cui vuoi registrarti e inserisci le informazioni richieste nel form.",
                "La registrazione su Map4Aid si effettua da Sign Up: scegli il tuo ruolo tra Beneficiario, Donatore ed Ente erogatore e compila i campi richiesti."
            ]
        },
        {
            "intent": "password_dimenticata",
            "questions": [
                "Cosa succede se dimentico la mia password?",
                "Ho perso la password, come faccio?",
                "Non ricordo la password per il login.",
                "Come resetto la password?",
                "Password dimenticata.",
                "Posso recuperare la password?",
                "Ho dimenticato la password.",
                "Posso cambiare la password se la dimentico?",
                "Reset password.",
                "Password errata.",
                "La password è sbagliata, cosa faccio?",
                "Cosa faccio se non ricordo la password?"
            ],
            "answers": [
                "Se dimentichi la password, nella pagina di Login clicca su Password dimenticata. Il sistema ti invierà un’email con un link per reimpostarla.",
                "Se hai dimenticato la password, dalla pagina di Login clicca su Password dimenticata: riceverai un’email con un link per reimpostarla.",
                "Se non ricordi la password, vai nella pagina di Login e seleziona Password dimenticata. Il sistema ti invierà un’email per reimpostarla."
            ]
        },
        {
            "intent": "email_dimenticata",
            "questions": [
                "Posso recuperare la mia email se la dimentico?",
                "Non ricordo quale email ho usato per registrarmi.",
                "Come faccio se ho perso l'email?",
                "Email persa.",
                "C'è una procedura per l'email persa?",
                "Ho scordato l'indirizzo email.",
                "Come recupero la mia email?",
                "Recupero email.",
                "Ho perso l'indirizzo email.",
                "Email dimenticata.",
                "Cosa faccio se ho dimenticato l'email?"
            ],
            "answers": [
                "Puoi recuperare l’email associata al tuo account dalla pagina di Login: clicca su Email dimenticata. Il sistema invierà un codice via SMS al numero di telefono associato al profilo; inserendo il codice, l’email verrà mostrata a schermo.",
                "Per recuperare l’email, dalla pagina di Login clicca su Email dimenticata: riceverai un SMS con un codice sul numero associato all’account. Inserisci il codice per visualizzare l’email a schermo.",
                "Se hai dimenticato l’email, vai nella pagina di Login e seleziona Email dimenticata. Ti verrà inviato un SMS con un codice da inserire per visualizzare l’email associata all’account."
            ]
        },
        {
            "intent": "tipi_donazione",
            "questions": [
                "Che tipo di donazioni posso effettuare?",
                "Quali sono le modalità di donazione?",
                "Cosa posso donare?",
                "In che modo posso aiutare tramite donazioni?",
                "Che opzioni di donazione ci sono?",
                "Come donare?",
                "Cosa accettate come donazione?",
                "Quali tipi di aiuti posso inviare?",
                "Modalità di donazione.",
                "Che donazioni posso fare?",
                "Posso donare solo denaro?",
                "Posso donare solo beni materiali?"
            ],
            "answers": [
                "Su Map4Aid puoi effettuare due tipi di donazioni: donazioni monetarie e donazioni di beni materiali. Puoi scegliere la modalità che preferisci dall’interfaccia principale.",
                "Map4Aid supporta due modalità di donazione: in denaro oppure tramite beni materiali. Puoi selezionare quella che preferisci dall’interfaccia principale.",
                "Puoi donare in due modi: con una donazione monetaria o con una donazione di beni materiali. La scelta si effettua dall’interfaccia principale."
            ]
        },
        {
            "intent": "donazione_monetaria",
            "questions": [
                "Come faccio a donare soldi?",
                "Voglio fare una donazione in denaro.",
                "Come funzionano le donazioni monetarie?",
                "Dove posso donare fondi agli enti?",
                "Mi aiuti a fare una donazione?",
                "Donazione monetaria.",
                "Posso donare con carta di credito?",
                "Come faccio una donazione in denaro?",
                "Metodi di pagamento per le donazioni.",
                "Vorrei supportare economicamente un ente.",
                "Se voglio donare dei soldi come faccio?"
            ],
            "answers": [
                "Per effettuare una donazione monetaria clicca su Donazione monetaria, scegli l’ente erogatore a cui destinare i fondi e l’importo da donare, poi compila il modulo con i dati richiesti. Una volta confermata la donazione, riceverai una notifica di successo.",
                "Per fare una donazione monetaria, seleziona Donazione monetaria, indica l’ente destinatario e l’importo, quindi inserisci i dati richiesti per completare la procedura. Al termine riceverai una notifica di conferma.",
                "Per donare denaro su Map4Aid vai su Donazione monetaria, scegli l’ente e l’importo, poi completa il modulo. Dopo la conferma, il sistema ti mostrerà una notifica di esito."
            ]
        },
        {
            "intent": "donazione_di_beni",
            "questions": [
                "Posso donare beni materiali?",
                "Come dono vestiti o cibo?",
                "Procedura per la donazione di beni materiali.",
                "Voglio regalare dei beni materiali.",
                "Come funziona la donazione dei beni?",
                "Donare beni fisici.",
                "Modulo per la donazione materiale.",
                "Donazione di beni.",
                "Posso fare una donazione materiale?",
                "Come invio beni materiali?",
                "Donazione beni di prima necessità",
                "Se voglio donare dei beni come faccio?"
            ],
            "answer": (
                "Se desideri donare oggetti o viveri puoi accedere alla sezione dedicata dalla home e seguire le istruzioni indicate a schermo. "
                "La proposta verrà poi valutata dall’ente erogatore e, se accettata, riceverai un’email con le indicazioni per il ritiro o la consegna."
            )
        },
        {
            "intent": "prenotazione_beni",
            "questions": [
                "Come prenoto un pacco?",
                "Voglio ritirare dei beni, come faccio?",
                "Come funziona la prenotazione dei beni?",
                "Posso scegliere un punto per ritirare dei beni?",
                "Come si prenota un ritiro sulla mappa?",
                "Ho bisogno di cibo, come faccio?",
                "Mi servono dei vestiti, come li ritiro?",
                "Come faccio a prenotare dei beni?",
                "Cosa devo fare per ricevere un pacco?",
                "Prenotazione dei beni di prima necessità.",
                "Mi servono delle medicine, come faccio?",
                "Per ritirare dei beni cosa devo fare?",
                "Se voglio ritirare dei beni cosa devo fare?"
            ],
            "answers": [
                "Per prenotare un pacco di beni utilizza la mappa presente nella home: seleziona un punto di distribuzione, verifica i beni disponibili e prenota uno slot orario. Poi recati al punto di distribuzione nell’orario scelto per ritirare il pacco.",
                "Il ritiro dei beni si prenota dalla mappa: scegli un punto di distribuzione, controlla i beni disponibili e seleziona uno slot orario. Successivamente recati al punto nell’orario prenotato.",
                "Per ritirare dei beni utilizza la mappa e seleziona un punto di tuo interesse. Potrai visualizzare i beni disponibili in quel punto e prenotare uno slot orario per recarti al punto di distribuzione e ricevere il pacco."
            ]
        },
        {
            "intent": "mappa_utilita",
            "questions": [
                "A cosa serve la mappa?",
                "Perché c'è una mappa nella home?",
                "Cosa posso vedere sulla mappa?",
                "Mi spieghi la funzione della mappa?",
                "Come uso la mappa del sito?",
                "Qual è lo scopo della mappa?",
                "Cosa indicano i punti sulla mappa?",
                "Come si usa la mappa?",
                "Perché c'è una mappa?",
                "Utilità della mappa."
            ],
            "answers": [
                "La mappa nella homepage serve per mostrarti i punti di distribuzione dai quali è possibile ritirare beni di prima necessità.",
                "Tramite la mappa puoi visualizzare i punti di distribuzione da cui è possibile ritirare beni di prima necessità.",
                "La mappa serve per mostrarti i punti di distribuzione dai quali è possibile ritirare i pacchi di beni disponibili."
            ]
        },
        {
            "intent": "mappa_problemi",
            "questions": [
                "Perché la mappa non mostra i punti vicino a me?",
                "Non vedo i punti vicini alla mia posizione sulla mappa.",
                "La geolocalizzazione non funziona.",
                "Perché la mappa non mostra la mia zona?",
                "Problemi con la posizione sulla mappa.",
                "Come attivo la posizione sulla mappa?",
                "Ho negato i permessi di posizione, come risolvo?",
                "La mappa non mi trova.",
                "Perché vedo punti di ritiro lontani da me?",
                "Perché non vedo i punti di distribuzione vicino a me?",
                "Problemi sulla mappa.",
                "I punti di ritiro sono troppo lontani"
            ],
            "answers": [
                "Se la mappa non mostra i punti vicini a te, probabilmente non hai concesso al sito i permessi di geolocalizzazione. Ricarica la pagina e concedi i permessi quando richiesto.",
                "I problemi della mappa sono spesso dovuti ai permessi di geolocalizzazione negati: senza autorizzazione non possiamo determinare la tua posizione. Ricarica la pagina e consenti l’accesso alla posizione quando richiesto.",
                "Se vedi punti lontani o non vedi quelli vicini, controlla i permessi di geolocalizzazione del browser per Map4Aid. Poi ricarica la pagina e autorizza la posizione."
            ]
        },
        {
            "intent": "descrizione_progetto",
            "questions": [
                "Che cos'è Map4Aid?",
                "Di cosa si occupa questo sito?",
                "Qual è lo scopo di Map4Aid?",
                "Mi parli del progetto Map4Aid?",
                "Cosa fa il sito Map4Aid?",
                "Map4Aid spiegazione.",
                "Perché esiste Map4Aid?",
                "Cosa posso fare su questo portale?",
                "Missione di Map4Aid.",
                "Puoi descrivermi Map4Aid?",
                "Vorrei capire meglio cosa fa questo sito.",
                "Quali sono gli obiettivi di Map4Aid?",
                "A cosa serve Map4Aid?",
                "Puoi farmi un riassunto di Map4Aid?"
            ],
            "answer": (
                "Map4Aid è una piattaforma nata per supportare le persone in difficoltà consentendo loro di prenotare il ritiro di beni di prima necessità. "
                "Allo stesso tempo permette a chi lo desidera di contribuire tramite donazioni monetarie o di beni materiali."
            )
        },
        {
            "intent": "identita_bot",
            "questions": [
                "Ciao chi sei?",
                "Chi sei tu?",
                "Come ti chiami?",
                "Sei un'intelligenza artificiale?",
                "Qual è il tuo compito?",
                "Mi spieghi chi sei?",
                "Chi è Aidano?",
                "Sei un assistente virtuale?",
                "Con chi sto parlando?",
                "Presentati.",
                "Cosa puoi fare per me?",
                "Dimmi chi sei.",
                "Sei un robot?",
                "Qual è la tua funzione qui?",
                "Parlami un po' di te."
            ],
            "answers": [
                "Io sono Aidano, l’assistente virtuale ufficiale di Map4Aid. Posso aiutarti a navigare sul sito e a rispondere alle tue domande sul suo funzionamento.",
                "Ciao! Sono Aidano, l’assistente virtuale di Map4Aid. Sono qui per aiutarti con registrazione, login, donazioni, mappa e prenotazione dei beni.",
                "Mi chiamo Aidano e sono l’assistente virtuale di Map4Aid: posso guidarti nell’utilizzo delle funzionalità principali della piattaforma."
            ]
        },
        {
            "intent": "stato_animo",
            "questions": [
                "Come stai?",
                "Tutto bene?",
                "Hey come va?",
                "Aidano, come ti senti oggi?",
                "Sei in forma?",
                "Come procede il tuo lavoro?",
                "Stai bene Aidano?",
                "Ciao Aidano, come stai?",
                "Ehi, come te la passi?",
                "Tutto a posto?",
                "Ti senti bene oggi?",
                "Come sta andando la giornata?",
                "Sei pronto ad aiutarmi?",
                "Va tutto per il meglio?",
                "Ti piace il tuo lavoro di assistente?"
            ],
            "answers": [
                "Sto bene, grazie! Dimmi pure di cosa hai bisogno su Map4Aid.",
                "Tutto bene! Se hai domande su Map4Aid, sono qui per aiutarti.",
                "Sto bene e sono pronto ad aiutarti: chiedimi pure informazioni su Map4Aid."
            ]
        },
        {
            "intent": "filtri_mappa",
            "questions": [
                "A cosa servono i filtri?",
                "Come funzionano i filtri della mappa?",
                "Perché ci sono quei filtri?",
                "Spiegami il sistema di filtraggio.",
                "Cosa succede se clicco su un filtro?",
                "Come faccio a filtrare la mappa?",
                "Utilizzo dei filtri in alto a sinistra.",
                "Filtrare i punti di interesse.",
                "A cosa serve il menu dei filtri?",
                "Posso vedere solo i punti di beni alimentari?",
                "Posso vedere i punti per ritirare i vestiti?",
                "Posso vedere i punti per le medicine?"
            ],
            "answers": [
                "I filtri servono a mostrare sulla mappa solo i punti di distribuzione relativi a una specifica categoria di beni. Selezionando un filtro, la mappa si aggiornerà di conseguenza.",
                "Con i filtri puoi visualizzare solo i punti di distribuzione che offrono una determinata categoria (ad esempio alimentari, vestiti o medicinali).",
                "Il sistema di filtraggio permette di limitare i punti mostrati sulla mappa in base alla categoria di beni selezionata."
            ]
        },
        {
            "intent": "categorie_beni",
            "questions": [
                "Quali sono le categorie di beni che posso ritirare?",
                "Che tipi di beni ci sono sul sito?",
                "Quali categorie di prodotti gestite?",
                "Elenco dei beni disponibili.",
                "Cosa si può trovare nei pacchi aiuti?",
                "Come sono classificati i beni?",
                "Quante categorie di beni esistono nel sistema?",
                "Posso sapere i tipi di prodotti ritirabili?",
                "Cosa offrite per il ritiro?",
                "Beni disponibili."
            ],
            "answers": [
                "Su Map4Aid i beni di prima necessità sono classificati in quattro categorie: Alimentari, Igiene personale, Medicinali e Vestiti.",
                "Le categorie di beni disponibili su Map4Aid sono quattro: Alimentari, Igiene personale, Medicinali e Vestiti.",
                "I beni sono suddivisi in 4 categorie: Alimentari, Igiene personale, Medicinali e Vestiti."
            ]
        },
        {
            "intent": "accesso_profilo",
            "questions": [
                "Come accedo al mio profilo?",
                "Come entro nel mio profilo?",
                "Dove posso trovare il mio profilo?",
                "Come faccio ad aprire la mia area personale?",
                "Voglio accedere al profilo, come si fa?",
                "Dopo il login come vado nel profilo?",
                "Come visualizzo il mio profilo utente?",
                "Non trovo il profilo, dove si accede?",
                "Come raggiungo la sezione profilo?",
                "Cosa fa il tasto profilo?",
                "Come entro nella mia area utente?"
            ],
            "answers": [
                "Per accedere al profilo devi prima effettuare il login. Una volta nella homepage, puoi aprire il profilo tramite il tasto dedicato in alto.",
                "L’accesso al profilo è disponibile solo dopo il login: dalla homepage puoi aprire la tua area personale con il tasto profilo in alto.",
                "Dopo aver effettuato l’accesso, dalla homepage puoi entrare nel profilo usando il tasto dedicato in alto."
            ]
        },
        {
            "intent": "storico_donazioni",
            "questions": [
                "Come faccio a vedere le mie donazioni?",
                "Dove vedo le donazioni che ho fatto?",
                "Posso controllare lo storico delle donazioni?",
                "Come visualizzo le mie donazioni passate?",
                "Voglio vedere le donazioni effettuate.",
                "C’è una sezione con le mie donazioni?",
                "Come controllo cosa ho donato?",
                "Dove trovo l’elenco delle mie donazioni?",
                "Posso vedere le donazioni dal profilo?",
                "Come verifico le donazioni fatte?",
                "Donazioni effettuate.",
                "Donazioni passate."
            ],
            "answers": [
                "Per vedere lo storico delle donazioni devi aver effettuato il login e accedere al profilo. Dal menù a sinistra puoi aprire la sezione Donazioni per visualizzare lo storico.",
                "Lo storico delle donazioni è disponibile nel profilo dopo il login: usa il menù a sinistra e seleziona la sezione Donazioni.",
                "Per controllare lo storico delle tue donazioni devi aver effettuato l’accesso e accedere alla tua area personale. Dalla pagina del profilo puoi visualizzare lo storico delle donazioni tramite il menù a sinistra."
            ]
        },
        {
            "intent": "storico_prenotazioni",
            "questions": [
                "Come faccio a controllare quali beni ho prenotato?",
                "Dove vedo le prenotazioni dei beni?",
                "Come controllo le prenotazioni fatte?",
                "Posso vedere cosa ho prenotato?",
                "Elenco prenotazioni.",
                "Voglio sapere quali beni ho prenotato.",
                "Come visualizzo le prenotazioni attive?",
                "Dove trovo le mie prenotazioni?",
                "Come verifico i beni prenotati?",
                "Beni prenotati da me.",
                "Come controllo i pacchi che ho prenotato?"
            ],
            "answers": [
                "Per verificare le prenotazioni devi eseguire il login e accedere al profilo. Dal menù a sinistra puoi visualizzare le prenotazioni associate al tuo account.",
                "Dopo il login, nella pagina del profilo puoi consultare le prenotazioni dal menù a sinistra.",
                "Per verificare quali beni hai prenotato devi aver eseguito l’accesso al sito. Dalla tua area personale, nella pagina del profilo, puoi visualizzare tutte le prenotazioni a tuo nome tramite il menù a sinistra."
            ]
        },
        {
            "intent": "problemi_login",
            "questions": [
                "Il login non funziona.",
                "Non riesco a loggarmi.",
                "Non riesco a fare il login.",
                "Errore nel login.",
                "Non posso fare il login.",
                "Che faccio se il login non funziona?",
                "Il login non va.",
                "Perché non riesco a fare login?",
                "Il login è rotto.",
                "Impossibile eseguire il login.",
                "Non mi fa loggare.",
                "Il sito non permette il login."
            ],
            "answers": [
                "Se non riesci a fare login, verifica di aver inserito correttamente email e password. Se mi indichi quale dei due campi risulta errato posso aiutarti in modo più preciso.",
                "I problemi di login sono spesso dovuti a email o password inserite in modo errato. Se mi dici quale campo dà errore posso darti indicazioni più mirate.",
                "Se non riesci a effettuare il login probabilmente non sei registrato oppure stai inserendo in modo errato l’email o la password. Se mi indichi quale dei due campi risulta errato posso aiutarti in modo più preciso."
            ]
        },
        {
            "intent": "non_disponibile",
            "questions": [
                "Ci sono dei piani della zona?",
                "Esiste un piano della zona?",
                "Quali requisiti sanitari servono?",
                "Dove inserisco lo stato di salute?"
            ],
            "answer": (
                "Non ho informazioni ufficiali su questa funzionalità in Map4Aid. "
                "Posso aiutarti con registrazione, login, donazioni, utilizzo della mappa e prenotazione dei beni."
            )
        }
        # --- END ---
    ]

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Output
    out_expanded = os.path.join(script_dir, "training_data_expanded.jsonl")
    out_intent = os.path.join(script_dir, "training_intent.jsonl")
    out_answerable = os.path.join(script_dir, "training_answerable.jsonl")
    out_runtime_cfg = os.path.join(script_dir, "aidano_runtime_config.json")

    # Prompt storico generativo
    system_prompt = (
        "Sei Aidano, l’assistente virtuale ufficiale di Map4Aid.\n\n"
        "Map4Aid è una piattaforma di aiuti che consente sia di ricevere beni di prima necessità "
        "sia di contribuire aiutando altre persone tramite donazioni monetarie o materiali.\n\n"
        "Il tuo compito è rispondere alle domande degli utenti in modo chiaro, diretto e conciso, "
        "utilizzando esclusivamente informazioni ufficiali relative al funzionamento di Map4Aid.\n\n"
        "Non fare supposizioni, non inventare funzionalità e non fornire informazioni esterne al progetto.\n"
        "Se una domanda non riguarda Map4Aid o se non disponi di informazioni certe, rispondi esclusivamente con:\n"
        "\"Mi dispiace, non dispongo delle conoscenze per rispondere a questa domanda.\""
    )

    def iter_answers(item: dict) -> List[str]:
        """Supporta sia 'answers' (lista) sia 'answer' (stringa)."""
        if "answers" in item and isinstance(item["answers"], list):
            return item["answers"]
        return [item["answer"]]

    # Prompt intent classification (label-only)
    intent_labels = sorted({t["intent"].strip().lower() for t in templates})
    intent_system = (
        "Sei un classificatore di intent per Map4Aid.\n"
        "Rispondi con UNA SOLA etichetta, senza testo aggiuntivo.\n"
        f"Etichette possibili: {', '.join(intent_labels)}, NONE.\n"
        "Regole:\n"
        "- Se la domanda non rientra chiaramente in una delle etichette, rispondi: NONE\n"
        "- Non aggiungere spiegazioni.\n"
    )

    # Prompt answerable/coerenza (label-only)
    answerable_system = (
        "Valuta se la RISPOSTA CANDIDATA è pertinente alla DOMANDA dell’utente.\n"
        "Rispondi SOLO con una parola:\n"
        "ANSWERABLE oppure NOT_ANSWERABLE\n\n"
        "ANSWERABLE: la risposta candidata risponde correttamente alla domanda.\n"
        "NOT_ANSWERABLE: la risposta candidata non è coerente con la domanda.\n"
    )

    # Costruisco una mappa intent -> risposte disponibili (pool per negativi)
    intent_to_answers: Dict[str, List[str]] = {}
    for item in templates:
        i = item["intent"].strip().lower()
        intent_to_answers[i] = iter_answers(item)

    # Intent confondibili: genera negativi più “difficili”
    confusable: Dict[str, List[str]] = {
    "donazione_di_beni": ["prenotazione_beni", "tipi_donazione", "categorie_beni", "donazione_monetaria"],
    "donazione_monetaria": ["tipi_donazione", "donazione_di_beni", "categorie_beni"],
    "tipi_donazione": ["donazione_di_beni", "donazione_monetaria", "categorie_beni"],
    "categorie_beni": ["tipi_donazione", "donazione_di_beni", "donazione_monetaria"],

    "prenotazione_beni": ["donazione_di_beni", "mappa_utilita"],
    "storico_donazioni": ["storico_prenotazioni", "accesso_profilo"],
    "storico_prenotazioni": ["storico_donazioni", "accesso_profilo"],

    # Famiglia MAPPA: qui c'era la confusione reale dai log
    "mappa_utilita": ["filtri_mappa", "mappa_problemi", "prenotazione_beni", "descrizione_progetto"],
    "filtri_mappa": ["mappa_utilita", "mappa_problemi"],
    "mappa_problemi": ["mappa_utilita", "filtri_mappa", "prenotazione_beni"],

    "problemi_login": ["password_dimenticata", "email_dimenticata", "accesso_profilo"],
    "password_dimenticata": ["problemi_login", "email_dimenticata"],
    "email_dimenticata": ["problemi_login", "password_dimenticata"],

    "identita_bot": ["stato_animo", "descrizione_progetto"],
    "stato_animo": ["identita_bot"],
    "descrizione_progetto": ["identita_bot", "mappa_utilita"],
}


    # Sanity check: confusable deve riferirsi a intent esistenti
    all_intents = set(intent_to_answers.keys())
    for k, lst in confusable.items():
        if k not in all_intents:
            raise ValueError(f"confusable contiene key non valida: {k}")
        missing = [x for x in lst if x not in all_intents]
        if missing:
            raise ValueError(f"confusable[{k}] contiene intent non validi: {missing}")

    # Quanti negativi per ogni domanda (oltre il positivo)
    NEGATIVES_PER_QUESTION = 2

    def make_answerable_payload(question: str, intent: str, candidate_answer: str) -> str:
        return f"Domanda: {question}\nIntent stimato: {intent}\nRisposta candidata: {candidate_answer}"

    def write_runtime_config(path: str) -> None:
        fixed_answers = {}
        for item in templates:
            intent = item["intent"].strip().lower()
            fixed_answers[intent] = iter_answers(item)

        cfg = {
            "intent_labels": intent_labels + ["NONE"],
            "fixed_answers": fixed_answers,
            "confusable": confusable,
            "negatives_per_question": NEGATIVES_PER_QUESTION,
            "fallback_intent": "NONE",
            "not_supported_intent": "non_disponibile",
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)

    with open(out_expanded, "w", encoding="utf-8") as f_exp, \
         open(out_intent, "w", encoding="utf-8") as f_int, \
         open(out_answerable, "w", encoding="utf-8") as f_ans:

        for item in templates:
            intent = item["intent"].strip().lower()
            answers = iter_answers(item)

            for q in item["questions"]:
                # 1) Storico generativo
                for a in answers:
                    entry_exp = {
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": q},
                            {"role": "assistant", "content": a}
                        ]
                    }
                    f_exp.write(json.dumps(entry_exp, ensure_ascii=False) + "\n")

                # 2) Intent label-only
                entry_int = {
                    "messages": [
                        {"role": "system", "content": intent_system},
                        {"role": "user", "content": q},
                        {"role": "assistant", "content": intent}
                    ]
                }
                f_int.write(json.dumps(entry_int, ensure_ascii=False) + "\n")

                # 3) Answerable/coerenza label-only
                if intent == "non_disponibile":
                    continue

                # Positivo: risposta corretta del proprio intent (prima variante)
                pos_answer = answers[0]
                entry_pos = {
                    "messages": [
                        {"role": "system", "content": answerable_system},
                        {"role": "user", "content": make_answerable_payload(q, intent, pos_answer)},
                        {"role": "assistant", "content": "ANSWERABLE"}
                    ]
                }
                f_ans.write(json.dumps(entry_pos, ensure_ascii=False) + "\n")

                # Negativi
                neg_sources = confusable.get(intent, [])
                if not neg_sources:
                    neg_sources = [i for i in intent_to_answers.keys() if i not in (intent, "non_disponibile")]

                chosen_intents = random.sample(
                    neg_sources,
                    k=min(NEGATIVES_PER_QUESTION, len(neg_sources))
                )

                for neg_intent in chosen_intents:
                    pool = intent_to_answers.get(neg_intent, [])
                    if not pool:
                        continue
                    neg_answer = random.choice(pool)
                    entry_neg = {
                        "messages": [
                            {"role": "system", "content": answerable_system},
                            {"role": "user", "content": make_answerable_payload(q, intent, neg_answer)},
                            {"role": "assistant", "content": "NOT_ANSWERABLE"}
                        ]
                    }
                    f_ans.write(json.dumps(entry_neg, ensure_ascii=False) + "\n")

    write_runtime_config(out_runtime_cfg)

    print(f">> Dataset espanso generato con successo in {out_expanded}")
    print(f">> Dataset intent generato con successo in {out_intent}")
    print(f">> Dataset answerable (coerenza) generato con successo in {out_answerable}")
    print(f">> Config runtime generata con successo in {out_runtime_cfg}")


if __name__ == "__main__":
    generate_variations()
