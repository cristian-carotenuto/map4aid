**REQUIREMENTS ANALYSIS DOCUMENT**

PROGETTISTI: Luciano Corvino, Cristian Carotenuto, Emilio Maione, Vito Francesco Maistrini, Giovanni De Caro, Gabriele Milone, Carlo Antonio Caserta, Nicola Luciano, Giovanni Esposito, Maria Chiara Gregorio, Riccardo Di Girolamo.

PROJECT MANAJER: Gabriele D'Auria, Antonio Botticchio

**\#1 CASI D'USO**

**CASO D’USO \#1 (REGISTRAZIONE)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 9%" />
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
<td colspan="4">Utente non registrato</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4">Sistema, servizio di posta elettronica</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente non possiede un account esistente. La connessione è protetta (HTTPS)</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente dispone di un account valido e può autenticarsi</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4"><p>Il sistema mostra un messaggio di errore:</p>
<ul>
<li><blockquote>
<p>Email già registrata</p>
</blockquote></li>
<li><blockquote>
<p>Password troppo debole</p>
</blockquote></li>
<li><blockquote>
<p>CF/P.iva non valido</p>
</blockquote></li>
</ul>
<p>L'utente rimane sulla pagina di registrazione (con i dati inseriti se possibile,</p>
<p>per correzione), dove viene richiesto un nuovo inserimento di dati</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">?/?</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Extension point</strong></td>
<td colspan="4">na</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">na</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente non registrato</p>
</blockquote></td>
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
<td colspan="2"><blockquote>
<p>Attore:</p>
</blockquote></td>
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
<p>Donatore(?), che avendo registrato la sua attività (verificata), è abilitato</p>
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
<td colspan="2"><strong>2.1</strong></td>
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
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4"><p>Il sistema notifica con un messaggio di errore “Password troppo debole” il fatto che la</p>
<p>password inserita non è sicura e richiede la ricompilazione del campo in questione.</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>…</strong></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> CF/P.iva non valido</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.2</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “CF/P.iva non valido” il fatto che i campi non risultano validi secondo i controlli formali</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">Nessuna informazione deve essere tracciata oltre quanto strettamente necessario (privacy by design</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">Tutti i dati sensibili (es. allergie, documenti medici) devono essere crittografati a riposo con AES-256</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4">Il modulo è accessibile solo tramite HTTPS con certificato valido.</td>
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
<col style="width: 12%" />
<col style="width: 8%" />
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
<td colspan="4">Utente registrato</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4">Sistema, servizio di posta elettronica</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente possiede un account valide con credenziali attive e vuole autenticarsi</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Sessione creata. L’utente ha accesso alle funzionalità.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4"><p>Il sistema mostra un messaggio di errore:</p>
<ul>
<li><blockquote>
<p>Password errata e/o email non registrata.</p>
</blockquote></li>
</ul>
<p>L'utente rimane sulla pagina di login (con i dati inseriti se possibile,</p>
<p>per correzione), dove viene richiesto un nuovo inserimento di dati.</p></td>
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
<td colspan="4">na</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">na</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente registrato</p>
</blockquote></td>
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
<td colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente registrato</p>
</blockquote></td>
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
<td colspan="2"><strong>Attore:</strong></td>
<td colspan="4">L’utente usa il link inviato per mail per accedere al form di reset</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4"><p>Il sistema propone il form per inserire la nuova password, quando la password inserita</p>
<p>supera gli standard di sicurezza, la password è correttamente modificata, e l’utente</p>
<p>riceve una notifica a schermo. Redirect al login.</p></td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> L’utente clicca su “Email dimenticata”</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.2</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Alla richiesta dell’utente del reset della mail, il Sistema invia un messaggio al numero di telefono associato, contenente un codice temporaneo ( OTP ) per sessione</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"><strong>Attore:</strong></td>
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
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Password errata</td>
</tr>
<tr class="even">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema notifica con un messaggio di errore “Email o password errate”, il fatto che i valori inseriti nei campi disponibili non risultano validi.</td>
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
<td colspan="4">about 4</td>
<td colspan="4">Successivamente sarà possibile implementare l'utilizzo dell’Autenticazione a due fattori ( 2FA ), richiesta solo dopo il riconoscimento dell’autenticazione da parte del Sistema.</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">Utilizzo di HTTPS con certificato valido garantendo la crittografia end-to-end dei dati trasmessi durante la fase di login.</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
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
<td colspan="4"><p><strong>Cittadino beneficiario (registrato, non registrato, donatore)</strong></p>
<p>Interessato a donare per beneficenza una certa somma di denaro</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione monetaria dal cittadino</p></td>
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
<p>Cittadino:</p>
</blockquote></td>
<td colspan="5">clicca su “Donazione monetaria”</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>mostra un modulo da compilare con informazioni su ente e metodo di pagamento</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>Cittadino:</p>
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
<td colspan="5"><em>Invia la donazione all’ente erogatore scelto</em></td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Invia una notifica di successo al cittadino</em></td>
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
<p><em>UC#04</em></p></td>
<td rowspan="3"><strong>DONAZIONE DI BENI</strong></td>
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
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>L’utente registrato può donare beni materiali a enti specifici, in base alla propria categoria di donatore. Compila un modulo dedicato con i dettagli dei beni, che viene inviato all’ente per la validazione. In caso di approvazione, l’ente comunica al donatore le istruzioni per il ritiro.</em></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Utente (registrato o loggato)</strong></p>
<p><strong>Ente ricevente</strong></p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><strong>Sistema</strong></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4"><ul>
<li><p>L’utente deve essere registrato o loggato come donatore</p></li>
<li><p>L'utente deve essere assegnato ad una determinata categoria di donazione</p></li>
<li><p>L’utente deve compilare un modulo, il quale varia a seconda della tipologia di donazione, ed inviarlo</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L’ente convalida i dati forniti e invia una email al donatore con informazioni sul ritiro dei beni da parte dell’ente</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">L’ente rifiuta la richiesta la richiesta di donazione da parte dell’utente</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Media</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Medio-bassa (parlarne)</td>
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
<p>Cittadino registrato:</p>
</blockquote></td>
<td colspan="5">Compila il modulo per la donazione specifica (parlarne)</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Inoltre il modulo all’ente</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Riceve e valida i dati del modulo</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></td>
<td colspan="5">Invia una mail sulle informazioni del punto di ritiro del bene</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><em>Salva la donazione effettuata</em></td>
</tr>
<tr class="even">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Ente rifiuta la donazione</td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Cittadino registrato:</p>
</blockquote></td>
<td colspan="5">Compila il modulo per la donazione specifica (parlarne)</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Inoltre il modulo all’ente</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>L’ente determina come negativa la richiesta e rifiuta</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></td>
<td colspan="5">Invia una mail con le motivazioni di rifiuto</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Errori (DB o Rete)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Timeout o errore durante l’invio del modulo</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Note</strong></td>
<td colspan="2"></td>
<td colspan="4">parlare dei punti in cui si hanno domande</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">Requisito n.f.#2 – Persistenza dei dati</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">Requisito n.f #5 - Protezione dei Dati e Autenticazione</td>
</tr>
</tbody>
</table>

**CASO D'USO \#5: (PRENOTAZIONE RITIRO BENI DI PRIMA NECESSITÀ)**

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
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
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>L'utente registrato seleziona una posizione sulla mappa tra quelle disponibili e ha la possibilità di selezionare ciò di cui ha bisogno e poi di prenotare uno slot orario nel quale potrà andare nel punto di ritiro scelto e ritirare i beni.</em></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><p><strong>Beneficiario (si può generalizzare a Utente registrato).</strong></p>
<p>Interessato a prenotare i beni di suo interesse</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente registrato clicca su un punto della mappa per il quale ha interesse e desidera utilizzare per ritirare i beni.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente riesce con successo a prenotare lo slot orario nel quale andare a ritirare i beni prenotati.</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">L'utente decide di non confermare la prenotazione (in caso di fallimento si retrocede di uno step ma non si termina il caso d'uso)</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Alta, è fondamentale per l'utente poter prenotare il ritiro dei beni.</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Alta, dovrebbe essere un’operazione comune per gli utenti beneficiari.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Flusso di Eventi Principale/Main Scenario</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td colspan="2"><blockquote>
<p><strong>Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>L’utente visualizza i punti di ritiro disponibili sulla mappa da cui effettuare l’operazione di prenotazione e seleziona il punto desiderato.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Il sistema modifica l'interfaccia e mostra all'utente la selezione dei beni disponibili nel punto di ritiro selezionato.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="2"><blockquote>
<p><strong>Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5">L'utente seleziona i beni che desidera e invia una conferma al sistema.</td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema mostra gli slot orari disponibili per quel punto di ritiro.</td>
</tr>
<tr class="even">
<td>5</td>
<td colspan="2"><blockquote>
<p><strong>Beneficiario:</strong></p>
</blockquote></td>
<td colspan="5">L'utente seleziona lo slot orario che preferisce e invia la prenotazione dello slot orario al sistema.</td>
</tr>
<tr class="odd">
<td>6</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema aggiorna gli slot orari disponibili ed elimina da essi quello appena prenotato dall'utente.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>I Scenario Alternativo:</strong> primo scenario alternativo</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>1.1</strong></td>
<td colspan="2"><strong>Beneficiario:</strong></td>
<td colspan="4">L'utente può decidere in una qualsiasi delle fasi da 1 a 5 di annullare la prenotazione, questo senza arrecare problemi al sistema che non aggiorna i dati fino alla fase 6, ossia dopo la conferma finale dell'utente.</td>
</tr>
</tbody>
</table>

**\#6: Segnalazione di un punto di bisogno sulla mappa**

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 35%" />
<col style="width: 17%" />
<col style="width: 0%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="8" rowspan="3"><p><strong>Identificativo</strong></p>
<p>UC #06</p></td>
<td colspan="4" rowspan="3"><em>Segnalazione di un punto di bisogno sulla mappa</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>17/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.001</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Gregorio Maria Chiara</em></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Descrizione</strong></td>
<td colspan="7">L’utente segnala sulla mappa un’area o un punto in cui ritiene necessario attivare un punto di raccolta o distribuzione (ad esempio zone con famiglie in difficoltà o situazioni di emergenza). La segnalazione comprende posizione, tipologia del bisogno e descrizione sintetica. Il sistema invia la segnalazione agli enti amministratori, che ne verificheranno la validità per approvarla o respingerla.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Attore Principale</strong></td>
<td colspan="7"><p><strong>Cittadino beneficiario (non autenticato o registrato)</strong></p>
<p>Segnalare un’area di criticità e permettere al sistema di attivare un nuovo punto di aiuto.</p></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Attori secondari</strong></td>
<td colspan="7"><p><strong>Amministratore di sistema / Ente erogatore</strong></p>
<p>Ricevere le segnalazioni, verificarle e decidere se attivare un nuovo punto di supporto.</p></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Entry Condition</strong></td>
<td colspan="7"><p>L’utente visualizza la mappa.</p>
<p>L’utente seleziona l’opzione “Segnala punto di bisogno”.</p></td>
</tr>
<tr class="even">
<td colspan="8"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="7"><p>La segnalazione è registrata nel sistema.</p>
<p>La segnalazione è inoltrata agli enti amministratori.</p></td>
</tr>
<tr class="odd">
<td colspan="8"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="7"><p>La segnalazione non viene inviata per errore tecnico o per dati mancanti.</p>
<p>L’utente riceve un messaggio di errore.</p></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Rilevanza/User Priority</strong></td>
<td colspan="7">Medio/alta – consente di individuare aree critiche non ancora mappate.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Frequenza stimata</strong></td>
<td colspan="7">1-10/giorno, variabile a seconda delle situazioni territoriali.</td>
</tr>
<tr class="even">
<td colspan="15"><strong>Flusso di Eventi Principale/Main Scenario</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="5"><blockquote>
<p>Attore:</p>
</blockquote></td>
<td colspan="9"><blockquote>
<p>STEP 1. Seleziona sulla mappa l’opzione <em>“Segnala punto di bisogno”</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="5"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="9"><blockquote>
<p>STEP 2. Mostra il modulo di segnalazione con i campi richiesti (posizione, tipologia bisogno, descrizione).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="5"><blockquote>
<p>Attore:</p>
</blockquote></td>
<td colspan="9">STEP 3. Inserisce i dati richiesti e seleziona sulla mappa la posizione del punto di bisogno.</td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="5"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="9">STEP 4. Valida i dati inseriti (tutti i campi obbligatori compilati).</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="5"><blockquote>
<p>Attore:</p>
</blockquote></td>
<td colspan="9">STEP 5. Conferma l’invio della segnalazione.</td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="5"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="9">STEP 6. Registra la segnalazione e la inoltra agli enti amministratori.</td>
</tr>
<tr class="odd">
<td>7</td>
<td colspan="5"><blockquote>
<p>Attore:</p>
</blockquote></td>
<td colspan="9">STEP 7. Visualizza il messaggio <em>“Segnalazione inviata correttamente”</em>.</td>
</tr>
<tr class="even">
<td colspan="15"></td>
</tr>
<tr class="odd">
<td colspan="15"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Posizione rilevata automaticamente (GPS attivo)</td>
</tr>
<tr class="even">
<td colspan="5"><strong>2.1</strong></td>
<td colspan="3"><strong>Sistema:</strong></td>
<td colspan="7">Se l’utente autorizza la geolocalizzazione, il sistema propone automaticamente la posizione corrente come punto di bisogno.</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>2.2</strong></td>
<td colspan="3"><strong>Attore:</strong></td>
<td colspan="7">Conferma o modifica manualmente la posizione proposta.</td>
</tr>
<tr class="even">
<td colspan="15"></td>
</tr>
<tr class="odd">
<td colspan="15"><strong>II Scenario Alternativo</strong>: L’utente seleziona la posizione attraverso indirizzo</td>
</tr>
<tr class="even">
<td colspan="3"><strong>2.3</strong></td>
<td colspan="6"><strong>Attore:</strong></td>
<td colspan="6">Inserisce un indirizzo manualmente invece di cliccare sulla mappa.</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>2.4</strong></td>
<td colspan="6"><strong>Sistema:</strong></td>
<td colspan="6">Converte l’indirizzo in coordinate (geocoding) e mostra l’anteprima sulla mappa.</td>
</tr>
<tr class="even">
<td colspan="15"></td>
</tr>
<tr class="odd">
<td colspan="15"><strong>III Scenario/Flusso di eventi Alternativo:</strong> Utente autenticato</td>
</tr>
<tr class="even">
<td colspan="5"><strong>3.1</strong></td>
<td colspan="3"><strong>Sistema:</strong></td>
<td colspan="7">Se l’utente è registrato, precompila automaticamente i dati opzionali associati al profilo (es. e-mail per feedback).</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
<td colspan="7"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>IV Scenario/Flusso di eventi Alternativo:</strong> Tipologia di bisogno non presente nelle categorie</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>3.2</strong></td>
<td colspan="5"><strong>Attore:</strong></td>
<td colspan="7">Non trova una tipologia coerente nell’elenco.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>3.3</strong></td>
<td colspan="5"><strong>Sistema:</strong></td>
<td colspan="7">Mostra un campo “Altro (specificare)” abilitando l’inserimento di testo libero.</td>
</tr>
<tr class="odd">
<td colspan="15"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>V Scenario Alternativo:</strong> Inserimento di allegati</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>3.4</strong></td>
<td colspan="3"><strong>Attore:</strong></td>
<td colspan="8">Aggiunge una foto o un file come supporto informativo.</td>
</tr>
<tr class="even">
<td colspan="4"><strong>3.5</strong></td>
<td colspan="3"><strong>Sistema:</strong></td>
<td colspan="8">Valida formato e dimensione dell’allegato prima dell’invio.</td>
</tr>
<tr class="odd">
<td colspan="15"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>VI Scenario Alternativo</strong>: Utente non autenticato lascia contatto</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>5.1</strong></td>
<td colspan="5"><strong>Sistema:</strong></td>
<td colspan="7">Se l’utente non è autenticato, propone un campo opzionale “Inserisci email per essere ricontattato”.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>5.2</strong></td>
<td colspan="5"><strong>Attore:</strong></td>
<td colspan="7">Inserisce un contatto oppure prosegue senza fornire nulla.</td>
</tr>
<tr class="odd">
<td colspan="15"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Dati mancanti</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>2.1</strong></td>
<td colspan="3"><strong>Sistema:</strong></td>
<td colspan="7">Indica quali campi obbligatori non sono stati compilati e richiede correzione.</td>
</tr>
<tr class="even">
<td colspan="15"></td>
</tr>
<tr class="odd">
<td colspan="15"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Allegato non valido</td>
</tr>
<tr class="even">
<td colspan="3"><strong>3.7</strong></td>
<td colspan="7"><strong>Sistema:</strong></td>
<td colspan="5">Se il file allegato è troppo grande o in un formato non consentito (es. .exe), blocca l’invio.<br />
Mostra: <em>“Formato o dimensione del file non supportati.”</em></td>
</tr>
<tr class="odd">
<td colspan="15"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>III Scenario/Flusso di eventi di ERRORE:</strong> Utente prova a segnalare un punto già segnalato</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>3.8</strong></td>
<td colspan="9"><strong>Sistema:</strong></td>
<td colspan="4">Individua che la stessa posizione è già stata segnalata recentemente da altri utenti.<br />
Propone all’utente:<br />
<em>“Questa area è già stata segnalata. Vuoi comunque inviare una nuova segnalazione?”</em></td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.9</strong></td>
<td colspan="9"><strong>Attore:</strong></td>
<td colspan="4">Conferma → la segnalazione prosegue normalmente (ritorna al passo 6).<br />
Annulla → la procedura termina.</td>
</tr>
<tr class="odd">
<td colspan="15"></td>
</tr>
<tr class="even">
<td colspan="15"><strong>IV Scenario/Flusso di eventi di ERRORE:</strong> Problema di rete/server</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>6.1</strong></td>
<td colspan="3"><strong>Sistema:</strong></td>
<td colspan="7">Mostra il messaggio <em>“Errore durante l’invio della segnalazione. Riprovare più tardi.”</em> senza salvare i dati.</td>
</tr>
<tr class="even">
<td colspan="8"></td>
<td colspan="7"></td>
</tr>
<tr class="odd">
<td colspan="15"><strong>Note</strong></td>
</tr>
<tr class="even">
<td colspan="8"></td>
<td colspan="7">Le segnalazioni non sono immediatamente visibili sulla mappa fino ad approvazione degli enti.</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
<td colspan="7"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>Special Requirements</strong></td>
<td colspan="7"></td>
</tr>
<tr class="odd">
<td colspan="8"></td>
<td colspan="7">La selezione della posizione deve essere semplice e precisa (es. click sulla mappa).</td>
</tr>
<tr class="even">
<td colspan="8"></td>
<td colspan="7">Le segnalazioni devono essere memorizzate in modo sicuro e accessibile solo agli enti autorizzati.</td>
</tr>
<tr class="odd">
<td colspan="8"></td>
<td colspan="7">Il sistema deve gestire un eventuale alto numero di segnalazioni contemporanee.</td>
</tr>
<tr class="even">
<td colspan="8"></td>
<td colspan="7">Deve essere rispettata la privacy (no dati sensibili non necessari).</td>
</tr>
</tbody>
</table>

**CASO D’USO \#7 (GESTIONE E AGGIORNAMENTO SCORTE)**

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 37%" />
<col style="width: 18%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
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
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4"><em>P</em>ermette agli enti erogatori di monitorare in tempo reale le scorte di beni disponibili nei propri punti di raccolta o distribuzione tramite una specifica interfaccia. Il sistema aggiorna automaticamente le scorte in base a due eventi principali:<br />
1. Aumento della quantità, quando un donatore esterno effettua una donazione (registrata tramite il sistema), oppure quando l'ente modifica la quantità di un bene o ne aggiunge uno non presente prima(la riduzione manuale non è consentita, per garantire tracciabilità e coerenza).<br />
2. Riduzione della quantità quando un bene viene prenotato ,e poi ritirato presso un punto di ritiro. (aggiornamento tramite automazione di sistema).</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4">Ente erogatore</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4">Sistema, Cittadino beneficiario, Utente donatore, Database</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">Aggiornamento scorte di beni</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Scorte aggiornate correttamente.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">Scorte non aggiornate. Tentata modifica in negativo di scorte da parte dell’ente.</td>
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
<td colspan="4"><strong>Generalization of</strong></td>
<td colspan="4">na.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></td>
</tr>
<tr class="even">
<td>1</td>
<td colspan="2"><blockquote>
<p>Attore: Ente erogatore</p>
</blockquote></td>
<td colspan="5"><p>Ente erogatore si logga con successo (UC_login) alla piattaforma, e accede alla dashboard dove è mostrata l’attuale traccia delle scorte</p>
<p>Ha a disposizione sull’interfaccia tutti i punti di ritiro associati con il loro inventario, e può sia incrementare il numero di beni sia aggiungerne di nuovi</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Mostra tramite interfaccia la gestione scorte nei vari punti di ritiro associati</td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="2"><blockquote>
<p>Attore:</p>
<p>Ente erogatore</p>
</blockquote></td>
<td colspan="5">Modifica quantità di un bene esistente in un determinato punto di ritiro (non ci occupiamo della logica dietro la consegna del nuovo bene incrementato)</td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">Il sistema aggiorna il database per tenere traccia di permanenza dell’aggiornamento, e di conseguenza l’interfaccia utente. Scorte e interfaccia utente aggiornate.</td>
</tr>
<tr class="even">
<td colspan="8">…</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Donazione di bene da utente donatore (UC_donazione bene)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>2.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema rileva una donazione di un bene all’ente da parte di un utente donatore<br />
Il sistema aggiorna le scorte del punto di ritiro associato alla ricezione di quel bene, e di conseguenza l’interfaccia utente.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> Prenotazione di un bene da cittadino beneficiario (UC_prenotazione bene)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.2</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema rileva la prenotazione di un bene in un determinato punto di ritiro.<br />
Il sistema aggiorna le scorte di quel punto di ritiro congelando il bene richiesto fino al ritiro, aggiornando dashboard e tenendo traccia delle scorte.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Aggiunta di un nuovo bene</td>
</tr>
<tr class="even">
<td colspan="2"><strong>3.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Il sistema rileva un nuovo bene allocato in un determinato punto di ritiro dall’ente.<br />
Il sistema provvede ad aggiornare le scorte relative a quel punto, aggiornare la persistenza su db e aggiornare interfaccia utente (dashboard)</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Errori ( DB o Rete )</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Timeout o errore durante l’aggiornamento ( per mancata connessione al DB o alla Rete )</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Note</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">n.f.#2 – Persistenza dei dati</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">n.f.#3 – Tassonomia gerarchica</td>
</tr>
<tr class="even">
<td colspan="4"></td>
<td colspan="4">n.f.#5 – Protezione dei dati e autenticazione</td>
</tr>
</tbody>
</table>

**CASO D’USO \#8 (SISTEMA DI NOTIFICHE E AVVISI)**

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 36%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#8</em></p></td>
<td rowspan="3">Sistema di Notifiche e Avvisi</td>
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
<td colspan="4"><strong>Descrizione</strong></td>
<td colspan="4">Il sistema invia notifiche automatiche a utenti ed enti in caso di eventi rilevanti, come disponibilità di beni compatibili o scadenze di ritiro. Le comunicazioni vengono recapitate tramite email o tramite l’area notifiche interna della piattaforma.</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Attore Principale</strong></td>
<td colspan="4"><strong>Sistema</strong></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Utente (registrato o loggato)</strong></p>
<p><strong>Ente donatore</strong></p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4"><ul>
<li><p>Il sistema invia un messaggio sulle scadenze di prenotazioni non ritirate o sulla disponibilità di nuovi beni compatibili con le preferenze dell’utente o compatibili con le patologie inserite.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">Il sistema invia una notifica attraverso una mail o un’area notifiche interna alla piattaforma</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">La notifica non viene inviata per un errore del sistema</td>
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
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO I</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Cittadino registrato:</p>
</blockquote></td>
<td colspan="5">effettua una prenotazione</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>ente donatore:</p>
</blockquote></td>
<td colspan="5">non conferma il ritiro del pacco</td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5">invia una notifica di scadenza della prenotazione</td>
</tr>
<tr class="even">
<td colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO II</span></strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>ente donatore:</p>
</blockquote></td>
<td colspan="5">Aggiorna le disponibilità dei beni</td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>invia una notifica a chi è interessato alla categoria del bene</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Errori (Rete)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>4.1</strong></td>
<td colspan="2"><strong>Sistema:</strong></td>
<td colspan="4">Timeout o errore durante l’invio della notifica</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Note</strong></td>
<td colspan="2"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Special Requirements</strong></td>
<td colspan="4">Requisito n.f.#2 – Persistenza dei dati</td>
</tr>
<tr class="odd">
<td colspan="4"></td>
<td colspan="4">Requisito n.f #5 - Protezione dei Dati e Autenticazione</td>
</tr>
</tbody>
</table>

**\#9: (STORICO ATTIVITÀ E REPORTISTICA)**

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
<td rowspan="3"><em><strong>Storico attività e reportistica</strong></em></td>
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
<td colspan="4"><p><strong>Donatore, Beneficiario, Ente (3 attori, o generalizzazione in 1 solo attore “Utente”),</strong></p>
<p>L'attore è interessato a visualizzare il proprio storico ordini</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>Attori secondari</strong></td>
<td colspan="4"><p><strong>Clock</strong></p>
<p>Attore non umano che gestisce passivamente i report settimanali mensili e annuali.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Entry Condition</strong></td>
<td colspan="4">L'utente accede alla specifica area dove gli è consentito visualizzare, filtrare per periodo o stampare i PDF forniti dal sistema.</td>
</tr>
<tr class="even">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></td>
<td colspan="4">L'utente visualizza o stampa il PDF di suo interesse.</td>
</tr>
<tr class="odd">
<td colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></td>
<td colspan="4">L'utente tenta di accedere all'area dei PDF senza essere loggato (si potrebbe far sì che per gli utenti non loggati il collegamento all'area non compaia).</td>
</tr>
<tr class="even">
<td colspan="4"><strong>Rilevanza/User Priority</strong></td>
<td colspan="4">Medio/Bassa non è fondamentale per il funzionamento basilare del sistema</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Frequenza stimata</strong></td>
<td colspan="4">Bassa-Media, verrà maggiormente eseguita dagli enti una volta a settimana o più raramente</td>
</tr>
<tr class="even">
<td colspan="8"><strong>Flusso di Eventi Principale/Main Scenario</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p><strong>Attore:</strong></p>
</blockquote></td>
<td colspan="5">L'Utente (Generalizzazione) Accede all'area dove è possibile visualizzare i vari PDF</td>
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
<p><strong>Attore:</strong></p>
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
<p><strong>Attore:</strong></p>
</blockquote></td>
<td colspan="5">L'utente decide se stampare il PDF o rimanere nella visualizzazione desktop.</td>
</tr>
<tr class="even">
<td colspan="8"><strong>II Scenario: secondo</strong> scenario</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>1</strong></td>
<td colspan="2"><strong>Clock:</strong></td>
<td colspan="4">Periodicamente il Clock informa il sistema che è necessario aggiornare il PDF delle attività dell'utente presente nel database</td>
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
<td colspan="4"><p><strong>Cittadino beneficiario (registrato)</strong></p>
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
<li><p>Il cittadino deve essere registrato</p></li>
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
<p>Cittadino registrato:</p>
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
<p>Cittadino registrato:</p>
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
<td colspan="4">Il Cittadino sceglie di uscire dall’interfaccia feedback</td>
</tr>
</tbody>
</table>
