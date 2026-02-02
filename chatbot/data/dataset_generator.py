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
                "Istruzioni per l'iscrizione a Map4Aid.",
                "Come posso registrarmi come beneficiario?",
                "Qual è la procedura per iscriversi come donatore?",
                "Come si crea un profilo per un ente erogatore?"
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
            "answer": "Sì, puoi recuperare l'email associata al tuo account cliccando su 'Email dimenticata' nella pagina di login. Il sistema invierà un codice SMS di sicurezza (OTP) al numero di telefono associato al tuo profilo. Una volta inserito il codice correttamente, l'email ti verrà mostrata a schermo."
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
            "answer": "Effettuare una donazione monetaria è semplice: clicca sul componente 'Donazione monetaria' nell'interfaccia, scegli l'ente erogatore a cui vuoi destinare i fondi e compila il modulo con i dati del tuo metodo di pagamento. Una volta confermata, riceverai una notifica di successo."
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
            "answer": "Se desideri donare oggetti o viveri, devi compilare la 'Proposta di Donazione Materiale'. Indica i dettagli dei beni; l'ente convaliderà la tua proposta e, se accettata, riceverai via email le istruzioni per il ritiro o la consegna."
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
                "Missione di Map4Aid.",
                "Puoi descrivermi Map4Aid?",
                "Vorrei capire meglio cos'è questo progetto.",
                "Quali sono gli obiettivi principali di Map4Aid?",
                "A cosa serve Map4Aid?",
                "Puoi farmi un riassunto di Map4Aid?"
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
                "Cosa puoi fare per me?",
                "Dimmi chi sei.",
                "Cosa rappresenta Aidano?",
                "Sei un robot?",
                "Qual è la tua funzione qui?",
                "Parlami un po' di te."
            ],
            "answer": "Io sono Aidano, l'assistente virtuale ufficiale di Map4Aid. Sono qui per rispondere alle tue domande e aiutarti a navigare sul sito. Non abbiamo una mail di supporto dedicata, quindi sentiti libero di chiedere a me per qualsiasi dubbio o problema!"
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
                "Tutto a posto?",
                "Ti senti bene oggi?",
                "Come sta andando la giornata?",
                "Sei pronto ad aiutarmi?",
                "Va tutto per il meglio?",
                "Ti piace il tuo lavoro di assistente?"
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
            "intent": "beni_alimentari",
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

        # =========================
        # NUOVI INTENTI AGGIUNTI
        # =========================
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
                "Tasto profilo, come lo uso?",
                "Come entro nella mia area utente?"
            ],
            "answer": "Per accedere al tuo profilo devi prima eseguire il login. Subito dopo averlo fatto verrai riportato nella nostra homepage, da lì dovrai solamente cliccare nella parte alta sul bottone che dice \"Profilo\"."
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
                "Donazioni effettuate, dove le vedo?"
            ],
            "answer": "Per controllare le tue donazioni devi aver eseguito l'accesso e spostarti nella tua area personale (Tasto \"Profilo\" in alto a destra). Fatto questo vedrai la pagina del tuo profilo nella quale ti basterà cliccare su \"Donazioni\" per visualizzare lo storico delle tue donazioni."
        },
        {
            "intent": "storico_prenotazioni",
            "questions": [
                "Come faccio a controllare quali beni ho prenotato?",
                "Dove vedo le prenotazioni dei beni?",
                "Come controllo le prenotazioni fatte?",
                "Posso vedere cosa ho prenotato?",
                "Elenco delle mie prenotazioni, dove si trova?",
                "Voglio sapere quali beni ho prenotato.",
                "Come visualizzo le prenotazioni attive?",
                "Dove trovo le mie prenotazioni?",
                "Come verifico i beni prenotati?",
                "Prenotazioni a mio nome, dove le vedo?",
                "Come controllo i pacchi che ho prenotato?"
            ],
            "answer": "Per verificare quali beni hai prenotato è necessario che tu abbia eseguito l'accesso al nostro sito, dopodiché ti basterà andare nella tua area personale (Tasto \"Profilo\" in alto a destra) e poi nella pagina del tuo profilo cliccando su \"Prenotazioni\" visualizzerai tutte le prenotazioni a tuo nome."
        },

        # =========================
        # Fallback (fuori dominio)
        # =========================
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