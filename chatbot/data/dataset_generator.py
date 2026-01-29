import json

def generate_variations():
    """Genera variazioni di domande e risposte basate sui template dei casi d'uso raffinati e allineati alla nuova UI."""
    
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
            "answer": "Per registrarti su Map4Aid, accedi alla pagina di registrazione cliccando su \"Sign Up\", poi dovrai selezionare il ruolo con cui desideri registrarti, scegliendone uno tra: Beneficiario, Donatore e Ente erogatore, poi compila il modulo con i tuoi dati. A seconda del ruolo scelto saranno richiesti dati diversi, ma per tutti serve inserire una E-mail e creare una password. Donatori ed Enti dovranno fornire anche IBAN o Partita IVA."
        },
        {
            "intent": "password_dimenticata",
            "questions": [
                "Cosa succede se dimentico la mia password?",
                "Ho perso la password, come faccio?",
                "Non ricordo la password per il login.",
                "Come resetto la password?",
                "Password dimenticata, quali sono i passaggi?",
                "Posso recuperare la chiave di accesso?",
                "Mi sono scordato la password.",
                "C'è un modo per cambiare la password persa?",
                "Reset password Map4Aid.",
                "Cosa fare se non riesco ad entrare per la password?"
            ],
            "answer": "Non preoccuparti! Se dimentichi la password, clicca su 'Password dimenticata' nella pagina di login. Il sistema ti invierà un'email con un link per resettarla. Assicurati che la nuova password rispetti gli standard di sicurezza richiesti."
        },
        {
            "intent": "email_dimenticata",
            "questions": [
                "Posso recuperare la mia email se la dimentico?",
                "Non ricordo quale email ho usato per registrarmi.",
                "Come trovo l'email del mio account?",
                "Email dimenticata, come faccio il recupero?",
                "C'è una procedura per l'email persa?",
                "Ho scordato l'indirizzo email di Map4Aid.",
                "Come recupero il mio username email?",
                "Recupero account tramite numero di telefono.",
                "Cosa fa il tasto Email dimenticata?",
                "Come funziona l'OTP per recuperare l'email?"
            ],
            "answer": "Sì, puoi recuperare l'email associata al tuo account cliccando su 'Email dimenticata' nella pagina di login. Il sistema invierà un codice temporaneo (OTP) al numero di telefono associato al tuo profilo. Una volta inserito il codice correttamente, l'email ti verrà mostrata a schermo."
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
            "answer": "Su Map4Aid puoi effettuare due tipi di donazioni: donazioni monetarie (fondi destinati agli enti erogatori) e donazioni di beni materiali (oggetti o viveri che vengono poi convalidati e ritirati dall'ente). Puoi scegliere la modalità più adatta a te direttamente dall'interfaccia principale, dopo aver selezionato la donazione che preferisci dovrai compilare il modulo richiesto prima di poter ultimare la tua donazione."
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
            "answer": "Effettuare una donazione monetaria è semplice: clicca sul componente 'Donazione monetaria' nell'interfaccia, scegli l'ente erogatore a cui vuoi destinare i fondi e compila il modulo with i dati del tuo metodo di pagamento. Una volta confermata, riceverai una notifica di successo."
        },
        {
            "intent": "donazione_materiale",
            "questions": [
                "Posso donare beni materiali invece di denaro?",
                "Come dono vestiti o cibo?",
                "Procedura per la donazione di oggetti materiali.",
                "Voglio regalare dei prodotti agli enti.",
                "Come funziona il ritiro dei beni donati?",
                "Donare beni fisici su Map4Aid.",
                "Modulo per la donazione materiale.",
                "Cosa succede dopo che propongo una donazione di beni?",
                "Validazione della donazione materiale.",
                "Come invio beni materiali agli enti erogatori?"
            ],
            "answer": "Certamente! Se sei registrato come donatore, puoi compilare un modulo specifico per la donazione di beni materiali. Dovrai inserire i dettagli degli oggetti che intendi donare; la richiesta verrà inviata all'ente per la validazione. Se approvata, riceverai un'email con le istruzioni per il ritiro."
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
                "Posso diminuire le scorte manually?",
                "Gestione inventario per gli enti erogatori."
            ],
            "answer": "La gestione delle scorte è riservata agli enti erogatori tramite la dashboard dedicata. Le quantità si aggiornano automaticamente in caso di donazioni ricevute o prenotazioni effettuate. È tuttavia possibile aggiungere manualmente nuovi beni o incrementare le scorte esistenti, ma la riduzione manuale non è consentita per garantire la coerenza dei dati."
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
            "answer": "Per prenotare un ritiro, visualizza i punti disponibili sulla mappa di Map4Aid e seleziona quello di tuo interesse. Potrai visualizzare i beni disponibili in ogni punto, dopo aver individuato il punto di tuo interesse potrai prenotare uno slot orario specifico per recarti al punto di ritiro e ricivere il tuo pacco."
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
            "answer": "La mappa presente nella homepage serve per mostrarti i punti di distribuzione, dai quali è possibile ritirare beni di prima necessità, cliccando su uno dei punti potrai visualizzare ciò che è disponibile ritirare in quel punto e prenotare uno slot orario per andarci e ricevere il tuo pacco."
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
            "answer": "Se la mappa non mostra i punti di ritiro vicino alla tua posizione probabilmente è perché hai negato al sito l'autorizzazione per conoscere la tua posizione; senza quell'autorizzazione non possiamo sapere dove ti trovi. Per risolvere facilmente il problema ti basterà ricaricare la pagina e cliccare su \"Usa la mia posizione\" in alto a sinistra, dopo di che dovrai anche acconsentire alla richiesta che ti apparirà leggermente più in alto, cliccando su \"Consenti durante la visita al sito\" oppure su \"consenti questa volta\"."
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
            "answer": "Benone sono felice di aiutare i miei utenti :) Fammi sapere se hai una qualsiasi domanda sul nostro sito"
        },
        {
            "intent": "filtri_mappa",
            "questions": [
                "A cosa servono i filtri?",
                "Come funzionano i filtri della mappa?",
                "Perché dovrei usare i filtri?",
                "Spiegami il sistema di filtraggio.",
                "Cosa succede se clicco su un filtro?",
                "Come mostro solo certi punti sulla mappa?",
                "Utilizzo dei filtri in alto a sinistra.",
                "Filtrare i punti di interesse.",
                "A cosa serve il menu dei filtri?",
                "Posso vedere solo le categorie che mi interessano?"
            ],
            "answer": "Il sistema di filtraggio che vedi in alto a sinistra serve per mostrare sulla mappa solo i punti di interesse nei quali è possibile ritirari beni di una determinata categoria, cliccando su uno dei filtri veranno visualizzati sulla mappa solo i punti nei quali è possibile ritirare i beni di quella specifica categoria"
        },
        {
            "intent": "categorie_beni",
            "questions": [
                "Quali sono le categorie di beni che posso ritirare?",
                "Che tipi di beni ci sono su Map4Aid?",
                "Quali categorie di prodotti gestite?",
                "Elenco delle categorie di beni disponibili.",
                "Cosa si può trovare nei pacchi aiuti?",
                "Come sono classificati i beni di prima necessità?",
                "Quante categorie di beni esistono nel sistema?",
                "Posso sapere i tipi di prodotti ritirabili?",
                "Medicinali o vestiti, cosa offrite?",
                "Categorie di aiuto disponibili."
            ],
            "answer": "Sul nostro sito i beni di prima necessità sono classificati secondo 4 categorie: Alimentari, Igiene Personale, Medicinali e Abbigliamento, è possibile filtrare i punti che appaiono sulla mappa per mostrare solo quelli dai quali è possibile ritirare i beni di quella specifica cattegoria"
        },
        {
            "intent": "visualizzare_alimentari",
            "questions": [
                "Come faccio a visualizzare i beni alimentari?",
                "Voglio vedere solo i punti con cibo.",
                "Come trovo i beni alimentari sulla mappa?",
                "Procedura per filtrare i beni alimentari.",
                "Dove sono i centri che distribuiscono cibo?",
                "Come attivo il filtro alimentare?",
                "Vedere solo la categoria alimentari sulla mappa.",
                "C'è un modo per isolare i beni alimentari?",
                "Mappa dei punti di ritiro cibo.",
                "Come cerco aiuti alimentari?"
            ],
            "answer": "La nostra mappa è fornita di una serie di punti di ritiro che se cliccati mostrano quale categoria di bene è possibile ritirare in quel punto. Se desidere filtrare solo i beni di una determinata categoria puoi usare il sistema di filtraggio in alto a sinistra dal quale potrai selezionare una categoria di beni e la mappa mostrerà automaticamente solo i punti nei quali è possibile ritirare i beni di quella categoria."
        },
        {
            "intent": "scelta_ruolo",
            "questions": [
                "Perchè nella registrazione devo scegliere un ruolo?",
                "Cosa cambia tra i ruoli nella registrazione?",
                "Perché Map4Aid chiede il mio ruolo?",
                "Che differenza c'è tra Beneficiario ed Ente?",
                "Quale ruolo dovrei scegliere per registrarmi?",
                "Importanza del ruolo nell'account.",
                "Posso cambiare ruolo dopo la registrazione?",
                "Perché il donatore ha campi diversi?",
                "Scelta tra Beneficiario, Donatore ed Ente.",
                "A cosa servono i 3 ruoli distinti?"
            ],
            "answer": "Map4aid mette a disposizione dei suoi utenti registrati 3 ruoli distinti: Il primo è Beneficiario, registrati come tale per poter visualizzare i punti di ritiro e prenotare gli slot orari nei quali recarti nel punto per ricevere il tuo pacco. Puoi anche registrarti come donatore o Ente erogatore nel caso tu abbia interesse a donare beni materiali o monetari piuttosto che usufluire del servizio di aiuti di prima necessità"
        },
        {
            "intent": "notifiche_chiarimento",
            "questions": [
                "Perchè ho ricevuto un E-mail?",
                "Come mai mi è arrivata una mail da Map4Aid?",
                "Ho ricevuto un messaggio OTP sul telefono, perché?",
                "Perchè ricevo un SMS da voi?",
                "Ricevuta mail non richiesta, cosa significa?",
                "Perché Map4Aid mi manda messaggi sul cellulare?",
                "Motivi per cui il sito invia notifiche.",
                "Spiegazione email o SMS ricevuto.",
                "Qualcuno ha usato il mio numero per errore?",
                "Ho un messaggio da Map4Aid ma non stavo facendo nulla."
            ],
            "answer": "Se hai ricevuto un'email o un SMS da Map4Aid senza aver fatto nulla, probabilmente un altro utente ha inserito per errore i tuoi dati. Solitamente queste comunicazioni servono per confermare operazioni o recuperare l'account. Troverai comunque il motivo specifico spiegato chiaramente all'interno del messaggio ricevuto."
        },
        {
            "intent": "fallback",
            "questions": [
                "Qual è la capitale della Francia?",
                "Come si cucina la pasta alla carbonara?",
                "Chi ha vinto l'ultimo mondiale di calcio?",
                "Mi consigli un film da vedere stasera?",
                "Come posso riparare una lavatrice?",
                "Qual è la distanza tra la Terra e la Luna?",
                "Mi scrivi una poesia d'amore?",
                "Come si dice 'ciao' in giapponese?",
                "Chi è il presidente degli Stati Uniti?",
                "Qual è la radice quadrata di 144?"
            ],
            "answer": "Mi dispiace non dispongo delle conoscenze per rispondere a questa domanda"
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
