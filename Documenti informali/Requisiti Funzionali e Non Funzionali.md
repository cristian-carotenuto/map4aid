Funzionalità principali Map4Aid


Funzionalità #1 – #Login e registrazione --->
Si danno per scontate, ma si precisa una distinzione al momento della registrazione in base al tipo di attività che si vuole effettuare (donatore o ricevitore). Questo serve a creare due tipologie di richieste di dati diverse, con lo scopo di migliorare la protezione delle informazioni ed evitare di chiedere dati inutili agli utenti (es. Gino il panettiere).

Funzionalità #2 – #Modifica dei dati --->
Anche questa è data per scontata, ma va comunque segnalata in quanto deve essere implementata.


Funzionalità #3 – #Filtraggio della mappa --->
La mappa deve consentire di filtrare i punti di raccolta/distribuzione in base all’utente che utilizza la piattaforma, permettendo all'utente di visualizzare solo gli elementi rilevanti e ridurre il sovraccarico visivo. Esempi:
-Filtro per punti di raccolta
-Filtro per punti di distribuzione (filtra magari per i punti di distribuzione pubblici, dato che
può servire all’ente sapere i punti di distribuzione pubblici cosa mettono a disposizione)


Funzionalità #4 – #Donazione monetaria --->
Come in molti altri enti, si dà all’utente la possibilità di effettuare una donazione in denaro. Questa verrà probabilmente gestita come una donazione diretta verso un ente: l’utente dovrà quindi solo inserire l’importo e i dati di base per il pagamento (che dovranno essere gestiti in maniera appropriata e sicura). A differenza della donazione di beni, questa funzionalità potrebbe essere disponibile anche per utenti non registrati o non loggati, poiché i dati richiesti sono diversi e in ogni caso i dati comuni (nome, cognome, ecc.) andrebbero comunque reinseriti nel form di pagamento.


Funzionalità #5 – #Donazione di beni --->
L'utente registrato (o loggato) può donare beni materiali (alimenti, vestiti, medicinali, ecc.) a enti specifici. Per fare ciò, l'utente deve essere registrato come donatore e deve essere assegnato a una categoria di donazione specifica (ad esempio, donatori di alimenti, donatori di medicinali, ecc.). Successivamente, l'utente compila un modulo specifico che raccoglie informazioni dettagliate sui beni che intende donare (il modulo varia a seconda della tipologia di donazione). Il modulo viene inviato all'ente ricevente, che convalida i dati forniti. In caso di validazione positiva, l'ente invia un'email al donatore con informazioni sul ritiro dei beni da parte dell'ente.


Funzionalità #6 – #Prenotazione ritiro beni di prima necessità --->
L’utente registrato come beneficiario avrà la possibilità di prenotare il ritiro di beni di prima necessità direttamente dalla mappa. Dopo aver selezionato un punto di distribuzione, il sistema mostrerà gli slot orari disponibili (Ricorda la suddivisione degli slot è di importanza cruciale dato che nessun utente beneficiario deve avere interazioni anche solo visive con
altri utenti beneficiari) in base alla disponibilità dell’ente e alla tipologia dei beni (alimentari,
vestiti, farmaci, ecc.).
L’ente ricevente potrà così verificare la prenotazione e aggiornare automaticamente le
scorte dei beni distribuiti, mantenendo il tracciamento anonimo dei movimenti.
I dati relativi al ritiro (ente, data, tipo di bene, quantità) saranno poi consultabili dallo stesso utente nello storico delle prenotazioni.


Funzionalità #7 – #Segnalazione punti di bisogno sulla mappa --->
L’utente potrà segnalare sulla mappa aree o punti di bisogno in cui ritiene necessario attivare un punto di raccolta o distribuzione (ad esempio zone con famiglie in difficoltà o situazioni di emergenza).
Durante la segnalazione, potrà indicare alcune informazioni necessarie come la posizione del luogo, la tipologia del bisogno (alimentare, sanitario…) con una breve descrizione del problema.
Le segnalazioni verranno inviate agli enti amministratori che successivamente alla verifica, decideranno se approvarle attivando un nuovo punto sulla mappa o respingerle
 
Funzionalità #8 - #Gestione variazione delle scorte da parte degli enti --->
Il sistema deve poter permettere agli enti erogatori di monitorare in tempo reale le scorte di beni disponibili nei propri punti di raccolta o distribuzione. Il sistema deve poter permettere di aggiornare automaticamente tali scorte in base ai flussi di entrata (donazioni) e i flussi di uscita (consegne ai cittadini). In pratica il sistema deve sempre sapere quanti beni ci sono, dove e in che stato

Funzionalità #9 – #Sistema di Notifiche e Avvisi --->
Il sistema deve inviare notifiche automatiche agli utenti e agli enti in seguito a eventi rilevanti come:
-	Conferma  di una prenotazione
-	Disponibilità di nuovi beni compatibili con le preferenze dell’utente o compatibili con le patologie inseriti (Es. Viene assegnato del pane senza glutine al punto di distribuzione A, allora agli utenti che avevano inserito come patologia celiachia verrà mandata una notifica di ciò)
-	Scadenza di prenotazioni non ritirate
Le notifiche verranno mandate o per e-mail o tramite un’area notifiche interna alla piattaforma

Funzionalità #10 – #Storico Attività e Reportistica --->
Il sistema deve permettere a ogni utente (donatore, ente o beneficiario) di poter visualizzare uno storico delle attività svolte:
-	Donatori: elenco delle donazioni effettuate con data, luogo e tipologia di bene
-	Beneficiari: elenco dei ritiri effettuati o prenotati (con all’interno ciò che è stato
selezionato)
-	Enti: elenco dei beni ricevuti e beni distribuiti
Il sistema deve consentire la generazione di report periodici (settimanali, mensili, annuali) scaricabili in formato PDF

Funzionalità #11 – #Sistema di Valutazione e Feedback --->
Dopo ogni interazione di ritiro, il sistema deve permettere agli utenti di lasciare un feedback.
-	Gli utenti beneficiari possono valutare la qualità dell’assistenza ricevuta e
l’organizzazione del punto di distribuzione (IDEA: valutazione in formato 5 stelle con
recensione)
-	Agli enti sarà mandata una notifica della valutazione in modo che potranno visualizzare le valutazioni per migliorare il servizio


Funzionalità #12 – #Sistema di filtraggio del catalogo e collegamento ai punti di distribuzione --->
Sappiamo che il sistema ha un catalogo dei beni ben organizzato per gerarchie, ma deve anche fornire una sezione sulla piattaforma dove visualizzare il catalogo globale quindi con tutti i beni presenti in un tutto i punti di distribuzione; in modo che quando un utente seleziona uno specifico bene, verrà filtrata la mappa solo con i punti di distribuzione che detengono quel bene.
Il catalogo deve presentare dei filtri specifici per semplificare il lavoro di ricerca all’utente (Es. Filtro per macrocategoria, poi per sottocategoria, poi magari per bene specifico se serve tipo pane senza glutine) quindi avremo un sistema di filtraggio gerarchico per semplificare il tutto




Requisiti non funzionali


Requisito n.f. #1-usabilità della mappa
La mappa del sistema deve garantire una lettura intuitiva, con una legenda che spieghi i simboli utilizzati e con simboli autoesplicativi che rendano chiaro il loro significato senza necessità di ulteriori spiegazioni (es. Croce Rossa per i medicinali), tenendo conto che contrasto tra simboli e mappa deve essere ben marcato affinché i simboli non si confondano con la mappa stessa. Il requisito funzionale #2 favorisce questo punto. L’obiettivo principale è migliorare la fruibilità e l’esperienza utente, permettendo una navigazione chiara, intuitiva e personalizzata in base alle esigenze dell’utente.


Requisito n.f. #2: Persistenza dei dati
Il sistema deve garantire la sincronizzazione tra utenti, ove è richiesta (es. prenotazione di un bene). Requisito fondamentale affinché venga garantita la persistenza e coerenza dei dati.
Requisito n.f. #2.1: Efficienza sulla sincronizzazione
Per evitare che un utente tenga una sessione occupata per troppo tempo (ad esempio, nel caso in cui abbia dimenticato aperta la pagina relativa a un prodotto che non desidera più prenotare), è necessario implementare un timer che, allo scadere, liberi la sessione e la renda disponibile per altri utenti. Questo meccanismo è essenziale per prevenire il rallentamento del sistema e per massimizzare la disponibilità dei beni per gli utenti che ne hanno effettivamente bisogno


Requisito n.f. #3 – Gestione Tassonomia e Catalogo dei Beni
 
Il sistema deve fornire una Tassonomia gerarchica dei beni, in modo che i beni vengano suddivisi in più categorie (es. Cibo/Vestiti/Farmaci) e poi una suddivisione in sottocategorie (es.
Felpe/Giubbotti/Scarpe); tutto questo per avere una suddivisione logica dei beni in modo che:
-	Gli Enti erogatori associno obbligatoriamente ogni lotto di beni a delle categorie e sottocategorie definite nel catalogo

Requisito n.f. #4 – Scalabilità sul numero di punti di interesse
Il sistema deve essere progettato per gestire l'inserimento di almeno 10 milioni di punti di interesse senza compromettere la velocità di aggiornamento della mappa e dei filtri.


Requisito n.f #5 - Protezione dei Dati e Autenticazione
Il sistema deve garantire la sicurezza dei dati, in particolare per quanto riguarda le informazioni sensibili relative alla distribuzione di beni di prima necessità (ad esempio, dettagli degli enti di distribuzione, dati degli utenti registrati). Deve essere implementato un sistema di protezione robusto per evitare accessi non autorizzati. I dati sensibili devono essere criptati in transito e in archivio. Il sistema deve implementare una autenticazione sicura per gli utenti (ad esempio, autenticazione a due fattori - 2FA) per l'accesso alle aree riservate del sito (come la gestione dei punti di distribuzione). L'applicazione deve rispettare le normative sulla privacy (ad esempio, GDPR in Europa) per la gestione dei dati personali degli utenti e delle organizzazioni.

