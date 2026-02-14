<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*REQUIREMENTS ANALYSIS DOCUMENT*

# Sommario

[**1. ATTORI [3](#attori)**](#attori)

[**2. REQUISITI FUNZIONALI [4](#requisiti-funzionali)**](#requisiti-funzionali)

[**3. REQUISITI NON FUNZIONALI [8](#requisiti-non-funzionali)**](#requisiti-non-funzionali)

[**4. SCENARI [10](#scenari)**](#scenari)

[**5. USE CASE [38](#use-case)**](#use-case)

[**6. OGGETTI ENTITY, BOUNDARY E CONTROL [53](#oggetti-entity-boundary-e-control)**](#oggetti-entity-boundary-e-control)

[**7. SEQUENCE DIAGRAMS [62](#sequence-diagrams)**](#sequence-diagrams)

[**8. STATECHART DIAGRAMS [66](#statechart-diagrams)**](#statechart-diagrams)

[**9. ACTIVITY DIAGRAM [70](#activity-diagramprenotazione-di-un-bene)**](#activity-diagramprenotazione-di-un-bene)

# ATTORI

Il funzionamento di **MAP4AID** coinvolge diverse tipologie di utenti, ognuna caratterizzata da necessità e responsabilità distinte. La definizione dei seguenti attori permette di delineare con chiarezza chi opera sul sistema e quali compiti è autorizzato a svolgere:

- **Utente**

Si riferisce a chiunque acceda e utilizzi il sistema.

- **Utente non registrato**

**Ruolo**: Navigazione della mappa geolocalizzata, filtraggio dei beni per tipologia (cibo, farmaci ecc.) e ricezione di informazioni tramite e-mail.

- **Utente registrato** (Classe Padre per Utente Beneficiario, Donatore, Erogatore e Amministratore)

**Ruolo**: Effettua il login, gestisce il proprio profilo, visualizza lo storico delle attività e può effettuare donazioni monetarie.

- **Utente beneficiario**

**Ruolo**: Include tutte le funzioni dell’utente non autenticato; permette inoltre di tenere traccia delle richieste passate, gestire lo storico delle prenotazioni, ricevere notifiche push, prenotare beni e cancellare prenotazioni esistenti.

- **Ente Donatore **

**Ruolo**: Include tutte le funzioni dell’utente non autenticato; si occupa della donazione di beni e dell'interazione con l’ente erogatore.

- **Ente Erogatore**

**Ruolo**: Include tutte le funzioni dell’utente non autenticato; gestisce l'inserimento e l'aggiornamento della disponibilità dei beni, amministra le prenotazioni e inoltra richieste all'amministratore per i punti di bisogno.

- **Amministratore di sistema**

**Ruolo**:  Provvede alla validazione degli account beneficiari tramite verifica dei documenti d’identità e gestisce i punti di distribuzione sul territorio.

# REQUISITI FUNZIONALI

- **Funzionalità \#1 – Registrazione**

Il sistema deve poter permettere a un nuovo utente di potersi registrare e quindi creare un nuovo account inserendo le informazioni richieste. 

- **Funzionalità \#1.1 – Registrazione per “Utente beneficiario”**

- Il sistema deve poter permettere a un nuovo utente di registrarsi come “utente beneficiario” al fine di usare le funzionalità specifiche per questa tipologia di utente

- **Funzionalità \#1.2 – Registrazione per “Ente donatore”**

- Il sistema deve poter permettere a un nuovo utente di registrarsi come “ente donatore” al fine di usare le funzionalità specifiche per questa tipologia di utente

- **Funzionalità \#1.3 –Registrazione per “Ente erogatore”**

- Il sistema deve poter permettere a un nuovo utente di registrare la propria organizzazione, quindi di registrarsi come “ente erogatore” al fine di usare le funzionalità specifiche per questa tipologia di utente 

- **Funzionalità \#1.4 -Validazione account “beneficiario”**

- Il sistema deve permettere all’amministratore di poter validare l’account di un utente beneficiario

<!-- -->

- **Funzionalità \#2 – Login**

Il sistema deve poter permettere a un utente di effettuare il login al proprio account, (o account dell’organizzazione se si tratta di un operatore dell’ente), tramite l’inserimento delle proprie credenziali 

- **Funzionalità \#3 – Logout**

Il sistema deve poter permettere a un utente di effettuare il logout dal proprio account (o account dell’organizzazione se si tratta di un operatore dell’ente)

- **Funzionalità \#4 – Visualizzazione profilo**

Il sistema deve poter permettere a ogni utente registrato di visualizzare il proprio profilo

- **Funzionalità \#5 – Modifica profilo**

Il sistema deve poter permettere a ogni utente registrato di modificare il proprio profilo

- **Funzionalità \#5.1 – Modifica profilo per “utente beneficiario"**

> Il sistema deve poter permettere a un utente beneficiario di modificare il proprio profilo, e quindi di modificare i dati per questa tipologia di utente 

- **Funzionalità \#5.2 – Modifica profilo per “ente donatore”**

> Il sistema deve poter permettere a ente donatore di modificare il proprio profilo, e quindi di modificare i dati per questa tipologia di utente

- **Funzionalità \#5.3 – Modifica profilo per “ente erogatore”**

> Il sistema deve poter permettere agli utenti che hanno l’accesso all’account della propria organizzazione registrata come “ente erogatore”, di modificare il profilo dell’organizzazione, e quindi di modificare i dati per questa tipologia di utente 

- **Funzionalità \#6 – Inserimento conto bancario per ente erogatore**

Il sistema deve permettere a un ente erogatore di inserire i dati di un proprio conto bancario affinché un qualsiasi utente possa effettuare una donazione

- **Funzionalità \#7 – Filtraggio della mappa**

Il sistema deve consentire all’utente di visualizzare punti di distribuzione sulla mappa in base a criteri visualizzabili, tra i quali: fascia oraria di attività 

- **Funzionalità \#8 – Donazione monetaria**

Il sistema deve consentire a un qualsiasi utente registrato di effettuare una donazione monetaria selezionando l’ente desiderato tra quelli disponibili, poi l’importo desiderato

- **Funzionalità \#9 – Donazione di beni**

Il sistema deve consentire a un utente registrato come “ente donatore” di effettuare una donazione di beni 

- **Funzionalità \#10 – Prenotazione beni**

Il sistema deve consentire a soli utenti registrati come “utente beneficiario” di effettuare la prenotazione di un qualsiasi bene disponibile in un qualsiasi punto di distribuzione 

- **Funzionalità \#11 – Cancellazione prenotazione**

Il sistema deve poter permettere a un utente beneficiario o ente erogatore che ha effettuato una prenotazione di un bene di cancellare la prenotazione 

- **Funzionalità \#12  – Validazione prenotazione di un medicinale**

Il sistema deve permettere ad un ente erogatore di validare una prenotazione di tipo “medicinale”

- **Funzionalità \#13 – Generazione QR code**

Il sistema dopo ogni prenotazione di un bene deve generare un QR code univoco e inviarlo all’utente beneficiario che ha conseguito la prenotazione  

- **Funzionalità \#14 – Segnalazione punti di bisogno sulla mappa**

Il sistema deve permettere a un utente di segnalare un punto di bisogno sulla mappa, indicando il luogo in cui ritiene necessario attivare un punto di distribuzione.

- **Funzionalità \#15 – Gestione dei beni nei punti di distribuzione**

Il sistema deve consentire agli enti erogatori la gestione dei beni presenti nei punti di distribuzione

- **Funzionalità \#15.1 – Aggiunta dei beni nei punti di distribuzione**

> Il sistema deve permettere agli enti erogatori di aggiungere dei beni nei punti di distribuzione specificando quantità e categoria 

- **Funzionalità \#15.2 – Rimozione dei beni nei punti di distribuzione**

> Il sistema deve permettere agli enti erogatori di rimuovere dei beni nei punti di distribuzione specificando quantità e categoria

- **Funzionalità \#15.3 – Modifica della quantità dei beni nei punti di distribuzione**

> Il sistema deve permettere di aggiornare la quantità dei beni nei punti di distribuzione, aggiungendo o rimuovendo dei beni in base alla tipologia del flusso.

- **Funzionalità \#16 – Notifiche e Avvisi (per email)**

Il sistema deve generare notifiche per email per informare gli utenti degli eventi che li riguardano 

- **Funzionalità \#17 – Visualizza storico attività**

Il sistema deve poter permettere a ogni utente registrato di poter visualizzare il proprio storico delle attività, che sarà differente in base al proprio ruolo all’interno della piattaforma

- **Funzionalità \#17.1 – Visualizza storico attività per “Utente beneficiario”**

> Il sistema deve consentire a un utente beneficiario di visualizzare il proprio storico delle attività 

- **Funzionalità \#17.2 – Visualizza storico attività per “Ente donatore”**

> Il sistema deve consentire a un ente donatore di visualizzare il proprio storico delle attività 

- **Funzionalità \#17.3 – Visualizza storico attività per “Ente erogatore”**

> Il sistema deve consentire agli utenti che hanno l’accesso all’account della propria organizzazione, registrata come “ente donatore”, di visualizzare lo storico delle attività della propria organizzazione 

- **Funzionalità \#18 – Download storico attività **

Il sistema deve poter permettere agli utenti registrati di poter scaricare il proprio storico attività in formato PDF

- **Funzionalità \#19 – Invio di valutazione e feedback**

Il sistema dopo ogni ritiro di bene e verifica del QR code dell’utente beneficiario in questione, deve consentire agli utenti beneficiari di inviare una feedback con valutazione all’ente erogatore da cui ha effettuato la prenotazione del bene 

- **Funzionalità \#21 – Gestione punti di distribuzione**

Il sistema deve poter permettere agli enti erogatori di gestire i propri punti di distribuzione

- **Funzionalità \#21.1 – Richiesta di aggiunta di un punto di distribuzione**

> Il sistema deve poter permettere a un ente erogatore di mandare una richiesta per aprire un nuovo punto di distribuzione che verrà poi gestita dall’amministratore 

- **Funzionalità \#21.2 – Aggiunta di un punto di distribuzione**

> Il sistema deve consentire l’aggiunta di punto di distribuzione. 

- **Funzionalità \#21.3 – Rimozione di un punto di distribuzione**

> Il sistema deve poter permettere a un ente erogatore di rimuovere un proprio punto di distribuzione 

- **Funzionalità \#21.4 – Aggiornamento punti di distribuzione**

> Il sistema deve poter permettere agli enti erogatori di poter aggiornare i propri punti di distribuzione, aggiornando gli orari e i giorni di attività del punto

- **Funzionalità \#22 – Visualizzazione richieste di aggiunta punti distribuzione**

Il sistema deve permettere all’amministratore di poter visualizzare le richieste di aggiunta di punti di distribuzione da parte degli enti erogatori

- **Funzionalità \#23 – Gestione richieste di aggiunta punti di distribuzione**

Il sistema deve permettere all’amministratore di gestire le richieste di aggiunta di punti di distribuzione, potendo accettare o rifiutare tali richieste. L’accettazione porta all’aggiunta automatica del punto di distribuzione coi suoi dati inviati dall’utente , mentre il rifiuto genera semplicemente un messaggio alle notifiche interne della piattaforma sul profilo dell’utente.

- **Funzionalità \#24 – Visualizzazione punti di distribuzione**

Il sistema deve permettere a ogni utente di poter visualizzare ogni punto di distribuzione sulla mappa, vedendo informazioni come orari e giorni di attività e categorie di beni presenti 

- **Funzionalità \#25 – Visualizzazione prenotazioni effettuate in corso**

Il sistema deve permettere agli utenti beneficiari che hanno una prenotazione in corso, di visualizzare la prenotazioni

# REQUISITI NON FUNZIONALI

- **Requisito n.f. \#1-usabilità della mappa**

La mappa del sistema deve garantire una lettura intuitiva, con una legenda che spieghi i simboli utilizzati e con simboli autoesplicativi che rendano chiaro il loro significato senza necessità di ulteriori spiegazioni (es. Croce Rossa per i medicinali), tenendo conto che contrasto tra simboli e mappa deve essere ben marcato affinché i simboli non si confondano con la mappa stessa. Il requisito funzionale \#2 favorisce questo punto. L’obiettivo principale è migliorare la fruibilità e l’esperienza utente, permettendo una navigazione chiara, intuitiva e personalizzata in base alle esigenze dell’utente.

- **Requisito n.f. \#2-Persistenza dei dati**

Il sistema deve garantire la sincronizzazione tra utenti, ove è richiesta (es. prenotazione di un bene). Requisito fondamentale affinché venga garantita la persistenza e coerenza dei dati.

- **Requisito n.f. \#3- Efficienza sulla sincronizzazione**

Per evitare che un utente tenga una sessione occupata per troppo tempo (ad esempio, nel caso in cui abbia dimenticato aperta la pagina relativa a un prodotto che non desidera più prenotare), è necessario implementare un timer che, allo scadere, liberi la sessione e la renda disponibile per altri utenti. Questo meccanismo è essenziale per prevenire il rallentamento del sistema e per massimizzare la disponibilità dei beni per gli utenti che ne hanno effettivamente bisogno

- **Requisito n.f. \#4 – Gestione Tassonomia e Catalogo dei Beni**

Il sistema deve fornire una Tassonomia gerarchica dei beni, in modo che i beni vengano suddivisi in più categorie (es. Cibo/Vestiti/Farmaci) e poi una suddivisione in sottocategorie (es.Felpe/Giubbotti/Scarpe); tutto questo per avere una suddivisione logica dei beni in modo che gli Enti erogatori associno obbligatoriamente ogni lotto di beni a delle categorie e sottocategorie definite nel catalogo

- **Requisito n.f. \#5 – Scalabilità sul numero di punti di interesse**

Il sistema deve essere progettato per gestire l'inserimento di almeno 10 milioni di punti di interesse senza compromettere la velocità di aggiornamento della mappa e dei filtri.

- **Requisito n.f \#6 - Protezione dei Dati e Autenticazione**

Il sistema deve garantire la sicurezza dei dati, in particolare per quanto riguarda le informazioni sensibili relative alla distribuzione di beni di prima necessità (ad esempio, dettagli degli enti di distribuzione, dati degli utenti registrati). Deve essere implementato un sistema di protezione robusto per evitare accessi non autorizzati. I dati sensibili devono essere criptati in transito e in archivio. Il sistema deve implementare una autenticazione sicura per gli utenti (ad esempio, autenticazione a due fattori - 2FA) per l'accesso alle aree riservate del sito (come la gestione dei punti di distribuzione). L'applicazione deve rispettare le normative sulla privacy (ad esempio, GDPR in Europa) per la gestione dei dati personali degli utenti e delle organizzazioni.

- 

# SCENARI

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>12</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Visualizzazione dello storico delle donazioni</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente registrato</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi è un utente registrato (ovvero un beneficiario un Ente donatore o un Ente erogatore) alla piattaforma MAP4AID, nel corso degli ultimi mesi in cui è stato registrato ha effettuato 3 donazioni monetarie la prima 4 giorni fa all’ente “Croce Rossa”, la seconda 20 giorni fa all’ente “Save The Children” e la terza 50 giorni fa all’ente “Unicef”.</p>
<p>Adesso ha dimenticato le quantità esatte donate a questi 3 enti, dunque, decide di accedere al sistema per verificare lo storico delle sue donazioni.</p>
<p>Mario, quindi, accede al sistema inserendo la sua E-mail Mariorossi67@gmail.com con la relativa password “password” e una volta che ha inserito i dati corretti il sistema lo riconosce e gli consente di accedere alla sua area utente.</p>
<p>A questo punto Mario clicca sul menù a tendina che si apre e tra le varie opzioni presenti sceglie quella che gli interessa, cioè, “Storico donazioni”.</p>
<p>Il sistema reindirizza Mario su una nuova pagina con tutte le donazioni effettuate.</p>
<p>Nella riga legata alla giornata di 4 giorni fa a Mario viene mostrata la sua donazione dove può vedere che l’ente che ha ricevuto i soldi era “Croce Rossa” e la donazione aveva un valore di 50 €, Mario avendo visualizzato il dato che gli interessava torna indietro.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>13</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Beneficiario scarica lo storico delle prenotazioni</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Paolo Verdi = Beneficiario</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Paolo Verdi è un Utente registrato alla piattaforma MAP4AID come Beneficiario, nel corso degli ultimi mesi in cui è stato registrato ha effettuato diverse prenotazioni per beni di prima necessità di cui aveva bisogno.</p>
<p>Adesso è interessato a scaricare in formato PDF gli storici di queste prenotazioni, Paolo ha interesse a scaricare le sue prenotazioni in formato settimanale mensile e annuale.</p>
<p>Paolo, quindi, accede al sistema e inserisce le credenziali E-mail e password, rispettivamente Paoloverdi67@gmail.com e “password” una volta che il sistema verifica la sua identità gli consente di accedere alla sua pagina utente.</p>
<p>Una volta che ha effettuato l’accesso Paolo clicca sul menu a tendina che si apre e tra le varie opzioni presenti sceglie quella che gli interessa, cioè, “Storico prenotazioni”.</p>
<p>Il sistema porta quindi Paolo su una nuova schermata dove il gli viene chiede “Di quale fascia temporale vuoi visualizzare lo storico?” e gli vengono mostrate 3 opzioni “Settimanale”, “Mensile”, “Annuale”.</p>
<p>Essendo interessato a tutte e 3 Paolo decide di cliccare prima su “Settimanale” il sistema, quindi, carica una nuova pagina, nella quale viene mostrata una tabella con i vari giorni della settimana e sotto di essi le varie prenotazioni effettuate in quel giorno con la relativa fascia oraria e i beni prenotati.</p>
<p>In basso Paolo vede che è presente un bottone che recita “Scarica come PDF” Paolo lo clicca e il sistema va a convertire la tabella in un PDF di 1 pagina dove è presente la tabella, Paolo dopo aver scaricato questo PDF torna indietro per scaricare anche gli altri 2.</p>
<p>Dopo essere tornato alla schermata precedente Paolo seleziona l’opzione “Mensile”, il sistema come prima carica una nuova pagina, stavolta con una tabella mensile strutturata come un calendario per il mese attuale, e nelle caselle legate ai singoli giorni sono presenti le varie prenotazioni effettuate, con i rispettivi dati.</p>
<p>Anche qui è presente il bottone “Scarica come PDF” che quindi Paolo clicca e il sistema converte la tabella mensile in un PDF di una pagina, dopodiché Paolo sceglie di nuovo di tornare indietro per scaricare anche l’ultimo PDF.</p>
<p>Dopo essere tornato indietro e aver aspettato che il sistema carichi di nuovo la pagina stavolta Paolo seleziona l’opzione “Annuale” e ancora una volta il sistema lo porta su una nuova pagina.<br />
Stavolta vengono caricate 12 tabelle ciascuna per il singolo mese dell’anno corrente, è da qui possibile cliccare su una delle 12 tabelle per zoomare su di essa e visualizzarla come se fosse una tabella mensile del caso precedente.</p>
<p>Paolo vede e clicca ancora una volta il bottone “Scarica come PDF” che stavolta scarica l’intero storico come un PDF di 12 pagine, ciascuna rappresenta un mese dell’anno come nel caso del PDF mensile.</p>
<p>A questo punto Paolo ha scaricato tutti i PDF per cui aveva interesse e soddisfatto può chiudere il sistema.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>3</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un utente vuole registrarsi e accedere come “donatore”</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Giovanni Esposito=Utente non registrato</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Giovanni Esposito accede alla homepage della piattaforma Map4aid. Clicca su “registrazione”, gli viene chiesto di scegliere di indicare il tipo di utente da diventare tra: “utente beneficiario”, “ente donatore” ed “ente erogatore”. Giovanni sceglie “ente donatore”. Viene reindirizzato ad un form inerente al donatore. Giovanni compila il form:</p>
<ul>
<li><p>nome: Giovanni</p></li>
<li><p>cognome: Esposito</p></li>
<li><p>email:<a href="mailto:PanificioDivertente@gmail.com"><u>PanificioDivertente@gmail.com</u></a></p></li>
<li><p>password:PaneCaldo24</p></li>
<li><p>Telefono:3245642398</p></li>
<li><p>Partita IVA:74653786543</p></li>
<li><p>Indirizzo sede: via Roma 23,Napoli, 80040</p></li>
<li><p>Settore: alimentare</p></li>
</ul>
<p>Giovanni conferma la registrazione e viene creato l’account, riceve una notifica che avvisa dell’avvenuta creazione dell’account. Per accedere alla piattaforma Giovanni clicca su “login” e inserisce email e password:</p>
<ul>
<li><p>email o username:<a href="mailto:PanificioDivertente@gmail.com"><u>PanificioDivertente@gmail.com</u></a></p></li>
<li><p>password:PaneCaldo24</p></li>
</ul>
<p>Clicca “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come donatore ha accesso a tutte le funzionalità da donatore.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>4</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un utente vuole registrarsi come “ente”</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Croce Rossa=organizzazione che vuole registrarsi come ente</p>
<p>Mattia Accardo=persona che fa parte dell’organizzazione Croce Rossa</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mattia Accardo fa parte dell’organizzazione Croce Rossa ed è incaricato di registrare l’organizzazione come ente sulla piattaforma Map4aid; quindi accede alla homepage della piattaforma Map4aid e clicca su “registrazione”, dopodichè gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mattia sceglie “ente donatore” e viene reindirizzato ad un form inerente all’ente erogatore. Mattia compila il form:</p>
<ul>
<li><p>Email: <a href="mailto:Crocerossa@gmail.com"><u>Crocerossa@gmail.com</u></a></p></li>
<li><p>Password: CroceAiutante</p></li>
</ul>
<ul>
<li><p>Nome dell’ente: Croce Rossa</p></li>
<li><p>Tipologia ente: associazione no-profit</p></li>
<li><p>Indirizzo della sede operativa: Via Pontecitra 76, Marigliano, 80034</p></li>
<li><p>Ambito di intervento: alimentare</p></li>
</ul>
<p>Mattia conferma la registrazione e viene creato l’account, riceve una notifica che avvisa dell’avvenuta creazione dell’account. Per accedere alla piattaforma Mattia clicca su “login” e inserisce email e password:</p>
<ul>
<li><p>email o username:Crocerossa@gmail.com</p></li>
<li><p>password: CroceAiutante</p></li>
</ul>
<p>Clicca “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come ente erogatore ha accesso a tutte le funzionalità da ente erogatore.</p>
<p>Infine Mattia condivide password ed email con tutte le persone facente parti dell’organizzazione</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>10</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Segnalazione di un punto di bisogno sulla mappa da parte di un utente</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Marianna Allocca = Utente</p>
<p>Tutti gli enti registrati alla piattaforma</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Marianna Allocca accede alla homepage di Map4aid e decide di cliccare su “Segnala un punto di bisogno”. Marianna viene reindirizzata su una pagina in cui è presente una mappa dinamica e un campo indirizzo: può scegliere di mandare la segnalazione tramite click sulla mappa oppure inserire un indirizzo specifico. Marianna decide di inserire un indirizzo:</p>
<ul>
<li><p>Indirizzo: Via Sgroppillo, 21, 95027 San Gregorio di Catania</p></li>
</ul>
<p>Marianna clicca su “invia segnalazione”, la segnalazione viene mandata con successo a tutti gli enti erogatori registrati sulla piattaforma. Un pop-up avvisa Marianna che la Segnalazione è andata a buon fine.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>18</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Recupero password da parte di un utente registrato</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Giulia Verdi= Utente registrato</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Giulia prova ad accedere alla piattaforma Map4Aid, ma si rende conto di non ricordare la password che aveva creato.</p>
<p>Dalla pagina di login clicca il link “Password dimenticata?”. Viene reindirizzata ad una pagina che le chiede di inserire l’indirizzo email associato al suo account. Giulia digita: <a href="mailto:giulia.verdi@gmail.com"><u>giulia.verdi@gmail.com</u></a>.</p>
<p>Premendo “Invia”, se l’email è corretta allora riceverà un codice per verificare l’email.</p>
<p>Giulia riceve una email per il recupero password, all’interno del quale c’è un codice che una volta inserito sarà reindirizzata alla pagina per cambiare password.</p>
<p>Giulia inserisce una nuova password: Gv1234* e la conferma. Appare il pop-up “la password è stata aggiornata con successo”.</p>
<p>Torna quindi alla pagina di login, inserisce l’email e la nuova password e accede.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>21</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td><mark>L’utente beneficiario decide di effettuare una prenotazione</mark></td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Mario Nappi = Utente beneficiario</p>
<p><mark>Medici Senza Frontiere</mark> = Ente erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Nappi accede alla homepage e decide di loggarsi con il suo account da “utente beneficiario”: clicca su Login e inserisce username e password:</p>
<ul>
<li><p>email o username: MarioBros</p></li>
<li><p>password:Marione1998</p></li>
</ul>
<p>Clicca su “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come utente beneficiario ha accesso a tutte le funzionalità da beneficiario. Mario ha bisogno di prenotare medicinali per la gola. Sulla mappa della homepage filtra i punti di distribuzione che hanno medicinali. Mario clicca sul punto di distribuzione a lui più vicino. Si apre una scheda che mostra tutti i beni prenotabili in quel momento nel punto di distribuzione selezionato. I beni disponibili sono:</p>
<ul>
<li><p>Confezione di Tachipirine 1000mg (10 supposte) x2 (erogato da Medici Senza Frontiere)</p></li>
<li><p>Pacco di fazzoletti (erogato da Medici Senza Frontiere)</p></li>
</ul>
<p>Mario clicca sul “+” del pacco di medicinali per visualizzarne il contenuto. Il pacco contiene:</p>
<p>Mario decide di prenotare il pacco di fazzoletti cliccando su “prenota”. La prenotazione viene mandata per email all’ente erogatore Medici Senza Frontiera che in risposta manda un ulteriore email a Mario per confermare la sua prenotazione.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>22</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Aggiunta di un punto di distribuzione tramite indirizzo</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Croce Rossa=Ente erogatore</p>
<p>Mattia Bianchi=Operatore dell’Ente erogatore</p>
<p>Marco Rossi=Amministratore del sistema</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mattia, operatore dell’Ente erogatore “Croce Rossa”, si accorge che in una determinata zona della città manca un punto di distribuzione e decide di aggiungerlo sulla piattaforma Map4Aid.</p>
<p>Accede alla piattaforma con il suo account Ente erogatore e si dirige nella sezione “Gestisci dei punti di distribuzione”.</p>
<p>Clicca su “Aggiungi nuovo punto”. Gli appare un form che richiede le seguenti informazioni:</p>
<ul>
<li><p>Indirizzo:Piazza Garibaldi, Napoli 80040</p></li>
<li><p>Orari di apertura: 9-12, 16-19</p></li>
<li><p>Giorni di distribuzione: Lunedì. Mercoledì, Venerdì</p></li>
<li><p>Descrizione: “Punto di distribuzione gestito dall’Ente Caritas Sant’Antonio…”.</p></li>
</ul>
<p>Una volta inseriti tutti i dati, Mattia preme “Conferma” e attende la risposta dell’amministratore del sistema che deciderà in questo caso di accettare la richiesta di aggiunta di un punto di distribuzione.</p>
<p>Una volta che il punto di distribuzione sarà approvato, sarà visibile sulla mappa.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>23</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Rimozione di un punto di distribuzione da parte di un ente</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Mattia accardo= operatore dell’ente erogatore</p>
<p>Croce Rossa= ente erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mattia Accardo che è un operatore dell’ente “Croce Rossa”, decide di voler rimuovere un punto di distribuzione, quindi effettua il login alla piattaforma Map4aid tramite l’account dell’ente “Croce Rossa”; dopodiché andrà nella sezione “Gestione dei punti di distribuzione” e clicca su “Rimuovi punto di distribuzione”, poi gli verrà mostrata la mappa con i propri punti di distribuzione e sceglie di rimuovere il punto con indirizzo “Piazza Garibaldi, Napoli 80040”.</p>
<p>Gli viene mostrato un pop-up “Punto di distribuzione rimosso con successo”. Il punto scompare dalla mappa e non è più visibile dagli utenti.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Registrazione e login di un utente benficiario (login andato a buon fine)</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Mario Rossi = Utente non registrato</p>
<p>Giovanni De Caro = Amministratore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi decide di usufruire del servizio di map4aid e inizia la registrazione tramite la piattaforma. Sulla pagina della registrazione gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mario sceglie “utente beneficiario” e viene reindirizzato al form inerente. Qui compila i campi:</p>
<ul>
<li><p>Nome: Mario</p></li>
<li><p>Cognome: Rossi</p></li>
<li><p>Data di nascita: 01/01/2000</p></li>
<li><p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p></li>
<li><p><mark>password: Password</mark></p></li>
<li><p><mark>Codice ID card: CodiceExample</mark></p></li>
<li><p><mark>File ID card: carta_id_Mario_Rossi.pdf</mark></p></li>
<li><p><mark>Allergeni/Patologie: N/A</mark></p></li>
</ul>
<p><mark>Mario compila il form e lo invia al sistema che, dopo aver validato i dati, il sistema invia una mail con un codice. Mario deve inserire correttamente il codice nella pagina mostrata.</mark></p>
<p><mark>A questo punto un amministratore, in questo caso Giovanni De Caro, di sistema dovrà provvedere a validare il suo account controllando che la sua carta d’identità corrisponda ai dati inseriti nel form. Giovanni dopo aver controllato che tutto corrisponda valida l’account.</mark></p>
<p><mark>Il sistema attiva l’account di Mario, il quale può andare sulla pagina di login dove compilare il seguente form:</mark></p>
<ul>
<li><p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p></li>
<li><p><mark>password: Password</mark></p></li>
</ul>
<p><mark>Il sistema invia una mail con un codice. . Mario deve inserire correttamente il codice nella pagina mostrata.</mark></p>
<p><mark>Il sistema riconosce e-mail, password e codice come corretti e crea la sessione, loggando Mario e sbloccando le funzionalità destinate agli utenti beneficiari.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>2</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Registrazione e login di un utente beneficiario(login andato male per via della password)</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente non registrato</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi decide di usufruire del servizio di map4aid e inizia la registrazione tramite la piattaforma. Sulla pagina della registrazione gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mario sceglie “utente beneficiario” e viene reindirizzato al form inerente. Qui compila i campi:</p>
<ul>
<li><p>Nome: Mario</p></li>
<li><p>Cognome: Rossi</p></li>
<li><p>Data di nascita: 01/01/2000</p></li>
<li><p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p></li>
<li><p><mark>password: Password</mark></p></li>
<li><p><mark>Codice ID card: CodiceExample</mark></p></li>
<li><p><mark>File ID card: carta_id_Mario_Rossi.pdf</mark></p></li>
<li><p><mark>Allergeni/Patologie: N/A</mark></p></li>
</ul>
<p><mark>Mario compila il form e lo invia al sistema che, dopo aver validato i dati, il sistema invia una mail con un codice. Mario deve inserire correttamente il codice nella pagina mostrata.</mark></p>
<p><mark>A questo punto un amministratore, in questo caso Giovanni De Caro, di sistema dovrà provvedere a validare il suo account controllando che la sua carta d’identità corrisponda ai dati inseriti nel form. Giovanni dopo aver controllato che tutto corrisponda valida l’account.</mark></p>
<p><mark>Il sistema attiva l’account di Mario, il quale può andare sulla pagina di login dove compilare il seguente form:</mark></p>
<ul>
<li><p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p></li>
<li><p><mark>password: abcd</mark></p></li>
</ul>
<p><mark>Il sistema riconosce che la password è sbagliata e notifica a Mario che le credenziali inserite sono sbagliate.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>5</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Donazione monetaria (andata a buon fine)</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Mario Nappi = Utente beneficiario</p>
<p>Croce Rossa= Ente erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Nappi che è un Utente beneficiario, decide di voler fare una donazione monetaria.</p>
<p>Procede al login. Clicca sulla sezione “Donazione Monetaria” compilando il modulo presentato dal sistema, inserendo:</p>
<ul>
<li><p>Ente erogatore: Croce Rossa</p></li>
<li><p>Importo: 5000 €</p></li>
<li><p>Numero carta: 1234 5678 1234 1344</p></li>
<li><p>Scadenza:05/7/2027</p></li>
</ul>
<p>I dati inseriti corrispondono e sono corretti, la transazione avviene. Mario Nappi riceve tempestivamente una notifica (email) di avvenuto successo.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>6</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Donazione monetaria (errore, credito insufficiente)</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Mario Nappi = Utente beneficiario</p>
<p>Croce Rossa = Ente Erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Nappi che è un Utente beneficiario, decide di voler fare una donazione monetaria. Procede al login. Clicca sulla sezione “Donazione Monetaria” compilando il modulo presentato dal sistema, inserendo:</p>
<ul>
<li><p>Importo: 5000 €</p></li>
<li><p>Ente erogatore: Croce Rossa</p></li>
<li><p>Numero carta: 1234 5678 1234 1344</p></li>
<li><p>Scadenza:05/7/2027</p></li>
</ul>
<p>I dati inseriti corrispondono e sono corretti, ma quando avviene la transazione Mario Nappi riceve una notifica a schermo “Transazione fallita”.<br />
Riceve tempestivamente una email dove gli viene comunicato che il credito a disposizione (carte di credito, conto,..) è insufficiente rispetto all’importo da lui scelto, e che la transazione non è andata a buon fine.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>7</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Donazione di un bene alimentare da parte di un ente donatore</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Utente Giampiero Neri (Panificio Bakery) = Ente donatore<br />
Croce Rossa = Ente erogatore</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Giampiero Neri, registrato come Ente Donatore con la sua attività Panificio Bakery, decide di effettuare una donazione all’Ente Erogatore “Croce Rossa” registrato nel sistema.<br />
<br />
L’utente accede nella sua area riservata, clicca sulla sezione “donazione di beni” e compila il modulo presentato dal sistema:</p>
<ul>
<li><p>Categoria: alimentare</p></li>
<li><p>Nome:Pane(2kg)</p></li>
<li><p>Quantità:20</p></li>
<li><p>Scdenza:26/04/2026</p></li>
</ul>
<p>L’utente clicca su “effettua donazione” e , vista la correttezza dei dati, la richiesta viene inoltrata all’ente erogatore e l’utente visualizza un messaggio “richiesta di donazione inoltrata correttamente all’ente erogatore”.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>8</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Donazione di un bene medicinale da parte di un ente donatore</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Ros Utente Gianni Rossi (Farmacia centrale) = Ente donatore<br />
FIDAS = Ente erogatore</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Gianni Rossi, registrato come Ente Donatore con la sua attività Farmacia Centrale, decide di effettuare una donazione all’Ente Erogatore “FIDAS” registrato nel sistema.<br />
<br />
L’utente accede nella sua area riservata, clicca sulla sezione “donazione di beni” e compila il modulo presentato dal sistema inserendo:</p>
<ul>
<li><p>Ente erogatore: FIDAS</p></li>
<li><p>Categoria: Medicinale</p></li>
<li><p>Nome: Confezione Tachipirina 1000 mg</p></li>
<li><p>Quantità: 10</p></li>
<li><p>Scadenza:25/12/2026</p></li>
</ul>
<p>L’utente clicca su “effettua donazione” e , vista la correttezza dei dati, la richiesta viene inoltrata all’ente erogatore e l’utente visualizza un messaggio “richiesta di donazione inoltrata correttamente all’ente erogatore”.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>14</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un Utente beneficiario inserisce una valutazione feedback dopo un ritiro di beni avvenuto</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente Beneficiario</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi dopo aver ritirato il bene tramite QR-code, vedrà comparire quest’ultimo nello storico di beni ritirati.</p>
<p>Cliccando sul bene appena ritirato, vedrà comparire a schermo un'interfaccia che conterrà:</p>
<p>- informazioni sul luogo ed orario di ritiro;<br />
- modulo per invio di valutazione e feedback.</p>
<p>Mario Rossi decide di compilare il modulo.</p>
<p>Inserisce una valutazione numerica del servizio ricevuto, che va da un valore minimo di 1 ad uno massimo di 5. Decide di inserire 2 stelle.</p>
<p>Ed inoltre compila il campo Feedback testuale del modulo inserendo commenti e opinioni su qualche aspetto particolare del servizio ricevuto.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>15</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un Utente beneficiario, dopo il ritiro del bene prenotato, decide di non inserire recensione e feedback</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente Mario Rossi = Utente Beneficiario</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi dopo aver ritirato il bene tramite QR-code, vedrà comparire quest’ultimo nello storico di beni ritirati.</p>
<p>Cliccando sul bene appena ritirato, vedrà comparire a schermo un'interfaccia che conterrà:</p>
<p>- informazioni sul luogo ed orario di ritiro;</p>
<p>- modulo per invio di valutazione e feedback.</p>
<p>Mario Rossi decide di non compilare il modulo.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>16</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un utente beneficiario prenota un bene medicinale</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Luca Bianchi= Utente beneficiario</p>
<p>Medici senza frontiera = Ente erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p><mark>Luca Bianchi è un utente registrato alla piattaforma MAP4AID come beneficiario e ha correttamente effettuato il login inserendo e-mail e password.</mark></p>
<p><mark>Dalla homepage utente, Luca ha bisogno di prenotare un bene in un punto di distribuzione vicino a casa. Decide quindi di cliccare sulla voce di menu “Mappa”.</mark></p>
<p><mark>Il sistema apre una schermata contenente una mappa interattiva che mostra i punti di distribuzione disponibili. Sul lato della mappa è presente un pannello di filtri che permette di selezionare la categoria di beni desiderata.</mark></p>
<p><mark>Luca seleziona la categoria “medicinali” che gli interessa e applica i filtri. Il sistema aggiorna i marker sulla mappa mostrando solo i punti che dispongono di beni appartenenti a quella categoria.</mark></p>
<p><mark>Luca individua il punto di distribuzione più comodo per lui e clicca sul relativo marker.</mark></p>
<p><mark>Il sistema apre un riquadro informativo con i dettagli del punto di distribuzione (nome, indirizzo, orari di apertura, breve descrizione) e l’elenco dei beni prenotabili in quel punto, con le relative quantità disponibili.</mark></p>
<p><mark>Dall’elenco dei beni disponibili, Luca seleziona “Confezione di tachipirine 1000mg”, inserisce un file che contiene la ricetta medica e clicca sul pulsante “Prenota”.</mark></p>
<p><mark>Il sistema mostra una schermata di riepilogo della prenotazione contenente: il punto di ritiro selezionato, i dettagli del bene e l’eventuale fascia oraria di ritiro.</mark></p>
<p><mark>Luca controlla che i dati siano corretti e conferma la prenotazione cliccando su “Conferma prenotazione”.</mark></p>
<p><mark>L’ente erogatore che possiede quel punto di ritiro, Medici senza frontiera, valida la prenotazione assicurandosi che la ricetta medica sia valida.</mark></p>
<p><mark>Il sistema registra la prenotazione, aggiorna le quantità disponibili del bene nel punto di distribuzione scelto e genera un codice QR univoco associato alla prenotazione stessa.</mark></p>
<p><mark>Il codice QR viene mostrato a schermo e salvato all’interno dell’area personale di Luca, nella sezione “Le mie prenotazioni”. Inoltre, il sistema invia una e-mail di conferma contenente i dettagli della prenotazione e il QR da utilizzare al momento del ritiro.</mark></p>
<p><mark>Terminata l’operazione, Luca può chiudere la schermata o tornare alla homepage, sapendo di poter mostrare il QR presso il punto di ritiro nel giorno e nell’orario indicati.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>17</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>L’utente visualizza la mappa (per una categoria) senza prenotare</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente beneficiario</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p>Mario Rossi è un utente registrato alla piattaforma MAP4AID e ha effettuato il login.<br />
Dalla homepage utente decide di visualizzare la mappa dei punti di distribuzione.</p>
<p>Mario clicca sulla voce “Mappa”.</p>
<p>Il sistema apre una schermata contenente una mappa interattiva che mostra tutti i punti di distribuzione registrati sulla piattaforma, ognuno con il proprio marker e la legenda corrispondente.</p>
<p>Sul lato destro della schermata è presente un pannello filtri.<br />
Mario decide di filtrare i punti selezionando la categoria Alimentari.</p>
<p>Il sistema applica il filtro aggiornando i marker sulla mappa, lasciando visibili solo quelli che dispongono di beni appartenenti alla categoria selezionata.</p>
<p>Mario clicca su uno dei marker.</p>
<p>Il sistema apre un riquadro informativo che mostra:</p>
<ul>
<li><p>Nome del punto di distribuzione</p></li>
<li><p>Indirizzo</p></li>
<li><p>Orari di apertura</p></li>
<li><p>Quantità complessive di beni alimentari disponibili</p></li>
<li><p>Pulsante “Prenota”</p></li>
</ul>
<p>Mario non è interessato a prenotare, quindi non clicca sul pulsante “Prenota”.</p>
<p>Dopo aver consultato le informazioni, chiude il riquadro informativo e torna alla homepage tramite il menu.</p>
<p>Il sistema non registra alcuna prenotazione e l’operazione si conclude come semplice visualizzazione informativa sulla mappa.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>19</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Modifica della password</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Mario Rossi = Utente registrato</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p><mark>Mario Rossi è un utente registrato alla piattaforma ed ha effettuato il login.<br />
Dalla homepage decide di modificare la password del proprio account per motivi di sicurezza.</mark></p>
<p><mark>Mario clicca sulla voce di menu “Profilo”.</mark></p>
<p><mark>Il sistema apre la schermata del profilo utente, che mostra i dati principali dell’account e le impostazioni disponibili.</mark></p>
<p><mark>Nella sezione “Sicurezza” Mario individua l’opzione “Modifica password” e la seleziona.</mark></p>
<p><mark>Il sistema apre una schermata/modale contenente il form per il cambio password, con i seguenti campi:</mark></p>
<ul>
<li><p><mark>Password attuale</mark></p></li>
<li><p><mark>Nuova password</mark></p></li>
<li><p><mark>Conferma nuova password</mark></p></li>
</ul>
<p><mark>Mario inserisce la propria password attuale nel campo dedicato.</mark></p>
<p><mark>Successivamente inserisce una nuova password che rispetta i requisiti indicati dal sistema.</mark></p>
<p><mark>Mario ripete la nuova password nel campo “Conferma nuova password” per confermarla.</mark></p>
<p><mark>Dopo aver compilato tutti i campi, Mario clicca sul pulsante “Salva” (o “Conferma”).</mark></p>
<p><mark>Il sistema verifica che la password attuale inserita sia corretta, che la nuova password rispetti i requisiti di sicurezza e che la conferma coincida con la nuova password.</mark></p>
<p><mark>Le verifiche vanno a buon fine: il sistema aggiorna la password di Mario nel database e invalida, se previsto, le eventuali sessioni attive su altri dispositivi.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>20</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Donazione di un'igiene personale da parte di un donatore</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Donato Torricelli = Utente registrato come ente donatore</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p><mark>Donato Torricelli è un utente registrato in qualità di donatore, che ha effettuato il login.<br />
Dalla homepage utente decide di effettuare una donazione della categoria di igiene personale.</mark></p>
<p><mark>Donato clicca sulla voce “Dona beni”.</mark></p>
<p><mark>Il sistema apre una schermata contenente l’elenco delle categorie di beni donabili.<br />
Tra queste Donato seleziona la categoria <strong>Igiene personale</strong>.</mark></p>
<p><mark>Il sistema mostra un modulo di inserimento nel quale Donato deve specificare:<br />
• Tipo di bene: flacone di Sapone 500ml<br />
• Quantità disponibile:3<br />
• Punto di bisogno: Via Napoli 3<br />
• Nome bene: flacone di Sapone 500ml</mark></p>
<p><mark>Donato compila tutti i campi richiesti e,</mark></p>
<p><mark>dopo aver inserito i dati, clicca su <strong>“Continua”</strong>.</mark></p>
<p><mark>Il sistema mostra un riepilogo della donazione con tutte le informazioni inserite da Donato.<br />
Donato conferma cliccando sul pulsante <strong>“Conferma donazione”</strong>.</mark></p>
<p><mark>Il sistema registra la donazione, la assegna all’ente selezionato e invia la notifica all’ente erogatore con i dettagli del bene donato.</mark></p>
<p><mark>Il sistema mostra un messaggio di conferma del tipo:<br />
“La tua donazione è stata registrata con successo. L’ente selezionato ti contatterà per il ritiro.”</mark></p>
<p><mark>Donato torna alla homepage utente, dove può visualizzare la donazione nella sua cronologia donazioni.</mark></p>
<p><mark>L’operazione si conclude con successo e la donazione è ora disponibile per gli enti erogatori.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>9</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Un utente beneficiario prenota un pacco alimentare in un punto di ritiro (con QR)</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td>Luca Bianchi = Utente beneficiario</td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p><mark>Luca Bianchi è un utente registrato alla piattaforma MAP4AID come beneficiario e ha correttamente effettuato il login inserendo e-mail e password.</mark></p>
<p><mark>Dalla homepage utente, Luca ha bisogno di prenotare un bene in un punto di distribuzione vicino a casa. Decide quindi di cliccare sulla voce di menu “Mappa”.</mark></p>
<p><mark>Il sistema apre una schermata contenente una mappa interattiva che mostra i punti di distribuzione disponibili. Sul lato della mappa è presente un pannello di filtri che permette di selezionare la categoria di beni desiderata.</mark></p>
<p><mark>Luca seleziona la categoria “alimentari” che gli interessa e applica i filtri. Il sistema aggiorna i marker sulla mappa mostrando solo i punti che dispongono di beni appartenenti a quella categoria.</mark></p>
<p><mark>Luca individua il punto di distribuzione più comodo per lui e clicca sul relativo marker.</mark></p>
<p><mark>Il sistema apre un riquadro informativo con i dettagli del punto di distribuzione (nome, indirizzo, orari di apertura, breve descrizione) e l’elenco dei beni prenotabili in quel punto, con le relative quantità disponibili.</mark></p>
<p><mark>Dall’elenco dei beni disponibili, Luca seleziona “Prenota pacco alimentare” di suo interesse e clicca sul pulsante “Prenota”.</mark></p>
<p><mark>Il sistema mostra una schermata di riepilogo della prenotazione contenente: il punto di ritiro selezionato, il contenuto del pacco e l’eventuale fascia oraria di ritiro.</mark></p>
<p><mark>Luca controlla che i dati siano corretti e conferma la prenotazione cliccando su “Conferma prenotazione”.</mark></p>
<p><mark>Il sistema registra la prenotazione, aggiorna le quantità disponibili del bene nel punto di distribuzione scelto e genera un codice QR univoco associato alla prenotazione stessa.</mark></p>
<p><mark>Il codice QR viene mostrato a schermo e salvato all’interno dell’area personale di Luca, nella sezione “Le mie prenotazioni”. Inoltre, il sistema invia una e-mail di conferma contenente i dettagli della prenotazione e il QR da utilizzare al momento del ritiro.</mark></p>
<p><mark>Terminata l’operazione, Luca può chiudere la schermata o tornare alla homepage, sapendo di poter mostrare il QR presso il punto di ritiro nel giorno e nell’orario indicati.</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td>11</td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>Aggiunta di scorte in un punto di distribuzione da parte di un ente</td>
</tr>
<tr class="odd">
<td><strong>Actors</strong></td>
<td><p>Caritas Sant’Anna = Ente erogatore</p>
<p>Anna Verdi = Operatrice dell’ente erogatore</p></td>
</tr>
<tr class="even">
<td><strong>Flow Events</strong></td>
<td><p><mark>Anna Verdi è un’operatrice dell’ente erogatore “Caritas Sant’Anna”, registrata alla piattaforma MAP4AID. Ha effettuato il login con le credenziali dell’ente.</mark></p>
<p><mark>Dalla homepage ente, Anna decide di aggiornare le scorte di un punto di distribuzione perché ha appena ricevuto una nuova fornitura di beni.</mark></p>
<p><mark>Clicca sulla voce di menu “Gestione punti di distribuzione” per accedere all’elenco dei punti associati all’ente.</mark></p>
<p><mark>Il sistema mostra una lista dei punti di distribuzione gestiti dall’ente, con il relativo indirizzo e un riepilogo delle scorte principali.</mark></p>
<p><mark>Anna seleziona il punto di distribuzione per il quale vuole aggiornare le scorte cliccando su “Gestisci scorte”.</mark></p>
<p><mark>Il sistema apre una schermata dedicata alla gestione delle scorte del punto selezionato, elencando i beni già presenti con le quantità attuali e mettendo a disposizione l’opzione per aggiungere nuove scorte.</mark></p>
<p><mark>Anna clicca su “Aggiungi scorte”. Il sistema mostra un modulo nel quale è possibile indicare: bene da aggiornare (o da aggiungere), categoria (es. alimentari, igiene personale, medicinali), quantità da aggiungere, eventuale data di scadenza e note opzionali.</mark></p>
<p><mark>Anna seleziona, ad esempio, la categoria “Alimentari” e il bene “Pasta”, inserendo una quantità aggiuntiva (ad esempio 50 confezioni) e, se necessario, una data di scadenza indicativa.</mark></p>
<p><mark>Dopo aver verificato i dati inseriti, Anna clicca su “Conferma aggiornamento scorte”.</mark></p>
<p><mark>Il sistema aggiorna le scorte del punto di distribuzione, incrementando la quantità del bene indicato e registrando l’operazione nello storico interno delle modifiche.</mark></p>
<p><mark>Al termine, il sistema mostra un messaggio di conferma del tipo: “Le scorte del punto di distribuzione sono state aggiornate correttamente”.</mark></p>
<p><mark>Anna torna alla schermata riepilogativa delle scorte del punto di distribuzione, dove può vedere le nuove quantità aggiornate e, se necessario, procedere con ulteriori modifiche.</mark></p></td>
</tr>
</tbody>
</table>

# USE CASE

**CASO D’USO \#1 (REGISTRAZIONE)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 0%" />
<col style="width: 35%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#01</em></p></td>
<td rowspan="3"><em>Registrazione</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><p><em>Giovanni Esposito /</em></p>
<p><em>Nicola Luciano</em></p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">Processo in cui un nuovo utente crea un account nel sistema</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><strong>Utente non registrato</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente non possiede un account esistente.</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente dispone di un account valido e può autenticarsi</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Il sistema mostra un messaggio di errore</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2">Utente non registrato:</td>
<td colspan="5"><blockquote>
<p>L'utente accede alla pagina di registrazione</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Il sistema propone il form da compilare all'utente.<br />
Il form prevede l'inserimento di dati anagrafici (C.F. annesso), email, creazione di una</p>
<p>password, e eventuali allergie/intolleranze alimentari o condizioni e</p>
<p>patologie particolari</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2">Utente non registrato:</td>
<td colspan="5">L'utente compila il form e invia i dati.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema invia una mail di conferma all'utente, dopodichè l'utente disporrà di un account valido.</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> L'utente compila il campo Partita Iva nel form</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4"><p>L’utente compila anche il campo della p.iva.</p>
<p>Il sistema ricevendo dati sul campo partita iva, registra l'utente come Utente</p>
<p>Donatore, che avendo registrato la sua attività (verificata), è abilitato</p>
<p>a donare beni agli enti.</p></td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Email già registrata</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “Email già registrata” il fatto che all’email inserita corrisponde già un account esistente.</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Password troppo debole</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “Password troppo debole” il fatto che la password inserita non è sicura e richiede la ricompilazione del campo in questione.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> CF/P.iva non valido</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “CF/P.iva non valido” il fatto che i campi non risultano validi secondo i controlli formali</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">Nessuna informazione deve essere tracciata oltre quanto strettamente necessario (privacy by design)</td>
</tr>
</tbody>
</table>

**CASO D’USO \#2 (LOGIN)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 6%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#02</em></p></td>
<td rowspan="3"><em>Login</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><p><em>Giovanni Esposito /</em></p>
<p><em>Nicola Luciano</em></p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">Processo in cui un utente già registrato accede al sistema fornendo credenziali valide</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><strong>Utente registrato</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente possiede un account valide con credenziali attive e vuole autenticarsi</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Sessione creata. L’utente è loggato e ha accesso alle funzionalità.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Il sistema mostra un messaggio di errore.</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2">Utente registrato:</td>
<td colspan="5"><blockquote>
<p>L'utente accede alla pagina di login</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Il sistema propone il form da compilare all'utente.<br />
Il form prevede l'inserimento di email e password.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2">Utente registrato:</td>
<td colspan="5">L'utente compila il form e invia i dati.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema riconosce l’autenticazione. Sessione creata, accesso eseguito e funzionalità disponibili.</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> L’utente clicca su “Password dimenticata”</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema invia una mail contenente il link per il reset della password.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"><strong>Utente registrato:</strong></td>
<td colspan="4">L’utente usa il link inviato per mail per accedere al form di reset</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema propone il form per inserire la nuova password, quando la password inserita supera gli standard di sicurezza, la password è correttamente modificata, e l’utente riceve una notifica a schermo.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> L’utente clicca su “Email dimenticata”</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.2</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Alla richiesta dell’utente del reset della mail, il Sistema invia un messaggio al numero di telefono associato, contenente un codice temporaneo per sessione</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"><strong>Utente registrato:</strong></td>
<td colspan="4">L’utente inserisce il codice ricevuto tramite messaggio nell’apposito form fornito dal Sistema</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il Sistema, superata la validità del codice inserito, mostra a vista la mail associata</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Password e/o email errata</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “Email e/o password errate”, il fatto che i valori inseriti nei campi disponibili non risultano validi.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Codice per recupero email non valido</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema verifica il codice inserito dall’utente, che risulta non valido.<br />
Il codice risulta non valido o per corrispondenza, o per la terminazione della sessione. In tal caso l’utente deve richiedere un nuovo codice.</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Note</strong></td>
</tr>
<tr class="odd">
<td colspan="4">Riguardo al 4</td>
<td colspan="4">Successivamente sarà possibile implementare l'utilizzo dell’Autenticazione a due fattori ( 2FA ), richiesta solo dopo il riconoscimento dell’autenticazione da parte del Sistema.</td>
</tr>
</tbody>
</table>

**CASO D’USO \#3 (DONAZIONE MONETARIA)**

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 0%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#03</em></p></td>
<td rowspan="3"><em>Donazione monetaria</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>17/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Vito Francesco Maistrini / Giovanni De Caro</em></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>Donazione monetaria da parte di qualsiasi utente nella piattaforma verso gli Enti erogatori</em></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente non registrato/Utente registrato</strong></p>
<p>Interessato a donare per beneficenza una certa somma di denaro</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione monetaria dal utente</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">Esiste almeno un ente disponibile per la donazione</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Transazione di pagamento andata a buon fine (La donazione è stata registrata)</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Transazione di pagamento andata in fallimento (Nessuna donazione è stata registrata)</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Media</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></td>
<td colspan="5">Clicca su “Donazione monetaria”</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Mostra un modulo da compilare con scelta dell’ente, importo desiderato e metodo di pagamento</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></td>
<td colspan="5">Compila il modulo e lo invia</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Compie un controllo sulle informazioni inserite</em></td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Invia la donazione e una notifica all’ente erogatore scelto</em></td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Invia una notifica di successo all’utente</em></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Saldo insufficiente</td>
</tr>
<tr class="even">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Notifica all’utente che il saldo è insufficiente per la donazione</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Metodo di pagamento non valido</td>
</tr>
<tr class="even">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema si accorge che il metodo di pagamento non è valido (CVV inesistente/numero carta inesistente), e notifica all’utente che il metodo di pagamento è inesistente</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Note</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>1</strong></td>
<td colspan="4">“Donazione monetaria” è un componente dell’interfaccia</td>
</tr>
</tbody>
</table>

**CASO D’USO \#4 (DONAZIONE DI BENI)**

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 0%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#04</em></p></td>
<td rowspan="3"><em>Donazioni di beni</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.0001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Gabriele Milone / Carlo Antonio Caserta</em></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Descrizione</strong></td>
<td colspan="4"><em>L’utente registrato come donatore può donare beni materiali a enti specifici, in base alla propria categoria di donatore.</em></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Ente Donatore</strong></p>
<p>Interessato a donare una certa quantità di beni.</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione dall’utente</p></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Entry Condition</strong></td>
<td colspan="4"><ul>
<li><p>L'utente deve essere assegnato ad una determinata categoria di donazione</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L’ente convalida i dati forniti e invia una email al donatore con informazioni sul ritiro dei beni da parte dell’ente</td>
</tr>
<tr class="odd">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">I dati dei beni da donare non sono validi</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Media</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Frequenza stimata</strong></td>
<td colspan="4">Medio-bassa</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>Ente Donatore:</p>
</blockquote></td>
<td colspan="5">Compila il modulo per la donazione specifica (inserendo l’ente che preferisce)</td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Convalida i dati e inoltra il modulo all’ente</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Ente Erogatore:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Riceve i dati del modulo</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Ente Erogatore:</p>
</blockquote></td>
<td colspan="5">Invia una mail sulle informazioni del punto di raccolta e orario del bene al donatore</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Salva la donazione effettuata nello storico</em></td>
</tr>
<tr class="even">
<td colspan="7"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> i dati inseriti non sono validi</td>
</tr>
<tr class="odd">
<td>1.1</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Notifica il donatore che i dati inseriti nel form non sono validi specificando quali</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Special Requirements</strong></td>
<td colspan="4">Requisito n.f.#2 – Persistenza dei dati</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="4">Requisito n.f #5 - Protezione dei Dati e Autenticazione</td>
</tr>
</tbody>
</table>

**CASO D'USO \#5: (PRENOTAZIONE RITIRO BENI DI PRIMA NECESSITÀ)**

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#05</em></p></td>
<td rowspan="3"><em>Prenotazione ritiro beni di prima necessità</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/25</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autori</em></td>
<td colspan="2"><em>Luciano Corvino / Cristian Carotenuto</em></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Descrizione</strong></td>
<td colspan="4"><em>L'utente registrato come beneficiario seleziona una posizione sulla mappa tra quelle disponibili e ha la possibilità di selezionare ciò di cui ha bisogno e poi di prenotare uno slot orario nel quale potrà andare nel punto di ritiro scelto e ritirare i beni.</em></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente Beneficiario</strong></p>
<p>Interessato a prenotare i beni di suo interesse</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Attore Secondario</strong></td>
<td colspan="4"><p><strong>Ente Erogatore</strong></p>
<p>Riceve una notifica della prenotazione dei beni</p></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Entry Condition</strong></td>
<td colspan="4">Esiste almeno un punto di distribuzione con dei beni disponibili</td>
</tr>
<tr class="even">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente riesce con successo a prenotare lo slot orario nel quale andare a ritirare i beni prenotati.</td>
</tr>
<tr class="odd">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p><strong>Utente Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>L’utente visualizza i punti di distribuzione disponibili sulla mappa da cui può effettuare l’operazione di prenotazione e seleziona il punto desiderato.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Il sistema mostra all'utente la selezione dei beni disponibili nel punto di ritiro selezionato.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p><strong>Utente Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5">L'utente seleziona i beni che desidera e invia una conferma al sistema.</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema mostra gli slot orari disponibili per quel punto di ritiro.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p><strong>Utente Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5">L'utente seleziona lo slot orario che preferisce e invia la prenotazione dello slot orario al sistema.</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema aggiorna gli slot orari disponibili ed elimina da essi quello appena prenotato dall'utente e invia una notifica per conferma.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></td>
<td colspan="5">Riceve la notifica della prenotazione dei beni</td>
</tr>
</tbody>
</table>

**CASO D’USO#6: (SEGNALAZIONE DI UN PUNTO DI BISOGNO SULLA MAPPA)**

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #06</p></td>
<td rowspan="3"><em>Segnalazione di un punto di bisogno sulla mappa</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>17/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Maria Chiara Gregorio/ Riccardo Di Girolamo</em></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">L’utente segnala sulla mappa un’area o un punto in cui ritiene necessario attivare un punto di raccolta o distribuzione (ad esempio zone con famiglie in difficoltà o situazioni di emergenza).</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente non registrato/Utente registrato</strong></p>
<p>Segnalare un’area di criticità e permettere al sistema di attivare un nuovo punto di aiuto.</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Ricevere le segnalazioni, verificarle e decidere se attivare un nuovo punto di supporto.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L’utente è autenticato.</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">La segnalazione è registrata nel sistema e inoltrata agli enti amministratori.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">L’utente riceve un messaggio di errore.</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Medio/alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Medio/bassa</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2">Utente<strong>:</strong></td>
<td colspan="5"><blockquote>
<p>Seleziona sulla mappa l’opzione <em>“Segnala punto di bisogno”</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Mostra il modulo di segnalazione con i campi richiesti (posizione, tipologia bisogno, descrizione).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></td>
<td colspan="5">Inserisce i dati richiesti e seleziona sulla mappa la posizione del punto di bisogno.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Valida i dati inseriti (tutti i campi obbligatori compilati).</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></td>
<td colspan="5">Conferma l’invio della segnalazione.</td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Registra la segnalazione e la inoltra agli enti erogatori</td>
</tr>
<tr class="odd">
<td>7</td>
<td colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></td>
<td colspan="5">Visualizza il messaggio <em>“Segnalazione inviata correttamente”</em>.</td>
</tr>
<tr class="even">
<td colspan="8"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Posizione rilevata automaticamente (GPS attivo)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Se l’utente autorizza la geolocalizzazione, il sistema propone automaticamente la posizione corrente come punto di bisogno.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>2.2</strong></td>
<td colspan="2"><strong>Cittadino beneficiario:</strong></td>
<td colspan="4">Conferma o modifica manualmente la posizione proposta.</td>
</tr>
<tr class="even">
<td colspan="8"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Dati non validi</td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Indica quali campi obbligatori non sono validi e richiede correzione.</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Note</strong></td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">Le segnalazioni non sono immediatamente visibili sulla mappa fino ad approvazione degli enti.</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4">La selezione della posizione deve essere semplice e precisa (es. click sulla mappa).</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">Le segnalazioni devono essere memorizzate in modo sicuro e accessibile solo agli enti autorizzati.</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4">Deve essere rispettata la privacy (no dati sensibili non necessari).</td>
</tr>
</tbody>
</table>

**CASO D’USO \#7 (GESTIONE E AGGIORNAMENTO SCORTE)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 37%" />
<col style="width: 18%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#07</em></p></td>
<td rowspan="3">Gestione e aggiornamento scorte</td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td>Autore</td>
<td colspan="2">Giovanni Esposito / Nicola Luciano</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Descrizione</strong></td>
<td colspan="4"><em>P</em>ermette agli enti erogatori di monitorare in tempo reale le scorte di beni disponibili nei propri punti di raccolta o distribuzione tramite una specifica interfaccia.</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>E’ interessato a inserire o rimuovere beni da punti di raccolta</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Attori secondari</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Entry Condition</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Scorte aggiornate correttamente.</td>
</tr>
<tr class="odd">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Scorte non aggiornate. Tentata modifica in negativo di scorte da parte dell’ente.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p><strong>Ente erogatore:</strong></p>
</blockquote></td>
<td colspan="5"><p>Accede alla dashboard dove è mostrata l’attuale traccia delle scorte.</p>
<p>Ha a disposizione sull’interfaccia tutti i punti di ritiro associati con il loro inventario, e può sia incrementare il numero di beni sia aggiungerne di nuovi</p></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Mostra tramite interfaccia la gestione scorte nei vari punti di ritiro associati</td>
</tr>
<tr class="odd">
<td>3</td>
<td><strong>Ente erogatore:</strong></td>
<td colspan="5">Modifica quantità di un bene esistente in un determinato punto di ritiro (non ci occupiamo della logica dietro la consegna del nuovo bene incrementato)</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema aggiorna il numero di scorte per tenere traccia di permanenza dell’aggiornamento, e di conseguenza l’interfaccia utente.</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="7"><strong>Note</strong></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Special Requirements</strong></td>
<td colspan="4">n.f.#2 – Persistenza dei dati</td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="4">n.f.#3 – Tassonomia gerarchica</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="4">n.f.#5 – Protezione dei dati e autenticazione</td>
</tr>
</tbody>
</table>

**CASO D’USO \#8 (RICHIESTA AGGIUNTA DI UN PUNTO DI DISTRIBUZIONE)**

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 30%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#8</em></p></td>
<td rowspan="3">Richiesta aggiunta di un punto di distribuzione</td>
<td colspan="2"><em>Data</em></td>
<td><em>2/12/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.0001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Gabriele Milone / Carlo Antonio Caserta</em></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Descrizione</strong></td>
<td colspan="4">Il sistema deve poter permettere a un ente erogatore di mandare una richiesta per inserire un nuovo punto di distribuzione/raccolta. Tale richiesta viene gestita dall’amministratore, che può decidere di approvarla o rifiutarla.</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>E’ interessato all’aggiunta di punti di distribuzione di sua appartenenza all’interno del sistema.</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Attori secondari</strong></td>
<td colspan="4"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Entry Condition</strong></td>
<td colspan="4">L’utente è autenticato all’interno del sistema come ente erogatore.</td>
</tr>
<tr class="even">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">1. La richiesta viene inoltrata al sistema e messa in stato di attesa di approvazione<br />
<br />
2. Viene visualizzato un messaggio all’utente che conferma l’inoltro della richiesta.</td>
</tr>
<tr class="odd">
<td colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Il sistema non registra alcuna nuova richiesta e visualizza un messaggio di errore indicando eventuali dati mancanti o non validi.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO I</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p><strong>Ente erogatore</strong>:</p>
</blockquote></td>
<td colspan="5">Accede alla sezione dedicata alla gestione dei punti e seleziona l'opzione "Aggiungi nuovo punto".</td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p><strong>Sistema</strong>:</p>
</blockquote></td>
<td colspan="5">Visualizza il form per l'inserimento dei dettagli del punto di distribuzione.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></td>
<td colspan="5">Compila i campi richiesti con le informazioni del nuovo punto.</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></td>
<td colspan="5">Preme il pulsante di conferma per inviare la richiesta.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Verifica la validità formale dei dati inseriti (es. campi obbligatori compilati, formato dati corretto).</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Salva la richiesta</td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Notifica l’ente erogatore che la richiesta è stata salvata correttamente.</td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Notifica l’amministratore dell’arrivo di una nuova richiesta di aggiunta di un punto di distribuzione.</td>
</tr>
<tr class="odd">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI ALTERNATIVO I :</span></strong> Annullamento inserimento</td>
</tr>
<tr class="even">
<td>3.1</td>
<td><blockquote>
<p><strong>Ente erogatore</strong>:</p>
</blockquote></td>
<td colspan="5">Prima di inviare i dati, l’utente decide di annullare l’operazione, premendo “indietro” o “annulla”.</td>
</tr>
<tr class="odd">
<td>3.2</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Il sistema scarta i dati inseriti senza salvarli.</td>
</tr>
<tr class="even">
<td>3.3</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Il sistema riporta l’utente alla schermata precedente.</td>
</tr>
<tr class="odd">
<td colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI DI ERRORE I :</span></strong> Dati mancanti o non validi</td>
</tr>
<tr class="even">
<td>5.1</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Durante la verifica dei dati, il sistema rileva che uno o più campi obbligatori sono vuoti o che alcuni dati non rispettano il formato richiesto.</td>
</tr>
<tr class="odd">
<td>5.2</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Il sistema scarta la richiesta.</td>
</tr>
<tr class="even">
<td>5.3</td>
<td><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></td>
<td colspan="5">Il sistema mostra un messaggio di errore in cui evidenzia i campi da correggere/aggiungere</td>
</tr>
</tbody>
</table>

**CASO D’USO \#9: (*VISIONE STORICO ATTIVITà E REPORTISTICA)***

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#9</em></p></td>
<td rowspan="3"><em><strong>Visione storico attività e reportistica</strong></em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/25</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Luciano Corvino / Cristian Carotenuto</em></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>L'utente registrato può accedere al suo storico attività che può essere mostrato in versione PDF in versione settimanale, mensile o annuale.</em><br />
<em>Inoltre il sistema aggiorna automaticamente questi PDF in modo periodico,</em></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente registrato</strong></p>
<p>L’utente è interessato a visualizzare il proprio storico movimenti</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Clock</strong></p>
<p>Attore non umano che gestisce passivamente i report settimanali mensili e annuali.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente visualizza o stampa il PDF di suo interesse.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Medio/Bassa</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Medio/Bassa</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p><strong>Utente registrato:</strong></p>
</blockquote></td>
<td colspan="5">L'Utente accede all'area dove è possibile visualizzare i vari PDF</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Il sistema lo porta sull'interfaccia adatta, mostrando anche le opzioni di filtraggio</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p><strong>Utente registrato:</strong></p>
</blockquote></td>
<td colspan="5">L'Utente sceglie quale filtro visualizzare.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema gli mostra il PDF con il filtro selezionato e offre la possibilità di stamparlo.</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p><strong>Utente registrato:</strong></p>
</blockquote></td>
<td colspan="5">L'utente decide se stampare il PDF o rimanere nella visualizzazione desktop.</td>
</tr>
<tr class="even">
<td colspan="8">Nota</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>1</strong></td>
<td colspan="2"><strong>Clock:</strong></td>
<td colspan="4">Periodicamente il Clock informa il sistema che è necessario aggiornare il PDF delle attività dell'utente</td>
</tr>
<tr class="even">
<td colspan="2"><strong>2</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema riceve la notifica e aggiorna il PDF adeguato eliminando il precedente e sostituendolo con uno nuovo nel quale sono presenti i nuovi dati per quel filtro temporale</td>
</tr>
</tbody>
</table>

**CASO D’USO \#10 (INVIO DI VALUTAZIONE E FEEDBACK)**

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 0%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#10</em></p></td>
<td rowspan="3"><em>Invio di valutazione e feedback</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>18/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Vito Francesco Maistrini / Giovanni De Caro</em></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>Il cittadino beneficiario inserisce una recensione ad un servizio offerto dalla piattaforma del quale ha usufruito</em></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente beneficiario</strong></p>
<p>Interessato a inserire una valutazione e scrivere un feedback dopo il ritiro di un pacco prenotato</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la valutazione e il feedback</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4"><ul>
<li><p>Il cittadino deve aver prenotato un pacco a uno dei punti di distribuzione</p></li>
<li><p>Il cittadino deve aver ricevuto una conferma della prenotazione</p></li>
<li><p>Il cittadino deve aver ritirato il pacco</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Il feedback viene ricevuto con successo dall’ente</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Il cittadino decide di non inserire feedback e valutazione</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Media</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p><strong>Utente beneficiario</strong>:</p>
</blockquote></td>
<td colspan="5">Apre la notifica di “pacco consegnato”</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Chiede al cittadino di inserire una valutazione e feedback tramite un’interfaccia</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p><strong>Utente beneficiario</strong>:</p>
</blockquote></td>
<td colspan="5">Inserisce una valutazione e un feedback e li invia</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Manda con successo la recensione all’ente erogatore</em></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo: Il cittadino decide di non inserire una recensione</strong></td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il Cittadino sceglie di uscire dall’interfaccia feedback non inserendo nessuna valutazione/feedback</td>
</tr>
</tbody>
</table>

> **CASO D’USO \#11 (FILTRAGGIO CATALOGO E COLLEGAMENTO AI PUNTI DI DISTRIBUZIONE)**

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #11</p></td>
<td rowspan="3">Filtraggio catalogo e collegamento ai punti di distribuzione</td>
<td colspan="2">Data</td>
<td>21/11/2025</td>
</tr>
<tr class="even">
<td>Vers.</td>
<td colspan="2">0.00.001</td>
</tr>
<tr class="odd">
<td>Autore</td>
<td colspan="2">Emilio Maione</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">L’utente visualizza il catalogo globale dei beni, applica filtri gerarchici (macrocategoria,sottocategoria, bene specifico) e la mappa viene aggiornata mostrando solo i punti di distribuzione che possiedono il bene selezionato.</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente non registrato/Utente registrato</strong></p>
<p>Interessato a cercare prodotti disponibili nei punti di distribuzione.</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attore secondario</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">Il catalogo globale è disponibile e contiene almeno un bene associato ad almeno un punto di distribuzione.</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">La mappa mostra correttamente i punti che possiedono il bene filtrato.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Nessun risultato trovato o errore nel caricamento del catalogo (nessun aggiornamento sulla mappa).</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension Point</strong></td>
<td colspan="4">Possibile integrazione futura con sistema di suggerimenti automatici basati sulle preferenze dell'utente.</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong>Flusso di Eventi Principale/Main Scenario</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2">Utente:</td>
<td colspan="5">Accesso alla sezione “Catalogo”.</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2">Sistema:</td>
<td colspan="5">Mostra tutti i beni del catalogo e tutte le opzioni per il filtraggio: macrocategoria, sottocategoria, e beni specifici.</td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2">Utente:</td>
<td colspan="5">Seleziona uno o più filtri disponibili (macrocategoria,sottocategoria,bene specifico ecc.) e avvia l’azione “applica filtri”.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2">Sistema:</td>
<td colspan="5">Restituisce i beni filtrati e li invia alla mappa, in modo che visualizzi solo i punti di distribuzione che contengono tali beni.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo: bene non disponibile in nessun punto di distribuzione</strong></td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4"><p>Il filtro applicato non ha prodotto risultati.</p>
<p>Il sistema visualizza il messaggio “Nessun bene disponibile”.</p></td>
</tr>
</tbody>
</table>

**CASO D’USO \#12 (FILTRAGGIO DELLA MAPPA)**

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #12</p></td>
<td rowspan="3">Filtraggio dei punti sulla mappa</td>
<td colspan="2">Data</td>
<td>25/11/2025</td>
</tr>
<tr class="even">
<td>Vers.</td>
<td colspan="2">0.00.001</td>
</tr>
<tr class="odd">
<td>Autore</td>
<td colspan="2">Riccardo Di Girolamo / Maria Chiara Gregorio</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">L’utente applica filtri ai punti visualizzati sulla mappa per visualizzare solo gli elementi rilevanti e ridurre il sovraccarico visivo.</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><strong>Utente non registrato/Utente registrato</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori Secondari</strong></td>
<td colspan="4"><strong>Ente erogatore</strong></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4"><p>L’utente visualizza la mappa.</p>
<p>L’utente seleziona l’opzione “Filtri”.</p></td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4"><p>I filtri vengono applicati correttamente.</p>
<p>La mappa mostra solo i punti che soddisfano i criteri selezionati.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4"><p>I filtri non vengono applicati perché l’utente non seleziona alcun criterio oppure la combinazione scelta non è utilizzabile.</p>
<p>Il sistema informa l’utente e la mappa rimane invariata.</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension Point</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">N/A</td>
</tr>
<tr class="even">
<td colspan="8"><strong>Flusso di Eventi Principale/Main Scenario</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="5">Apre il pannello dei filtri della mappa.</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="5">Mostra i filtri disponibili (es. tipologia: raccolta/distribuzione, orari, distanza).</td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="5">Seleziona uno o più criteri di filtraggio.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="5">Applica i criteri selezionati ai punti disponibili.</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="5">Conferma l’applicazione (o chiude il pannello) per visualizzare i risultati.</td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="5">Aggiorna la mappa mostrando solo i punti che soddisfano i criteri selezionati.</td>
</tr>
<tr class="odd">
<td>7</td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="5">Visualizza la mappa filtrata e interagisce con i punti mostrati.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo: Filtri preimpostati in base al profilo/ruolo</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Se l’utente è autenticato, evidenzia o pre-imposta filtri coerenti con il profilo (es. punti dell’ente o punti pubblici).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.2</strong></td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="4">Accetta i filtri proposti oppure li modifica e prosegue (ritorna al passo 3).</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>II Scenario/Flusso di eventi Alternativo: Selezione di un preset (filtri rapidi)</strong></td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.3</strong></td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="4">Inserisce un indirizzo manualmente invece di cliccare sulla mappa.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>2.4</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Converte l’indirizzo in coordinate (geocoding) e mostra l’anteprima sulla mappa.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>III Scenario/Flusso di eventi Alternativo: Nessun punto trovato con filtri selezionati</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>6.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Mostra un messaggio: “Nessun punto trovato con i filtri selezionati” e propone di modificare o reimpostare i filtri.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>6.2</strong></td>
<td colspan="2"><strong>Utente:</strong></td>
<td colspan="4">Sceglie “Modifica” per cambiare i filtri (ritorna al passo 3) oppure “Reimposta” per tornare alla visualizzazione completa.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE: Nessuno.</strong></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Note</strong></td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"><p>Il filtraggio può essere utilizzato anche senza autenticazione; alcune opzioni possono dipendere dal profilo/ruolo utente.</p>
<p>Il filtro “Solo distribuzione pubblica” consente di visualizzare i punti pubblici e i beni/servizi dichiarati.</p></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Special Requirements</strong></td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"><p>Il filtraggio deve aggiornare la mappa senza ricaricare la pagina.</p>
<p>I filtri devono essere combinabili e facilmente re-impostabili.</p>
<p>La mappa deve restare leggibile anche con molti punti (es. raggruppamento dei marker).</p></td>
</tr>
</tbody>
</table>

# OGGETTI ENTITY, BOUNDARY E CONTROL

- **Entity**

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>CLASSE</strong></td>
<td><strong>DESCRIZIONE</strong></td>
<td><strong>ATTRIBUTI</strong></td>
<td><strong>CASO D’USO</strong></td>
</tr>
<tr class="even">
<td>Account</td>
<td><p>Rappresenta l’account generico del sistema.</p>
<p>Account di ogni tipologia di utente</p></td>
<td><ul>
<li><p>idUtente</p></li>
<li><p>email</p></li>
<li><p>password</p></li>
</ul></td>
<td>1,2,3</td>
</tr>
<tr class="odd">
<td>AccountBeneficiario</td>
<td>Rappresenta un utente che beneficia dei beni distribuiti</td>
<td><p>-nome</p>
<p>-cognome</p></td>
<td>1,2,5</td>
</tr>
<tr class="even">
<td>AccountDonatore</td>
<td>Rappresenta un ente che dona i beni</td>
<td><p>-partita Iva</p>
<p>-categoria</p>
<p>-nome attività</p>
<p>-indirizzo sede</p>
<p>- nome</p>
<p>- cognome</p></td>
<td>1,2,3,4</td>
</tr>
<tr class="odd">
<td>AccountEnteErogatore</td>
<td>Rappresenta un ente che gestisce la distribuzione di beni</td>
<td><p>-nome organizzazione</p>
<p>-indirizzo sede</p>
<p>-tipologia ente</p>
<p>- iban</p></td>
<td>1,2,3,4,5,6,8</td>
</tr>
<tr class="even">
<td>DonazioneMonetaria</td>
<td>Rappresenta una donazione da parte del donatore</td>
<td><p>-IdUtente</p>
<p>-IdErogatore</p>
<p>-Somma monetaria</p>
<p>-Data</p></td>
<td>3</td>
</tr>
<tr class="odd">
<td>ArticoloDonato</td>
<td>Rappresenta un bene che è stato donato</td>
<td><p>-IdBene</p>
<p>-Nome</p>
<p>-Categoria</p>
<p>-Quantità</p></td>
<td>4,5,10</td>
</tr>
<tr class="even">
<td>ArticoloAlimentare</td>
<td>Rappresenta un bene alimentare che è stato donato</td>
<td><p>-Allergeni</p>
<p>-Scadenza</p></td>
<td>4,5,11</td>
</tr>
<tr class="odd">
<td>ArticoloMedicinale</td>
<td>Rappresenta un medicinale che è stato donato</td>
<td><p>-Tipo</p>
<p>-Scadenza</p></td>
<td>4,5,11</td>
</tr>
<tr class="even">
<td>ArticoloVestiario</td>
<td>Rappresenta un capo d’abbigliamento che è stato donato</td>
<td><p>-Taglia</p>
<p>-Condizioni</p></td>
<td>4,5,11</td>
</tr>
<tr class="odd">
<td>ArticoloIgiene</td>
<td>Rappresenta un articolo di igiene personale che è stato donato</td>
<td>-Destinatari</td>
<td>4,5,11</td>
</tr>
<tr class="even">
<td>ArticoloMobilità</td>
<td>Rappresenta un articolo per supporto o mobilità</td>
<td><p>-Tipo</p>
<p>-Stato</p></td>
<td>4,5,11</td>
</tr>
<tr class="odd">
<td>DonazioneBene</td>
<td>Rappresenta una donazione di un bene</td>
<td><p>-IdDonazione</p>
<p>-IdDonatore</p>
<p>-IdErogatore</p>
<p>-IdBene</p>
<p>-Data</p>
<p>-nomePuntoDistribuzione</p></td>
<td>4,5</td>
</tr>
<tr class="even">
<td>PuntoDistribuzione</td>
<td>Rappresenta un punto di distribuzione sulla mappa</td>
<td><p>-nome</p>
<p>-regione</p>
<p>-città</p>
<p>-idErogatore</p>
<p>-Cordinate</p></td>
<td>5,8,11,12</td>
</tr>
<tr class="odd">
<td>PrenotazioneBene</td>
<td>Rappresenta la prenotazione di un bene da parte di un beneficiario</td>
<td><p>-IdPrenotazione</p>
<p>-IdBeneficiario</p>
<p>-IdBene</p>
<p>-Data</p></td>
<td>5</td>
</tr>
<tr class="even">
<td>Feedback</td>
<td>Rappresenta un feedback da parte di un utente a valle di un ritiro completato</td>
<td><p>-IdFeedback</p>
<p>-IdUtenteBeneficiario</p>
<p>-IdPuntoDistribuzione</p>
<p>-recensione</p>
<p>-valutazione</p></td>
<td>10</td>
</tr>
<tr class="odd">
<td>Notifica</td>
<td>Rappresenta una notifica visualizzabile nell’apposita sezione</td>
<td><p>-IdNotifica</p>
<p>-Titolo</p>
<p>-Descrizione</p></td>
<td>N/A</td>
</tr>
</tbody>
</table>

- **Boundary**

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>CLASSE</strong></td>
<td><strong>DESCRIZIONE</strong></td>
<td><strong>RESPONSABILITA</strong></td>
<td><strong>CASO D’USO</strong></td>
</tr>
<tr class="even">
<td>BoundarySelezioneRegistrazione</td>
<td>Interfaccia che consente all’utente di selezionare la tipologia di registrazione desiderata</td>
<td><ul>
<li><p>Visualizzare le opzioni di registrazione(Beneficiario,Ente Donatore, Ente Erogatore)</p></li>
</ul></td>
<td>1</td>
</tr>
<tr class="odd">
<td>BoundaryRegistrazioneBeneficiario</td>
<td>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione del beneficiario</td>
<td><ul>
<li><p>Raccogliere dati utente</p></li>
</ul></td>
<td>1</td>
</tr>
<tr class="even">
<td>BoundaryRegistrazioneEnteDonatore</td>
<td>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione del Donatore</td>
<td><ul>
<li><p>Raccogliere i dati utente e dell’attività</p></li>
</ul></td>
<td>1</td>
</tr>
<tr class="odd">
<td>BoundaryRegistrazioneEnteErogatore</td>
<td>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione dell’ente erogatore</td>
<td><ul>
<li><p>Raccogliere le informazioni necessarie alla creazione dell’ente</p></li>
</ul></td>
<td>1</td>
</tr>
<tr class="even">
<td>BoundaryLogin</td>
<td>Schermata utilizzata per l’inserimento dei dati necessari per il login</td>
<td><ul>
<li><p>Raccogliere i dati inseriti dall’utente</p></li>
<li><p>Inviare i dati di control di autenticazione</p></li>
<li><p>Mostrare messaggi di errore o di conferma</p></li>
</ul></td>
<td>2</td>
</tr>
<tr class="odd">
<td>BoundaryVisualizzaProfilo</td>
<td>Schermata utilizzata per visualizzare le proprie informazioni</td>
<td><ul>
<li><p>Visualizzare le informazioni relative all’account</p></li>
<li><p>Permettere il logout dall’account</p></li>
<li><p>Permette di scaricare il pdf con lo storico delle proprio attività</p></li>
</ul></td>
<td>9</td>
</tr>
<tr class="even">
<td>BoundaryModificaProfilo</td>
<td>Schermata utilizzata per modificare le proprie informazioni</td>
<td><ul>
<li><p>Visualizzare le informazioni modificabili relative all’account</p></li>
<li><p>Permettere la modifica di alcuni dei dati</p></li>
<li><p>Inviare al control collegato la richiesta di aggiornamento dei dati profilo</p></li>
<li><p>Mostrare messaggi di conferma o errore relativi alle operazioni effettuate</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>BoundryDonazioneMonetaria</td>
<td>Schermata utilizzata per inserire le informazioni per effettuare una donazione monetaria</td>
<td><ul>
<li><p>Visualizzare l’elenco degli enti erogatori disponibili</p></li>
<li><p>Permettere la selezione dell’ente erogatore desiderato</p></li>
<li><p>Permettere di inserire dati della propria carta di credito/debito e somma dell’importo</p></li>
<li><p>Inviare la richiesta al control collegato</p></li>
<li><p>Mostrare all’utente l’esito dell’operazione (successo/errore pagamento)</p></li>
</ul></td>
<td>3</td>
</tr>
<tr class="even">
<td>BoundaryDonazioneBene</td>
<td>Schermata utilizzata per inserire le informazioni per effettuare una donazione di un bene</td>
<td><ul>
<li><p>Visualizzare l’elenco degli enti erogatori disponibili</p></li>
<li><p>Permettere la selezione dell’ente erogatore desiderato</p></li>
<li><p>Permette di inserire i dati del bene da donare</p></li>
<li><p>Inviare la richiesta al control collegato</p></li>
<li><p>Mostrare all’utente l’esitodell’operazione</p></li>
</ul></td>
<td>4</td>
</tr>
<tr class="odd">
<td>BoundaryPrenotazioneBene</td>
<td>Schermata utilizzata per visualizzare e prenotare uno o più beni</td>
<td><ul>
<li><p>Visualizzare un bene o più beni prenotabili</p></li>
<li><p>Permette di prenotare uno o più bene in un punto di distribuzione</p></li>
</ul></td>
<td>5</td>
</tr>
<tr class="even">
<td>EmailConfermaDonazioneMonetaria</td>
<td>Email mandata per confermare una donazione monetaria mandata all’ente erogatore</td>
<td>-Visualizzare la conferma della donazione e l’importo donato</td>
<td>3</td>
</tr>
<tr class="odd">
<td>EmailConfermaDonazioneBene</td>
<td>Email mandata per c onfermare la donazione di un bene all’ente erogatore</td>
<td><p>-Fornisce i dati del donatore</p>
<p>-Fornisce i dati del bene donato</p></td>
<td>4</td>
</tr>
<tr class="even">
<td>EmailConfermaPrenotazione</td>
<td>Email mandata per c onfermare la prenotaionee di un bene all’ente erogatore</td>
<td><p>-Fornisce i dati dell’utente beneficiario</p>
<p>-Visualizza il bene che ha prenotato l’utente</p></td>
<td>5</td>
</tr>
<tr class="odd">
<td>BoundaryVisualizzaPrenotazioni</td>
<td>Schermata utilizzata per la visualizzazione delle prenotazioni effetuate</td>
<td><p>-Visualizzazione prenotazioni effettuate</p>
<p>-Permette la cancellazione di una prenotazione non ancora ritirata</p></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>BoundarySegnalazionePunto</td>
<td>Schermata utilizzata per inserire i dati sul punto di bisogno da voler segnalare</td>
<td>-Permette di inserire i dati nel punto di bisogno manualmente o tramite marker sulla mappa</td>
<td>6</td>
</tr>
<tr class="odd">
<td>BoundaryGestionePunti</td>
<td>Schermata utilizzata per gestire i beni in un punto di distribuzione da parte di un ente erogatore</td>
<td><p>-Permette di aggiungere/rimuovere beni ad un punto di distribuzione</p>
<p>-Permette la modifica della quantità di ciascun bene</p></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>BoundaryVisualizzazioneNotifiche</td>
<td>Schermata utilizzata per visualizzare le notifiche</td>
<td>-Permette di visualizzare le notifiche</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>BoundaryFeedback</td>
<td>Schermata utilizzata per inviare un feedback da parte dell’utente</td>
<td><p>-Permette di inserire un feedback testuale</p>
<p>-Permette di inserire una valutazione</p></td>
<td>10</td>
</tr>
<tr class="even">
<td>BoundaryCatalogo</td>
<td>Schermata utilizzata per vedere tutti i beni disponibili registrati nel sistema</td>
<td>-Permette di visualizzare un bene e vederne i dettagli</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>BoundaryFiltroCatalogo</td>
<td>Schermata utilizzata per filtrare il catalogo(e di conseguenza la mappa) in base ai beni</td>
<td><p>-Permette di scegliere come filtrare i beni</p>
<p>-Il filtro verrà applicato anche sulla mappa</p></td>
<td>11</td>
</tr>
<tr class="even">
<td>BoundaryFiltroMappa</td>
<td>Schermata utilizzata per filtrare la mappa in base ai punti di distribuzione</td>
<td>-Permette di filtrare i punti sulla mappa</td>
<td>12</td>
</tr>
</tbody>
</table>

- **Control**

|                              |                                                                                                |                |
|------------------------------|------------------------------------------------------------------------------------------------|----------------|
| **CLASSE**                   | **DESCRIZIONE**                                                                                | **CASO D’USO** |
| GestioneRegistrazioneControl | Coordinatore della logica di registrazione per le varie tipologie di utente                    | 1              |
| AutenticazioneControl        | Coordinatore della logica di login/logout per le varie tipologie di utente                     | 2              |
| GestioneProfiloControl       | Coordinatore della logica della visualizzazione e modifica del profilo                         | N/A            |
| DonazioneMonetariaControl    | Coordinatore della logica della donazione monetaria da parte di un utente ad un ente erogatore | 3              |
| DonazioneBeniControl         | Coordinatore della logica della donazione di beni da parte di un donatore ad un ente erogatore | 4              |
| GestionePrenotazioneControl  | Coordinatore della logica della prenotazione di beni da parte di un beneficiario               | 5              |
| GesationePuntiControl        | Coordinatore della logica della dei punti di bisogno e gestisce i filtri                       | 6,8,11,12      |
| InvioNotificheContrl         | Crea e invia le e-mail di notifica ai vari utenti e crea le notifiche sul sistema              | 10             |
| GestioneStoricoControl       | Crea il file con i dati delle attività dell'utente                                             | 9              |

# SEQUENCE DIAGRAMS

- **Donazione Monetaria**

<img src="media/image2.png" style="width:6.15625in;height:4.25863in" alt="Immagine che contiene testo, diagramma, Parallelo, Disegno tecnico Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **Segnalazione di un Punto di Bisogno**

<img src="media/image3.png" style="width:6in;height:3.54655in" alt="Immagine che contiene testo, diagramma, Disegno tecnico, Parallelo Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **Gestione delle Scorte**

<img src="media/image4.png" style="width:5.70833in;height:4.56738in" alt="Immagine che contiene testo, diagramma, Disegno tecnico, Piano Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **Donazione di un Bene**

<img src="media/image5.png" style="width:6.89167in;height:5.69375in" alt="Immagine che contiene testo, diagramma, Parallelo, Rettangolo" />

- **Prenotazione Ritiro Beni**

<img src="media/image6.png" style="width:6.95in;height:3.2665in" />

# STATECHART DIAGRAMS

- **PrenotazioneBene**

<img src="media/image7.png" style="width:5.75553in;height:7.3681in" alt="Immagine che contiene diagramma, Disegno tecnico, Piano, schematico Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **SegnalazioneControl**

<img src="media/image8.png" style="width:6.89167in;height:5.87917in" alt="Immagine che contiene diagramma, testo, Piano, linea Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **DonazioneMonetariaControl**

<img src="media/image9.png" style="width:4.86667in;height:6.9in" alt="Immagine che contiene testo, schermata, diagramma, linea Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

- **AutenticazioneControl**<img src="media/image10.png" style="width:5.62708in;height:7in" />

# ACTIVITY DIAGRAM:PRENOTAZIONE DI UN BENE

<img src="media/image11.PNG" style="width:5.02239in;height:7.81702in" />
