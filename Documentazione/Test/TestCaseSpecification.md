<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*TEST CASE SPECIFICATION*

All’interno di questo documento viene riportata l’applicazione della metodologia di individuazione dei casi di test definita nel Test Plan (TP).

Il documento raccoglie i test frame generati attraverso la tecnica di progettazione indicata nel TP e le specifiche dettagliate dei casi di test associati alle funzionalità da verificare.

L’obiettivo è garantire una copertura sistematica e completa dei requisiti, assicurando che ogni funzionalità venga validata rispetto ai comportamenti attesi.

Sono riportati tutti i test design relativi alle funzionalità da testare, così come identificate nel TP. Per ciascuna funzionalità vengono presentati i test frame derivati dall’applicazione della tecnica di progettazione scelta e, successivamente, le specifiche dei casi di test che ne discendono.

Ogni test case è descritto in modo strutturato, includendo input, condizioni, vincoli e oracoli necessari alla sua esecuzione.

**UC01 Registrazione**

Un utente non registrato crea un nuovo account nel sistema, selezionando il proprio ruolo (beneficiario, donatore o ente erogatore) e compilando i campi richiesti.

L'utente inserisce email, password e i dati specifici in base al ruolo scelto: per il beneficiario sono richiesti nome, cognome, data di nascita, eventuali allergeni e patologie, codice carta d'identità e relativo documento; per il donatore sono richiesti nome, cognome, partita IVA, nome attività, indirizzo sede e categoria; per l'ente erogatore sono richiesti nome organizzazione, indirizzo sede, tipologia ente e IBAN.

Il sistema verifica che i campi obbligatori siano compilati, che l'email non sia già registrata e che il ruolo sia valido.

Se i dati sono validi, il sistema genera un codice OTP a 4 cifre e lo invia all'indirizzo email dell'utente.

L'utente inserisce il codice OTP ricevuto. Il sistema confronta il codice con quello generato e, se valido, completa la registrazione creando l'account.

Per gli utenti di tipo beneficiario, l'account viene creato in stato "non accettato" e richiede la validazione da parte di un amministratore.

Se l'OTP è errato o se l'email non può essere inviata, la registrazione non viene completata.

**UC02 Login**

Un utente registrato accede al sistema inserendo email e password.

Il sistema verifica che le credenziali siano corrette e che l’utente non sia già autenticato.

Se la verifica ha esito positivo, il sistema genera un codice OTP e lo invia all’indirizzo email dell’utente.

L’utente inserisce il codice OTP ricevuto.

Il sistema confronta il codice con quello generato e, se valido, completa l’autenticazione creando la sessione utente.

Per gli utenti di tipo beneficiario, l’accesso è consentito solo se l’account risulta approvato da un amministratore.

Se l’OTP è errato, mancante o non più valido, il login non viene completato.

**UC03 Donazione monetaria**

Un utente autenticato (donatore, beneficiario o ente erogatore) effettua una donazione monetaria verso un ente erogatore selezionato.

L’utente inserisce i dati necessari al pagamento: numero carta, data di scadenza, CVV, importo e nome dell’ente destinatario.

Il sistema verifica che:

- l’ente erogatore esista

- l’importo sia valido e maggiore di zero

- i dati della carta siano formalmente corretti

- l’IBAN dell’ente sia valido (inizia con “IT”)

Se i dati sono validi, il sistema simula la transazione.

Se la transazione viene accettata, il sistema registra la donazione nel database, associandola all’utente e all’ente erogatore, con data e importo.

Al termine, il sistema invia una email di conferma all’ente erogatore con i dettagli della donazione.

Se l’email non può essere inviata, la donazione rimane comunque registrata, ma il sistema notifica che la conferma via email non è stata inviata.

**UC04 Donazione di beni**

Un utente autenticato come donatore decide di effettuare una donazione di beni compilando il form nella pagina dedicata. L’utente inserisce i dati per la donazione: punto di distribuzione, categoria del bene, nome del bene, descrizione(opzionale), quantità dei beni, data utile per il ritiro, foto(opzionale), recapito telefonico(opzionale)

**UC06 Segnalazione di un punto di bisogno**

Un utente autenticato (donatore, beneficiario o ente erogatore) segnala una posizione geografica dove è necessario un intervento o un aiuto. Il sistema invia una notifica via email a tutti gli enti erogatori registrati sulla piattaforma.

L’utente inserisce i dati della posizione: latitudine, longitudine e un indirizzo descrittivo.

Il sistema verifica che i campi latitudine, longitudine e indirizzo non siano vuoti e che l'utente abbia un ruolo autorizzato (donatore, beneficiario, ente).

Se i dati sono validi, il sistema recupera la lista di tutti gli enti erogatori dal database.

Il sistema tenta di inviare una email di segnalazione a ciascun ente con i dettagli della posizione.

Al termine, il sistema conferma l'avvenuta segnalazione all'utente.

**UC11 Filtraggio della mappa**

Un utente (registrato o non registrato) applica un filtro per categoria ai punti di distribuzione visualizzati sulla mappa, al fine di visualizzare solo gli elementi rilevanti e ridurre il sovraccarico visivo.

L'utente seleziona una categoria dal menu a tendina nella sidebar della home page. Le categorie disponibili sono: Alimentari, Medicinali, Igiene Personale, oppure "Tutte le categorie" per visualizzare tutti i punti.

Il sistema invia una richiesta GET /api/punti-distribuzione con il parametro categoria selezionato. Il backend esegue una query con JOIN sulle tabelle beni, sotto_categorie e macro_categorie per filtrare i punti di distribuzione che contengono beni della categoria richiesta.

Se il filtro è valido, la mappa viene aggiornata mostrando solo i marker corrispondenti. Se non viene selezionato alcun filtro, vengono mostrati tutti i punti di distribuzione.

Se le tabelle delle categorie non esistono nello schema, il filtro viene ignorato e tutti i punti vengono restituiti con una nota informativa.

# 

**UC01 Registrazione**

## 

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
<tr class="odd">
<th>email</th>
<th>Formato(FM)</th>
<th><p>1.l’email è in un formato del tipo ^[a-zA-Z0-9.<em>%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ <strong>[propietà FM</strong></em><strong>_OK]</strong></p>
<p>2. l’email non rispetta il formato<strong>[ERR]</strong></p></th>
</tr>
<tr class="header">
<th>email</th>
<th>NonRegistrata(NR)</th>
<th><p>1.L’email non è registrata nel database<strong>[IF FM_OK][Proprietà NR_OK]</strong></p>
<p>2.L’email è registrata nel database<strong>[IF FM_OK][ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>password</th>
<th>Presente(PW)</th>
<th><p>1. La password è presente e non vuota <strong>[Proprietà PW_OK]</strong></p>
<p>2. La password è assente o vuota <strong>[ERR]</strong></p></th>
</tr>
<tr class="header">
<th>ruolo</th>
<th>Validitá(RL)</th>
<th><p>1. Il ruolo è "beneficiario" <strong>[Proprietà RL_BN]</strong></p>
<p>2. Il ruolo è "donatore" <strong>[Proprietà RL_DN]</strong></p>
<p>3. Il ruolo è "erogatore" <strong>[Proprietà RL_ER]</strong></p>
<p>4. Il ruolo non è valido o è vuoto <strong>[ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>campi_specifici</th>
<th>Completezza (CS)</th>
<th><p>1. Tutti i campi specifici per il ruolo sono compilati <strong>[IF RL_BN OR RL_DN OR RL_ER] [Proprietà CS_OK]</strong></p>
<p>2. Uno o più campi specifici obbligatori mancano <strong>[IF RL_BN OR RL_DN OR RL_ER] [ERR]</strong></p></th>
</tr>
<tr class="header">
<th>email_otp</th>
<th>Invio(EM)</th>
<th>1. L'email OTP viene inviata correttamente <strong>[IF CS_OK AND UN_OK AND PW_OK] [Proprietà EM_OK]</strong><br />
2. L'email OTP non viene inviata <strong>[IF CS_OK AND NR_OK AND PW_OK] [ERR]</strong></th>
</tr>
<tr class="odd">
<th>codice</th>
<th>Lunghezza(LN)</th>
<th><p>1. Il codice ha lunghezza 0 <strong>[IF EM_OK] [ERR]</strong></p>
<p>2. Il codice ha lunghezza &gt; 5 <strong>[IF EM_OK] [ERR]</strong></p>
<p>3. Il codice ha 0&lt;lunghezza &lt; 5 <strong>[IF EM_OK] [Proprietà LN_OK]</strong></p></th>
</tr>
<tr class="header">
<th>codice</th>
<th>Corretto(CT)</th>
<th><p>1. Il codice è corretto <strong>[IF OK_LN] [Proprietà OK_CT]</strong></p>
<p>2. Il codice non è corretto <strong>[IF OK_LN] [ERR]</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 

**UC02 Login**

## 

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
<tr class="odd">
<th>email</th>
<th>Formato(FM)</th>
<th><p>1.l’email è in un formato del tipo ^[a-zA-Z0-9.<em>%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ <strong>[propietà FM</strong></em><strong>_OK]</strong></p>
<p>2. l’email non rispetta il formato<strong>[ERR]</strong></p></th>
</tr>
<tr class="header">
<th>email</th>
<th>Registrata(RG)</th>
<th><p>1.L’email è registrata nel database<strong>[IF FM_OK][Proprietà RG_OK]</strong></p>
<p>2.L’email non è registrata nel database<strong>[IF FM_OK][ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>ruolo</th>
<th>Beneficiario(BN)</th>
<th><p>1.L’account è un tipo “Beneficiario”<strong>[IF RG_OK][Proprietà IS_BN]</strong></p>
<p>2.L'account non è “Beneficiario”<strong>[IF RG_OK][Proprietà NOT_BN]</strong></p></th>
</tr>
<tr class="header">
<th>stato_beneficiario</th>
<th>Accettato(AC)</th>
<th><p>1.L’account è stato accettato<strong>[IF IS_BN][Proprietà OK_ACC]</strong></p>
<p>2.L’account è in attesa[IF <strong>IS_BN][ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>password</th>
<th>Corretta(CR)</th>
<th><p>1.La password è corretta<strong>[IF RG_OK][Proprietà OK_CR]</strong></p>
<p>2.La password non è corretta<strong>[IF RG_OK][ERR]</strong></p></th>
</tr>
<tr class="header">
<th>codice</th>
<th>Lunghezza(LN)</th>
<th><p>1.Il codice ha lunghezza 0 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][ERR]</strong></p>
<p>2.Il codice ha lunghezza &gt;4 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][ERR]</strong></p>
<p>3.Il codice ha 0&lt;lunghezza&lt;5 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][Proprietà OK_LN]</strong></p></th>
</tr>
<tr class="odd">
<th>codice</th>
<th>Corretto(CT)</th>
<th><p>1.Il codice è corretto<strong>[IF OK_LN][Proprietà OK_CT]</strong></p>
<p>2.Il codice non è corretto<strong>[IF OK_LN][ERR]</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 

**UC03 Donazione Monetaria**

## 

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
<tr class="odd">
<th>importo</th>
<th>Validità Importo (<strong>IM</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>L’importo è numerico e maggiore di 0 → <strong>[Proprietà IM_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’importo è numerico ma &lt;= 0 → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’importo non è numerico → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’importo è mancante → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="header">
<th>numero_carta</th>
<th>Formato Numero Carta (<strong>NC</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>Il numero carta ha lunghezza 16 → <strong>[Proprietà NC_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Lunghezza != 16 → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Campo mancante → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th>scadenza</th>
<th>Validità scadenza (<strong>SC</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>La scadenza è futura → <strong>[Proprietà SC_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>La scadenza è passata → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Formato data non valido → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Campo mancante → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="header">
<th>utente</th>
<th>Utente Autenticato(<strong>RU</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>L’utente è autenticato → <strong>[Proprietà RU_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’utente non è autenticato → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th>cvv</th>
<th>Validità CVV (<strong>CV</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>Il CVV ha lunghezza 3 → <strong>[Proprietà CV_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Lunghezza != 3 → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Campo mancante → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="header">
<th>nome_ente_erogatore</th>
<th>Ente Esistente (<strong>EN</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>L’ente esiste nel db → <strong>[Proprietà EN_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’ente non esiste → <strong>[ERR]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Campo mancante → <strong>[ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th>iban_destinatario</th>
<th>Validità IBAN (<strong>IB</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>L’IBAN inizia con “IT” → <strong>[Proprietà IB_OK] [IF EN_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’IBAN non inizia con “IT” → <strong>[ERR] [IF EN_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>Campo mancante → <strong>[ERR] [IF EN_OK]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="header">
<th>transazione</th>
<th>Esito Transazione (<strong>TR</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>La transazione è accettata → <strong>[Proprietà TR_OK] [IF IM_OK AND NC_OK AND SC_OK AND CV_OK AND IB_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>La transazione è rifiutata → <strong>[ERR] [IF uno qualsiasi tra IM, NC, SC, CV, IB è ERR]</strong></p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th>email</th>
<th>Invio Email (<strong>EM</strong>)</th>
<th><ol type="1">
<li><blockquote>
<p>L’email è inviata correttamente → <strong>[Proprietà EM_OK] [IF TR_OK]</strong></p>
</blockquote></li>
<li><blockquote>
<p>L’email non è inviata → <strong>[ERR NON BLOCCANTE] [IF TR_OK]</strong></p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##  UC6 Segnalazione di un punto di bisogno

##  

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 32%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
<tr class="odd">
<th>Latitudine</th>
<th>Validità Posizione (VP)</th>
<th><p>1. Presente e non vuota → <strong>[VP_OK]</strong></p>
<p>2. Mancante → <strong>[ERR]</strong></p></th>
</tr>
<tr class="header">
<th>Longitudine</th>
<th>Validità Posizione (<strong>VP</strong>)</th>
<th><p>1. Presente e non vuota → <strong>[VP_OK]</strong></p>
<p>2. Mancante o stringa vuota → <strong>[ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>Indirizzo</th>
<th>Validità Dati (<strong>VD</strong>)</th>
<th><p>1. Testo presente → <strong>[VD_OK]</strong></p>
<p>2. Campo vuoto → <strong>[ERR]</strong></p></th>
</tr>
<tr class="header">
<th>Utente</th>
<th>Utente Autenticato (<strong>UA</strong>)</th>
<th><p>1. Ruolo autorizzato → <strong>[UA_OK]</strong></p>
<p>2. Utente non loggato/non autorizzato → <strong>[ERR]</strong></p></th>
</tr>
<tr class="odd">
<th>Enti Destinatari</th>
<th>Invio Multiplo (<strong>IM</strong>)</th>
<th>1. Lista enti erogatori caricata correttamente → <strong>[IM_OK]</strong></th>
</tr>
<tr class="header">
<th>Email</th>
<th>Invio Email (<strong>EM</strong>)</th>
<th>1. Inviata correttamente a tutti → <strong>[EM_OK]</strong></th>
</tr>
<tr class="odd">
<th>Esito</th>
<th>Esito Segnalazione (<strong>ES</strong>)</th>
<th>1. Pop-up di successo mostrato all’utente → <strong>[ES_OK]</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##  

##  UC11 Filtraggio della mappa

##  

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 32%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
<tr class="odd">
<th>categoria</th>
<th>Selezione(SL)</th>
<th><p>1. Nessuna categoria selezionata ("Tutte le categorie") <strong>[Proprietà SL_ALL]</strong></p>
<p>2. Una categoria specifica è selezionata <strong>[Proprietà SL_OK]</strong></p></th>
</tr>
<tr class="header">
<th>categoria</th>
<th>Esistenza(ES)</th>
<th><p>1. La categoria esiste nel database (macro_categorie) <strong>[IF SL_OK] [Proprietà ES_OK]</strong></p>
<p>2. La categoria non esiste nel database <strong>[IF SL_OK] [Proprietà ES_NO]</strong></p></th>
</tr>
<tr class="odd">
<th>punti</th>
<th>Disponibilitá(DP)</th>
<th><p>1. Esistono punti di distribuzione con beni della categoria <strong>[IF ES_OK] [Proprietà DP_OK]</strong></p>
<p>2. Nessun punto ha beni della categoria <strong>[IF ES_OK] [Proprietà DP_NO]</strong></p></th>
</tr>
<tr class="header">
<th>tabelle_categorie</th>
<th>Presenza(TB)</th>
<th><p>1. Le tabelle beni, sotto_categorie, macro_categorie esistono <strong>[Proprietà TB_OK]</strong></p>
<p>2. Una o più tabelle mancano <strong>[Proprietà TB_NO]</strong></p></th>
</tr>
<tr class="odd">
<th>risposta</th>
<th>Esito(RS)</th>
<th><p>1. La risposta contiene dati validi <strong>[IF (SL_ALL OR DP_OK) AND TB_OK] [Proprietà RS_OK]</strong></p>
<p>2. La risposta è lista vuota <strong>[IF DP_NO AND TB_OK] [Proprietà RS_EMPTY]</strong></p>
<p>3. Errore del database <strong>[ERR]</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 

## 

## 

## 

## 

## 

**UC01 Registrazione**

| **Test case** | **FM** | **NR** | **PW** | **RL** | **CS**    | **EM** | **LN**    | **CT**    | **Esito atteso**                                       |
|---------------|--------|--------|--------|--------|-----------|--------|-----------|-----------|--------------------------------------------------------|
| **TC01**      | ERR    | **-**  | **-**  | **-**  | **-**     | **-**  | **-**     | **-**     | **\[ERR\]** Formato email non valido                   |
| **TC02**      | FM_OK  | ERR    | **-**  | **-**  | **-**     | **-**  | **-**     | **-**     | **\[ERR\]** Email già registrata                       |
| **TC03**      | FM_OK  | UN_OK  | ERR    | **-**  | **-**     | **-**  | **-**     | **-**     | **\[ERR\]** Password mancante                          |
| **TC04**      | FM_OK  | UN_OK  | PW_OK  | ERR    | \-        | **-**  | **-**     | **-**     | **\[ERR\]** Ruolo non valido                           |
| **TC05**      | FM_OK  | UN_OK  | PW_OK  | RL_BN  | ERR       | \-     | **-**     | **-**     | **\[ERR\]** Campi specifici mancanti                   |
| **TC06**      | FM_OK  | UN_OK  | PW_OK  | RL_DN  | **CS_OK** | ERR    | **-**     | **-**     | **\[ERR\]** Email OTP non inviata                      |
| **TC07**      | FM_OK  | UN_OK  | PW_OK  | RL_DN  | **CS_OK** | EM_OK  | ERR(LN1)  | \-        | **\[ERR\]** Codice mancante                            |
| **TC08**      | FM_OK  | UN_OK  | PW_OK  | RL_DN  | **CS_OK** | EM_OK  | ERR(LN2)  | \-        | **\[ERR\]** Codice troppo lungo                        |
| **TC09**      | FM_OK  | UN_OK  | PW_OK  | RL_DN  | CS_OK     | EM_OK  | **LN_OK** | ERR       | **\[ERR\]** Codice non valido                          |
| **TC10**      | FM_OK  | UN_OK  | PW_OK  | RL_BN  | CS_OK     | EM_OK  | **LN_OK** | **CT_OK** | Registrazione completata (in attesa validazione admin) |
| **TC11**      | FM_OK  | UN_OK  | PW_OK  | RL_DN  | CS_OK     | EM_OK  | LN_OK     | CT_OK     | Registrazione completata                               |
| **TC12**      | FM_OK  | UN_OK  | PW_OK  | RL_ER  | CS_OK     | EM_OK  | LN_OK     | CT_OK     | Registrazione completata                               |

**UC02 Login**

| **Test case** | **FM** | **RG** | **CR** | **BN** | **AC** | **LN**   | **CT** | **Esito atteso**                  |
|---------------|--------|--------|--------|--------|--------|----------|--------|-----------------------------------|
| **TC01**      | ERR    | **-**  | **-**  | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Errore formattazione   |
| **TC02**      | FM_OK  | ERR    | **-**  | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Email non registrata   |
| **TC03**      | FM_OK  | RG_OK  | ERR    | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Credenziali non valide |
| **TC04**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | ERR    | **-**    | **-**  | **\[ERR\]**Account non accettato  |
| **TC05**      | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | ERR(LN1) | **-**  | **\[ERR\]**Codice mancante        |
| **TC06**      | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | ERR(LN2) | **-**  | **\[ERR\]**Codice troppo lungo    |
| **TC07**      | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | LN_OK    | ERR    | **\[ERR\]**Codice non valido      |
| **TC08**      | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | LN_OK    | CT_OK  | Login completato                  |
| **TC09**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | ERR(LN1) | **-**  | **\[ERR\]**Codice mancante        |
| **TC10**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | ERR(LN2) | **-**  | **\[ERR\]**Codice troppo lungo    |
| **TC11**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | LN_OK    | ERR    | **\[ERR\]**Codice non valido      |
| **TC12**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | LN_OK    | CT_OK  | Login completato                  |

**UC03 Donazione Monetaria**

| **Test case** | **IM** | **NC** | **SC** | **CV** | **EN** | **IB** | **TR** | **EM** | **Esito atteso**                         |
|---------------|--------|--------|--------|--------|--------|--------|--------|--------|------------------------------------------|
| **TC01**      | ERR    | **-**  | **-**  | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]** Importo non valido           |
| **TC02**      | IM_OK  | ERR    | **-**  | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]**Numero carta non valido       |
| **TC03**      | IM_OK  | NC_OK  | ERR    | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]**Scadenza non valida           |
| **TC04**      | IM_OK  | NC_OK  | SC_OK  | ERR    | **-**  | **-**  | **-**  |        | **\[ERR\]**CVV non valido                |
| **TC05**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | ERR    | **-**  | **-**  |        | **\[ERR\]**Ente non trovato              |
| **TC06**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | ERR    | ERR    | **-**  | **\[ERR\]**IBAN non valido               |
| **TC07**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | TR_OK  | ERR    | **\[ERR\]**Email di conferma non inviata |
| **TC08**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | ERR    | **-**  | **\[ERR\]** Errore generico transazione  |
| **TC09**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | TR_OK  | EM_OK  | Donazione registrata + email inviata     |

**UC06 Segnalazione di un punto di bisogno**

| **Test Case** | **VP**    | **VD**    | **UA**    | **IM**    | **EM**    | **ES**    | **Esito atteso**                               |
|---------------|-----------|-----------|-----------|-----------|-----------|-----------|------------------------------------------------|
| **TC01**      | **-**     | **-**     | **ERR**   | **-**     | **-**     | **-**     | **\[ERR\] Utente non autorizzato**             |
| **TC02**      | **ERR**   | **VP_OK** | **UA_OK** | **-**     | **-**     | **ERR**   | **\[ERR\] Coordinate mancanti**                |
| **TC03**      | **VP_OK** | **ERR**   | **UA_OK** | **-**     | **-**     | **ERR**   | **\[ERR\] Indirizzo mancante o vuoto**         |
| **TC04**      | **VP_OK** | **VD_OK** | **UA_OK** | **IM_OK** | **EM_OK** | **ES_OK** | **\[SUCCESS\] Segnalazione OK +email inviate** |

Per ciascun test case vengono definiti:

- gli input necessari all’esecuzione della funzionalità a cui il test fa riferimento,

- i valori assegnati a ciascun input, scelti sulla base delle combinazioni individuate tramite tecnica Category Partition,

- l’oracolo, ovvero il risultato atteso dal sistema a fronte degli input specificati**.**

**UC01 Registrazione**

| **ID TEST CASE**                                                                                                                                        |                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| TC01                                                                                                                                                    |                 |
| Email                                                                                                                                                   | DonkeyKong      |
| Password                                                                                                                                                | TestPassword123 |
| Ruolo                                                                                                                                                   | Beneficiario    |
| Campi Specifici                                                                                                                                         | N/A             |
| Codice                                                                                                                                                  | N/A             |
| **Esito atteso**                                                                                                                                        |                 |
| La registrazione non va a buon fine perché l'email non è in un formato valido e il sistema mostra un messaggio di errore: "Campi obbligatori mancanti". |                 |

| **ID TEST CASE**                                                                                                                                   |                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| TC02                                                                                                                                               |                          |
| Email                                                                                                                                              | yogurtmangiato@gmail.com |
| Password                                                                                                                                           | TestPassword123          |
| Ruolo                                                                                                                                              | Donatore                 |
| Campi Specifici                                                                                                                                    | N/A                      |
| Codice                                                                                                                                             | N/A                      |
| **Esito atteso**                                                                                                                                   |                          |
| La registrazione non va a buon fine perché l'email è già presente nel database e il sistema mostra un messaggio di errore: "Email già registrata". |                          |

| **ID TEST CASE**                                                                                                                            |                       |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| TC03                                                                                                                                        |                       |
| Email                                                                                                                                       | nuovoutente@gmail.com |
| Password                                                                                                                                    | (vuoto)               |
| Ruolo                                                                                                                                       | Beneficiario          |
| Campi Specifici                                                                                                                             | N/A                   |
| Codice                                                                                                                                      | N/A                   |
| **Esito atteso**                                                                                                                            |                       |
| La registrazione non va a buon fine perché la password è mancante e il sistema mostra un messaggio di errore: "Campi obbligatori mancanti". |                       |

| **ID TEST CASE**                                                                                                                          |                       |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| TC04                                                                                                                                      |                       |
| Email                                                                                                                                     | nuovoutente@gmail.com |
| Password                                                                                                                                  | TestPassword123       |
| Ruolo                                                                                                                                     | Amministratore        |
| Campi Specifici                                                                                                                           | N/A                   |
| Codice                                                                                                                                    | N/A                   |
| **Esito atteso**                                                                                                                          |                       |
| La registrazione non va a buon fine perché il ruolo inserito non è valido e il sistema mostra un messaggio di errore: "Ruolo non valido". |                       |

| **ID TEST CASE**                                                                                                                                                  |                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| TC05                                                                                                                                                              |                       |
| Email                                                                                                                                                             | nuovoutente@gmail.com |
| Password                                                                                                                                                          | TestPassword123       |
| Ruolo                                                                                                                                                             | Beneficiario          |
| Nome                                                                                                                                                              | Mario                 |
| Cognome                                                                                                                                                           | Rossi                 |
| Data nascita                                                                                                                                                      | 1990-05-13            |
| Carta identitá (file)                                                                                                                                             | (mancante)            |
| Codice                                                                                                                                                            | N/A                   |
| **Esito atteso**                                                                                                                                                  |                       |
| La registrazione non va a buon fine perché manca il file della carta d'identità (campo obbligatorio per beneficiario) e il sistema restituisce un errore interno. |                       |

| **ID TEST CASE**                                                                                                                                                                      |                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| TC06                                                                                                                                                                                  |                               |
| Email                                                                                                                                                                                 | nuovoutente2@gmail.com        |
| Password                                                                                                                                                                              | TestPassword123               |
| Ruolo                                                                                                                                                                                 | Donatore                      |
| Campi specifici                                                                                                                                                                       | Tutti compilati correttamente |
| Codice                                                                                                                                                                                | N/A                           |
| **Esito atteso**                                                                                                                                                                      |                               |
| La registrazione non va a buon fine perché tramite un mock forzato nel backend simuliamo un problema al servizio mail. Il sistema mostra un messaggio di errore: "Email non inviata". |                               |

| **ID TEST CASE**                                                                                                                                 |                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| TC07                                                                                                                                             |                               |
| Email                                                                                                                                            | nuovoutente2@gmail.com        |
| Password                                                                                                                                         | TestPassword123               |
| Ruolo                                                                                                                                            | Donatore                      |
| Campi Specifici                                                                                                                                  | Tutti compilati completamente |
| Codice                                                                                                                                           | (vuoto)                       |
| **Esito atteso**                                                                                                                                 |                               |
| La registrazione non viene completata perché il codice OTP non è stato inserito e il sistema mostra un messaggio di errore: "Codice non valido". |                               |

| **ID TEST CASE**                                                                                                                                                  |                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| TC08                                                                                                                                                              |                               |
| Email                                                                                                                                                             | nuovoutente2@gmail.com        |
| Password                                                                                                                                                          | TestPassword123               |
| Ruolo                                                                                                                                                             | Donatore                      |
| Campi Specifici                                                                                                                                                   | Tutti compilati completamente |
| Codice                                                                                                                                                            | 389678                        |
| **Esito atteso**                                                                                                                                                  |                               |
| La registrazione non viene completata perché il codice OTP contiene troppe cifre (6 invece di 4) e il sistema mostra un messaggio di errore: "Codice non valido". |                               |

| **ID TEST CASE**                                                                                                                                                                   |                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| TC09                                                                                                                                                                               |                                       |
| Email                                                                                                                                                                              | nuovoutente2@gmail.com                |
| Password                                                                                                                                                                           | TestPassword123                       |
| Ruolo                                                                                                                                                                              | Donatore                              |
| Campi Specifici                                                                                                                                                                    | Tutti i campi compilati correttamente |
| Codice                                                                                                                                                                             | 99999                                 |
| **Esito atteso**                                                                                                                                                                   |                                       |
| La registrazione non viene completata perché il codice OTP inserito non corrisponde a quello generato dal sistema e il sistema mostra un messaggio di errore: "Codice non valido". |                                       |

| **ID TEST CASE**                                                                                                                                                                                         |                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| TC10                                                                                                                                                                                                     |                                        |
| Email                                                                                                                                                                                                    | beneficiario_nuovo@gmail.com           |
| Password                                                                                                                                                                                                 | TestPassword123                        |
| Ruolo                                                                                                                                                                                                    | Beneficiario                           |
| Campi Specifici                                                                                                                                                                                          | Tutti compilati correttamente          |
| Codice                                                                                                                                                                                                   | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                                                                                         |                                        |
| La registrazione va a buon fine, l'account viene creato nel database come beneficiario in stato "non accettato" e il sistema mostra: "Codice valido, registrazione in attesa di validazione dall'admin". |                                        |

| **ID TEST CASE**                                                                                                                            |                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| TC11                                                                                                                                        |                                        |
| Email                                                                                                                                       | donatore_nuovo@gmail.com               |
| Password                                                                                                                                    | TestPassword123                        |
| Ruolo                                                                                                                                       | donatore                               |
| Campi Specifici                                                                                                                             | Tutti compilati correttamente          |
| Codice                                                                                                                                      | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                            |                                        |
| La registrazione va a buon fine, l'account donatore viene creato nel database e il sistema mostra: "Codice valido, registrazione avvenuta". |                                        |

| **ID TEST CASE**                                                                                                                                  |                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| TC12                                                                                                                                              |                                        |
| Email                                                                                                                                             | erogatore_nuovo@gmail.com              |
| Password                                                                                                                                          | TestPassword123                        |
| Ruolo                                                                                                                                             | Erogatore                              |
| Campi Specifici                                                                                                                                   | Tutti compilati correttamente          |
| Codice                                                                                                                                            | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                                  |                                        |
| La registrazione va a buon fine, l'account ente erogatore viene creato nel database e il sistema mostra: "Codice valido, registrazione avvenuta". |                                        |

**UC02 Login**

| **ID TEST CASE**                                                |            |
|-----------------------------------------------------------------|------------|
| TC01                                                            |            |
| Email                                                           | DonkeyKong |
| Ruolo                                                           | Donatore   |
| Stato                                                           | N/A        |
| Password                                                        | Bananza29  |
| Codice                                                          | N/A        |
| **Esito atteso**                                                |            |
| Il codice OTP non viene mandato perché la mail non può esistere |            |

| **ID TEST CASE**                                                             |                     |
|------------------------------------------------------------------------------|---------------------|
| TC02                                                                         |                     |
| Email                                                                        | DiddyKong@gmail.com |
| Ruolo                                                                        | Ente erogatore      |
| Stato                                                                        | N/A                 |
| Password                                                                     | Bananza15           |
| Codice                                                                       | N/A                 |
| **Esito atteso**                                                             |                     |
| Il codice OTP non viene mandato perchè la mail non è registrata nel database |                     |

| **ID TEST CASE**                                            |                       |
|-------------------------------------------------------------|-----------------------|
| TC03                                                        |                       |
| Email                                                       | nannidecaro@gmail.com |
| Ruolo                                                       | Beneficiario          |
| Stato                                                       | Non ancora accettato  |
| Password                                                    | Sbagliata_12          |
| Codice                                                      | N/A                   |
| **Esito atteso**                                            |                       |
| Il codice OTP non viene mandato perché la password è errata |                       |

| **ID TEST CASE**                                                                    |                       |
|-------------------------------------------------------------------------------------|-----------------------|
| TC04                                                                                |                       |
| Email                                                                               | nannidecaro@gmail.com |
| Ruolo                                                                               | Beneficiario          |
| Stato                                                                               | Non ancora accettato  |
| Password                                                                            | giogiu07              |
| Codice                                                                              | N/A                   |
| **Esito atteso**                                                                    |                       |
| Il codice OTP non viene mandato perché il beneficiario non è stato ancora accettato |                       |

| **ID TEST CASE**                                         |                          |
|----------------------------------------------------------|--------------------------|
| TC05                                                     |                          |
| Email                                                    | yogurtmangiato@gmail.com |
| Ruolo                                                    | Donatore                 |
| Stato                                                    | N/A                      |
| Password                                                 | latte2012                |
| Codice                                                   | N/A                      |
| **Esito atteso**                                         |                          |
| L’utente non logga perché il codice non è stato inserito |                          |

| **ID TEST CASE**                                                                  |                          |
|-----------------------------------------------------------------------------------|--------------------------|
| TC06                                                                              |                          |
| Email                                                                             | yogurtmangiato@gmail.com |
| Ruolo                                                                             | Donatore                 |
| Stato                                                                             | N/A                      |
| Password                                                                          | latte2012                |
| Codice                                                                            | 38967896                 |
| **Esito atteso**                                                                  |                          |
| L’utente non logga perché il codice non può essere giusto contenendo troppe cifre |                          |

| **ID TEST CASE**                                   |                          |
|----------------------------------------------------|--------------------------|
| TC07                                               |                          |
| Email                                              | yogurtmangiato@gmail.com |
| Ruolo                                              | Donatore                 |
| Stato                                              | N/A                      |
| Password                                           | latte2012                |
| Codice                                             | 3983                     |
| **Esito atteso**                                   |                          |
| L’utente non logga perché il codice non è corretto |                          |

| **ID TEST CASE**            |                          |
|-----------------------------|--------------------------|
| TC08                        |                          |
| Email                       | yogurtmangiato@gmail.com |
| Ruolo                       | Donatore                 |
| Stato                       | N/A                      |
| Password                    | latte2012                |
| Codice                      |                          |
| **Esito atteso**            |                          |
| L’utente logga con successo |                          |

| **ID TEST CASE**                                         |                       |
|----------------------------------------------------------|-----------------------|
| TC09                                                     |                       |
| Email                                                    | nannidecaro@gmail.com |
| Ruolo                                                    | Beneficiario          |
| Stato                                                    | Accettato             |
| Password                                                 | giogiu07              |
| Codice                                                   | N/A                   |
| **Esito atteso**                                         |                       |
| L’utente non logga perché il codice non è stato inserito |                       |

| **ID TEST CASE**                                                                  |                       |
|-----------------------------------------------------------------------------------|-----------------------|
| TC10                                                                              |                       |
| Email                                                                             | nannidecaro@gmail.com |
| Ruolo                                                                             | Beneficiario          |
| Stato                                                                             | Accettato             |
| Password                                                                          | giogiu07              |
| Codice                                                                            | 5437583               |
| **Esito atteso**                                                                  |                       |
| L’utente non logga perché il codice non può essere giusto contenendo troppe cifre |                       |

| **ID TEST CASE**                                   |                       |
|----------------------------------------------------|-----------------------|
| TC11                                               |                       |
| Email                                              | nannidecaro@gmail.com |
| Ruolo                                              | Beneficiario          |
| Stato                                              | Accettato             |
| Password                                           | giogiu07              |
| Codice                                             | 3000                  |
| **Esito atteso**                                   |                       |
| L’utente non logga perché il codice non è corretto |                       |

| **ID TEST CASE**            |                       |
|-----------------------------|-----------------------|
| TC12                        |                       |
| Email                       | nannidecaro@gmail.com |
| Ruolo                       | Beneficiario          |
| Stato                       | Accettato             |
| Password                    | giogiu07              |
| Codice                      |                       |
| **Esito atteso**            |                       |
| L’utente logga con successo |                       |

**UC03 Donazione Monetaria**

| **ID TEST FRAME**                                                                                                              |                  |
|--------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC01                                                                                                                           |                  |
| **INPUT**                                                                                                                      | **VALORE**       |
| nome_ente_erogatore                                                                                                            | Caritas Salerno  |
| numero_carta                                                                                                                   | 1234567812345678 |
| scadenza                                                                                                                       | 2026-12-31       |
| cvv                                                                                                                            | 123              |
| importo                                                                                                                        | 0                |
| **OUTPUT**                                                                                                                     |                  |
| La donazione non va a buon fine perchè l’importo non è valido e il sistema mostra un messaggio di errore: “Importo non valido” |                  |

| **ID TEST FRAME**                                                                                                                        |                 |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| TC02                                                                                                                                     |                 |
| **INPUT**                                                                                                                                | **VALORE**      |
| nome_ente_erogatore                                                                                                                      | Caritas Salerno |
| numero_carta                                                                                                                             | 12345678        |
| scadenza                                                                                                                                 | 2026-12-31      |
| cvv                                                                                                                                      | 123             |
| importo                                                                                                                                  | 50              |
| **OUTPUT**                                                                                                                               |                 |
| La donazione non va a buon fine perchè il numero carta non è valido e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                 |

| **ID TEST FRAME**                                                                                                                    |                  |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC03                                                                                                                                 |                  |
| **INPUT**                                                                                                                            | **VALORE**       |
| nome_ente_erogatore                                                                                                                  | Caritas Salerno  |
| numero_carta                                                                                                                         | 1234567812345678 |
| scadenza                                                                                                                             | 2021-12-31       |
| cvv                                                                                                                                  | 123              |
| importo                                                                                                                              | 50               |
| **OUTPUT**                                                                                                                           |                  |
| La donazione non va a buon fine perchè la scadenza non è valida e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                  |

| **ID TEST FRAME**                                                                                                               |                  |
|---------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC04                                                                                                                            |                  |
| **INPUT**                                                                                                                       | **VALORE**       |
| nome_ente_erogatore                                                                                                             | Caritas Salerno  |
| numero_carta                                                                                                                    | 1234567812345678 |
| scadenza                                                                                                                        | 2021-12-31       |
| cvv                                                                                                                             | 12               |
| importo                                                                                                                         | 50               |
| **OUTPUT**                                                                                                                      |                  |
| La donazione non va a buon fine perchè il cvv non è idoneo e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                  |

| **ID TEST FRAME**                                                                                                                                      |                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC05                                                                                                                                                   |                  |
| **INPUT**                                                                                                                                              | **VALORE**       |
| nome_ente_erogatore                                                                                                                                    | Ente inesistente |
| numero_carta                                                                                                                                           | 1234567812345678 |
| scadenza                                                                                                                                               | 2026-12-31       |
| cvv                                                                                                                                                    | 123              |
| importo                                                                                                                                                | 50               |
| **OUTPUT**                                                                                                                                             |                  |
| La donazione non va a buon fine perchè l’ente inserito non è presente nel db e il sistema mostra un messaggio di errore: “Ente erogatore non trovato”. |                  |

| **ID TEST FRAME**                                                                                                                                   |                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| TC06                                                                                                                                                |                                           |
| **INPUT**                                                                                                                                           | **VALORE**                                |
| nome_ente_erogatore                                                                                                                                 | UNISA - Università degli Studi di Salerno |
| numero_carta                                                                                                                                        | 1234567812345678                          |
| scadenza                                                                                                                                            | 2026-12-31                                |
| cvv                                                                                                                                                 | 123                                       |
| importo                                                                                                                                             | 50                                        |
| **OUTPUT**                                                                                                                                          |                                           |
| La donazione non va a buon fine perchè l’IBAN dell’ente erogatore non è valido e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                                           |

| **ID TEST FRAME**                                                                                                                                                                                   |                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC08                                                                                                                                                                                                |                  |
| **INPUT**                                                                                                                                                                                           | **VALORE**       |
| nome_ente_erogatore                                                                                                                                                                                 | Caritas Salerno  |
| numero_carta                                                                                                                                                                                        | 1234567812345678 |
| scadenza                                                                                                                                                                                            | 2026-12-31       |
| cvv                                                                                                                                                                                                 | 123              |
| importo                                                                                                                                                                                             | 50               |
| **OUTPUT**                                                                                                                                                                                          |                  |
| Tramite un false imposto nel backend simuliamo un problema al servizio mail, la donazione non va a buon fine e il sistema mostra un messaggio di errore: “Donazione eseguita ma email non inviata”. |                  |

| **ID TEST FRAME**                                                                                                                           |                  |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| TC09                                                                                                                                        |                  |
| **INPUT**                                                                                                                                   | **VALORE**       |
| nome_ente_erogatore                                                                                                                         | Caritas Salerno  |
| numero_carta                                                                                                                                | 1234567812345678 |
| scadenza                                                                                                                                    | 2026-12-31       |
| cvv                                                                                                                                         | 123              |
| importo                                                                                                                                     | 50               |
| **OUTPUT**                                                                                                                                  |                  |
| La donazione va a buon fine, viene registrata nel database e il sistema mostra un messaggio: “Donazione monetaria completata con successo”. |                  |

**UC06 Segnalazione di un punto di bisogno**

| **ID TEST FRAME**                                                                                                                   |                                      |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| TC01                                                                                                                                |                                      |
| **INPUT**                                                                                                                           | **VALORE**                           |
| utente                                                                                                                              | Nessun login effettuato              |
| longitudine                                                                                                                         | 12.4922                              |
| latitudine                                                                                                                          | 41.8902                              |
| indirizzo                                                                                                                           | Via Giuseppe Mazzini 62, Battipaglia |
| **OUTPUT**                                                                                                                          |                                      |
| La segnalazione non va a buon fine perché l’utente non è autenticato e il sistema mostra un messaggio di errore: “Non autenticato”. |                                      |

| **ID TEST FRAME**                                                                                                                                                                          |                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| TC02                                                                                                                                                                                       |                                      |
| **INPUT**                                                                                                                                                                                  | **VALORE**                           |
| utente                                                                                                                                                                                     | Associazione “Cuori Uniti”           |
| longitudine                                                                                                                                                                                | (vuoto)                              |
| latitudine                                                                                                                                                                                 | (vuoto)                              |
| indirizzo                                                                                                                                                                                  | Via Giuseppe Mazzini 62, Battipaglia |
| **OUTPUT**                                                                                                                                                                                 |                                      |
| La segnalazione non va a buon fine perché le coordinate non sono valide e il sistema mostra un messaggio di errore: “Dati mancanti: latitudine, longitudine e indirizzo sono obbligatori”. |                                      |

| **ID TEST FRAME**                                                                                                                                                                   |                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| TC03                                                                                                                                                                                |                            |
| **INPUT**                                                                                                                                                                           | **VALORE**                 |
| utente                                                                                                                                                                              | Associazione “Cuori Uniti” |
| longitudine                                                                                                                                                                         | 15.1165                    |
| latitudine                                                                                                                                                                          | 37.5418                    |
| indirizzo                                                                                                                                                                           | (vuoto)                    |
| **OUTPUT**                                                                                                                                                                          |                            |
| La segnalazione non va a buon fine perché l’indirizzo è mancante e il sistema mostra un messaggio di errore: “Dati mancanti: latitudine, longitudine e indirizzo sono obbligatori". |                            |

| **ID TEST FRAME**                                                                                                                                         |                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| TC04                                                                                                                                                      |                                      |
| **INPUT**                                                                                                                                                 | **VALORE**                           |
| utente                                                                                                                                                    | Associazione “Cuori Uniti”           |
| longitudine                                                                                                                                               | 15.1165                              |
| latitudine                                                                                                                                                | 37.5418                              |
| indirizzo                                                                                                                                                 | Via Giuseppe Mazzini 62, Battipaglia |
| **OUTPUT**                                                                                                                                                |                                      |
| La segnalazione va a buon fine, viene inviata via email a tutti gli enti erogatori e il sistema mostra un pop-up: “Segnalazione completata con successo”. |                                      |

**UC11 Filtraggio della mappa**

| **ID TEST CASE**                                                                                                                          |                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| TC01                                                                                                                                      |                                  |
| **INPUT**                                                                                                                                 | **VALORE**                       |
| categoria                                                                                                                                 | (nessuna - "Tutte le categorie") |
| **OUTPUT**                                                                                                                                |                                  |
| Il sistema restituisce tutti i punti di distribuzione presenti nel database senza applicare alcun filtro. La mappa mostra tutti i marker. |                                  |

| **ID TEST CASE**                                                                                                                                       |            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| TC02                                                                                                                                                   |            |
| **INPUT**                                                                                                                                              | **VALORE** |
| categoria                                                                                                                                              | Alimentari |
| **OUTPUT**                                                                                                                                             |            |
| Il sistema restituisce solo i punti di distribuzione che contengono beni di macrocategoria "Alimentari". La mappa mostra solo i marker corrispondenti. |            |

| **ID TEST CASE**                                                                                                                                                                                              |             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| TC03                                                                                                                                                                                                          |             |
| **INPUT**                                                                                                                                                                                                     | **VALORE**  |
| categoria                                                                                                                                                                                                     | Elettronica |
| **OUTPUT**                                                                                                                                                                                                    |             |
| Il sistema esegue la query con JOIN ma non trova nessun punto di distribuzione con beni della categoria "elettronica" (inesistente). La risposta contiene una lista vuota e la mappa non mostra alcun marker. |             |

| **ID TEST CASE**                                                                                                                                              |            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| TC04                                                                                                                                                          |            |
| **INPUT**                                                                                                                                                     | **VALORE** |
| categoria                                                                                                                                                     | Medicinali |
| **OUTPUT**                                                                                                                                                    |            |
| Il sistema esegue la query ma nessun punto di distribuzione attivo ha beni di categoria "Medicinali" in questo momento. La risposta contiene una lista vuota. |            |

| **ID TEST CASE**                                                                                                                                                                                                           |                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| TC05                                                                                                                                                                                                                       |                                                   |
| **INPUT**                                                                                                                                                                                                                  | **VALORE**                                        |
| categoria                                                                                                                                                                                                                  | Alimentari                                        |
| stato_schema                                                                                                                                                                                                               | Tabelle sotto_categorie e macro_categorie ASSENTI |
| **OUTPUT**                                                                                                                                                                                                                 |                                                   |
| Il sistema rileva che le tabelle delle categorie non esistono nello schema, ignora il filtro per categoria e restituisce tutti i punti di distribuzione. La risposta include meta.categoria_ignored = true con la ragione. |                                                   |

| **ID TEST CASE**                                                                                                                     |                                         |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| TC06                                                                                                                                 |                                         |
| **INPUT**                                                                                                                            | **VALORE**                              |
| categoria                                                                                                                            | Alimentari                              |
| stato_schema                                                                                                                         | Connessione al database non disponibile |
| **OUTPUT**                                                                                                                           |                                         |
| Il sistema non riesce a connettersi al database e restituisce un errore 500 con messaggio "db_error". La mappa non viene aggiornata. |                                         |
