# **TEST PLAN** 

# **1.1 INTRODUZIONE**

- Il presente Test Plan descrive le attività di testing previste per il sistema, con l’obiettivo di verificare il corretto funzionamento delle funzionalità individuate nell’analisi dei requisiti e modellate nei vari Use Case.

All’interno del documento vengono illustrate:

- le funzionalità da sottoporre a verifica,

- i criteri di successo e fallimento dei test,

- l’approccio metodologico adottato,

- il materiale necessario per l’esecuzione delle attività di testing.

<!-- -->

- Il processo di testing è finalizzato a garantire che ogni funzionalità implementata rispetti i requisiti funzionali e non funzionali definiti nel RAD, e che il comportamento del sistema sia conforme alle aspettative dell’utente finale.

Per ogni funzionalità vengono progettati casi di test basati sulla tecnica **black-box Category Partition**, che consente di individuare in modo sistematico le combinazioni di input più significative da verificare.

## **1.2 PANORAMICA DEL SISTEMA**

Il sistema è strutturato secondo un’architettura a più livelli che separa:

- **presentazione**,

- **logica applicativa**,

- **persistenza dei dati**.

<!-- -->

- Il backend gestisce autenticazione, donazioni, prenotazioni, segnalazioni, gestione scorte e operazioni degli enti erogatori.

- Il database memorizza utenti, enti, donazioni, prenotazioni, punti di distribuzione e storico attività.

Le API esposte permettono l’interazione tra client e server in modo sicuro e coerente con i requisiti.

## **1.3 FUNZIONALITÀ DA TESTARE**

Le funzionalità da testare corrispondono agli **Use Case ufficiali** presenti nel RAD.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ID</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Nome</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Descrizione sintetica</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC01</strong></p>
</blockquote></td>
<td><blockquote>
<p>Registrazione</p>
</blockquote></td>
<td><blockquote>
<p>Un utente non registrato crea un nuovoaccount; per i beneficiari è prevista validazione da parte dell’amministratore.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UC02</strong></p>
</blockquote></td>
<td><blockquote>
<p>Login</p>
</blockquote></td>
<td><blockquote>
<p>L’utente accede tramite email, password e codice OTP; i beneficiari devono essere approvati.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC03</strong></p>
</blockquote></td>
<td><blockquote>
<p>Donazione Monetaria</p>
</blockquote></td>
<td><blockquote>
<p>L’utente autenticato effettua una donazione in denaro verso un ente erogatore; il sistema valida i dati di pagamento e registra la transazione.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UC04</strong></p>
</blockquote></td>
<td><blockquote>
<p>Donazione di Beni</p>
</blockquote></td>
<td><blockquote>
<p>Un donatore invia una donazione di beni materiali verso un punto di distribuzione; il sistema registra la donazione e invia email di conferma.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC05</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prenotazione Ritiro Beni</p>
</blockquote></td>
<td><blockquote>
<p>Un beneficiario seleziona un punto di distribuzione, sceglie un bene e prenota uno slot orario per il ritiro.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UC06</strong></p>
</blockquote></td>
<td><blockquote>
<p>Segnalazione Punto di Bisogno</p>
</blockquote></td>
<td><blockquote>
<p>Un utente autenticato invia una segnalazione indicando posizione e indirizzo; il sistema inoltra la segnalazione agli enti erogatori.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC07</strong></p>
</blockquote></td>
<td><blockquote>
<p>Gestione e Aggiornamento Scorte</p>
</blockquote></td>
<td><blockquote>
<p>Un ente erogatore visualizza e aggiorna le scorte dei propri punti di raccolta.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UC08</strong></p>
</blockquote></td>
<td><blockquote>
<p>Richiesta Aggiunta Punto di Distribuzione</p>
</blockquote></td>
<td><blockquote>
<p>Un ente erogatore invia una richiesta per aggiungere un nuovo punto di distribuzione; il sistema valida i dati e notifica l’amministratore.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC09</strong></p>
</blockquote></td>
<td><blockquote>
<p>Visione Storico Attività e Reportistica</p>
</blockquote></td>
<td><blockquote>
<p>L’utente autenticato visualizza lo storico delle proprie attività e può scaricare un PDF riepilogativo.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UC10</strong></p>
</blockquote></td>
<td><blockquote>
<p>Invio Valutazione e Feedback</p>
</blockquote></td>
<td><blockquote>
<p>Un beneficiario inserisce una valutazione e un feedback dopo il ritiro di un pacco prenotato.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>UC11</strong></p>
</blockquote></td>
<td><blockquote>
<p>Filtraggio dei Punti sulla Mappa</p>
</blockquote></td>
<td><blockquote>
<p>L’utente applica filtri ai punti mostrati sulla mappa per visualizzare solo quelli rilevanti.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## **1.4 PASS/FAIL CRITERIA**

- Un test è considerato **superato** quando il comportamento osservato coincide con quello atteso, definito tramite oracolo.

Un test è considerato **fallito** quando l’output del sistema differisce dal risultato atteso.

L’obiettivo del testing è individuare eventuali fallimenti, così da risalire ai fault presenti nel sistema e consentirne la correzione.

## **1.5 APPROCCIO**

- L’approccio adottato è di tipo **black-box**, con progettazione dei test basata sulla tecnica **Category Partition**.

Per ogni UC vengono:

1.  individuati i parametri rilevanti,

2.  suddivisi in categorie,

3.  definite proprietà e vincoli,

4.  generate le combinazioni significative,

5.  trasformate in test case eseguibili.

L’esecuzione dei test avverrà tramite strumenti come **Postman** per le API e, se necessario, framework di testing automatico.

## **1.6 MATERIALE DI TESTING**

Per l’esecuzione delle attività di testing verranno utilizzati:

- PC o laptop idonei,

- Postman per l’invio delle richieste HTTP,

- database di test con dati coerenti,

- strumenti di logging e monitoraggio del backend.
