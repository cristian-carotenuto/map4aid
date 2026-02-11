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

Il sistema tenta di inviare una email di segnalazione  a ciascun ente con i dettagli della posizione.

Al termine, il sistema conferma l'avvenuta segnalazione all'utente.

# 

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
<h2 id="section-6"></h2></td>
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

## 

## 

## 

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

Per ciascun test case vengono definiti:

- gli input necessari all’esecuzione della funzionalità a cui il test fa riferimento,

- i valori assegnati a ciascun input, scelti sulla base delle combinazioni individuate tramite tecnica Category Partition,

- l’oracolo, ovvero il risultato atteso dal sistema a fronte degli input specificati**.**

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
