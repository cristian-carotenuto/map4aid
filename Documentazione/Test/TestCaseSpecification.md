<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*TEST CASE SPECIFICATION*

All’interno di questo documento viene riportata l’applicazione della metodologia di individuazione dei casi di test definita nel Test Plan (TP).

Il documento raccoglie i test frame generati attraverso la tecnica di progettazione indicata nel TP e le specifiche dettagliate dei casi di test associati alle funzionalità da verificare.

L’obiettivo è garantire una copertura sistematica e completa dei requisiti, assicurando che ogni funzionalità venga validata rispetto ai comportamenti attesi.

Sono riportati tutti i test design relativi alle funzionalità da testare, così come identificate nel TP. Per ciascuna funzionalità vengono presentati i test frame derivati dall’applicazione della tecnica di progettazione scelta e, successivamente, le specifiche dei casi di test che ne discendono.

Ogni test case è descritto in modo strutturato, includendo input, condizioni, vincoli e oracoli necessari alla sua esecuzione.

**UC02 Login**

Un utente registrato accede al sistema inserendo email e password.

Il sistema verifica che le credenziali siano corrette e che l’utente non sia già autenticato.

Se la verifica ha esito positivo, il sistema genera un codice OTP e lo invia all’indirizzo email dell’utente.

L’utente inserisce il codice OTP ricevuto.

Il sistema confronta il codice con quello generato e, se valido, completa l’autenticazione creando la sessione utente.

Per gli utenti di tipo beneficiario, l’accesso è consentito solo se l’account risulta approvato da un amministratore.

Se l’OTP è errato, mancante o non più valido, il login non viene completato.

**UC04 Donazione monetaria**

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

**UC06 Segnalazione di un punto di bisogno**

Un utente autenticato (donatore, beneficiario o ente erogatore) segnala una posizione geografica dove è necessario un intervento o un aiuto. Il sistema invia una notifica via email a tutti gli enti erogatori registrati sulla piattaforma.

L’utente inserisce i dati della posizione: latitudine, longitudine e un indirizzo descrittivo.

Il sistema verifica che i campi latitudine, longitudine e indirizzo non siano vuoti e che l'utente abbia un ruolo autorizzato (donatore, beneficiario, ente).

Se i dati sono validi, il sistema recupera la lista di tutti gli enti erogatori dal database.

Il sistema tenta di inviare una e-mail di segnalazione  a ciascun ente con i dettagli della posizione.

Al termine, il sistema conferma l'avvenuta segnalazione all'utente.

**UC 09 Storico attività e reportistica**

Un utente autenticato accede alla sezione dedicata al suo profilo

L’utente richiede la generazione del PDF dello storico

Il sistema verifica che l’utente sia autenticato.

Il sistema recupera dal database le attività associate all’utente in base al suo ruolo:

- prenotazioni (per beneficiario)

- donazioni di beni e monetarie (per donatore)

- prenotazioni e donazioni legate ai punti dell’ente (per ente erogatore)

Il sistema genera dinamicamente un file in formato PDF contenente lo storico delle attività recuperate

Il PDF viene restituito come file scaricabile con nome storico.pdf

Se lo storico risulta vuoto il sistema genera comunque il PDF e contiene le sezioni previste ma risulta vuoto

# 

**UC01 Registrazione**

## 

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Parametro</strong></td>
<td><strong>Categoria</strong></td>
<td><strong>Vincoli e proprietà</strong></td>
</tr>
<tr class="even">
<td>email</td>
<td>Formato(FM)</td>
<td><p>1.l’email è in un formato del tipo ^[a-zA-Z0-9.<em>%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ <strong>[propietà FM</strong></em><strong>_OK]</strong></p>
<p>2. l’email non rispetta il formato<strong>[ERR]</strong></p></td>
</tr>
<tr class="odd">
<td>email</td>
<td>NonRegistrata(NR)</td>
<td><p>1.L’email non è registrata nel database<strong>[IF FM_OK][Proprietà NR_OK]</strong></p>
<p>2.L’email è registrata nel database<strong>[IF FM_OK][ERR]</strong></p></td>
</tr>
<tr class="even">
<td>password</td>
<td>Presente(PW)</td>
<td><p>1. La password è presente e non vuota <strong>[Proprietà PW_OK]</strong></p>
<p>2. La password è assente o vuota <strong>[ERR]</strong></p></td>
</tr>
<tr class="odd">
<td>ruolo</td>
<td>Validitá(RL)</td>
<td><p>1. Il ruolo è "beneficiario" <strong>[Proprietà RL_BN]</strong></p>
<p>2. Il ruolo è "donatore" <strong>[Proprietà RL_DN]</strong></p>
<p>3. Il ruolo è "erogatore" <strong>[Proprietà RL_ER]</strong></p>
<p>4. Il ruolo non è valido o è vuoto <strong>[ERR]</strong></p></td>
</tr>
<tr class="even">
<td>campi_specifici</td>
<td>Completezza (CS)</td>
<td><p>1. Tutti i campi specifici per il ruolo sono compilati <strong>[IF RL_BN OR RL_DN OR RL_ER] [Proprietà CS_OK]</strong></p>
<p>2. Uno o più campi specifici obbligatori mancano <strong>[IF RL_BN OR RL_DN OR RL_ER] [ERR]</strong></p></td>
</tr>
<tr class="odd">
<td>email_otp</td>
<td>Invio(EM)</td>
<td>1. L'email OTP viene inviata correttamente <strong>[IF CS_OK AND UN_OK AND PW_OK] [Proprietà EM_OK]</strong><br />
2. L'email OTP non viene inviata <strong>[IF CS_OK AND NR_OK AND PW_OK] [ERR]</strong></td>
</tr>
<tr class="even">
<td>codice</td>
<td>Lunghezza(LN)</td>
<td><p>1. Il codice ha lunghezza 0 <strong>[IF EM_OK] [ERR]</strong></p>
<p>2. Il codice ha lunghezza &gt; 5 <strong>[IF EM_OK] [ERR]</strong></p>
<p>3. Il codice ha 0&lt;lunghezza &lt; 5 <strong>[IF EM_OK] [Proprietà LN_OK]</strong></p></td>
</tr>
<tr class="odd">
<td>codice</td>
<td>Corretto(CT)</td>
<td><p>1. Il codice è corretto <strong>[IF OK_LN] [Proprietà OK_CT]</strong></p>
<p>2. Il codice non è corretto <strong>[IF OK_LN] [ERR]</strong></p></td>
</tr>
</tbody>
</table>

**UC02 Login**

## 

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Parametro</strong></td>
<td><strong>Categoria</strong></td>
<td><strong>Vincoli e proprietà</strong></td>
</tr>
<tr class="even">
<td>email</td>
<td>Formato(FM)</td>
<td><p>1.l’email è in un formato del tipo ^[a-zA-Z0-9.<em>%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ <strong>[propietà FM</strong></em><strong>_OK]</strong></p>
<p>2. l’email non rispetta il formato<strong>[ERR]</strong></p></td>
</tr>
<tr class="odd">
<td>email</td>
<td>Registrata(RG)</td>
<td><p>1.L’email è registrata nel database<strong>[IF FM_OK][Proprietà RG_OK]</strong></p>
<p>2.L’email non è registrata nel database<strong>[IF FM_OK][ERR]</strong></p></td>
</tr>
<tr class="even">
<td>ruolo</td>
<td>Beneficiario(BN)</td>
<td><p>1.L’account è un tipo “Beneficiario”<strong>[IF RG_OK][Proprietà IS_BN]</strong></p>
<p>2.L'account non è “Beneficiario”<strong>[IF RG_OK][Proprietà NOT_BN]</strong></p></td>
</tr>
<tr class="odd">
<td>stato_beneficiario</td>
<td>Accettato(AC)</td>
<td><p>1.L’account è stato accettato<strong>[IF IS_BN][Proprietà OK_ACC]</strong></p>
<p>2.L’account è in attesa[IF <strong>IS_BN][ERR]</strong></p></td>
</tr>
<tr class="even">
<td>password</td>
<td>Corretta(CR)</td>
<td><p>1.La password è corretta<strong>[IF RG_OK][Proprietà OK_CR]</strong></p>
<p>2.La password non è corretta<strong>[IF RG_OK][ERR]</strong></p></td>
</tr>
<tr class="odd">
<td>codice</td>
<td>Lunghezza(LN)</td>
<td><p>1.Il codice ha lunghezza 0 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][ERR]</strong></p>
<p>2.Il codice ha lunghezza &gt;4 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][ERR]</strong></p>
<p>3.Il codice ha 0&lt;lunghezza&lt;5 <strong>[IF OK_CR AND(OK_ACC OR NOT_BN)][Proprietà OK_LN]</strong></p></td>
</tr>
<tr class="even">
<td>codice</td>
<td>Corretto(CT)</td>
<td><p>1.Il codice è corretto<strong>[IF OK_LN][Proprietà OK_CT]</strong></p>
<p>2.Il codice non è corretto<strong>[IF OK_LN][ERR]</strong></p></td>
</tr>
</tbody>
</table>

## 

**UC04 Donazione Monetaria**

## 

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 54%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Parametro</strong></td>
<td><strong>Categoria</strong></td>
<td><strong>Vincoli e proprietà</strong></td>
</tr>
<tr class="even">
<td>importo</td>
<td>Validità Importo (<strong>IM</strong>)</td>
<td><ol type="1">
<li><p>L’importo è numerico e maggiore di 0 → <strong>[Proprietà IM_OK]</strong></p></li>
<li><p>L’importo è numerico ma &lt;= 0 → <strong>[ERR]</strong></p></li>
<li><p>L’importo non è numerico → <strong>[ERR]</strong></p></li>
<li><p>L’importo è mancante → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="odd">
<td>numero_carta</td>
<td>Formato Numero Carta (<strong>NC</strong>)</td>
<td><ol type="1">
<li><p>Il numero carta ha lunghezza 16 → <strong>[Proprietà NC_OK]</strong></p></li>
<li><p>Lunghezza != 16 → <strong>[ERR]</strong></p></li>
<li><p>Campo mancante → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="even">
<td>scadenza</td>
<td>Validità scadenza (<strong>SC</strong>)</td>
<td><ol type="1">
<li><p>La scadenza è futura → <strong>[Proprietà SC_OK]</strong></p></li>
<li><p>La scadenza è passata → <strong>[ERR]</strong></p></li>
<li><p>Formato data non valido → <strong>[ERR]</strong></p></li>
<li><p>Campo mancante → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="odd">
<td>utente</td>
<td>Utente Autenticato(<strong>RU</strong>)</td>
<td><ol type="1">
<li><p>L’utente è autenticato → <strong>[Proprietà RU_OK]</strong></p></li>
<li><p>L’utente non è autenticato → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="even">
<td>cvv</td>
<td>Validità CVV (<strong>CV</strong>)</td>
<td><ol type="1">
<li><p>Il CVV ha lunghezza 3 → <strong>[Proprietà CV_OK]</strong></p></li>
<li><p>Lunghezza != 3 → <strong>[ERR]</strong></p></li>
<li><p>Campo mancante → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="odd">
<td>nome_ente_erogatore</td>
<td>Ente Esistente (<strong>EN</strong>)</td>
<td><ol type="1">
<li><p>L’ente esiste nel db → <strong>[Proprietà EN_OK]</strong></p></li>
<li><p>L’ente non esiste → <strong>[ERR]</strong></p></li>
<li><p>Campo mancante → <strong>[ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="even">
<td>iban_destinatario</td>
<td>Validità IBAN (<strong>IB</strong>)</td>
<td><ol type="1">
<li><p>L’IBAN inizia con “IT” → <strong>[Proprietà IB_OK] [IF EN_OK]</strong></p></li>
<li><p>L’IBAN non inizia con “IT” → <strong>[ERR] [IF EN_OK]</strong></p></li>
<li><p>Campo mancante → <strong>[ERR] [IF EN_OK]</strong></p></li>
</ol></td>
</tr>
<tr class="odd">
<td>transazione</td>
<td>Esito Transazione (<strong>TR</strong>)</td>
<td><ol type="1">
<li><p>La transazione è accettata → <strong>[Proprietà TR_OK] [IF IM_OK AND NC_OK AND SC_OK AND CV_OK AND IB_OK]</strong></p></li>
<li><p>La transazione è rifiutata → <strong>[ERR] [IF uno qualsiasi tra IM, NC, SC, CV, IB è ERR]</strong></p></li>
</ol></td>
</tr>
<tr class="even">
<td>email</td>
<td>Invio Email (<strong>EM</strong>)</td>
<td><ol type="1">
<li><p>L’email è inviata correttamente → <strong>[Proprietà EM_OK] [IF TR_OK]</strong></p></li>
<li><p>L’email non è inviata → <strong>[ERR NON BLOCCANTE] [IF TR_OK]</strong></p></li>
</ol></td>
</tr>
</tbody>
</table>

## 

## UC6 Segnalazione di un punto di bisogno

##         

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="parametro">Parametro</h2></th>
<th><h2 id="categoria">Categoria</h2></th>
<th><h2 id="vincoli-e-proprietà">Vincoli e proprietà</h2></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><h2 id="latitudine">Latitudine</h2></td>
<td><h2 id="validità-posizione-vp">Validità Posizione (VP)</h2></td>
<td><h2 id="presente-e-non-vuota-vp_ok">1. Presente e non vuota → [VP_OK]</h2>
<h2 id="mancante-err">2. Mancante → [ERR]</h2></td>
</tr>
<tr class="even">
<td><h2 id="longitudine">Longitudine</h2></td>
<td><h2 id="validità-posizione-vp-1">Validità Posizione (VP)</h2></td>
<td><h2 id="presente-e-non-vuota-vp_ok-1">1. Presente e non vuota → [VP_OK]</h2>
<h2 id="mancante-o-stringa-vuota-err">2. Mancante o stringa vuota → [ERR]</h2></td>
</tr>
<tr class="odd">
<td><h2 id="indirizzo">Indirizzo</h2></td>
<td><h2 id="validità-dati-vd">Validità Dati (VD)</h2></td>
<td><h2 id="testo-presente-vd_ok">1. Testo presente → [VD_OK]</h2>
<h2 id="campo-vuoto-err">2. Campo vuoto → [ERR]</h2>
<h2 id="section-7"></h2></td>
</tr>
<tr class="even">
<td><h2 id="utente">Utente</h2></td>
<td><h2 id="utente-autenticato-ua">Utente Autenticato (UA)</h2></td>
<td><h2 id="ruolo-autorizzato-ua_ok">1. Ruolo autorizzato → [UA_OK]</h2>
<h2 id="utente-non-loggatonon-autorizzato-err">2. Utente non loggato/non autorizzato → [ERR]</h2></td>
</tr>
<tr class="odd">
<td><h2 id="enti-destinatari">Enti Destinatari</h2></td>
<td><h2 id="invio-multiplo-im">Invio Multiplo (IM)</h2></td>
<td><h2 id="lista-enti-erogatori-caricata-correttamente-im_ok">1. Lista enti erogatori caricata correttamente → [IM_OK]</h2></td>
</tr>
<tr class="even">
<td><h2 id="email">Email</h2></td>
<td><h2 id="invio-email-em">Invio Email (EM)</h2></td>
<td><h2 id="inviata-correttamente-a-tutti-em_ok">1. Inviata correttamente a tutti → [EM_OK]</h2></td>
</tr>
<tr class="odd">
<td><h2 id="esito">Esito</h2></td>
<td><h2 id="esito-segnalazione-es">Esito Segnalazione (ES)</h2></td>
<td><h2 id="pop-up-di-successo-mostrato-allutente-es_ok">1. Pop-up di successo mostrato all’utente → [ES_OK]</h2></td>
</tr>
</tbody>
</table>

## 

## 

## 

**UC 09 Storico attività e reportistica**

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parametro</strong></th>
<th><strong>Categoria</strong></th>
<th><strong>Vincoli e proprietà</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sessione_Utente</td>
<td>Autenticato (<strong>AU</strong>)</td>
<td><p>1. L’utente è autenticato <strong>[Proprietà AU_OK]</strong></p>
<p>2. L’utente non è autenticato <strong>[ERR]</strong></p></td>
</tr>
<tr class="even">
<td>Ruolo_Utente</td>
<td>Ruolo (<strong>RU</strong>)</td>
<td><p>1. L’utente è Beneficiario <strong>[IF AU_OK][Proprietà RU_BEN]</strong></p>
<p>2. L’utente è Donatore <strong>[IF AU_OK][Proprietà RU_DON]</strong></p>
<p>3. L’utente è Ente erogatore <strong>[IF AU_OK][Proprietà RU_ENT]</strong></p></td>
</tr>
<tr class="odd">
<td>Storico_Prenotazioni</td>
<td>Presenza (<strong>PR</strong>)</td>
<td><p>1. Esistono prenotazioni associate <strong>[IF RU_BEN OR RU_ENT][Proprietà PR_HAS]</strong></p>
<p>2. Nessuna prenotazione <strong>[IF RU_BEN OR RU_ENT][Proprietà PR_0]</strong></p></td>
</tr>
<tr class="even">
<td>Storico_Donazioni_Beni</td>
<td>Presenza (<strong>DB</strong>)</td>
<td><p>1. Esistono donazioni beni <strong>[IF RU_DON OR RU_ENT][Proprietà DB_HAS]</strong></p>
<p>2. Nessuna donazione beni <strong>[IF RU_DON OR RU_ENT][Proprietà DB_0]</strong></p></td>
</tr>
<tr class="odd">
<td>storico_donazioni_monetarie</td>
<td>Presenza (<strong>DM</strong>)</td>
<td><p>1. Esistono donazioni monetarie <strong>[IF RU_DON OR RU_ENT][Proprietà DM_HAS]</strong></p>
<p>2. Nessuna donazione monetaria <strong>[IF RU_DON OR RU_ENT][Proprietà DM_0]</strong></p></td>
</tr>
<tr class="even">
<td>generazione_pdf</td>
<td>Esito (<strong>GP</strong>)</td>
<td><p>1. PDF generato correttamente <strong>[IF AU_OK][Proprietà GP_OK]</strong></p>
<p>2. Errore generazione PDF <strong>[ERR]</strong></p></td>
</tr>
</tbody>
</table>

##  UC11 Filtraggio della mappa

##  

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 32%" />
<col style="width: 42%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Parametro</strong></td>
<td><strong>Categoria</strong></td>
<td><strong>Vincoli e proprietà</strong></td>
</tr>
<tr class="even">
<td>categoria</td>
<td>Selezione(SL)</td>
<td><p>1. Nessuna categoria selezionata ("Tutte le categorie") <strong>[Proprietà SL_ALL]</strong></p>
<p>2. Una categoria specifica è selezionata <strong>[Proprietà SL_OK]</strong></p></td>
</tr>
<tr class="odd">
<td>categoria</td>
<td>Esistenza(ES)</td>
<td><p>1. La categoria esiste nel database (macro_categorie) <strong>[IF SL_OK] [Proprietà ES_OK]</strong></p>
<p>2. La categoria non esiste nel database <strong>[IF SL_OK] [Proprietà ES_NO]</strong></p></td>
</tr>
<tr class="even">
<td>punti</td>
<td>Disponibilitá(DP)</td>
<td><p>1. Esistono punti di distribuzione con beni della categoria <strong>[IF ES_OK] [Proprietà DP_OK]</strong></p>
<p>2. Nessun punto ha beni della categoria <strong>[IF ES_OK] [Proprietà DP_NO]</strong></p></td>
</tr>
<tr class="odd">
<td>tabelle_categorie</td>
<td>Presenza(TB)</td>
<td><p>1. Le tabelle beni, sotto_categorie, macro_categorie esistono <strong>[Proprietà TB_OK]</strong></p>
<p>2. Una o più tabelle mancano <strong>[Proprietà TB_NO]</strong></p></td>
</tr>
<tr class="even">
<td>risposta</td>
<td>Esito(RS)</td>
<td><p>1. La risposta contiene dati validi <strong>[IF (SL_ALL OR DP_OK) AND TB_OK] [Proprietà RS_OK]</strong></p>
<p>2. La risposta è lista vuota <strong>[IF DP_NO AND TB_OK] [Proprietà RS_EMPTY]</strong></p>
<p>3. Errore del database <strong>[ERR]</strong></p></td>
</tr>
</tbody>
</table>

## 

## 

## 

**UC01 Registrazione**

|               |        |        |        |        |           |        |           |           |                                                        |
|---------------|--------|--------|--------|--------|-----------|--------|-----------|-----------|--------------------------------------------------------|
| **Test case** | **FM** | **NR** | **PW** | **RL** | **CS**    | **EM** | **LN**    | **CT**    | **Esito atteso**                                       |
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

|               |        |        |        |        |        |          |        |                                   |
|---------------|--------|--------|--------|--------|--------|----------|--------|-----------------------------------|
| **Test case** | **FM** | **RG** | **CR** | **BN** | **AC** | **LN**   | **CT** | **Esito atteso**                  |
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

**UC04 Donazione Monetaria**

|               |        |        |        |        |        |        |        |        |                                          |
|---------------|--------|--------|--------|--------|--------|--------|--------|--------|------------------------------------------|
| **Test case** | **IM** | **NC** | **SC** | **CV** | **EN** | **IB** | **TR** | **EM** | **Esito atteso**                         |
| **TC01**      | ERR    | **-**  | **-**  | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]** Importo non valido           |
| **TC02**      | IM_OK  | ERR    | **-**  | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]**Numero carta non valido       |
| **TC03**      | IM_OK  | NC_OK  | ERR    | **-**  | **-**  | **-**  | **-**  |        | **\[ERR\]**Scadenza non valida           |
| **TC04**      | IM_OK  | NC_OK  | SC_OK  | ERR    | **-**  | **-**  | **-**  |        | **\[ERR\]**CVV non valido                |
| **TC05**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | ERR    | **-**  | **-**  |        | **\[ERR\]**Ente non trovato              |
| **TC06**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | ERR    | ERR    | **-**  | **\[ERR\]**IBAN non valido               |
| **TC07**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | TR_OK  | ERR    | **\[ERR\]**Email di conferma non inviata |
| **TC08**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | ERR    | **-**  | **\[ERR\]** Errore generico transazione  |
| **TC09**      | IM_OK  | NC_OK  | SC_OK  | CV_OK  | EN_OK  | IB_OK  | TR_OK  | EM_OK  | Donazione registrata + email inviata     |

**UC6 Segnalazione di un punto di bisogno**

| **Test Case** | **VP** | **VD** | **UA** | **IM** | **EM** | **ES** | **Esito atteso**                                 |
|---------------|--------|--------|--------|--------|--------|--------|--------------------------------------------------|
| **TC01**      | \-     | \-     | ERR    | \-     | \-     | \-     | **\[ERR\]** Utente non autorizzato o non loggato |
| **TC02**      | ERR    | VP_OK  | UA_OK  | \-     | \-     | ERR    | **\[ERR\]** Coordinate mancanti                  |
| **TC03**      | VP_OK  | ERR    | UA_OK  | \-     | \-     | ERR    | **\[ERR\]** Indirizzo mancante o vuoto           |
| **TC04**      | VP_OK  | VD_OK  | UA_OK  | IM_OK  | EM_OK  | ES_OK  | **\[SUCCESS\]** Segnalazione OK +email inviate   |

**UC 09 Storico e Reportistica**

| **Test Case** | **AU**    | **RU**     | **PR**     | **DB**     | **DM**     | **Esito Atteso**                                                                     |
|---------------|-----------|------------|------------|------------|------------|--------------------------------------------------------------------------------------|
| **TC01**      | **ERR**   | **-**      | **-**      | **-**      | **-**      | **\[ERR\]** Utente non loggato                                                       |
| **TC02**      | **AU_OK** | **RU_BEN** | **PR_0**   | **-**      | **-**      | PDF generato con successo ma vuoto perché non esistono attività associate all’utente |
| **TC03**      | **AU_OK** | **RU_BEN** | **PR_HAS** | **-**      | **-**      | PDF Generato con successo con i dati presenti nel database                           |
| **TC04**      | **AU_OK** | **RU_DON** | **-**      | **DB_0**   | **DM_0**   | PDF Generato con successo ma vuoto perché non esistono attività associate all’utente |
| **TC05**      | **AU_OK** | **RU_DON** | **-**      | **DB_HAS** | **DM_HAS** | PDF Generato con successo con i dati presenti nel database                           |
| **TC06**      | **AU_OK** | **RU_ENT** | **PR_0**   | **DB_0**   | **DM_0**   | PDF generato con successo ma vuoto perché non esistono attività associate all’utente |
| **TC07**      | **AU_OK** | **RU_ENT** | **PR_HAS** | **DB_HAS** | **DM_HAS** | PDF Generato con successo con i dati presenti nel database                           |

**UC11 Filtraggio della mappa**

|               |        |        |        |        |          |                                                           |
|---------------|--------|--------|--------|--------|----------|-----------------------------------------------------------|
| **Test case** | **SL** | **ES** | **DP** | **TB** | **RS**   | **Esito atteso**                                          |
| TC01          | SL_ALL | \-     | \-     | TB_OK  | RS_OK    | **\[SUCCESS\]** Tutti i punti restituiti                  |
| TC02          | SL_OK  | ES_OK  | DP_OK  | TB_OK  | RS_OK    | **\[SUCCESS\]** Punti filtrati per categoria              |
| TC03          | SL_OK  | ES_NO  | \-     | TB_OK  | RS_EMPTY | **\[SUCCESS\]** Lista vuota (categoria inesistente)       |
| TC04          | SL_OK  | ES_OK  | DP_NO  | TB_OK  | RS_EMPTY | **\[SUCCESS\]** Lista vuota (nessun punto con beni)       |
| TC05          | SL_OK  | \-     | \-     | TB_NO  | RS_OK    | **\[SUCCESS\]** Filtro ignorato, tutti i punti restituiti |
| TC06          | \-     | \-     | \-     | \-     | ERR      | **\[ERR\]** Errore database                               |

Per ciascun test case vengono definiti:

- gli input necessari all’esecuzione della funzionalità a cui il test fa riferimento,

- i valori assegnati a ciascun input, scelti sulla base delle combinazioni individuate tramite tecnica Category Partition,

- l’oracolo, ovvero il risultato atteso dal sistema a fronte degli input specificati**.**

**UC01 Registrazione**

|                                                                                                                                                         |                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **ID TEST CASE**                                                                                                                                        |                 |
| TC01                                                                                                                                                    |                 |
| Email                                                                                                                                                   | DonkeyKong      |
| Password                                                                                                                                                | TestPassword123 |
| Ruolo                                                                                                                                                   | Beneficiario    |
| Campi Specifici                                                                                                                                         | N/A             |
| Codice                                                                                                                                                  | N/A             |
| **Esito atteso**                                                                                                                                        |                 |
| La registrazione non va a buon fine perché l'email non è in un formato valido e il sistema mostra un messaggio di errore: "Campi obbligatori mancanti". |                 |

|                                                                                                                                                    |                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| **ID TEST CASE**                                                                                                                                   |                          |
| TC02                                                                                                                                               |                          |
| Email                                                                                                                                              | yogurtmangiato@gmail.com |
| Password                                                                                                                                           | TestPassword123          |
| Ruolo                                                                                                                                              | Donatore                 |
| Campi Specifici                                                                                                                                    | N/A                      |
| Codice                                                                                                                                             | N/A                      |
| **Esito atteso**                                                                                                                                   |                          |
| La registrazione non va a buon fine perché l'email è già presente nel database e il sistema mostra un messaggio di errore: "Email già registrata". |                          |

|                                                                                                                                             |                       |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                                                                                                            |                       |
| TC03                                                                                                                                        |                       |
| Email                                                                                                                                       | nuovoutente@gmail.com |
| Password                                                                                                                                    | (vuoto)               |
| Ruolo                                                                                                                                       | Beneficiario          |
| Campi Specifici                                                                                                                             | N/A                   |
| Codice                                                                                                                                      | N/A                   |
| **Esito atteso**                                                                                                                            |                       |
| La registrazione non va a buon fine perché la password è mancante e il sistema mostra un messaggio di errore: "Campi obbligatori mancanti". |                       |

|                                                                                                                                           |                       |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                                                                                                          |                       |
| TC04                                                                                                                                      |                       |
| Email                                                                                                                                     | nuovoutente@gmail.com |
| Password                                                                                                                                  | TestPassword123       |
| Ruolo                                                                                                                                     | Amministratore        |
| Campi Specifici                                                                                                                           | N/A                   |
| Codice                                                                                                                                    | N/A                   |
| **Esito atteso**                                                                                                                          |                       |
| La registrazione non va a buon fine perché il ruolo inserito non è valido e il sistema mostra un messaggio di errore: "Ruolo non valido". |                       |

|                                                                                                                                                                   |                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                                                                                                                                  |                       |
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

|                                                                                                                                                                                       |                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| **ID TEST CASE**                                                                                                                                                                      |                               |
| TC06                                                                                                                                                                                  |                               |
| Email                                                                                                                                                                                 | nuovoutente2@gmail.com        |
| Password                                                                                                                                                                              | TestPassword123               |
| Ruolo                                                                                                                                                                                 | Donatore                      |
| Campi specifici                                                                                                                                                                       | Tutti compilati correttamente |
| Codice                                                                                                                                                                                | N/A                           |
| **Esito atteso**                                                                                                                                                                      |                               |
| La registrazione non va a buon fine perché tramite un mock forzato nel backend simuliamo un problema al servizio mail. Il sistema mostra un messaggio di errore: "Email non inviata". |                               |

|                                                                                                                                                  |                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| **ID TEST CASE**                                                                                                                                 |                               |
| TC07                                                                                                                                             |                               |
| Email                                                                                                                                            | nuovoutente2@gmail.com        |
| Password                                                                                                                                         | TestPassword123               |
| Ruolo                                                                                                                                            | Donatore                      |
| Campi Specifici                                                                                                                                  | Tutti compilati completamente |
| Codice                                                                                                                                           | (vuoto)                       |
| **Esito atteso**                                                                                                                                 |                               |
| La registrazione non viene completata perché il codice OTP non è stato inserito e il sistema mostra un messaggio di errore: "Codice non valido". |                               |

|                                                                                                                                                                   |                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| **ID TEST CASE**                                                                                                                                                  |                               |
| TC08                                                                                                                                                              |                               |
| Email                                                                                                                                                             | nuovoutente2@gmail.com        |
| Password                                                                                                                                                          | TestPassword123               |
| Ruolo                                                                                                                                                             | Donatore                      |
| Campi Specifici                                                                                                                                                   | Tutti compilati completamente |
| Codice                                                                                                                                                            | 389678                        |
| **Esito atteso**                                                                                                                                                  |                               |
| La registrazione non viene completata perché il codice OTP contiene troppe cifre (6 invece di 4) e il sistema mostra un messaggio di errore: "Codice non valido". |                               |

|                                                                                                                                                                                    |                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| **ID TEST CASE**                                                                                                                                                                   |                                       |
| TC09                                                                                                                                                                               |                                       |
| Email                                                                                                                                                                              | nuovoutente2@gmail.com                |
| Password                                                                                                                                                                           | TestPassword123                       |
| Ruolo                                                                                                                                                                              | Donatore                              |
| Campi Specifici                                                                                                                                                                    | Tutti i campi compilati correttamente |
| Codice                                                                                                                                                                             | 99999                                 |
| **Esito atteso**                                                                                                                                                                   |                                       |
| La registrazione non viene completata perché il codice OTP inserito non corrisponde a quello generato dal sistema e il sistema mostra un messaggio di errore: "Codice non valido". |                                       |

|                                                                                                                                                                                                          |                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| **ID TEST CASE**                                                                                                                                                                                         |                                        |
| TC10                                                                                                                                                                                                     |                                        |
| Email                                                                                                                                                                                                    | beneficiario_nuovo@gmail.com           |
| Password                                                                                                                                                                                                 | TestPassword123                        |
| Ruolo                                                                                                                                                                                                    | Beneficiario                           |
| Campi Specifici                                                                                                                                                                                          | Tutti compilati correttamente          |
| Codice                                                                                                                                                                                                   | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                                                                                         |                                        |
| La registrazione va a buon fine, l'account viene creato nel database come beneficiario in stato "non accettato" e il sistema mostra: "Codice valido, registrazione in attesa di validazione dall'admin". |                                        |

|                                                                                                                                             |                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| **ID TEST CASE**                                                                                                                            |                                        |
| TC11                                                                                                                                        |                                        |
| Email                                                                                                                                       | donatore_nuovo@gmail.com               |
| Password                                                                                                                                    | TestPassword123                        |
| Ruolo                                                                                                                                       | donatore                               |
| Campi Specifici                                                                                                                             | Tutti compilati correttamente          |
| Codice                                                                                                                                      | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                            |                                        |
| La registrazione va a buon fine, l'account donatore viene creato nel database e il sistema mostra: "Codice valido, registrazione avvenuta". |                                        |

|                                                                                                                                                   |                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| **ID TEST CASE**                                                                                                                                  |                                        |
| TC12                                                                                                                                              |                                        |
| Email                                                                                                                                             | erogatore_nuovo@gmail.com              |
| Password                                                                                                                                          | TestPassword123                        |
| Ruolo                                                                                                                                             | Erogatore                              |
| Campi Specifici                                                                                                                                   | Tutti compilati correttamente          |
| Codice                                                                                                                                            | (codice corretto generato dal sistema) |
| **Esito atteso**                                                                                                                                  |                                        |
| La registrazione va a buon fine, l'account ente erogatore viene creato nel database e il sistema mostra: "Codice valido, registrazione avvenuta". |                                        |

**UC02 Login**

|                                                                 |            |
|-----------------------------------------------------------------|------------|
| **ID TEST CASE**                                                |            |
| TC01                                                            |            |
| Email                                                           | DonkeyKong |
| Ruolo                                                           | Donatore   |
| Stato                                                           | N/A        |
| Password                                                        | Bananza29  |
| Codice                                                          | N/A        |
| **Esito atteso**                                                |            |
| Il codice OTP non viene mandato perché la mail non può esistere |            |

|                                                                              |                     |
|------------------------------------------------------------------------------|---------------------|
| **ID TEST CASE**                                                             |                     |
| TC02                                                                         |                     |
| Email                                                                        | DiddyKong@gmail.com |
| Ruolo                                                                        | Ente erogatore      |
| Stato                                                                        | N/A                 |
| Password                                                                     | Bananza15           |
| Codice                                                                       | N/A                 |
| **Esito atteso**                                                             |                     |
| Il codice OTP non viene mandato perchè la mail non è registrata nel database |                     |

|                                                             |                       |
|-------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                            |                       |
| TC03                                                        |                       |
| Email                                                       | nannidecaro@gmail.com |
| Ruolo                                                       | Beneficiario          |
| Stato                                                       | Non ancora accettato  |
| Password                                                    | Sbagliata_12          |
| Codice                                                      | N/A                   |
| **Esito atteso**                                            |                       |
| Il codice OTP non viene mandato perché la password è errata |                       |

|                                                                                     |                       |
|-------------------------------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                                                    |                       |
| TC04                                                                                |                       |
| Email                                                                               | nannidecaro@gmail.com |
| Ruolo                                                                               | Beneficiario          |
| Stato                                                                               | Non ancora accettato  |
| Password                                                                            | giogiu07              |
| Codice                                                                              | N/A                   |
| **Esito atteso**                                                                    |                       |
| Il codice OTP non viene mandato perché il beneficiario non è stato ancora accettato |                       |

|                                                          |                          |
|----------------------------------------------------------|--------------------------|
| **ID TEST CASE**                                         |                          |
| TC05                                                     |                          |
| Email                                                    | yogurtmangiato@gmail.com |
| Ruolo                                                    | Donatore                 |
| Stato                                                    | N/A                      |
| Password                                                 | latte2012                |
| Codice                                                   | N/A                      |
| **Esito atteso**                                         |                          |
| L’utente non logga perché il codice non è stato inserito |                          |

|                                                                                   |                          |
|-----------------------------------------------------------------------------------|--------------------------|
| **ID TEST CASE**                                                                  |                          |
| TC06                                                                              |                          |
| Email                                                                             | yogurtmangiato@gmail.com |
| Ruolo                                                                             | Donatore                 |
| Stato                                                                             | N/A                      |
| Password                                                                          | latte2012                |
| Codice                                                                            | 38967896                 |
| **Esito atteso**                                                                  |                          |
| L’utente non logga perché il codice non può essere giusto contenendo troppe cifre |                          |

|                                                    |                          |
|----------------------------------------------------|--------------------------|
| **ID TEST CASE**                                   |                          |
| TC07                                               |                          |
| Email                                              | yogurtmangiato@gmail.com |
| Ruolo                                              | Donatore                 |
| Stato                                              | N/A                      |
| Password                                           | latte2012                |
| Codice                                             | 3983                     |
| **Esito atteso**                                   |                          |
| L’utente non logga perché il codice non è corretto |                          |

|                             |                          |
|-----------------------------|--------------------------|
| **ID TEST CASE**            |                          |
| TC08                        |                          |
| Email                       | yogurtmangiato@gmail.com |
| Ruolo                       | Donatore                 |
| Stato                       | N/A                      |
| Password                    | latte2012                |
| Codice                      |                          |
| **Esito atteso**            |                          |
| L’utente logga con successo |                          |

|                                                          |                       |
|----------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                         |                       |
| TC09                                                     |                       |
| Email                                                    | nannidecaro@gmail.com |
| Ruolo                                                    | Beneficiario          |
| Stato                                                    | Accettato             |
| Password                                                 | giogiu07              |
| Codice                                                   | N/A                   |
| **Esito atteso**                                         |                       |
| L’utente non logga perché il codice non è stato inserito |                       |

|                                                                                   |                       |
|-----------------------------------------------------------------------------------|-----------------------|
| **ID TEST CASE**                                                                  |                       |
| TC10                                                                              |                       |
| Email                                                                             | nannidecaro@gmail.com |
| Ruolo                                                                             | Beneficiario          |
| Stato                                                                             | Accettato             |
| Password                                                                          | giogiu07              |
| Codice                                                                            | 5437583               |
| **Esito atteso**                                                                  |                       |
| L’utente non logga perché il codice non può essere giusto contenendo troppe cifre |                       |

|                                                    |                       |
|----------------------------------------------------|-----------------------|
| **ID TEST CASE**                                   |                       |
| TC11                                               |                       |
| Email                                              | nannidecaro@gmail.com |
| Ruolo                                              | Beneficiario          |
| Stato                                              | Accettato             |
| Password                                           | giogiu07              |
| Codice                                             | 3000                  |
| **Esito atteso**                                   |                       |
| L’utente non logga perché il codice non è corretto |                       |

|                             |                       |
|-----------------------------|-----------------------|
| **ID TEST CASE**            |                       |
| TC12                        |                       |
| Email                       | nannidecaro@gmail.com |
| Ruolo                       | Beneficiario          |
| Stato                       | Accettato             |
| Password                    | giogiu07              |
| Codice                      |                       |
| **Esito atteso**            |                       |
| L’utente logga con successo |                       |

**UC04 Donazione Monetaria**

|                                                                                                                                |                  |
|--------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                              |                  |
| TC01                                                                                                                           |                  |
| **INPUT**                                                                                                                      | **VALORE**       |
| nome_ente_erogatore                                                                                                            | Caritas Salerno  |
| numero_carta                                                                                                                   | 1234567812345678 |
| scadenza                                                                                                                       | 2026-12-31       |
| cvv                                                                                                                            | 123              |
| importo                                                                                                                        | 0                |
| **OUTPUT**                                                                                                                     |                  |
| La donazione non va a buon fine perchè l’importo non è valido e il sistema mostra un messaggio di errore: “Importo non valido” |                  |

|                                                                                                                                          |                 |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **ID TEST FRAME**                                                                                                                        |                 |
| TC02                                                                                                                                     |                 |
| **INPUT**                                                                                                                                | **VALORE**      |
| nome_ente_erogatore                                                                                                                      | Caritas Salerno |
| numero_carta                                                                                                                             | 12345678        |
| scadenza                                                                                                                                 | 2026-12-31      |
| cvv                                                                                                                                      | 123             |
| importo                                                                                                                                  | 50              |
| **OUTPUT**                                                                                                                               |                 |
| La donazione non va a buon fine perchè il numero carta non è valido e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                 |

|                                                                                                                                      |                  |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                                    |                  |
| TC03                                                                                                                                 |                  |
| **INPUT**                                                                                                                            | **VALORE**       |
| nome_ente_erogatore                                                                                                                  | Caritas Salerno  |
| numero_carta                                                                                                                         | 1234567812345678 |
| scadenza                                                                                                                             | 2021-12-31       |
| cvv                                                                                                                                  | 123              |
| importo                                                                                                                              | 50               |
| **OUTPUT**                                                                                                                           |                  |
| La donazione non va a buon fine perchè la scadenza non è valida e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                  |

|                                                                                                                                 |                  |
|---------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                               |                  |
| TC04                                                                                                                            |                  |
| **INPUT**                                                                                                                       | **VALORE**       |
| nome_ente_erogatore                                                                                                             | Caritas Salerno  |
| numero_carta                                                                                                                    | 1234567812345678 |
| scadenza                                                                                                                        | 2021-12-31       |
| cvv                                                                                                                             | 12               |
| importo                                                                                                                         | 50               |
| **OUTPUT**                                                                                                                      |                  |
| La donazione non va a buon fine perchè il cvv non è idoneo e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                  |

|                                                                                                                                                        |                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                                                      |                  |
| TC05                                                                                                                                                   |                  |
| **INPUT**                                                                                                                                              | **VALORE**       |
| nome_ente_erogatore                                                                                                                                    | Ente inesistente |
| numero_carta                                                                                                                                           | 1234567812345678 |
| scadenza                                                                                                                                               | 2026-12-31       |
| cvv                                                                                                                                                    | 123              |
| importo                                                                                                                                                | 50               |
| **OUTPUT**                                                                                                                                             |                  |
| La donazione non va a buon fine perchè l’ente inserito non è presente nel db e il sistema mostra un messaggio di errore: “Ente erogatore non trovato”. |                  |

|                                                                                                                                                     |                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| **ID TEST FRAME**                                                                                                                                   |                                           |
| TC06                                                                                                                                                |                                           |
| **INPUT**                                                                                                                                           | **VALORE**                                |
| nome_ente_erogatore                                                                                                                                 | UNISA - Università degli Studi di Salerno |
| numero_carta                                                                                                                                        | 1234567812345678                          |
| scadenza                                                                                                                                            | 2026-12-31                                |
| cvv                                                                                                                                                 | 123                                       |
| importo                                                                                                                                             | 50                                        |
| **OUTPUT**                                                                                                                                          |                                           |
| La donazione non va a buon fine perchè l’IBAN dell’ente erogatore non è valido e il sistema mostra un messaggio di errore: “Transazione rifiutata”. |                                           |

|                                                                                                                                                                                                     |                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                                                                                                   |                  |
| TC08                                                                                                                                                                                                |                  |
| **INPUT**                                                                                                                                                                                           | **VALORE**       |
| nome_ente_erogatore                                                                                                                                                                                 | Caritas Salerno  |
| numero_carta                                                                                                                                                                                        | 1234567812345678 |
| scadenza                                                                                                                                                                                            | 2026-12-31       |
| cvv                                                                                                                                                                                                 | 123              |
| importo                                                                                                                                                                                             | 50               |
| **OUTPUT**                                                                                                                                                                                          |                  |
| Tramite un false imposto nel backend simuliamo un problema al servizio mail, la donazione non va a buon fine e il sistema mostra un messaggio di errore: “Donazione eseguita ma email non inviata”. |                  |

|                                                                                                                                             |                  |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **ID TEST FRAME**                                                                                                                           |                  |
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
| La segnalazione non va a buon fine perché l’indirizzo è mancante e il sistema mostra un messaggio di errore: “Dati mancanti: latitudine, longitudine e indirizzo sono obbligatori”. |                            |

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

**UC 09 Storico e reportistica**

| **ID TEST FRAME**                                                  |                |
|--------------------------------------------------------------------|----------------|
| TC 01                                                              |                |
| **INPUT**                                                          | **VALORE**     |
| E-Mail                                                             | N/A            |
| Password                                                           | N/A            |
| OTP                                                                | N/A            |
| Ruolo                                                              | N/A            |
| Accesso al profilo                                                 | Non effettuato |
| **Output**                                                         |                |
| L’accesso all’endpoint viene negato e l’utente viene reindirizzato |                |

| **ID TEST FRAME**                                                                                                          |                        |
|----------------------------------------------------------------------------------------------------------------------------|------------------------|
| TC 02                                                                                                                      |                        |
| **INPUT**                                                                                                                  | **VALORE**             |
| E-Mail                                                                                                                     | Nico.rossi@example.com |
| Password                                                                                                                   | password123            |
| Ruolo                                                                                                                      | Beneficiario           |
| Prenotazioni                                                                                                               | No                     |
| **Output**                                                                                                                 |                        |
| Il PDF viene generato con successo e al suo interno non è presente nessun dato perché l’utente non ha nessuna prenotazione |                        |

| **ID TEST FRAME**                                                                                                                                                                 |                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| TC 03                                                                                                                                                                             |                        |
| **INPUT**                                                                                                                                                                         | **VALORE**             |
| E-Mail                                                                                                                                                                            | Nico.rossi@example.com |
| Password                                                                                                                                                                          | password123            |
| Ruolo                                                                                                                                                                             | Beneficiario           |
| Prenotazioni                                                                                                                                                                      | Si                     |
| **Output**                                                                                                                                                                        |                        |
| Il PDF viene generato con successo e al suo interno è presente la stampa dei beni prenotati con le loro informazioni, quali: Nome del bene, Punto di Distribuzione, Data e Stato. |                        |

| **ID TEST FRAME**                                                                                                          |                     |
|----------------------------------------------------------------------------------------------------------------------------|---------------------|
| TC 04                                                                                                                      |                     |
| **INPUT**                                                                                                                  | **VALORE**          |
| E-Mail                                                                                                                     | privato@example.com |
| Password                                                                                                                   | password123         |
| Ruolo                                                                                                                      | Donatore            |
| Donazioni                                                                                                                  | N/A                 |
| **Output**                                                                                                                 |                     |
| Il PDF viene generato con successo e al suo interno non è presente nessun dato perché l’utente non ha nessuna prenotazione |                     |

| **ID TEST FRAME**                                                                                                                             |                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| TC 05                                                                                                                                         |                     |
| **INPUT**                                                                                                                                     | **VALORE**          |
| E-Mail                                                                                                                                        | privato@example.com |
| Password                                                                                                                                      | password123         |
| Ruolo                                                                                                                                         | Donatore            |
| Donazioni                                                                                                                                     | SI                  |
| **Output**                                                                                                                                    |                     |
| Il PDF viene generato con successo e al suo interno è presente la stampa delle donazioni con le loro informazioni, quali Importo, Ente e Data |                     |

| **ID TEST FRAME**                                                                                                          |                |
|----------------------------------------------------------------------------------------------------------------------------|----------------|
| TC 06                                                                                                                      |                |
| **INPUT**                                                                                                                  | **VALORE**     |
| E-Mail                                                                                                                     | ente@unisa.it  |
| Password                                                                                                                   | password123    |
| Ruolo                                                                                                                      | Ente Erogatore |
| Prenotazioni e Donazioni                                                                                                   | N/A            |
| **Output**                                                                                                                 |                |
| Il PDF viene generato con successo e al suo interno non è presente nessun dato perché l’utente non ha nessuna prenotazione |                |

| **ID TEST FRAME**                                                                                                                                                                                                          |                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| TC 07                                                                                                                                                                                                                      |                |
| **INPUT**                                                                                                                                                                                                                  | **VALORE**     |
| E-Mail                                                                                                                                                                                                                     | ente@unisa.it  |
| Password                                                                                                                                                                                                                   | password123    |
| Ruolo                                                                                                                                                                                                                      | Ente Erogatore |
| Prenotazioni e Donazioni                                                                                                                                                                                                   | SI             |
| **Output**                                                                                                                                                                                                                 |                |
| Il PDF viene generato con successo e al suo interno è presente la stampa delle prenotazioni e delle donazioni con le loro rispettive informazioni, rispettivamente Bene, Donatore e Data insieme a Importo Donatore e Data |                |

**UC11 Filtraggio della mappa**

|                                                                                                                                           |                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| **ID TEST CASE**                                                                                                                          |                                  |
| TC01                                                                                                                                      |                                  |
| **INPUT**                                                                                                                                 | **VALORE**                       |
| categoria                                                                                                                                 | (nessuna - "Tutte le categorie") |
| **OUTPUT**                                                                                                                                |                                  |
| Il sistema restituisce tutti i punti di distribuzione presenti nel database senza applicare alcun filtro. La mappa mostra tutti i marker. |                                  |

|                                                                                                                                                        |            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **ID TEST CASE**                                                                                                                                       |            |
| TC02                                                                                                                                                   |            |
| **INPUT**                                                                                                                                              | **VALORE** |
| categoria                                                                                                                                              | Alimentari |
| **OUTPUT**                                                                                                                                             |            |
| Il sistema restituisce solo i punti di distribuzione che contengono beni di macrocategoria "Alimentari". La mappa mostra solo i marker corrispondenti. |            |

|                                                                                                                                                                                                               |             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| **ID TEST CASE**                                                                                                                                                                                              |             |
| TC03                                                                                                                                                                                                          |             |
| **INPUT**                                                                                                                                                                                                     | **VALORE**  |
| categoria                                                                                                                                                                                                     | Elettronica |
| **OUTPUT**                                                                                                                                                                                                    |             |
| Il sistema esegue la query con JOIN ma non trova nessun punto di distribuzione con beni della categoria "elettronica" (inesistente). La risposta contiene una lista vuota e la mappa non mostra alcun marker. |             |

|                                                                                                                                                               |            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **ID TEST CASE**                                                                                                                                              |            |
| TC04                                                                                                                                                          |            |
| **INPUT**                                                                                                                                                     | **VALORE** |
| categoria                                                                                                                                                     | Medicinali |
| **OUTPUT**                                                                                                                                                    |            |
| Il sistema esegue la query ma nessun punto di distribuzione attivo ha beni di categoria "Medicinali" in questo momento. La risposta contiene una lista vuota. |            |

|                                                                                                                                                                                                                            |                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| **ID TEST CASE**                                                                                                                                                                                                           |                                                   |
| TC05                                                                                                                                                                                                                       |                                                   |
| **INPUT**                                                                                                                                                                                                                  | **VALORE**                                        |
| categoria                                                                                                                                                                                                                  | Alimentari                                        |
| stato_schema                                                                                                                                                                                                               | Tabelle sotto_categorie e macro_categorie ASSENTI |
| **OUTPUT**                                                                                                                                                                                                                 |                                                   |
| Il sistema rileva che le tabelle delle categorie non esistono nello schema, ignora il filtro per categoria e restituisce tutti i punti di distribuzione. La risposta include meta.categoria_ignored = true con la ragione. |                                                   |

|                                                                                                                                      |                                         |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| **ID TEST CASE**                                                                                                                     |                                         |
| TC06                                                                                                                                 |                                         |
| **INPUT**                                                                                                                            | **VALORE**                              |
| categoria                                                                                                                            | Alimentari                              |
| stato_schema                                                                                                                         | Connessione al database non disponibile |
| **OUTPUT**                                                                                                                           |                                         |
| Il sistema non riesce a connettersi al database e restituisce un errore 500 con messaggio "db_error". La mappa non viene aggiornata. |                                         |
