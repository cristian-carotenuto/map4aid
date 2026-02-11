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

# 

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

**UC04 Donazione Monetaria**

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

## 

## 

## 

## 

## 

## 

## 

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

**UC04 Donazione Monetaria**

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

Per ciascun test case vengono definiti:

- gli input necessari all’esecuzione della funzionalità a cui il test fa riferimento,

- i valori assegnati a ciascun input, scelti sulla base delle combinazioni individuate tramite tecnica Category Partition,

- l’oracolo, ovvero il risultato atteso dal sistema a fronte degli input specificati**.**

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

**UC04 Donazione Monetaria**

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
