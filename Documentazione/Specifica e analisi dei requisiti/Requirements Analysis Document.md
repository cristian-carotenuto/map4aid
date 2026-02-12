<img src="media/image11.png" style="width:1.32986in;height:1.32153in" />

*REQUIREMENTS ANALYSIS DOCUMENT*

**-Utente**

Si riferisce a chiunque acceda e utilizzi il sistema

**-Utente non registrato**

Ruolo: Navigare la mappa geolocalizzata, filtrare per tipologia bene (cibo/farmaci..), ricevere informazioni via e-mail

**-Utente registrato**(padre di Utente Beneficiario,Donatore,erogatore e amministratore)

Login e gestione del proprio profilo, visualizza lo storico,donazione monetaria

**-Utente beneficiario**

Ruolo: Tutte le funzioni dell’utente non autenticato, tenere traccia delle richieste passate e delle prenotazioni (storico), ricevere notifiche push,prenotazioni bene,cancellazione prenotazione

**-Ente Donatore**

Ruolo: Tutte le funzioni dell’utente non autenticato, donare beni,interagire con ente erogatore

**-Ente erogatore**

Ruolo: Tutte le funzioni dell’utente non autenticato, inserimento e aggiornamento della disponibilità e quantità dei beni, gestione prenotazione,crea la richiesta per i punti di bisogno all’admin.

**-Amministratore di sistema**

Ruolo: Validazione account beneficiario tramite documento d’identità,gestione punti di distribuzione.

**Funzionalità \#1 – Registrazione**

Il sistema deve poter permettere a un nuovo utente di potersi registrare e quindi creare un nuovo account inserendo le informazioni richieste.

**Funzionalità \#1.1 – Registrazione per “Utente beneficiario”**

Il sistema deve poter permettere a un nuovo utente di registrarsi come “utente beneficiario” al fine di usare le funzionalità specifiche per questa tipologia di utente

**Funzionalità \#1.2 – Registrazione per “Ente donatore”**

Il sistema deve poter permettere a un nuovo utente di registrarsi come “ente donatore” al fine di usare le funzionalità specifiche per questa tipologia di utente

**Funzionalità \#1.3 –Registrazione per “Ente erogatore”**

Il sistema deve poter permettere a un nuovo utente di registrare la propria organizzazione, quindi di registrarsi come “ente erogatore” al fine di usare le funzionalità specifiche per questa tipologia di utente

**Funzionalità \#1.4 -Validazione account “beneficiario”**

Il sistema deve permettere all’amministratore di poter validare l’account di un utente beneficiario .

**Funzionalità \#2 – Login**

Il sistema deve poter permettere a un utente di effettuare il login al proprio account, (o account dell’organizzazione se si tratta di un operatore dell’ente), tramite l’inserimento delle proprie credenziali

**Funzionalità \#3 – Logout**

Il sistema deve poter permettere a un utente di effettuare il logout dal proprio account (o account dell’organizzazione se si tratta di un operatore dell’ente)

**Funzionalità \#4 – Visualizzazione profilo**

Il sistema deve poter permettere a ogni utente registrato di visualizzare il proprio profilo

**Funzionalità \#5 – Modifica profilo**

Il sistema deve poter permettere a ogni utente registrato di modificare il proprio profilo

**Funzionalità \#5.1 – Modifica profilo per “utente beneficiario"**

Il sistema deve poter permettere a un utente beneficiario di modificare il proprio profilo, e quindi di modificare i dati per questa tipologia di utente

**Funzionalità \#5.2 – Modifica profilo per “ente donatore”**

Il sistema deve poter permettere a ente donatore di modificare il proprio profilo, e quindi di modificare i dati per questa tipologia di utente

**Funzionalità \#5.3 – Modifica profilo per “ente erogatore”**

Il sistema deve poter permettere agli utenti che hanno l’accesso all’account della propria organizzazione registrata come “ente erogatore”, di modificare il profilo dell’organizzazione, e quindi di modificare i dati per questa tipologia di utente

**Funzionalità \#6 – Inserimento conto bancario per ente erogatore**

Il sistema deve permettere a un ente erogatore di inserire i dati di un proprio conto bancario affinché un qualsiasi utente possa effettuare una donazione

**Funzionalità \#7 – Filtraggio della mappa**

Il sistema deve consentire all’utente di visualizzare punti di distribuzione sulla mappa in base a criteri visualizzabili, tra i quali: fascia oraria di attività

**Funzionalità \#8 – Donazione monetaria**

Il sistema deve consentire a un qualsiasi utente registrato di effettuare una donazione monetaria selezionando l’ente desiderato tra quelli disponibili, poi l’importo desiderato

**Funzionalità \#9 – Donazione di beni**

Il sistema deve consentire a un utente registrato come “ente donatore” di effettuare una donazione di beni

**Funzionalità \#10 – Prenotazione beni**

Il sistema deve consentire a soli utenti registrati come “utente beneficiario” di effettuare la prenotazione di un qualsiasi bene disponibile in un qualsiasi punto di distribuzione

**Funzionalità \#11 – Cancellazione prenotazione**

Il sistema deve poter permettere a un utente beneficiario o ente erogatore che ha effettuato una prenotazione di un bene di cancellare la prenotazione

**Funzionalità \#12 – Validazione prenotazione di un medicinale**

Il sistema deve permettere ad un ente erogatore di validare una prenotazione di tipo “medicinale”

**Funzionalità \#13 – Generazione QR code**

Il sistema dopo ogni prenotazione di un bene deve generare un QR code univoco e inviarlo all’utente beneficiario che ha conseguito la prenotazione

**Funzionalità \#14 – Segnalazione punti di bisogno sulla mappa**

Il sistema deve permettere a un utente di segnalare un punto di bisogno sulla mappa,indicando il luogo in cui ritiene necessario attivare un punto di distribuzione.

**Funzionalità \#15 – Gestione dei beni nei punti di distribuzione**

Il sistema deve consentire agli enti erogatori la gestione dei beni presenti nei punti di distribuzione

**Funzionalità \#15.1 – Aggiunta dei beni nei punti di distribuzione**

Il sistema deve permettere agli enti erogatori di aggiungere dei beni nei punti di distribuzione specificando quantità e categoria

**Funzionalità \#15.2 – Rimozione dei beni nei punti di distribuzione**

Il sistema deve permettere agli enti erogatori di rimuovere dei beni nei punti di distribuzione specificando quantità e categoria

**Funzionalità \#15.3 – Modifica della quantità dei beni nei punti di distribuzione**

Il sistema deve permettere di aggiornare la quantità dei beni nei punti di distribuzione, aggiungendo o rimuovendo dei beni in base alla tipologia del flusso.

**Funzionalità \#16 – Notifiche e Avvisi (per email)**

Il sistema deve generare notifiche per email per informare gli utenti degli eventi che li riguardano

**Funzionalità \#17 – Visualizza storico attività**

Il sistema deve poter permettere a ogni utente registrato di poter visualizzare il proprio storico delle attività, che sarà differente in base al proprio ruolo all’interno della piattaforma

**Funzionalità \#17.1 – Visualizza storico attività per “Utente beneficiario”**

Il sistema deve consentire a un utente beneficiario di visualizzare il proprio storico delle attività

**Funzionalità \#17.2 – Visualizza storico attività per “Ente donatore”**

Il sistema deve consentire a un ente donatore di visualizzare il proprio storico delle attività

**Funzionalità \#17.3 – Visualizza storico attività per “Ente erogatore”**

Il sistema deve consentire agli utenti che hanno l’accesso all’account della propria organizzazione, registrata come “ente donatore”, di visualizzare lo storico delle attività della propria organizzazione

**Funzionalità \#18 – Download storico attività**

Il sistema deve poter permettere agli utenti registrati di poter scaricare il proprio storico attività in formato PDF

**Funzionalità \#19 – Invio di valutazione e feedback**

Il sistema dopo ogni ritiro di bene e verifica del QR code dell’utente beneficiario in questione, deve consentire agli utenti beneficiari di inviare una feedback con valutazione all’ente erogatore da cui ha effettuato la prenotazione del bene

**Funzionalità \#21 – Gestione punti di distribuzione**

Il sistema deve poter permettere agli enti erogatori di gestire i propri punti di distribuzione

**Funzionalità \#21.1 – Richiesta di aggiunta di un punto di distribuzione**

Il sistema deve poter permettere a un ente erogatore di mandare una richiesta per aprire un nuovo punto di distribuzione che verrà poi gestita dall’amministratore

**Funzionalità \#21.2 – Aggiunta di un punto di distribuzione**

Il sistema deve consentire l’aggiunta di punto di distribuzione.

**Funzionalità \#21.3 – Rimozione di un punto di distribuzione**

Il sistema deve poter permettere a un ente erogatore di rimuovere un proprio punto di distribuzione

**Funzionalità \#21.4 – Aggiornamento punti di distribuzione**

Il sistema deve poter permettere agli enti erogatori di poter aggiornare i propri punti di distribuzione, aggiornando gli orari e i giorni di attività del punto

**Funzionalità \#22 – Visualizzazione richieste di aggiunta punti distribuzione**

Il sistema deve permettere all’amministratore di poter visualizzare le richieste di aggiunta di punti di distribuzione da parte degli enti erogatori

**Funzionalità \#23 – Gestione richieste di aggiunta punti di distribuzione**

Il sistema deve permettere all’amministratore di gestire le richieste di aggiunta di punti di distribuzione, potendo accettare o rifiutare tali richieste. L’accettazione porta all’aggiunta automatica del punto di distribuzione coi suoi dati inviati dall’utente , mentre il rifiuto genera semplicemente un messaggio alle notifiche interne della piattaforma sul profilo dell’utente.

**Funzionalità \#24 – Visualizzazione punti di distribuzione**

Il sistema deve permettere a ogni utente di poter visualizzare ogni punto di distribuzione sulla mappa, vedendo informazioni come orari e giorni di attività e categorie di beni presenti

**Funzionalità \#25 – Visualizzazione prenotazioni effettuate in corso**

Il sistema deve permettere agli utenti beneficiari che hanno una prenotazione in corso, di visualizzare la prenotazioni

**Requisito n.f. \#1-usabilità della mappa**

La mappa del sistema deve garantire una lettura intuitiva, con una legenda che spieghi i simboli utilizzati e con simboli autoesplicativi che rendano chiaro il loro significato senza necessità di ulteriori spiegazioni (es. Croce Rossa per i medicinali), tenendo conto che contrasto tra simboli e mappa deve essere ben marcato affinché i simboli non si confondano con la mappa stessa. Il requisito funzionale \#2 favorisce questo punto. L’obiettivo principale è migliorare la fruibilità e l’esperienza utente, permettendo una navigazione chiara, intuitiva e personalizzata in base alle esigenze dell’utente.

**Requisito n.f. \#2-Persistenza dei dati**

Il sistema deve garantire la sincronizzazione tra utenti, ove è richiesta (es. prenotazione di un bene). Requisito fondamentale affinché venga garantita la persistenza e coerenza dei dati.

**Requisito n.f. \#3- Efficienza sulla sincronizzazione**

Per evitare che un utente tenga una sessione occupata per troppo tempo (ad esempio, nel caso in cui abbia dimenticato aperta la pagina relativa a un prodotto che non desidera più prenotare), è necessario implementare un timer che, allo scadere, liberi la sessione e la renda disponibile per altri utenti. Questo meccanismo è essenziale per prevenire il rallentamento del sistema e per massimizzare la disponibilità dei beni per gli utenti che ne hanno effettivamente bisogno

**Requisito n.f. \#4 – Gestione Tassonomia**

Il sistema deve fornire una Tassonomia gerarchica dei beni, in modo che i beni vengano suddivisi in più categorie (es. Cibo/Vestiti/Farmaci) e poi una suddivisione in sottocategorie (es.Felpe/Giubbotti/Scarpe); tutto questo per avere una suddivisione logica dei beni in modo che gli Enti erogatori associno obbligatoriamente ogni lotto di beni a delle categorie e sottocategorie definite nel catalogo

**Requisito n.f. \#5 – Scalabilità sul numero di punti di interesse**

Il sistema deve essere progettato per gestire l'inserimento di almeno 10 milioni di punti di interesse senza compromettere la velocità di aggiornamento della mappa e dei filtri.

**Requisito n.f \#6 - Protezione dei Dati e Autenticazione**

Il sistema deve garantire la sicurezza dei dati, in particolare per quanto riguarda le informazioni sensibili relative alla distribuzione di beni di prima necessità (ad esempio, dettagli degli enti di distribuzione, dati degli utenti registrati). Deve essere implementato un sistema di protezione robusto per evitare accessi non autorizzati. I dati sensibili devono essere criptati in transito e in archivio. Il sistema deve implementare una autenticazione sicura per gli utenti (ad esempio, autenticazione a due fattori - 2FA) per l'accesso alle aree riservate del sito (come la gestione dei punti di distribuzione). L'applicazione deve rispettare le normative sulla privacy (ad esempio, GDPR in Europa) per la gestione dei dati personali degli utenti e delle organizzazioni.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>12</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Visualizzazione dello storico delle donazioni</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi è un utente registrato (ovvero un beneficiario un Ente donatore o un Ente erogatore) alla piattaforma MAP4AID, nel corso degli ultimi mesi in cui è stato registrato ha effettuato 3 donazioni monetarie la prima 4 giorni fa all’ente “Croce Rossa”, la seconda 20 giorni fa all’ente “Save The Children” e la terza 50 giorni fa all’ente “Unicef”.</p>
<p>Adesso ha dimenticato le quantità esatte donate a questi 3 enti, dunque, decide di accedere al sistema per verificare lo storico delle sue donazioni.</p>
<p>Mario, quindi, accede al sistema inserendo la sua E-mail Mariorossi67@gmail.com con la relativa password “password” e una volta che ha inserito i dati corretti e confermato il codice mandato via email, il sistema lo riconosce e gli consente di accedere alla sua area utente.</p>
<p>A questo punto Mario clicca sul menù a tendina che si apre e tra le varie opzioni presenti sceglie quella che gli interessa, cioè, “Storico donazioni”.</p>
<p>Il sistema reindirizza Mario su una nuova pagina con tutte le donazioni effettuate.</p>
<p>Nella riga legata alla giornata di 4 giorni fa a Mario viene mostrata la sua donazione dove può vedere che l’ente che ha ricevuto i soldi era “Croce Rossa” e la donazione aveva un valore di 50 €, Mario avendo visualizzato il dato che gli interessava torna indietro.</p></th>
</tr>
<tr class="header">
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>13</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Beneficiario scarica lo storico delle prenotazioni</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Paolo Verdi = Beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Paolo Verdi è un Utente registrato alla piattaforma MAP4AID come Beneficiario, nel corso degli ultimi mesi in cui è stato registrato ha effettuato diverse prenotazioni per beni di prima necessità di cui aveva bisogno.</p>
<p>Adesso è interessato a scaricare in formato PDF gli storici di queste prenotazioni, Paolo ha interesse a scaricare le sue prenotazioni in formato settimanale mensile e annuale.</p>
<p>Paolo, quindi, accede al sistema e inserisce le credenziali E-mail e password, rispettivamente Paoloverdi67@gmail.com e “password” una volta che il sistema verifica la sua identità gli consente di accedere alla sua pagina utente.</p>
<p>Una volta che ha effettuato l’accesso Paolo clicca sul menu a tendina che si apre e tra le varie opzioni presenti sceglie quella che gli interessa, cioè, “Storico prenotazioni”.</p>
<p>Il sistema, quindi, carica una nuova pagina, nella quale viene mostrata una tabella con i vari giorni della settimana e sotto di essi le varie prenotazioni effettuate in quel giorno con la relativa fascia oraria e i beni prenotati.</p>
<p>In basso Paolo vede che è presente un bottone che recita “Scarica come PDF” Paolo lo clicca e il sistema va a convertire la tabella in un PDF di 1 pagina dove è presente la tabella.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>3</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Un utente vuole registrarsi e accedere come “donatore”</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Giovanni Esposito=Utente non registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Giovanni Esposito accede alla homepage della piattaforma Map4aid. Clicca su “registrazione”, gli viene chiesto di scegliere di indicare il tipo di utente da diventare tra: “utente beneficiario”, “ente donatore” ed “ente erogatore”. Giovanni sceglie “ente donatore”. Viene reindirizzato ad un form inerente al donatore. Giovanni compila il form:</p>
<ul>
<li><blockquote>
<p>nome:Giovanni</p>
</blockquote></li>
<li><blockquote>
<p>cognome:Esposito</p>
</blockquote></li>
<li><blockquote>
<p>email:<a href="mailto:PanificioDivertente@gmail.com"><u>PanificioDivertente@gmail.com</u></a></p>
</blockquote></li>
<li><blockquote>
<p>password:PaneCaldo24</p>
</blockquote></li>
<li><blockquote>
<p>Partita IVA: IT653786543</p>
</blockquote></li>
<li><blockquote>
<p>Indirizzo sede: via Roma 23,Napoli, 80040</p>
</blockquote></li>
<li><blockquote>
<p>Categoria:alimentare</p>
</blockquote></li>
</ul>
<p>Giovanni riceve una notifica via email che, dato un codice, chiede di inserirlo in un form per confermare l’email. Il codice è corretto, ora Giovanni è registrato. Per accedere alla piattaforma Giovanni clicca su “login” e inserisce email e password:</p>
<ul>
<li><blockquote>
<p>email o username:<a href="mailto:PanificioDivertente@gmail.com"><u>PanificioDivertente@gmail.com</u></a></p>
</blockquote></li>
<li><blockquote>
<p>password:PaneCaldo24</p>
</blockquote></li>
</ul>
<p>Clicca “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come donatore ha accesso a tutte le funzionalità da donatore.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>4</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Un utente vuole registrarsi come “ente erogatore”</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Croce Rossa=organizzazione che vuole registrarsi come ente erogatore</p>
<p>Mattia Accardo=persona che fa parte dell’organizzazione Croce Rossa</p></th>
</tr>
<tr class="odd">
<th><strong>Flow events</strong></th>
<th><p>Mattia Accardo fa parte dell’organizzazione Croce Rossa ed è incaricato di registrare l’organizzazione come ente sulla piattaforma Map4aid; quindi accede alla homepage della piattaforma Map4aid e clicca su “registrazione”, dopodichè gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mattia sceglie "ente erogatore" e viene reindirizzato ad un form inerente all’ente erogatore. Mattia compila il form:</p>
<ul>
<li><blockquote>
<p>Email: <a href="mailto:Crocerossa@gmail.com"><u>Crocerossa@gmail.com</u></a></p>
</blockquote></li>
<li><blockquote>
<p>Password: CroceAiutante</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Nome dell’ente: Croce Rossa</p>
</blockquote></li>
<li><blockquote>
<p>Tipologia ente: associazione no-profit</p>
</blockquote></li>
<li><blockquote>
<p>Indirizzo della sede operativa: Via Pontecitra 76, Marigliano, 80034</p>
</blockquote></li>
<li><blockquote>
<p>Iban: IT6543567456743236754323454</p>
</blockquote></li>
</ul>
<p>Mattia riceve una notifica via email che, dato un codice, chiede di inserirlo in un form per confermare l’email. Il codice è corretto, ora Mattia è registrato. Per accedere alla piattaforma Mattia clicca su “login” e inserisce email e password: email o username:<a href="mailto:Crocerossa@gmail.com"><u>Crocerossa@gmail.com</u></a></p>
<ul>
<li><blockquote>
<p>password:CroceAiutante</p>
</blockquote></li>
</ul>
<p>Clicca “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come ente erogatore ha accesso a tutte le funzionalità da ente erogatore.</p>
<p>Infine Mattia condivide password ed email con tutte le persone facente parti dell’organizzazione</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>10</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Segnalazione di un punto di bisogno sulla mappa da parte di un utente</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Marianna Allocca = Utente</p>
<p>Tutti gli enti registrati alla piattaforma</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Marianna Allocca accede alla homepage di Map4aid e decide di cliccare su “Segnala un punto di bisogno”. Marianna viene reindirizzata su una pagina in cui è presente una mappa dinamica e un campo indirizzo: può scegliere di mandare la segnalazione tramite click sulla mappa oppure inserire un indirizzo specifico. Marianna decide di inserire un indirizzo:</p>
<ul>
<li><blockquote>
<p>Indirizzo: Via Sgroppillo, 21, 95027 San Gregorio di Catania</p>
</blockquote></li>
</ul>
<p>Marianna clicca su “invia segnalazione”, la segnalazione viene mandata con successo a tutti gli enti erogatori registrati sulla piattaforma. Un pop-up avvisa Marianna che la Segnalazione è andata a buon fine.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>18</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Recupero password da parte di un utente registrato</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Giulia Verdi= Utente registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Giulia prova ad accedere alla piattaforma Map4Aid, ma si rende conto di non ricordare la password che aveva creato.</p>
<p>Dalla pagina di login clicca il link “Password dimenticata?”. Viene reindirizzata ad una pagina che le chiede di inserire l’indirizzo email associato al suo account. Giulia digita: <a href="mailto:giulia.verdi@gmail.com"><u>giulia.verdi@gmail.com</u></a>.</p>
<p>Premendo “Invia”, se l’email è corretta allora riceverà un codice da inserire per verificare l’email, altrimenti un messaggio di errore per riprovare ad inserire l’email corretta.</p>
<p>Dopo aver verificato la sua email Giulia viene reindirizzata alla pagina per modificare la password.</p>
<p>Giulia inserisce una nuova password: Gv1234* e la conferma. Appare il pop-up “la password è stata aggiornata con successo”.</p>
<p>Torna quindi alla pagina di login, inserisce l’email e la nuova password e accede.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>21</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th><mark>L’utente beneficiario decide di effettuare una prenotazione, ma successivamente decide di cancellarla</mark></th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Mario Nappi = Utente beneficiario</p>
<p><mark>Medici Senza Frontiere</mark> = Ente erogatore</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Nappi accede alla homepage e decide di loggarsi con il suo account da “utente beneficiario”: clicca su Login e inserisce username e password:</p>
<ul>
<li><blockquote>
<p>email o username: MarioBros</p>
</blockquote></li>
<li><blockquote>
<p>password:Marione1998</p>
</blockquote></li>
</ul>
<p>Clicca su “accedi” e viene reindirizzato alla homepage della piattaforma. Ora che è loggato come utente beneficiario ha accesso a tutte le funzionalità da beneficiario. Mario ha bisogno di prenotare medicinali per la gola. Sulla mappa della homepage filtra i punti di distribuzione che hanno medicinali. Mario clicca sul punto di distribuzione a lui più vicino. Si apre una scheda che mostra tutti i beni prenotabili in quel momento nel punto di distribuzione selezionato. I beni disponibili sono:</p>
<ul>
<li><blockquote>
<p>Pacco di medicinali(erogato da Medici Senza Frontiere)</p>
</blockquote></li>
<li><blockquote>
<p>Pacco di igiene personale(erogato da Medici Senza Frontiere)</p>
</blockquote></li>
</ul>
<p>Mario clicca sul “+” del pacco di medicinali per visualizzarne il contenuto. Il pacco contiene:</p>
<ul>
<li><blockquote>
<p>Tachipirina 1000mg paracetamolo(10 supposte) x2</p>
</blockquote></li>
<li><blockquote>
<p>Tantum verde gola spray x3</p>
</blockquote></li>
</ul>
<p>Mario decide di prenotare il pacco di medicinali cliccando su “prenota”. La prenotazione viene mandata per email all’ente erogatore Medici Senza Frontiera che in risposta manda un ulteriore email a Mario per confermare la sua prenotazione.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>22</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Aggiunta di un punto di distribuzione tramite indirizzo</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Croce Rossa=Ente erogatore</p>
<p>Mattia Bianchi=Operatore dell’Ente erogatore</p>
<p>Marco Rossi=Amministratore del sistema</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mattia, operatore dell’Ente erogatore “Croce Rossa”, si accorge che in una determinata zona della città manca un punto di distribuzione e decide di aggiungerlo sulla piattaforma Map4Aid.</p>
<p>Accede alla piattaforma con il suo account Ente erogatore e si dirige nella sezione “Gestisci dei punti di distribuzione”.</p>
<p>Clicca su “Aggiungi nuovo punto”. Gli appare un form che richiede le seguenti informazioni:</p>
<ul>
<li><blockquote>
<p>Indirizzo:Piazza Garibaldi, Napoli 80040</p>
</blockquote></li>
<li><blockquote>
<p>Orari di apertura: 9-12, 16-19</p>
</blockquote></li>
<li><blockquote>
<p>Giorni di distribuzione: Lunedì. Mercoledì, Venerdì</p>
</blockquote></li>
</ul>
<p>Una volta inseriti tutti i dati, Mattia preme “Conferma” e attende la risposta dell’amministratore del sistema che deciderà in questo caso di accettare la richiesta di aggiunta di un punto di distribuzione.</p>
<p>Una volta che il punto di distribuzione sarà approvato, sarà visibile sulla mappa.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>23</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Rimozione di un punto di distribuzione da parte di un ente</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Mattia accardo= operatore dell’ente erogatore</p>
<p>Croce Rossa= ente erogatore</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mattia Accardo che è un operatore dell’ente “Croce Rossa”, decide di voler rimuovere un punto di distribuzione, quindi effettua il login alla piattaforma Map4aid tramite l’account dell’ente “Croce Rossa”; dopodichè andrà nella sezione “Gestione dei punti di distribuzione” e clicca su “Rimuovi punto di distribuzione”, poi gli verrà mostrata la mappa con i propri punti di distribuzione e sceglie di rimuovere il punto con indirizzo “Piazza Garibaldi, Napoli 80040”.</p>
<p>Gli viene mostrato un pop-up “Punto di distribuzione rimosso con successo”. Il punto scompare dalla mappa e non è più visibile dagli utenti.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>1</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Registrazione e login di un utente (login andato a buon fine)</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente non registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi decide di usufruire del servizio di map4aid e inizia la registrazione tramite la piattaforma. Sulla pagina della registrazione gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mario sceglie “utente beneficiario” e viene reindirizzato al form inerente. Qui compila i campi:</p>
<ul>
<li><blockquote>
<p>Nome: Mario</p>
</blockquote></li>
<li><blockquote>
<p>Cognome: Rossi</p>
</blockquote></li>
<li><blockquote>
<p>Data di nascita: 01/01/2000</p>
</blockquote></li>
<li><blockquote>
<p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>password: Password</mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>Allergeni/Patologie: N/A</mark></p>
</blockquote></li>
</ul>
<p><mark>Mario compila il form e lo invia al sistema che, dopo aver validato i dati, invia una mail di conferma. Il sistema attiva l’account di Mario, il quale può andare sulla pagina di login dove compilare il seguente form:</mark></p>
<ul>
<li><blockquote>
<p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>password: Password</mark></p>
</blockquote></li>
</ul>
<p><mark>Il sistema riconosce e-mail e password come corretti e crea la sessione, loggando Mario e sbloccando le funzionalità destinate agli utenti beneficiari.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>2</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Registrazione e login di un utente (login andato male per via della password)</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente non registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi decide di usufruire del servizio di map4aid e inizia la registrazione tramite la piattaforma. Sulla pagina della registrazione gli viene chiesto di indicare il tipo di utente da diventare tra “utente beneficiario”, “ente donatore”, “ente erogatore”, Mario sceglie “utente beneficiario” e viene reindirizzato al form inerente. Qui compila i campi:</p>
<ul>
<li><blockquote>
<p>Nome: Mario</p>
</blockquote></li>
<li><blockquote>
<p>Cognome: Rossi</p>
</blockquote></li>
<li><blockquote>
<p>Data di nascita: 01/01/2000</p>
</blockquote></li>
<li><blockquote>
<p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>password: Password</mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>Allergeni/Patologie: N/A</mark></p>
</blockquote></li>
</ul>
<p><mark>Mario compila il form e lo invia al sistema che, dopo aver validato i dati, invia una mail di conferma. Il sistema attiva l’account di Mario, il quale può andare sulla pagina di login dove compilare il seguente form:</mark></p>
<ul>
<li><blockquote>
<p><mark>e-mail: <a href="mailto:mariorossi@gmail.com"><u>mariorossi@gmail.com</u></a></mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>password: abcd</mark></p>
</blockquote></li>
</ul>
<p><mark>Il sistema riconosce che la password inserita non è inserita correttamente e notifica Mario, sulla stessa pagina di login, con un messaggio di “E-Mail e/o password errate”. Il sistema non crea la sessione e dà la possibilità a Mario di riprovare l’inserimento dei dati di login.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>5</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Donazione monetaria (andata a buon fine)</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Mario Nappi = Utente beneficiario</p>
<p>Croce Rossa= Ente erogatore</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Nappi che è un Utente beneficiario, decide di voler fare una donazione monetaria.</p>
<p>Procede al login. Clicca sulla sezione “Donazione Monetaria” compilando il modulo presentato dal sistema, inserendo:<br />
-Croce Rossa come Ente erogatore;<br />
-sceglie l’importo della donazione;<br />
-compila i campi relativi ai dati di pagamento e al metodo.</p>
<p>I dati inseriti corrispondono e sono corretti, la transazione avviene. Mario Nappi riceve tempestivamente una notifica (email) di avvenuto successo.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>6</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Donazione monetaria (errore, credito insufficiente)</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Mario Nappi = Utente beneficiario</p>
<p>Croce Rossa = Ente Erogatore</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Nappi che è un Utente beneficiario, decide di voler fare una donazione monetaria.</p>
<p>Procede al login. Clicca sulla sezione “Donazione Monetaria” compilando il modulo presentato dal sistema, inserendo:<br />
-Croce Rossa come Ente erogatore;<br />
-sceglie l’importo della donazione;<br />
-compila i campi relativi ai dati di pagamento e al metodo.</p>
<p>I dati inseriti corrispondono e sono corretti, ma quando avviene la transazione Mario Nappi riceve una notifica a schermo “Transazione fallita”.<br />
Riceve tempestivamente una email dove gli viene comunicato che il credito a disposizione (carte di credito, conto,..) è insufficiente rispetto all’importo da lui scelto, e che la transazione non è andata a buon fine.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>7</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Donazione di un bene alimentare da parte di un ente donatore</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente Giampiero Neri (Panificio Bakery) = Ente donatore<br />
Croce Rossa = Ente erogatore</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th>Giampiero Neri, registrato come Ente Donatore con la sua attività Panificio Bakery, decide di effettuare una donazione all’Ente Erogatore “Croce Rossa” registrato nel sistema.<br />
<br />
L’utente accede nella sua area riservata, clicca sulla sezione “donazione di beni” e compila il modulo presentato dal sistema inserendo:<br />
<br />
- Categoria:Alimentare<br />
- Nome:Pane<br />
- Quantità:2kg<br />
- Ente:Croce rossa<br />
- allergeni:Glutine<br />
- scadenza:10/12/2025<br />
<br />
L’utente clicca su “effettua donazione” e , vista la correttezza dei dati, la richiesta viene inoltrata all’ente erogatore e l’utente visualizza un messaggio “richiesta di donazione inoltrata correttamente all’ente erogatore”.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>8</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Donazione di un bene medicinale da parte di un ente donatore</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente Gianni Rossi (Farmacia centrale) = Ente donatore<br />
FIDAS = Ente erogatore</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th>Gianni Rossi, registrato come Ente Donatore con la sua attività Farmacia Centrale, decide di effettuare una donazione all’Ente Erogatore “FIDAS” registrato nel sistema.<br />
<br />
L’utente accede nella sua area riservata, clicca sulla sezione “donazione di beni” e compila il modulo presentato dal sistema inserendo:<br />
<br />
-Categoria: Medicinali<br />
- Nome:Ibuprofene<br />
- Quantità:1000 mg (5 tubi)<br />
-ente: FIDAS<br />
- tipo:Antinfiammatorio<br />
- scadenza 04/2026<br />
<br />
L’utente clicca su “effettua donazione” e , vista la correttezza dei dati, la richiesta viene inoltrata all’ente erogatore e l’utente visualizza un messaggio “richiesta di donazione inoltrata correttamente all’ente erogatore”.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>14</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Un Utente beneficiario inserisce una valutazione feedback dopo un ritiro di beni avvenuto</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente Beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi dopo aver ritirato il bene, vedrà comparire quest’ultimo nello storico di beni ritirati.</p>
<p>Cliccando sul bene appena ritirato, vedrà comparire a schermo un'interfaccia che conterrà:</p>
<p>- informazioni sul luogo ed orario di ritiro;<br />
- modulo per invio di valutazione e feedback.</p>
<p>Mario Rossi decide di compilare il modulo.</p>
<p>Inserisce una valutazione numerica del servizio ricevuto, che va da un valore minimo di 1 ad uno massimo di 5.</p>
<p>Ed inoltre compila il campo Feedback testuale del modulo inserendo commenti e opinioni su qualche aspetto particolare del servizio ricevuto.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>15</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Un Utente beneficiario, dopo il ritiro del bene prenotato, decide di non inserire recensione e feedback</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente Mario Rossi = Utente Beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi dopo aver ritirato il bene, vedrà comparire quest’ultimo nello storico di beni ritirati.</p>
<p>Cliccando sul bene appena ritirato, vedrà comparire a schermo un'interfaccia che conterrà:</p>
<p>- informazioni sul luogo ed orario di ritiro;</p>
<p>- modulo per invio di valutazione e feedback.</p>
<p>Mario Rossi decide di non compilare il modulo.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>16</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>L’utente visualizza il catalogo (per una categoria) senza prenotare</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi è un utente registrato alla piattaforma MAP4AID e ha effettuato correttamente il login inserendo e-mail e password.</p>
<p>Una volta sulla sua homepage utente, decide di consultare il catalogo dei beni disponibili senza effettuare alcuna prenotazione.</p>
<p>Mario clicca sulla voce di menu “Catalogo”.</p>
<p>Il sistema lo indirizza su una pagina in cui sono mostrate le categorie principali dei beni messi a disposizione dagli enti erogatori</p>
<ul>
<li><blockquote>
<p>Alimentari</p>
</blockquote></li>
<li><blockquote>
<p>Vestiti</p>
</blockquote></li>
<li><blockquote>
<p>Igiene</p>
</blockquote></li>
<li><blockquote>
<p>Medicinali</p>
</blockquote></li>
<li><blockquote>
<p>Varie</p>
</blockquote></li>
</ul>
<p>Mario decide di cliccare sulla categoria Alimentari.</p>
<p>Il sistema aggiorna la schermata mostrando le sottocategorie specifiche (ad esempio: Pane, Pasta, Scatolame, Prodotti senza glutine).</p>
<p>Mario seleziona la sottocategoria “Pane”.</p>
<p>Il sistema visualizza l’elenco dei beni disponibili con le seguenti informazioni:</p>
<ul>
<li><blockquote>
<p>Nome del bene (es. Pane comune, Pane integrale, Pane senza glutine)</p>
</blockquote></li>
<li><blockquote>
<p>Eventuali allergeni</p>
</blockquote></li>
<li><blockquote>
<p>Quantità totale disponibile</p>
</blockquote></li>
<li><blockquote>
<p>Pulsante “Mostra sulla mappa” per visualizzare dove è reperibile</p>
</blockquote></li>
</ul>
<p>Mario scorre la lista dei beni disponibili, ma non clicca su “Mostra sulla mappa” e non effettua alcuna prenotazione.</p>
<p>Dopo aver consultato le informazioni che gli interessavano, decide di tornare alla homepage tramite il menu.</p>
<p>Il sistema non registra alcuna prenotazione e l’operazione si conclude come semplice visualizzazione del catalogo.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>17</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>L’utente visualizza la mappa (per una categoria) senza prenotare</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p>Mario Rossi è un utente registrato alla piattaforma MAP4AID e ha effettuato il login.<br />
Dalla homepage utente decide di visualizzare la mappa dei punti di distribuzione.</p>
<p>Mario clicca sulla voce “Mappa”.</p>
<p>Il sistema apre una schermata contenente una mappa interattiva che mostra tutti i punti di distribuzione registrati sulla piattaforma, ognuno con il proprio marker e la legenda corrispondente.</p>
<p>Sul lato destro della schermata è presente un pannello filtri.<br />
Mario decide di filtrare i punti selezionando la categoria Alimentari.</p>
<p>Il sistema applica il filtro aggiornando i marker sulla mappa, lasciando visibili solo quelli che dispongono di beni appartenenti alla categoria selezionata.</p>
<p>Mario clicca su uno dei marker.</p>
<p>Il sistema apre un riquadro informativo che mostra:</p>
<ul>
<li><blockquote>
<p>Nome del punto di distribuzione</p>
</blockquote></li>
<li><blockquote>
<p>Indirizzo</p>
</blockquote></li>
<li><blockquote>
<p>Orari di apertura</p>
</blockquote></li>
<li><blockquote>
<p>Quantità complessive di beni alimentari disponibili</p>
</blockquote></li>
<li><blockquote>
<p>Pulsante “Prenota”</p>
</blockquote></li>
</ul>
<p>Mario non è interessato a prenotare, quindi non clicca sul pulsante “Prenota”.</p>
<p>Dopo aver consultato le informazioni, chiude il riquadro informativo e torna alla homepage tramite il menu.</p>
<p>Il sistema non registra alcuna prenotazione e l’operazione si conclude come semplice visualizzazione informativa sulla mappa.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>19</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Modifica della password</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Mario Rossi = Utente registrato</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p><mark>Mario Rossi è un utente registrato alla piattaforma ed ha effettuato il login.<br />
Dalla homepage decide di modificare la password del proprio account per motivi di sicurezza.</mark></p>
<p><mark>Mario clicca sulla voce di menu “Profilo”.</mark></p>
<p><mark>Il sistema apre la schermata del profilo utente, che mostra i dati principali dell’account e le impostazioni disponibili.</mark></p>
<p><mark>Nella sezione “Sicurezza” Mario individua l’opzione “Modifica password” e la seleziona.</mark></p>
<p><mark>Il sistema apre una schermata/modale contenente il form per il cambio password, con i seguenti campi:</mark></p>
<ul>
<li><blockquote>
<p><mark>Password attuale</mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>Nuova password</mark></p>
</blockquote></li>
<li><blockquote>
<p><mark>Conferma nuova password</mark></p>
</blockquote></li>
</ul>
<p><mark>Mario inserisce la propria password attuale nel campo dedicato.</mark></p>
<p><mark>Successivamente inserisce una nuova password che rispetta i requisiti indicati dal sistema.</mark></p>
<p><mark>Mario ripete la nuova password nel campo “Conferma nuova password” per confermarla.</mark></p>
<p><mark>Dopo aver compilato tutti i campi, Mario clicca sul pulsante “Salva” (o “Conferma”).</mark></p>
<p><mark>Il sistema verifica che la password attuale inserita sia corretta, che la nuova password rispetti i requisiti di sicurezza e che la conferma coincida con la nuova password.</mark></p>
<p><mark>Le verifiche vanno a buon fine: il sistema aggiorna la password di Mario neil database e invalida, se previsto, le eventuali sessioni attive su altri dispositivi.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>20</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Donazione di un'igiene personale da parte di un donatore</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Donato Torricelli = Utente registrato come ente donatore</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p><mark>Donato Torricelli è un utente registrato in qualità di donatore, che ha effettuato il login.<br />
Dalla homepage utente decide di effettuare una donazione della categoria di igiene personale.</mark></p>
<p><mark>Donato clicca sulla voce “Dona beni”.</mark></p>
<p><mark>Il sistema apre una schermata contenente l’elenco delle categorie di beni donabili.<br />
Tra queste Donato seleziona la categoria <strong>Igiene personale</strong>.</mark></p>
<p><mark>Il sistema apre una schermata che mostra l’elenco degli <strong>enti erogatori registrati</strong> che accettano beni di igiene personale nella zona selezionata.<br />
Per ciascun ente vengono mostrati:<br />
• Nome dell’ente<br />
• Indirizzo<br />
• Orari di ritiro</mark></p>
<p><mark>Il sistema mostra un modulo di inserimento nel quale Donato deve specificare:<br />
-Tipo di bene (es. sapone, shampoo, dentifricio, assorbenti, ecc.)<br />
-Quantità disponibile</mark></p>
<p><mark>-Destinatari<br />
<br />
• Nome</mark></p>
<p><mark>Donato compila tutti i campi richiesti e,</mark></p>
<p><mark>dopo aver inserito i dati, clicca su <strong>“Continua”</strong>.</mark></p>
<p><mark>Donato individua l’ente a cui desidera destinare la donazione e clicca su <strong>“Dona ora”</strong>.</mark></p>
<p><mark>Il sistema mostra un riepilogo della donazione con tutte le informazioni inserite da Donato.<br />
Donato conferma cliccando sul pulsante <strong>“Conferma donazione”</strong>.</mark></p>
<p><mark>Il sistema registra la donazione, la assegna all’ente selezionato e invia la notifica all’ente erogatore con i dettagli del bene donato.</mark></p>
<p><mark>Il sistema mostra un messaggio di conferma del tipo:<br />
“La tua donazione è stata registrata con successo. L’ente selezionato ti contatterà per il ritiro.”</mark></p>
<p><mark>Donato torna alla homepage utente, dove può visualizzare la donazione nella sua cronologia donazioni.</mark></p>
<p><mark>L’operazione si conclude con successo e la donazione è ora disponibile per gli enti erogatori.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>9</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Un utente beneficiario prenota un bene in un punto di ritiro (con QR)</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th>Luca Bianchi = Utente beneficiario</th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p><mark>Luca Bianchi è un utente registrato alla piattaforma MAP4AID come beneficiario e ha correttamente effettuato il login inserendo e-mail e password.</mark></p>
<p><mark>Dalla homepage utente, Luca ha bisogno di prenotare un bene in un punto di distribuzione vicino a casa. Decide quindi di cliccare sulla voce di menu “Mappa”.</mark></p>
<p><mark>Il sistema apre una schermata contenente una mappa interattiva che mostra i punti di distribuzione disponibili. Sul lato della mappa è presente un pannello di filtri che permette di selezionare la categoria di beni desiderata.</mark></p>
<p><mark>Luca seleziona la categoria di beni che gli interessa (ad esempio “Alimentari”, “Igiene personale” o “Medicinali”) e applica i filtri. Il sistema aggiorna i marker sulla mappa mostrando solo i punti che dispongono di beni appartenenti a quella categoria.</mark></p>
<p><mark>Luca individua il punto di distribuzione più comodo per lui e clicca sul relativo marker.</mark></p>
<p><mark>Il sistema apre un riquadro informativo con i dettagli del punto di distribuzione (nome, indirizzo, orari di apertura, breve descrizione) e l’elenco dei beni prenotabili in quel punto, con le relative quantità disponibili.</mark></p>
<p><mark>Dall’elenco dei beni disponibili, Luca seleziona il bene di suo interesse e clicca sul pulsante “Prenota”.</mark></p>
<p><mark>Il sistema mostra una schermata di riepilogo della prenotazione contenente: il punto di ritiro selezionato, il bene scelto, la quantità, l’eventuale fascia oraria di ritiro e, se previsto, le condizioni del servizio.</mark></p>
<p><mark>Luca controlla che i dati siano corretti e conferma la prenotazione cliccando su “Conferma prenotazione”.</mark></p>
<p><mark>Il sistema registra la prenotazione, aggiorna le quantità disponibili del bene nel punto di distribuzione scelto e genera un codice QR univoco associato alla prenotazione stessa.</mark></p>
<p><mark>Il codice QR viene mostrato a schermo e salvato all’interno dell’area personale di Luca, nella sezione “Le mie prenotazioni”. Inoltre, il sistema invia una e-mail di conferma contenente i dettagli della prenotazione e il QR da utilizzare al momento del ritiro.</mark></p>
<p><mark>Terminata l’operazione, Luca può chiudere la schermata o tornare alla homepage, sapendo di poter mostrare il QR presso il punto di ritiro nel giorno e nell’orario indicati.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th>11</th>
</tr>
<tr class="odd">
<th><strong>Name</strong></th>
<th>Aggiunta di scorte in un punto di distribuzione da parte di un ente</th>
</tr>
<tr class="header">
<th><strong>Actors</strong></th>
<th><p>Caritas Sant’Anna = Ente erogatore</p>
<p>Anna Verdi = Operatrice dell’ente erogatore</p></th>
</tr>
<tr class="odd">
<th><strong>Flow Events</strong></th>
<th><p><mark>Anna Verdi è un’operatrice dell’ente erogatore “Caritas Sant’Anna”, registrata alla piattaforma MAP4AID. Ha effettuato il login con le credenziali dell’ente.</mark></p>
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
<p><mark>Anna torna alla schermata riepilogativa delle scorte del punto di distribuzione, dove può vedere le nuove quantità aggiornate e, se necessario, procedere con ulteriori modifiche.</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#1 (REGISTRAZIONE)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#01</em></p></th>
<th colspan="3" rowspan="3"><em>Registrazione</em></th>
<th colspan="6"><em>Data</em></th>
<th colspan="3"><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th colspan="3"><em>Vers.</em></th>
<th colspan="6"><em>0.00.002</em></th>
</tr>
<tr class="header">
<th colspan="3"><em>Autore</em></th>
<th colspan="6"><p><em>Giovanni Esposito /</em></p>
<p><em>Nicola Luciano</em></p></th>
</tr>
<tr class="odd">
<th colspan="12"><strong>Descrizione</strong></th>
<th colspan="12">Processo in cui un nuovo utente crea un account nel sistema</th>
</tr>
<tr class="header">
<th colspan="12"><strong>Attore Principale</strong></th>
<th colspan="12"><strong>Utente non registrato</strong></th>
</tr>
<tr class="odd">
<th colspan="12"><strong>Attori secondari</strong></th>
<th colspan="12"><strong>Amministratore</strong></th>
</tr>
<tr class="header">
<th colspan="12"><strong>Entry Condition</strong></th>
<th colspan="12">L'utente non possiede un account esistente.</th>
</tr>
<tr class="odd">
<th colspan="12"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="12">L'utente dispone di un account valido e può autenticarsi</th>
</tr>
<tr class="header">
<th colspan="12"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="12">L’utente non viene registrato nel sistema</th>
</tr>
<tr class="odd">
<th colspan="12"><strong>Rilevanza/User Priority</strong></th>
<th colspan="12">Alta</th>
</tr>
<tr class="header">
<th colspan="12"><strong>Frequenza stimata</strong></th>
<th colspan="12">Alta</th>
</tr>
<tr class="odd">
<th colspan="12"><strong>Extension point</strong></th>
<th colspan="12">N/A</th>
</tr>
<tr class="header">
<th colspan="12"><strong>Generalization of</strong></th>
<th colspan="12">N/A</th>
</tr>
<tr class="odd">
<th colspan="24"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th colspan="3">1</th>
<th colspan="6">Utente non registrato:</th>
<th colspan="15"><blockquote>
<p>L'utente accede alla pagina di registrazione e sceglie il tipo di account tra “beneficiario”,”ente donatore" e “ente erogatore”</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3">2</th>
<th colspan="6"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="15"><blockquote>
<p>Il sistema propone il form da compilare all'utente in base al ruolo scelto.</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3">3</th>
<th colspan="6">Utente non registrato:</th>
<th colspan="15">L'utente compila il form e invia i dati.</th>
</tr>
<tr class="odd">
<th colspan="3">4</th>
<th colspan="6"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="15">Il sistema invia una mail con un codice di conferma che l’utente dovrà utilizzare per validare la sua email</th>
</tr>
<tr class="header">
<th colspan="3">5</th>
<th colspan="6"><blockquote>
<p>Utente non registrato</p>
</blockquote></th>
<th colspan="15">L’utente inserisce correttamente il codice di verifica</th>
</tr>
<tr class="odd">
<th colspan="3">6</th>
<th colspan="6"><blockquote>
<p>Sistema</p>
</blockquote></th>
<th colspan="15">Il sistema registra l’account dell’utente nel suo database</th>
</tr>
<tr class="header">
<th colspan="24"></th>
</tr>
<tr class="odd">
<th colspan="24"><strong>I Scenario/Flusso di eventi Alternativo:</strong> L'utente sceglie di essere beneficiario</th>
</tr>
<tr class="header">
<th colspan="6"><strong>3.1</strong></th>
<th colspan="6"><strong>Sistema:</strong></th>
<th colspan="12">Il sistema manda l’account con i dati all’amministratore</th>
</tr>
<tr class="odd">
<th colspan="6"><strong>3.2</strong></th>
<th colspan="6"><strong>Amministratore:</strong></th>
<th colspan="12">L’amministratore valida la carta d’identità dell’utente, controllando che il codice inserito corrisponda alla carta.</th>
</tr>
<tr class="header">
<th colspan="6"><strong>3.3</strong></th>
<th colspan="6"><strong>Sistema:</strong></th>
<th colspan="12">Il sistema registra l’account dell’utente nel suo database</th>
</tr>
<tr class="odd">
<th colspan="12"></th>
<th colspan="12"></th>
</tr>
<tr class="header">
<th colspan="24"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> L’account beneficiario non viene validato</th>
</tr>
<tr class="odd">
<th colspan="6"><strong>3.2.1</strong></th>
<th colspan="6"><strong>Amministratore:</strong></th>
<th colspan="12">L’amministratore decide di rifiutare l’account del beneficiario</th>
</tr>
<tr class="header">
<th colspan="6"><strong>3.2.1</strong></th>
<th colspan="6"><strong>Sistema:</strong></th>
<th colspan="12">Il sistema notifica tramite email all’utente che il suo account non è stato validato</th>
</tr>
<tr class="odd">
<th colspan="24"></th>
</tr>
<tr class="header">
<th colspan="24"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Email già registrata</th>
</tr>
<tr class="odd">
<th colspan="6"><strong>3.1</strong></th>
<th colspan="6"><strong>Sistema:</strong></th>
<th colspan="12">Il sistema notifica con un messaggio di errore “Email già registrata” il fatto che all’email inserita corrisponde già un account esistente.</th>
</tr>
<tr class="header">
<th colspan="12"></th>
<th colspan="12"></th>
</tr>
<tr class="odd">
<th colspan="24"><strong>III Scenario/Flusso di eventi di ERRORE:</strong> Codice di verifica non valido</th>
</tr>
<tr class="header">
<th colspan="6"><strong>5.1</strong></th>
<th colspan="6"><strong>Sistema:</strong></th>
<th colspan="12">Il sistema notifica con un messaggio di errore “codice non valido” il fatto che i campi non risultano validi secondo i controlli formali</th>
</tr>
<tr class="odd">
<th colspan="12"></th>
<th colspan="12"></th>
</tr>
<tr class="header">
<th colspan="12"><strong>Special Requirements</strong></th>
<th colspan="12">Nessuna informazione deve essere tracciata oltre quanto strettamente necessario (privacy by design)</th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#02</em></p></th>
<th rowspan="3"><em>Login</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><p><em>Giovanni Esposito /</em></p>
<p><em>Nicola Luciano</em></p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">Un utente registrato accede al sistema inserendo email e password. Se le credenziali sono corrette, il sistema invia un codice OTP via email. L’utente inserisce il codice e completa l’accesso. Per i beneficiari è richiesto che l’account sia stato approvato dall’amministratore.</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><strong>Utente registrato</strong></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">L’utente possiede un account valido, non è già autenticato. Se l’utente è un beneficiario, l’account deve essere approvato</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Autenticazione utente riuscita</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">L’utente non è riuscito ad autenticarsi</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2">Utente registrato:</th>
<th colspan="5"><blockquote>
<p>L'utente accede alla pagina di login</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Il sistema propone il form da compilare all'utente.<br />
Il form prevede l'inserimento di email e password.</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2">Utente registrato:</th>
<th colspan="5">L'utente compila il form e invia i dati.</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema verifica i dati e se l’account è di tipo beneficiario, controlla che se è stato approvato dall’amministratore. Genera un codice OTP e lo invia per email</th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><blockquote>
<p>Utente registrato:</p>
</blockquote></th>
<th colspan="5">Inserisce il codice OTP ricevuto via email</th>
</tr>
<tr class="odd">
<th>6</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Verifica codice inserito, se corretto crea la sessione e autentica l’</th>
</tr>
<tr class="header">
<th colspan="8"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> L’utente clicca su “Password dimenticata”</th>
</tr>
<tr class="header">
<th colspan="2"><strong>3.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema invia una mail contenente il link per il reset della password.</th>
</tr>
<tr class="odd">
<th colspan="2"></th>
<th colspan="2"><strong>Utente registrato:</strong></th>
<th colspan="4">L’utente usa il link inviato per mail per accedere al form di reset</th>
</tr>
<tr class="header">
<th colspan="2"></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema propone il form per inserire la nuova password, quando la password inserita supera gli standard di sicurezza, la password è correttamente modificata, e l’utente riceve una notifica a schermo.</th>
</tr>
<tr class="odd">
<th colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> Account beneficiario non approvato</th>
</tr>
<tr class="header">
<th colspan="2"><strong>3.2</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema riferisce all’utente che l’account non è stato ancora approvato dall’amministratore</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Codice OTP errato</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema non trova corrispondenza con il codice OTP inserito dall’utente, glielo comunica tramite messaggio di errore e lo invita a riprovare.</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Credenziali non valide</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema verifica le credenziali e non trovando corrispondenza, notifica all’utente “Credenziali non valide” e lo invita ad inserirle nuovamente.</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#03</em></p></th>
<th rowspan="3"><em>Donazione monetaria</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>17/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Vito Francesco Maistrini / Giovanni De Caro</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">Un utente autenticato (donatore, beneficiario o ente erogatore) effettua una donazione monetaria verso un ente erogatore. Il sistema valida i dati della carta, effettua la transazione, registra la donazione e invia una email di conferma all’ente.</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente non registrato/Utente registrato</strong></p>
<p>Interessato a donare per beneficenza una certa somma di denaro</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione monetaria dal utente</p></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">Esiste almeno un ente disponibile per la donazione</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Transazione di pagamento andata a buon fine (La donazione è stata registrata)</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">Transazione di pagamento andata in fallimento (Nessuna donazione è stata registrata)</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Medio-Alta</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Media</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></th>
<th colspan="5">Clicca su “Donazione monetaria”</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Mostra un modulo da compilare con scelta dell’ente, importo desiderato e dati di pagamento.</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Utente:</p>
</blockquote></th>
<th colspan="5">Compila il modulo e lo invia</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Compie un controllo sulle informazioni inserite</th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Invia la donazione e una notifica all’ente erogatore scelto</th>
</tr>
<tr class="odd">
<th>6</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Invia una notifica di successo all’utente</th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Dati di pagamento non validi</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema si accorge che il metodo di pagamento non è valido (CVV inesistente/numero carta inesistente), e notifica all’utente che i dati inseriti non sono validi</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Importo non valido</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema si accorge che l’importo inserito non è valido, e lo notifica all’utente</th>
</tr>
<tr class="header">
<th colspan="8"><strong>Note</strong></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>1</strong></th>
<th colspan="4">“Donazione monetaria” è un componente dell’interfaccia</th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#04</em></p></th>
<th rowspan="3"><em>Donazioni di beni</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.0001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Gabriele Milone / Carlo Antonio Caserta</em></th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Descrizione</strong></th>
<th colspan="4">Un utente donatore effettua una donazione di beni materiali verso un punto di distribuzione. Il sistema registra il bene, crea la donazione, determina l’indirizzo e invia email di conferma sia al donatore che all’ente erogatore.</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente Donatore</strong></p>
<p>Interessato a donare una certa quantità di beni.</p></th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Attori secondari</strong></th>
<th colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione dall’utente</p></th>
</tr>
<tr class="header">
<th colspan="3"><strong>Entry Condition</strong></th>
<th colspan="4">L’utente è autenticato come donatore ed esiste un punto distribuzione valido</th>
</tr>
<tr class="odd">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Entrambe le mail vengono inviate, e donatore e ente erogatore sono pronti per accordarsi per la consegna del bene.</th>
</tr>
<tr class="header">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">I dati dei beni da donare non sono validi</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Frequenza stimata</strong></th>
<th colspan="4">Medio-bassa</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th><blockquote>
<p>Ente Donatore:</p>
</blockquote></th>
<th colspan="5">Compila il modulo per la donazione specifica indicando anche il punto di distribuzione scelto.</th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Convalida i dati e inoltra il modulo all’ente</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th><blockquote>
<p>Ente Erogatore:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Riceve i dati del modulo</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Invia le mail al donatore e all’erogatore mettendoli in contatto diretto per organizzare il ritiro.</th>
</tr>
<tr class="header">
<th>5</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Salva la donazione effettuata nello storico</em></th>
</tr>
<tr class="odd">
<th colspan="7"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> i dati inseriti non sono validi</th>
</tr>
<tr class="header">
<th>1.1</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Notifica il donatore che i dati inseriti nel form non sono validi specificando quali</th>
</tr>
<tr class="odd">
<th colspan="7"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Email non inviate</th>
</tr>
<tr class="header">
<th>1.1</th>
<th>Sistema</th>
<th colspan="5">Il sistema notifica il donatore con un avviso “Donazione effettuata ma email non inviate”</th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#05</em></p></th>
<th rowspan="3"><em>Prenotazione ritiro beni di prima necessità</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/25</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autori</em></th>
<th colspan="2"><em>Luciano Corvino / Cristian Carotenuto</em></th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Descrizione</strong></th>
<th colspan="4"><em>L'utente registrato come beneficiario seleziona una posizione sulla mappa tra quelle disponibili e ha la possibilità di selezionare ciò di cui ha bisogno e poi di prenotare uno slot orario nel quale potrà andare nel punto di ritiro scelto e ritirare i beni.</em></th>
</tr>
<tr class="header">
<th colspan="3"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente Beneficiario</strong></p>
<p>Interessato a prenotare i beni di suo interesse</p></th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Attore Secondario</strong></th>
<th colspan="4"><p><strong>Ente Erogatore</strong></p>
<p>Riceve una notifica della prenotazione dei beni</p></th>
</tr>
<tr class="header">
<th colspan="3"><strong>Entry Condition</strong></th>
<th colspan="4">Esiste almeno un punto di distribuzione con dei beni disponibili e l’account ha a disposizione almeno una prenotazione per un tipo di bene</th>
</tr>
<tr class="odd">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">L'utente riesce con successo a prenotare lo slot orario nel quale andare a ritirare i beni prenotati.</th>
</tr>
<tr class="header">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">L’utente riesce a prenotarsi,a ritirare il pacco e la quantità del bene decrementa di 1</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Frequenza stimata</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th><blockquote>
<p><strong>Utente Beneficiario:</strong></p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>L’utente visualizza i punti di distribuzione disponibili sulla mappa da cui può effettuare l’operazione di prenotazione e seleziona il punto desiderato.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Il sistema mostra all'utente la selezione dei beni disponibili nel punto di ritiro selezionato.</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th><blockquote>
<p><strong>Utente Beneficiario:</strong></p>
</blockquote></th>
<th colspan="5">L'utente seleziona il bene che desidera oppure un pacco alimentare e invia una conferma al sistema.</th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema registra la prenotazione e manda un’email all’ente erogatore e al beneficiario</th>
</tr>
<tr class="header">
<th>5</th>
<th><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></th>
<th colspan="5">Riceve la notifica della prenotazione dei beni</th>
</tr>
<tr class="odd">
<th>6</th>
<th><blockquote>
<p><strong>Utente beneficiario:</strong></p>
</blockquote></th>
<th colspan="5">Si presenta al punto di ritiro con il QRcode fornitogli dall’email.</th>
</tr>
<tr class="header">
<th>7</th>
<th><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></th>
<th colspan="5">Scannerizza il QRCode</th>
</tr>
<tr class="odd">
<th>8</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Aggiorna la prenotazione come “ritirata”</th>
</tr>
<tr class="header">
<th colspan="7"><strong>I Scenario/Flusso di eventi ALTERNATIVO:</strong> il beneficiario prenota un bene di tipo medicinale</th>
</tr>
<tr class="odd">
<th>3.1</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema registra la prenotazione come “in validazione”</th>
</tr>
<tr class="header">
<th>3.2</th>
<th><blockquote>
<p><strong>Ente erogatore:</strong></p>
</blockquote></th>
<th colspan="5">L’ente valida la prenotazione controllando se la ricetta fornita dall’ente è corretta.</th>
</tr>
<tr class="odd">
<th>3.3</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema registra la prenotazione come “in attesa"</th>
</tr>
<tr class="header">
<th>3.4</th>
<th><blockquote>
<p><strong>Utente beneficiario:</strong></p>
</blockquote></th>
<th colspan="5">Si presenta al punto di ritiro con il QRcode fornitogli dall’email.</th>
</tr>
<tr class="odd">
<th>3.5</th>
<th><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></th>
<th colspan="5">Scannerizza il QRcode</th>
</tr>
<tr class="header">
<th>3.6</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Aggiorna la prenotazione come “ritirata”</th>
</tr>
<tr class="odd">
<th colspan="7" rowspan="2"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> l’ente rifiuta la prenotazione del bene medicinale</th>
</tr>
<tr class="header">
</tr>
<tr class="odd">
<th>3.1.1</th>
<th><blockquote>
<p><strong>Ente erogatore:</strong></p>
</blockquote></th>
<th colspan="5">L’ente decide di rifiutare la prenotazione del bene medicinale</th>
</tr>
<tr class="header">
<th>3.1.2</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema cancella la prenotazione, aggiorna le quantità nel database e manda un’email per notificare il beneficiario</th>
</tr>
<tr class="odd">
<th colspan="7"></th>
</tr>
<tr class="header">
<th colspan="7"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> il beneficiario cancella la sua prenotazione</th>
</tr>
<tr class="odd">
<th>5.1</th>
<th><blockquote>
<p><strong>Utente beneficiario:</strong></p>
</blockquote></th>
<th colspan="5">L’utente decide di cancellare la sua prenotazione</th>
</tr>
<tr class="header">
<th>5.2</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema cancella la prenotazione, aggiorna le quantità nel database e manda un’email per notificare l’ente</th>
</tr>
<tr class="odd">
<th colspan="7"></th>
</tr>
<tr class="header">
<th colspan="7"><strong>III Scenario/Flusso di eventi di ERRORE:</strong> il beneficiario ha terminato momentaneamente le prenotazioni per un tipo di bene</th>
</tr>
<tr class="odd">
<th>3.1</th>
<th><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5">Il sistema avvisa l'utente che non può effettuare la donazione del bene specifico, poiché ne ha piazzata una troppo recentemente</th>
</tr>
<tr class="header">
<th colspan="7"></th>
</tr>
<tr class="odd">
<th colspan="7"><strong>IV Scenario/Flusso di eventi di ERRORE:</strong> il beneficiario non ritira la prenotazione entro 4 giorni</th>
</tr>
<tr class="header">
<th>5.1</th>
<th><strong>Sistema:</strong></th>
<th colspan="5">Passati 4 giorni da una prenotazione il sistema la cancella se non è stata ritirata,aggiorna le quantità nel database e manda un’email all’utente per notificarlo</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO#6: (SEGNALAZIONE DI UN PUNTO DI BISOGNO SULLA MAPPA)**

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 35%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #06</p></th>
<th colspan="2" rowspan="3"><em>Segnalazione di un punto di bisogno sulla mappa</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>17/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Maria Chiara Gregorio/ Riccardo Di Girolamo</em></th>
</tr>
<tr class="odd">
<th colspan="5"><strong>Descrizione</strong></th>
<th colspan="5">Un utente autenticato (donatore, beneficiario o ente erogatore) invia una segnalazione riguardante un punto di bisogno, indicando latitudine, longitudine e indirizzo. Il sistema inoltra la segnalazione via email a tutti gli enti erogatori presenti nel sistema.</th>
</tr>
<tr class="header">
<th colspan="5"><strong>Attore Principale</strong></th>
<th colspan="5"><p><strong>Utente autenticato</strong></p>
<p>Segnalare un’area di criticità e permettere al sistema di attivare un nuovo punto di aiuto.</p></th>
</tr>
<tr class="odd">
<th colspan="5"><strong>Attori secondari</strong></th>
<th colspan="5"><p><strong>Ente erogatore</strong></p>
<p>Ricevere le segnalazioni, verificarle e decidere se attivare un nuovo punto di supporto.</p></th>
</tr>
<tr class="header">
<th colspan="5"><strong>Entry Condition</strong></th>
<th colspan="5">L’utente è autenticato, ed esiste almeno un ente erogatore nel sistema.</th>
</tr>
<tr class="odd">
<th colspan="5"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="5">La segnalazione è registrata nel sistema e inoltrata agli enti amministratori.</th>
</tr>
<tr class="header">
<th colspan="5"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="5">N/A</th>
</tr>
<tr class="odd">
<th colspan="5"><strong>Rilevanza/User Priority</strong></th>
<th colspan="5">Medio</th>
</tr>
<tr class="header">
<th colspan="5"><strong>Frequenza stimata</strong></th>
<th colspan="5">Medio/bassa</th>
</tr>
<tr class="odd">
<th colspan="5"><strong>Extension point</strong></th>
<th colspan="5">N/A</th>
</tr>
<tr class="header">
<th colspan="5"><strong>Generalization of</strong></th>
<th colspan="5">N/A</th>
</tr>
<tr class="odd">
<th colspan="10"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="3">Utente<strong>:</strong></th>
<th colspan="6"><blockquote>
<p>Seleziona sulla mappa l’opzione <em>“Segnala punto di bisogno”</em>.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="3"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="6"><blockquote>
<p>Mostra il modulo di segnalazione con i campi richiesti</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="3"><blockquote>
<p>Utente:</p>
</blockquote></th>
<th colspan="6">Inserisce i dati richiesti</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="3"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="6">Valida i dati inseriti (tutti i campi obbligatori compilati).</th>
</tr>
<tr class="header">
<th>6</th>
<th colspan="3"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="6">Registra la segnalazione e la inoltra agli enti erogatori tramite mail</th>
</tr>
<tr class="odd">
<th>7</th>
<th colspan="3"><blockquote>
<p>Utente:</p>
</blockquote></th>
<th colspan="6">Visualizza il messaggio <em>“Segnalazione inviata correttamente”</em>.</th>
</tr>
<tr class="header">
<th colspan="10"></th>
</tr>
<tr class="odd">
<th colspan="10"><strong>I Scenario Alternativo</strong>: L’utente seleziona la posizione attraverso indirizzo</th>
</tr>
<tr class="header">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="4"><strong>Cittadino beneficiario:</strong></th>
<th colspan="4">Inserisce un indirizzo manualmente invece di cliccare sulla mappa.</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.2</strong></th>
<th colspan="4"><strong>Sistema:</strong></th>
<th colspan="4">Converte l’indirizzo in coordinate (geocoding) e mostra l’anteprima sulla mappa.</th>
</tr>
<tr class="header">
<th colspan="10"></th>
</tr>
<tr class="odd">
<th colspan="10"><strong>Note</strong></th>
</tr>
<tr class="header">
<th colspan="5"></th>
<th colspan="5">Le segnalazioni non sono immediatamente visibili sulla mappa fino ad approvazione degli enti.</th>
</tr>
<tr class="odd">
<th colspan="5"></th>
<th colspan="5"></th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="3" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#07</em></p></th>
<th rowspan="3">Gestione e aggiornamento scorte</th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th>Autore</th>
<th colspan="2">Giovanni Esposito / Nicola Luciano</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Descrizione</strong></th>
<th colspan="4"><em>P</em>ermette agli enti erogatori di monitorare in tempo reale le scorte di beni disponibili nei propri punti di raccolta o distribuzione tramite una specifica interfaccia.</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Ente erogatore</strong></p>
<p>E’ interessato a inserire o rimuovere beni da punti di raccolta</p></th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Attori secondari</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Entry Condition</strong></th>
<th colspan="4">L’utente è autenticato come ente erogatore</th>
</tr>
<tr class="odd">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Le scorte vengono visualizzate, modificate, aggiunte o rimosse correttamente</th>
</tr>
<tr class="header">
<th colspan="3"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">Scorte non aggiornate.</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Frequenza stimata</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="odd">
<th colspan="3"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="3"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="7"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th><blockquote>
<p><strong>Ente erogatore:</strong></p>
</blockquote></th>
<th colspan="5">Accede alla dashboard dove è possibile richiedere la lista dei beni in un proprio punto e gestirli.</th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Mostra i dati relativi all’operazione selezionata</th>
</tr>
<tr class="header">
<th>3</th>
<th><strong>Ente erogatore:</strong></th>
<th colspan="5">Modifica quantità di un bene esistente in un determinato punto di ritiro (non ci occupiamo della logica dietro la consegna del nuovo bene incrementato)</th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema aggiorna il numero di scorte per tenere traccia di permanenza dell’aggiornamento, e di conseguenza l’interfaccia utente.</th>
</tr>
<tr class="header">
<th colspan="3"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="7"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Punto non valido</th>
</tr>
<tr class="header">
<th><strong>1</strong></th>
<th colspan="2">Sistema:</th>
<th colspan="4">Il sistema notifica l’ente che il punto selezionato non è sotto la propria gestione</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#8 RICHIESTA AGGIUNTA DI UN PUNTO DI DISTRIBUZIONE**

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#8</em></p></th>
<th colspan="3" rowspan="3">Richiesta aggiunta di un punto di distribuzione</th>
<th colspan="6"><em>Data</em></th>
<th colspan="3"><em>2/12/2025</em></th>
</tr>
<tr class="odd">
<th colspan="3"><em>Vers.</em></th>
<th colspan="6"><em>0.00.0001</em></th>
</tr>
<tr class="header">
<th colspan="3"><em>Autore</em></th>
<th colspan="6"><em>Gabriele Milone / Carlo Antonio Caserta</em></th>
</tr>
<tr class="odd">
<th colspan="9"><strong>Descrizione</strong></th>
<th colspan="12">Un ente erogatore autenticato invia una richiesta per creare un nuovo punto di distribuzione. Il sistema verifica lo schema della tabella, inserisce il punto con i campi disponibili.</th>
</tr>
<tr class="header">
<th colspan="9"><strong>Attore Principale</strong></th>
<th colspan="12"><p><strong>Ente erogatore</strong></p>
<p>E’ interessato all’aggiunta di punti di distribuzione di sua appartenenza all’interno del sistema.</p></th>
</tr>
<tr class="odd">
<th colspan="9"><strong>Attori secondari</strong></th>
<th colspan="12"><strong>N/A</strong></th>
</tr>
<tr class="header">
<th colspan="9"><strong>Entry Condition</strong></th>
<th colspan="12">L’utente è autenticato all’interno del sistema come ente erogatore.</th>
</tr>
<tr class="odd">
<th colspan="9"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="12">Richiesta inoltrata e se accettata, punto creato</th>
</tr>
<tr class="header">
<th colspan="9"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="12">Il sistema non registra alcuna nuova richiesta e visualizza un messaggio di errore indicando eventuali dati mancanti o non validi.</th>
</tr>
<tr class="odd">
<th colspan="9"><strong>Rilevanza/User Priority</strong></th>
<th colspan="12">Alta</th>
</tr>
<tr class="header">
<th colspan="9"><strong>Frequenza stimata</strong></th>
<th colspan="12">Alta</th>
</tr>
<tr class="odd">
<th colspan="9"><strong>Extension point</strong></th>
<th colspan="12">N/A</th>
</tr>
<tr class="header">
<th colspan="9"><strong>Generalization of</strong></th>
<th colspan="12">N/A</th>
</tr>
<tr class="odd">
<th colspan="21"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO I</span></strong></th>
</tr>
<tr class="header">
<th colspan="3">1</th>
<th colspan="3"><blockquote>
<p><strong>Ente erogatore</strong>:</p>
</blockquote></th>
<th colspan="15">Accede alla sezione dedicata alla gestione dei punti e seleziona l'opzione "Aggiungi nuovo punto".</th>
</tr>
<tr class="odd">
<th colspan="3">2</th>
<th colspan="3"><blockquote>
<p><strong>Sistema</strong>:</p>
</blockquote></th>
<th colspan="15">Visualizza il form per l'inserimento dei dettagli del punto di distribuzione.</th>
</tr>
<tr class="header">
<th colspan="3">3</th>
<th colspan="3"><blockquote>
<p><strong>Ente Erogatore:</strong></p>
</blockquote></th>
<th colspan="15">Compila i campi richiesti con le informazioni del nuovo punto.</th>
</tr>
<tr class="odd">
<th colspan="3">5</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Verifica la validità formale dei dati inseriti (es. campi obbligatori compilati, formato dati corretto).</th>
</tr>
<tr class="header">
<th colspan="3">7</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Notifica l’ente erogatore che la richiesta è stata salvata correttamente.</th>
</tr>
<tr class="odd">
<th colspan="3">8</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Notifica l’amministratore dell’arrivo di una nuova richiesta di aggiunta di un punto di distribuzione.</th>
</tr>
<tr class="header">
<th colspan="21"><strong><span class="smallcaps">FLUSSO DI EVENTI ALTERNATIVO I :</span></strong> Annullamento inserimento</th>
</tr>
<tr class="odd">
<th colspan="3">3.1</th>
<th colspan="3"><blockquote>
<p><strong>Ente erogatore</strong>:</p>
</blockquote></th>
<th colspan="15">Prima di inviare i dati, l’utente decide di annullare l’operazione, premendo “indietro” o “annulla”.</th>
</tr>
<tr class="header">
<th colspan="3">3.2</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Il sistema scarta i dati inseriti senza salvarli.</th>
</tr>
<tr class="odd">
<th colspan="3">3.3</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Il sistema riporta l’utente alla schermata precedente.</th>
</tr>
<tr class="header">
<th colspan="21"><strong><span class="smallcaps">FLUSSO DI EVENTI DI ERRORE I :</span></strong> Dati mancanti o non validi</th>
</tr>
<tr class="odd">
<th colspan="3">5.1</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Durante la verifica dei dati, il sistema rileva che uno o più campi obbligatori sono vuoti o che alcuni dati non rispettano il formato richiesto.</th>
</tr>
<tr class="header">
<th colspan="3">5.2</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Il sistema scarta la richiesta.</th>
</tr>
<tr class="odd">
<th colspan="3">5.3</th>
<th colspan="3"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="15">Il sistema mostra un messaggio di errore in cui evidenzia i campi da correggere/aggiungere</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**\#9: (*Visione storico attività e reportistica*)**

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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#9</em></p></th>
<th rowspan="3"><em><strong>Visione storico attività e reportistica</strong></em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/25</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Luciano Corvino / Cristian Carotenuto</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">L’utente autenticato può visualizzare il proprio storico attività (prenotazioni, donazioni di beni, donazioni monetarie) e scaricare un PDF riepilogativo generato dinamicamente dal sistema. Il contenuto del PDF varia in base al tipo di account.</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente registrato</strong></p>
<p>L’utente è interessato a visualizzare il proprio storico movimenti</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">L’utente è autenticato ed esistono attività associate ad esso.</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">L'utente visualizza il proprio storico attività o scarica il PDF relativo ad esse</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">Nessuna attività trovata</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Medio/Bassa</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Medio/Bassa</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p><strong>Utente registrato:</strong></p>
</blockquote></th>
<th colspan="5">L'Utente accede all'area del profilo dove puo esserre visualizzato lo storico.</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Il sistema lo porta sull'interfaccia adatta, mostrando anche le opzioni di report</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p><strong>Utente registrato:</strong></p>
</blockquote></th>
<th colspan="5">L'Utente in base al ruolo puo generare le informazioni che gli interessano (donazioni per donatori, prenotazioni per beneficiari..)</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema mostra lo storico delle attività</th>
</tr>
<tr class="header">
<th colspan="8"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI ALTERNATIVO I :</span></strong> Download pdf</th>
</tr>
<tr class="header">
<th colspan="2"><strong>2</strong></th>
<th colspan="2"><strong>Utente registrato:</strong></th>
<th colspan="4">L’utente clicca sulla sezione che permette il download del pdf, contenente lo storico delle attività in base al ruolo dell’account.</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema genera il pdf e lo rende disponibile per il download</th>
</tr>
<tr class="header">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI DI ERRORE I :</span></strong> Nessuna attività trovata</th>
</tr>
<tr class="odd">
<th colspan="2"><strong><span class="smallcaps">3.1</span></strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema notifica l’utente che non è stato trovato storico di attività ad esso collegate.</th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#10</em></p></th>
<th rowspan="3"><em>Invio di valutazione e feedback</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Vito Francesco Maistrini / Giovanni De Caro</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4"><em>Il cittadino beneficiario inserisce una recensione ad un servizio offerto dalla piattaforma del quale ha usufruito</em></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente beneficiario</strong></p>
<p>Interessato a inserire una valutazione e scrivere un feedback dopo il ritiro di un pacco prenotato</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la valutazione e il feedback</p></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4"><ul>
<li><blockquote>
<p>Il cittadino deve aver prenotato un pacco a uno dei punti di distribuzione</p>
</blockquote></li>
<li><blockquote>
<p>Il cittadino deve aver ricevuto una conferma della prenotazione</p>
</blockquote></li>
<li><blockquote>
<p>Il cittadino deve aver ritirato il pacco</p>
</blockquote></li>
</ul></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Il feedback viene ricevuto con successo dall’ente</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Il cittadino decide di non inserire feedback e valutazione</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Media</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p><strong>Utente beneficiario</strong>:</p>
</blockquote></th>
<th colspan="5">Apre la notifica di “pacco consegnato”</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Chiede al cittadino di inserire una valutazione e feedback tramite un’interfaccia</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p><strong>Utente beneficiario</strong>:</p>
</blockquote></th>
<th colspan="5">Inserisce una valutazione e un feedback e li invia</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p><strong>Sistema:</strong></p>
</blockquote></th>
<th colspan="5"><em>Manda con successo la recensione all’ente erogatore</em></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE: Il cittadino decide di non inserire una recensione</strong></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il Cittadino sceglie di uscire dall’interfaccia feedback non inserendo nessuna valutazione/feedback</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#11 (FILTRAGGIO DELLA MAPPA)**

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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #12</p></th>
<th rowspan="3">Filtraggio dei punti sulla mappa</th>
<th colspan="2">Data</th>
<th>25/11/2025</th>
</tr>
<tr class="odd">
<th>Vers.</th>
<th colspan="2">0.00.001</th>
</tr>
<tr class="header">
<th>Autore</th>
<th colspan="2">Riccardo Di Girolamo / Maria Chiara Gregorio</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">L’utente applica filtri ai punti visualizzati sulla mappa per visualizzare solo gli elementi rilevanti e ridurre il sovraccarico visivo.</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><strong>Utente non registrato/Utente registrato</strong></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori Secondari</strong></th>
<th colspan="4"><strong>Ente erogatore</strong></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4"><p>L’utente visualizza la mappa.</p>
<p>L’utente seleziona l’opzione “Filtri”.</p></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4"><p>I filtri vengono applicati correttamente.</p>
<p>La mappa mostra solo i punti che soddisfano i criteri selezionati.</p></th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4"><p>I filtri non vengono applicati perché l’utente non seleziona alcun criterio oppure la combinazione scelta non è utilizzabile.</p>
<p>Il sistema informa l’utente e la mappa rimane invariata.</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Bassa</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension Point</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">N/A</th>
</tr>
<tr class="odd">
<th colspan="8"><strong>Flusso di Eventi Principale/Main Scenario</strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="5">Apre il pannello dei filtri della mappa.</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="5">Mostra i filtri disponibili (es. tipologia: raccolta/distribuzione, orari, distanza).</th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="5">Seleziona uno o più criteri di filtraggio.</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="5">Applica i criteri selezionati ai punti disponibili.</th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="5">Conferma l’applicazione (o chiude il pannello) per visualizzare i risultati.</th>
</tr>
<tr class="odd">
<th>6</th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="5">Aggiorna la mappa mostrando solo i punti che soddisfano i criteri selezionati.</th>
</tr>
<tr class="header">
<th>7</th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="5">Visualizza la mappa filtrata e interagisce con i punti mostrati.</th>
</tr>
<tr class="odd">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo: Filtri preimpostati in base al profilo/ruolo</strong></th>
</tr>
<tr class="header">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Se l’utente è autenticato, evidenzia o pre-imposta filtri coerenti con il profilo (es. punti dell’ente o punti pubblici).</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.2</strong></th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="4">Accetta i filtri proposti oppure li modifica e prosegue (ritorna al passo 3).</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi Alternativo: Selezione di un preset (filtri rapidi)</strong></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.3</strong></th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="4">Inserisce un indirizzo manualmente invece di cliccare sulla mappa.</th>
</tr>
<tr class="header">
<th colspan="2"><strong>2.4</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Converte l’indirizzo in coordinate (geocoding) e mostra l’anteprima sulla mappa.</th>
</tr>
<tr class="odd">
<th colspan="8"><strong>III Scenario/Flusso di eventi Alternativo: Nessun punto trovato con filtri selezionati</strong></th>
</tr>
<tr class="header">
<th colspan="2"><strong>6.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Mostra un messaggio: “Nessun punto trovato con i filtri selezionati” e propone di modificare o reimpostare i filtri.</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>6.2</strong></th>
<th colspan="2"><strong>Utente:</strong></th>
<th colspan="4">Sceglie “Modifica” per cambiare i filtri (ritorna al passo 3) oppure “Reimposta” per tornare alla visualizzazione completa.</th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE: Nessuno.</strong></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>Note</strong></th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"><p>Il filtraggio può essere utilizzato anche senza autenticazione; alcune opzioni possono dipendere dal profilo/ruolo utente.</p>
<p>Il filtro “Solo distribuzione pubblica” consente di visualizzare i punti pubblici e i beni/servizi dichiarati.</p></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>Special Requirements</strong></th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"><p>Il filtraggio deve aggiornare la mappa senza ricaricare la pagina.</p>
<p>I filtri devono essere combinabili e facilmente re-impostabili.</p>
<p>La mappa deve restare leggibile anche con molti punti (es. raggruppamento dei marker).</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="media/image5.png" style="width:8.12604in;height:9.36458in" />

**Entity**

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>CLASSE</th>
<th>DESCRIZIONE</th>
<th>ATTRIBUTI</th>
<th>CASO D’USO</th>
</tr>
<tr class="odd">
<th>Account</th>
<th><p>Rappresenta l’account generico del sistema.</p>
<p>Account di ogni tipologia di utente</p></th>
<th><ul>
<li><blockquote>
<p>idUtente</p>
</blockquote></li>
<li><blockquote>
<p>email</p>
</blockquote></li>
<li><blockquote>
<p>password</p>
</blockquote></li>
</ul></th>
<th>1,2,3</th>
</tr>
<tr class="header">
<th>AccountBeneficiario</th>
<th>Rappresenta un utente che beneficia dei beni distribuiti</th>
<th><p>-nome</p>
<p>-cognome</p>
<p>-data nascita</p>
<p>-patologia/allergeni</p></th>
<th>1,2,5</th>
</tr>
<tr class="odd">
<th>AccountDonatore</th>
<th>Rappresenta un ente che dona i beni</th>
<th><p>-partita Iva</p>
<p>-categoria</p>
<p>-nome attività</p>
<p>-indirizzo sede</p>
<p>- nome</p>
<p>- cognome</p></th>
<th>1,2,3,4</th>
</tr>
<tr class="header">
<th>AccountEnteErogatore</th>
<th>Rappresenta un ente che gestisce la distribuzione di beni</th>
<th><p>-nome organizzazione</p>
<p>-indirizzo sede</p>
<p>-tipologia ente</p>
<p>- iban</p></th>
<th>1,2,3,4,5,6,8</th>
</tr>
<tr class="odd">
<th>DonazioneMonetaria</th>
<th>Rappresenta una donazione da parte del donatore</th>
<th><p>-IdUtente</p>
<p>-IdErogatore</p>
<p>-Somma monetaria</p>
<p>-Data</p></th>
<th>3</th>
</tr>
<tr class="header">
<th>ArticoloDonato</th>
<th>Rappresenta un bene che è stato donato</th>
<th><p>-IdBene</p>
<p>-Nome</p>
<p>-Categoria</p>
<p>-Quantità</p>
<p>-idPuntodiDistribuzione</p></th>
<th>4,5,10</th>
</tr>
<tr class="odd">
<th>ArticoloAlimentare</th>
<th>Rappresenta un bene alimentare che è stato donato</th>
<th><p>-Allergeni</p>
<p>-Scadenza</p></th>
<th>4,5,11</th>
</tr>
<tr class="header">
<th>ArticoloMedicinale</th>
<th>Rappresenta un medicinale che è stato donato</th>
<th><p>-Tipo</p>
<p>-Scadenza</p></th>
<th>4,5,11</th>
</tr>
<tr class="odd">
<th>ArticoloVestiario</th>
<th>Rappresenta un capo d’abbigliamento che è stato donato</th>
<th><p>-Taglia</p>
<p>-Condizioni</p></th>
<th>4,5,11</th>
</tr>
<tr class="header">
<th>ArticoloIgiene</th>
<th>Rappresenta un articolo di igiene personale che è stato donato</th>
<th>-Destinatari</th>
<th>4,5,11</th>
</tr>
<tr class="odd">
<th>ArticoloMobilità</th>
<th>Rappresenta un articolo per supporto o mobilità</th>
<th><p>-Tipo</p>
<p>-Stato</p></th>
<th>4,5,11</th>
</tr>
<tr class="header">
<th>DonazioneBene</th>
<th>Rappresenta una donazione di un bene</th>
<th><p>-IdDonazione</p>
<p>-IdDonatore</p>
<p>-IdErogatore</p>
<p>-IdBene</p>
<p>-Data</p>
<p>-nomePuntoDistribuzione</p></th>
<th>4,5</th>
</tr>
<tr class="odd">
<th>PuntoDistribuzione</th>
<th>Rappresenta un punto di distribuzione sulla mappa</th>
<th><p>-nome</p>
<p>-Cordinate</p>
<p>-Orari</p>
<p>-Giorni di distribuzione</p>
<p>-StatoApprovazione</p>
<p>-idErogatore</p></th>
<th>5,8,11,12</th>
</tr>
<tr class="header">
<th>PrenotazioneBene</th>
<th>Rappresenta la prenotazione di un bene da parte di un beneficiario</th>
<th><p>-IdPrenotazione</p>
<p>-IdBeneficiario</p>
<p>-IdBene</p>
<p>-IdPuntoBisogno</p>
<p>-Data</p></th>
<th>5</th>
</tr>
<tr class="odd">
<th>Feedback</th>
<th>Rappresenta un feedback da parte di un utente a valle di un ritiro completato</th>
<th><p>-IdFeedback</p>
<p>-IdPrenotazione</p>
<p>-recensione</p>
<p>-valutazione</p></th>
<th>10</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Boundary**

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>CLASSE</th>
<th>DESCRIZIONE</th>
<th>RESPONSABILITA</th>
<th>CASO D’USO</th>
</tr>
<tr class="odd">
<th>BoundarySelezioneRegistrazione</th>
<th>Interfaccia che consente all’utente di selezionare la tipologia di registrazione desiderata</th>
<th><ul>
<li><blockquote>
<p>Visualizzare le opzioni di registrazione(Beneficiario,Ente Donatore, Ente Erogatore)</p>
</blockquote></li>
</ul></th>
<th>1</th>
</tr>
<tr class="header">
<th>BoundaryRegistrazioneBeneficiario</th>
<th>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione del beneficiario</th>
<th><ul>
<li><blockquote>
<p>Raccogliere dati utente</p>
</blockquote></li>
</ul></th>
<th>1</th>
</tr>
<tr class="odd">
<th>BoundaryRegistrazioneEnteDonatore</th>
<th>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione del Donatore</th>
<th><ul>
<li><blockquote>
<p>Raccogliere i dati utente e dell’attività</p>
</blockquote></li>
</ul></th>
<th>1</th>
</tr>
<tr class="header">
<th>BoundaryRegistrazioneEnteErogatore</th>
<th>Schermata utilizzata per l’inserimento dei dati necessari alla registrazione dell’ente erogatore</th>
<th><ul>
<li><blockquote>
<p>Raccogliere le informazioni necessarie alla creazione dell’ente</p>
</blockquote></li>
</ul></th>
<th>1</th>
</tr>
<tr class="odd">
<th>BoundaryLogin</th>
<th>Schermata utilizzata per l’inserimento dei dati necessari per il login</th>
<th><ul>
<li><blockquote>
<p>Raccogliere i dati inseriti dall’utente</p>
</blockquote></li>
<li><blockquote>
<p>Inviare i dati di control di autenticazione</p>
</blockquote></li>
<li><blockquote>
<p>Mostrare messaggi di errore o di conferma</p>
</blockquote></li>
</ul></th>
<th>2</th>
</tr>
<tr class="header">
<th>BoundaryVisualizzaProfilo</th>
<th>Schermata utilizzata per visualizzare le proprie informazioni</th>
<th><ul>
<li><blockquote>
<p>Visualizzare le informazioni relative all’account</p>
</blockquote></li>
<li><blockquote>
<p>Permettere il logout dall’account</p>
</blockquote></li>
<li><blockquote>
<p>Permette di scaricare il pdf con lo storico delle proprio attività</p>
</blockquote></li>
</ul></th>
<th>9</th>
</tr>
<tr class="odd">
<th>BoundaryModificaProfilo</th>
<th>Schermata utilizzata per modificare le proprie informazioni</th>
<th><ul>
<li><blockquote>
<p>Visualizzare le informazioni modificabili relative all’account</p>
</blockquote></li>
<li><blockquote>
<p>Permettere la modifica di alcuni dei dati</p>
</blockquote></li>
<li><blockquote>
<p>Inviare al control collegato la richiesta di aggiornamento dei dati profilo</p>
</blockquote></li>
<li><blockquote>
<p>Mostrare messaggi di conferma o errore relativi alle operazioni effettuate</p>
</blockquote></li>
</ul></th>
<th>N/A</th>
</tr>
<tr class="header">
<th>BoundryDonazioneMonetaria</th>
<th>Schermata utilizzata per inserire le informazioni per effettuare una donazione monetaria</th>
<th><ul>
<li><blockquote>
<p>Visualizzare l’elenco degli enti erogatori disponibili</p>
</blockquote></li>
<li><blockquote>
<p>Permettere la selezione dell’ente erogatore desiderato</p>
</blockquote></li>
<li><blockquote>
<p>Permettere di inserire dati della propria carta di credito/debito e somma dell’importo</p>
</blockquote></li>
<li><blockquote>
<p>Inviare la richiesta al control collegato</p>
</blockquote></li>
<li><blockquote>
<p>Mostrare all’utente l’esito dell’operazione (successo/errore pagamento)</p>
</blockquote></li>
</ul></th>
<th>3</th>
</tr>
<tr class="odd">
<th>BoundaryDonazioneBene</th>
<th>Schermata utilizzata per inserire le informazioni per effettuare una donazione di un bene</th>
<th><ul>
<li><blockquote>
<p>Visualizzare l’elenco degli enti erogatori disponibili</p>
</blockquote></li>
<li><blockquote>
<p>Permettere la selezione dell’ente erogatore desiderato</p>
</blockquote></li>
<li><blockquote>
<p>Permette di inserire i dati del bene da donare</p>
</blockquote></li>
<li><blockquote>
<p>Inviare la richiesta al control collegato</p>
</blockquote></li>
<li><blockquote>
<p>Mostrare all’utente l’esitodell’operazione</p>
</blockquote></li>
</ul></th>
<th>4</th>
</tr>
<tr class="header">
<th>BoundaryPrenotazioneBene</th>
<th>Schermata utilizzata per visualizzare e prenotare uno o più beni</th>
<th><ul>
<li><blockquote>
<p>Visualizzare un bene o più beni prenotabili</p>
</blockquote></li>
<li><blockquote>
<p>Permette di prenotare uno o più bene in un punto di distribuzione</p>
</blockquote></li>
</ul></th>
<th>5</th>
</tr>
<tr class="odd">
<th>EmailConfermaDonazioneMonetaria</th>
<th>Email mandata per confermare una donazione monetaria mandata all’ente erogatore</th>
<th>-Visualizzare la conferma della donazione e l’importo donato</th>
<th>3</th>
</tr>
<tr class="header">
<th>EmailConfermaDonazioneBene</th>
<th>Email mandata per c onfermare la donazione di un bene all’ente erogatore</th>
<th><p>-Fornisce i dati del donatore</p>
<p>-Fornisce i dati del bene donato</p></th>
<th>4</th>
</tr>
<tr class="odd">
<th>EmailConfermaPrenotazione</th>
<th>Email mandata per c onfermare la prenotaionee di un bene all’ente erogatore</th>
<th><p>-Fornisce i dati dell’utente beneficiario</p>
<p>-Visualizza il bene che ha prenotato l’utente</p></th>
<th>5</th>
</tr>
<tr class="header">
<th>BoundaryVisualizzaPrenotazioni</th>
<th>Schermata utilizzata per la visualizzazione delle prenotazioni effetuate</th>
<th><p>-Visualizzazione prenotazioni effettuate</p>
<p>-Permette la cancellazione di una prenotazione non ancora ritirata</p></th>
<th>N/A</th>
</tr>
<tr class="odd">
<th>BoundarySegnalazionePunto</th>
<th>Schermata utilizzata per inserire i dati sul punto di bisogno da voler segnalare</th>
<th>-Permette di inserire i dati nel punto di bisogno manualmente o tramite marker sulla mappa</th>
<th>6</th>
</tr>
<tr class="header">
<th>BoundaryGestionePunti</th>
<th>Schermata utilizzata per gestire i beni in un punto di distribuzione da parte di un ente erogatore</th>
<th><p>-Permette di aggiungere/rimuovere beni ad un punto di distribuzione</p>
<p>-Permette la modifica della quantità di ciascun bene</p></th>
<th>N/A</th>
</tr>
<tr class="odd">
<th>BoundaryVisualizzazioneNotifiche</th>
<th>Schermata utilizzata per visualizzare le notifiche</th>
<th>-Permette di visualizzare le notifiche</th>
<th>N/A</th>
</tr>
<tr class="header">
<th>BoundaryFeedback</th>
<th>Schermata utilizzata per inviare un feedback da parte dell’utente</th>
<th><p>-Permette di inserire un feedback testuale</p>
<p>-Permette di inserire una valutazione</p></th>
<th>10</th>
</tr>
<tr class="odd">
<th>BoundaryCatalogo</th>
<th>Schermata utilizzata per vedere tutti i beni disponibili registrati nel sistema</th>
<th>-Permette di visualizzare un bene e vederne i dettagli</th>
<th>N/A</th>
</tr>
<tr class="header">
<th>BoundaryFiltroCatalogo</th>
<th>Schermata utilizzata per filtrare il catalogo(e di conseguenza la mappa) in base ai beni</th>
<th><p>-Permette di scegliere come filtrare i beni</p>
<p>-Il filtro verrà applicato anche sulla mappa</p></th>
<th>11</th>
</tr>
<tr class="odd">
<th>BoundaryFiltroMappa</th>
<th>Schermata utilizzata per filtrare la mappa in base ai punti di distribuzione</th>
<th>-Permette di filtrare i punti sulla mappa</th>
<th>12</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Control**

| CLASSE                      | DESCRIZIONE                                                                                    | CASO D’USO |
|-----------------------------|------------------------------------------------------------------------------------------------|------------|
| AutenticazioneControl       | Coordinatore della logica di registrazione per le varie tipologie di utente                    | 1          |
| LoginControl                | Coordinatore della logica di login/logout per le varie tipologie di utente                     | 2          |
| GestioneProfiloControl      | Coordinatore della logica della visualizzazione e modifica del profilo                         | N/A        |
| DonazioneMonetariaControl   | Coordinatore della logica della donazione monetaria da parte di un utente ad un ente erogatore | 3          |
| DonazioneBeniControl        | Coordinatore della logica della donazione di beni da parte di un donatore ad un ente erogatore | 4          |
| GestionePrenotazioneControl | Coordinatore della logica della prenotazione di beni da parte di un beneficiario               | 5          |
| GesationePuntiControl       | Coordinatore della logica della dei punti di bisogno e gestisce i filtri                       | 6,8,11,12  |
| InvioNotificheContrl        | Crea e invia le e-mail di notifica ai vari utenti e crea le notifiche sul sistema              | 10         |
| GestioneStoricoControl      | Crea il file con i dati delle attività dell'utente                                             | 9          |

**1.Prenotazione di un bene**

<img src="media/image24.png" style="width:7.04063in;height:4.57866in" />

**2.Donazione di un bene**

<img src="media/image6.png" style="width:8.20833in;height:5.81527in" />

**3.Donazione monetaria**

<img src="media/image1.png" style="width:6.95937in;height:4.82292in" />

**4.Segnalazione punti di bisogno**

<img src="media/image2.png" style="width:6.89133in;height:4.23611in" />

**5.Gestione scorte**

<img src="media/image9.png" style="width:6.89583in;height:6.12711in" />

**1.DonazioneMonetariaControl**

<img src="media/image4.png" style="width:5.67708in;height:7.84859in" />

**2.LoginControl**

<img src="media/image7.png" style="width:6.34792in;height:7.89583in" />

**3.PrenotazioneBene**

<img src="media/image26.png" style="width:5.375in;height:7.76042in" />

**4.SegnalazioneControl**<img src="media/image3.png" style="width:6.89583in;height:5.86667in" />

<img src="media/image19.png" style="width:6.89133in;height:7.97222in" />
