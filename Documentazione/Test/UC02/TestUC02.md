<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*CATEGORY PARTITION TESTING \#UC02*

**Login**

Un utente registrato accede al sistema inserendo email e password.

Il sistema verifica che le credenziali siano corrette e che l’utente non sia già autenticato.

Se la verifica ha esito positivo, il sistema genera un codice OTP e lo invia all’indirizzo email dell’utente.

L’utente inserisce il codice OTP ricevuto.

Il sistema confronta il codice con quello generato e, se valido, completa l’autenticazione creando la sessione utente.

Per gli utenti di tipo beneficiario, l’accesso è consentito solo se l’account risulta approvato da un amministratore.

Se l’OTP è errato, mancante o non più valido, il login non viene completato.

# 

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

## 

## 

## 

## 

## 

## 

| **Test case** | **FM** | **RG** | **CR** | **BN** | **AC** | **LN**   | **CT** | **Esito atteso**                  |
|---------------|--------|--------|--------|--------|--------|----------|--------|-----------------------------------|
| **TC1**       | ERR    | **-**  | **-**  | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Errore formattazione   |
| **TC2**       | FM_OK  | ERR    | **-**  | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Email non registrata   |
| **TC3**       | FM_OK  | RG_OK  | ERR    | **-**  | **-**  | **-**    | **-**  | **\[ERR\]**Credenziali non valide |
| **TC4**       | FM_OK  | RG_OK  | OK_CR  | IS_BN  | ERR    | **-**    | **-**  | **\[ERR\]**Account non accettato  |
| **TC5**       | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | ERR(LN1) | **-**  | **\[ERR\]**Codice mancante        |
| **TC6**       | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | ERR(LN2) | **-**  | **\[ERR\]**Codice troppo lungo    |
| **TC7**       | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | LN_OK    | ERR    | **\[ERR\]**Codice non valido      |
| **TC8**       | FM_OK  | RG_OK  | OK_CR  | NOT_BN | **-**  | LN_OK    | CT_OK  | Login completato                  |
| **TC9**       | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | ERR(LN1) | **-**  | **\[ERR\]**Codice mancante        |
| **TC10**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | ERR(LN2) | **-**  | **\[ERR\]**Codice troppo lungo    |
| **TC10**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | LN_OK    | ERR    | **\[ERR\]**Codice non valido      |
| **TC11**      | FM_OK  | RG_OK  | OK_CR  | IS_BN  | AC_OK  | LN_OK    | CT_OK  | Login completato                  |
