**CASO D’USO \#3 (DONAZIONE MONETARIA)**

<table>
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
<p><em>UC#3</em></p></th>
<th rowspan="3"><em>Donazione monetaria</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>17/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.000</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Maistrini &amp; De Caro</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4"><em>Donazione monetaria da parte di qualsiasi utente nella piattaforma verso gli Enti erogatori</em></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Cittadino beneficiario (registrato, non registrato, donatore)</strong></p>
<p>Interessato a donare per beneficenza una certa somma di denaro</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4"><p><strong>Ente erogatore</strong></p>
<p>Riceve la donazione monetaria</p></th>
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
<th colspan="4">Alta</th>
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
<p>Cittadino:</p>
</blockquote></th>
<th colspan="5">clicca su “Donazione monetaria”</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>mostra un modulo da compilare con informazioni su ente e metodo di pagamento</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Cittadino:</p>
</blockquote></th>
<th colspan="5">Compila il modulo e lo invia</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Compie un controllo sulle informazioni inserite</em></th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Invia la donazione all’ente erogatore scelto</em></th>
</tr>
<tr class="odd">
<th>6</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Invia una notifica di successo al cittadino</em></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Saldo insufficiente</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Notifica all’utente che il saldo è insufficiente per la donazione</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Metodo di pagamento non valido</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema si accorge che il metodo di pagamento non è valido (CVV inesistente/numero carta inesistente), e notifica all’utente che il metodo di pagamento è inesistente</th>
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

**CASO D’USO \#10 (INVIO DI VALUTAZIONE E FEEDBACK)**

<table>
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
<th colspan="2"><em>0.00.000</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Maistrini &amp; De Caro</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4"><em>Il cittadino beneficiario inserisce una recensione ad un servizio offerto dalla piattaforma del quale ha usufruito</em></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Cittadino beneficiario (registrato)</strong></p>
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
<p>Il cittadino deve essere registrato</p>
</blockquote></li>
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
<p>Cittadino registrato:</p>
</blockquote></th>
<th colspan="5">Apre la notifica di “pacco consegnato”</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Chiede al cittadino di inserire una valutazione e feedback tramite un’interfaccia</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Cittadino registrato:</p>
</blockquote></th>
<th colspan="5">Inserisce una valutazione e un feedback e li invia</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Manda con successo la recensione all’ente erogatore</em></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo: Il cittadino decide di non inserire una recensione</strong></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il Cittadino sceglie di uscire dall’interfaccia feedback</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#1a (REGISTRAZIONE)**

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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC_01a</em></p></th>
<th rowspan="3"><em>Registrazione</em></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><p><em>Giovanni Esposito</em></p>
<p><em>Nicola Luciano</em></p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">Processo in cui un nuovo utente crea un account nel sistema</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4">Utente non registrato</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4">Sistema, servizio di posta elettronica</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">L'utente non possiede un account esistente. La connessione è protetta (HTTPS)</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">L'utente dispone di un account valido e può autenticarsi</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4"><p>Il sistema mostra un messaggio di errore:</p>
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
<p>per correzione), dove viene richiesto un nuovo inserimento di dati</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Alta</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">?/?</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Extension point</strong></th>
<th colspan="4">na</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">na</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente non registrato</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>L'utente accede alla pagina di registrazione</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Il sistema propone il form da compilare all'utente.<br />
Il form prevede l'inserimento di dati anagrafici (C.F. annesso), email, creazione di una</p>
<p>password, e eventuali allergie/intolleranze alimentari o condizioni e</p>
<p>patologie particolari</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Attore:</p>
</blockquote></th>
<th colspan="5">L'utente compila il form e invia i dati.</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema invia una mail di conferma all'utente, dopodichè l'utente disporrà di un account valido.</th>
</tr>
<tr class="header">
<th colspan="8"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> L'utente compila il campo Partita Iva nel form</th>
</tr>
<tr class="header">
<th colspan="2"><strong>3.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4"><p>L’utente compila anche il campo della p.iva.</p>
<p>Il sistema ricevendo dati sul campo partita iva, registra l'utente come Utente</p>
<p>Donatore(?), che avendo registrato la sua attività (verificata), è abilitato</p>
<p>a donare beni agli enti.</p></th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Email già registrata</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema notifica con un messaggio di errore “Email già registrata” il fatto che all’email inserita corrisponde già un account esistente.</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Password troppo debole</th>
</tr>
<tr class="header">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4"><p>Il sistema notifica con un messaggio di errore “Password troppo debole” il fatto che la</p>
<p>password inserita non è sicura e richiede la ricompilazione del campo in questione.</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>…</strong></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> CF/P.iva non valido</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.2</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema notifica con un messaggio di errore “CF/P.iva non valido” il fatto che i campi non risultano validi secondo i controlli formali</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Special Requirements</strong></th>
<th colspan="4">Nessuna informazione deve essere tracciata oltre quanto strettamente necessario (privacy by design</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4">Tutti i dati sensibili (es. allergie, documenti medici) devono essere crittografati a riposo con AES-256</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4">Il modulo è accessibile solo tramite HTTPS con certificato valido.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#1b (LOGIN)**

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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC_01b</em></p></th>
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
<th colspan="2"><p><em>Giovanni Esposito</em></p>
<p><em>Nicola Luciano</em></p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">Processo in cui un utente già registrato accede al sistema fornendo credenziali valide</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4">Utente registrato</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4">Sistema, servizio di posta elettronica</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">L'utente possiede un account valide con credenziali attive e vuole autenticarsi</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Sessione creata. L’utente ha accesso alle funzionalità.</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4"><p>Il sistema mostra un messaggio di errore:</p>
<ul>
<li><blockquote>
<p>Password errata e/o email non registrata.</p>
</blockquote></li>
</ul>
<p>L'utente rimane sulla pagina di login (con i dati inseriti se possibile,</p>
<p>per correzione), dove viene richiesto un nuovo inserimento di dati.</p></th>
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
<th colspan="4">na</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">na</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente registrato</p>
</blockquote></th>
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
<th colspan="2"><blockquote>
<p>Attore:</p>
<p>Utente registrato</p>
</blockquote></th>
<th colspan="5">L'utente compila il form e invia i dati.</th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema riconosce l’autenticazione. Sessione creata, accesso eseguito e funzionalità disponibili.</th>
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
<th colspan="2"><strong>Attore:</strong></th>
<th colspan="4">L’utente usa il link inviato per mail per accedere al form di reset</th>
</tr>
<tr class="header">
<th colspan="2"></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4"><p>Il sistema propone il form per inserire la nuova password, quando la password inserita</p>
<p>supera gli standard di sicurezza, la password è correttamente modificata, e l’utente</p>
<p>riceve una notifica a schermo. Redirect al login.</p></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> L’utente clicca su “Email dimenticata”</th>
</tr>
<tr class="header">
<th colspan="2"><strong>3.2</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Alla richiesta dell’utente del reset della mail, il Sistema invia un messaggio al numero di telefono associato, contenente un codice temporaneo ( OTP ) per sessione</th>
</tr>
<tr class="odd">
<th colspan="2"></th>
<th colspan="2"><strong>Attore:</strong></th>
<th colspan="4">L’utente inserisce il codice ricevuto tramite messaggio nell’apposito form fornito dal Sistema</th>
</tr>
<tr class="header">
<th colspan="2"></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il Sistema, superata la validità del codice inserito, mostra a vista la mail associata</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Password errata</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema notifica con un messaggio di errore “Email o password errate”, il fatto che i valori inseriti nei campi disponibili non risultano validi.</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Codice per recupero email non valido</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema verifica il codice inserito dall’utente, che risulta non valido.<br />
Il codice risulta non valido o per corrispondenza, o per la terminazione della sessione. In tal caso l’utente deve richiedere un nuovo codice.</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>Note</strong></th>
</tr>
<tr class="header">
<th colspan="4">about 4</th>
<th colspan="4">Successivamente sarà possibile implementare l'utilizzo dell’Autenticazione a due fattori ( 2FA ), richiesta solo dopo il riconoscimento dell’autenticazione da parte del Sistema.</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Special Requirements</strong></th>
<th colspan="4">Utilizzo di HTTPS con certificato valido garantendo la crittografia end-to-end dei dati trasmessi durante la fase di login.</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC-07</em></p></th>
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
<th colspan="2"><p>Giovanni Esposito</p>
<p>Nicola Luciano</p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4"><em>P</em>ermette agli enti erogatori di monitorare in tempo reale le scorte di beni disponibili nei propri punti di raccolta o distribuzione tramite una specifica interfaccia. Il sistema aggiorna automaticamente le scorte in base a due eventi principali:<br />
1. Aumento della quantità, quando un donatore esterno effettua una donazione (registrata tramite il sistema), oppure quando l'ente modifica la quantità di un bene o ne aggiunge uno non presente prima(la riduzione manuale non è consentita, per garantire tracciabilità e coerenza).<br />
2. Riduzione della quantità quando un bene viene prenotato ,e poi ritirato presso un punto di ritiro. (aggiornamento tramite automazione di sistema).</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4">Ente erogatore</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4">Sistema, Cittadino beneficiario, Utente donatore, Database</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4">Aggiornamento scorte di beni</th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Scorte aggiornate correttamente.</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">Scorte non aggiornate. Tentata modifica in negativo di scorte da parte dell’ente.</th>
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
<th colspan="4"><strong>Generalization of</strong></th>
<th colspan="4">na.</th>
</tr>
<tr class="header">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO</span></strong></th>
</tr>
<tr class="odd">
<th>1</th>
<th colspan="2"><blockquote>
<p>Attore: Ente erogatore</p>
</blockquote></th>
<th colspan="5"><p>Ente erogatore si logga con successo (UC_login) alla piattaforma, e accede alla dashboard dove è mostrata l’attuale traccia delle scorte</p>
<p>Ha a disposizione sull’interfaccia tutti i punti di ritiro associati con il loro inventario, e può sia incrementare il numero di beni sia aggiungerne di nuovi</p></th>
</tr>
<tr class="header">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Mostra tramite interfaccia la gestione scorte nei vari punti di ritiro associati</th>
</tr>
<tr class="odd">
<th>3</th>
<th colspan="2"><blockquote>
<p>Attore:</p>
<p>Ente erogatore</p>
</blockquote></th>
<th colspan="5">Modifica quantità di un bene esistente in un determinato punto di ritiro (non ci occupiamo della logica dietro la consegna del nuovo bene incrementato)</th>
</tr>
<tr class="header">
<th>4</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">Il sistema aggiorna il database per tenere traccia di permanenza dell’aggiornamento, e di conseguenza l’interfaccia utente. Scorte e interfaccia utente aggiornate.</th>
</tr>
<tr class="odd">
<th colspan="8">…</th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Donazione di bene da utente donatore (UC_donazione bene)</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>2.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema rileva una donazione di un bene all’ente da parte di un utente donatore<br />
Il sistema aggiorna le scorte del punto di ritiro associato alla ricezione di quel bene, e di conseguenza l’interfaccia utente.</th>
</tr>
<tr class="header">
<th colspan="8"><strong>II Scenario/Flusso di eventi Alternativo:</strong> Prenotazione di un bene da cittadino beneficiario (UC_prenotazione bene)</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.2</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema rileva la prenotazione di un bene in un determinato punto di ritiro.<br />
Il sistema aggiorna le scorte di quel punto di ritiro congelando il bene richiesto fino al ritiro, aggiornando dashboard e tenendo traccia delle scorte.</th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Aggiunta di un nuovo bene</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>3.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Il sistema rileva un nuovo bene allocato in un determinato punto di ritiro dall’ente.<br />
Il sistema provvede ad aggiornare le scorte relative a quel punto, aggiornare la persistenza su db e aggiornare interfaccia utente (dashboard)</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>II Scenario/Flusso di eventi di ERRORE:</strong> Errori ( DB o Rete )</th>
</tr>
<tr class="header">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Timeout o errore durante l’aggiornamento ( per mancata connessione al DB o alla Rete )</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4"></th>
</tr>
<tr class="header">
<th colspan="8"><strong>Note</strong></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Special Requirements</strong></th>
<th colspan="4">n.f.#2 – Persistenza dei dati</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4">n.f.#3 – Tassonomia gerarchica</th>
</tr>
<tr class="odd">
<th colspan="4"></th>
<th colspan="4">n.f.#5 – Protezione dei dati e autenticazione</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**CASO D’USO \#4 (DONAZIONE DI BENI)**

<table>
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
<p><em>UC#4</em></p></th>
<th rowspan="3"><strong>DONAZIONE DI BENI</strong></th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.0001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Milone e Caserta</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4"><em>L’utente registrato può donare beni materiali a enti specifici, in base alla propria categoria di donatore. Compila un modulo dedicato con i dettagli dei beni, che viene inviato all’ente per la validazione. In caso di approvazione, l’ente comunica al donatore le istruzioni per il ritiro.</em></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><p><strong>Utente (registrato o loggato)</strong></p>
<p><strong>Ente ricevente</strong></p></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4"><strong>Sistema</strong></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4"><ul>
<li><blockquote>
<p>L’utente deve essere registrato o loggato come donatore</p>
</blockquote></li>
<li><blockquote>
<p>L'utente deve essere assegnato ad una determinata categoria di donazione</p>
</blockquote></li>
<li><blockquote>
<p>L’utente deve compilare un modulo, il quale varia a seconda della tipologia di donazione, ed inviarlo</p>
</blockquote></li>
</ul></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">L’ente convalida i dati forniti e invia una email al donatore con informazioni sul ritiro dei beni da parte dell’ente</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">L’ente rifiuta la richiesta la richiesta di donazione da parte dell’utente</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Rilevanza/User Priority</strong></th>
<th colspan="4">Media</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Frequenza stimata</strong></th>
<th colspan="4">Medio-bassa (parlarne)</th>
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
<p>Cittadino registrato:</p>
</blockquote></th>
<th colspan="5">Compila il modulo per la donazione specifica (parlarne)</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Inoltre il modulo all’ente</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Riceve e valida i dati del modulo</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></th>
<th colspan="5">Invia una mail sulle informazioni del punto di ritiro del bene</th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><em>Salva la donazione effettuata</em></th>
</tr>
<tr class="odd">
<th colspan="8"><strong>I Scenario/Flusso di eventi Alternativo:</strong> Ente rifiuta la donazione</th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>Cittadino registrato:</p>
</blockquote></th>
<th colspan="5">Compila il modulo per la donazione specifica (parlarne)</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>Inoltre il modulo all’ente</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3</th>
<th colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>L’ente determina come negativa la richiesta e rifiuta</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>4</th>
<th colspan="2"><blockquote>
<p>Ente ricevente:</p>
</blockquote></th>
<th colspan="5">Invia una mail con le motivazioni di rifiuto</th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Errori (DB o Rete)</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Timeout o errore durante l’invio del modulo</th>
</tr>
<tr class="header">
<th colspan="2"><strong>Note</strong></th>
<th colspan="2"></th>
<th colspan="4">parlare dei punti in cui si hanno domande</th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Special Requirements</strong></th>
<th colspan="4">Requisito n.f.#2 – Persistenza dei dati</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4">Requisito n.f #5 - Protezione dei Dati e Autenticazione</th>
</tr>
</thead>
<tbody>
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
<thead>
<tr class="header">
<th colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#8</em></p></th>
<th rowspan="3">Sistema di Notifiche e Avvisi</th>
<th colspan="2"><em>Data</em></th>
<th><em>18/11/2025</em></th>
</tr>
<tr class="odd">
<th><em>Vers.</em></th>
<th colspan="2"><em>0.00.0001</em></th>
</tr>
<tr class="header">
<th><em>Autore</em></th>
<th colspan="2"><em>Milone e Caserta</em></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Descrizione</strong></th>
<th colspan="4">Il sistema invia notifiche automatiche a utenti ed enti in caso di eventi rilevanti, come disponibilità di beni compatibili o scadenze di ritiro. Le comunicazioni vengono recapitate tramite email o tramite l’area notifiche interna della piattaforma.</th>
</tr>
<tr class="header">
<th colspan="4"><strong>Attore Principale</strong></th>
<th colspan="4"><strong>Sistema</strong></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Attori secondari</strong></th>
<th colspan="4"><p><strong>Utente (registrato o loggato)</strong></p>
<p><strong>Ente donatore</strong></p></th>
</tr>
<tr class="header">
<th colspan="4"><strong>Entry Condition</strong></th>
<th colspan="4"><ul>
<li><blockquote>
<p>Il sistema invia un messaggio sulle scadenze di prenotazioni non ritirate o sulla disponibilità di nuovi beni compatibili con le preferenze dell’utente o compatibili con le patologie inserite.</p>
</blockquote></li>
</ul></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On success</p></th>
<th colspan="4">Il sistema invia una notifica attraverso una mail o un’area notifiche interna alla piattaforma</th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Exit condition</strong></p>
<p>On failure</p></th>
<th colspan="4">La notifica non viene inviata per un errore del sistema</th>
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
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO I</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>Cittadino registrato:</p>
</blockquote></th>
<th colspan="5">effettua una prenotazione</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>ente donatore:</p>
</blockquote></th>
<th colspan="5">non conferma il ritiro del pacco</th>
</tr>
<tr class="header">
<th>5</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5">invia una notifica di scadenza della prenotazione</th>
</tr>
<tr class="odd">
<th colspan="8"><strong><span class="smallcaps">FLUSSO DI EVENTI PRINCIPALE/MAIN SCENARIO II</span></strong></th>
</tr>
<tr class="header">
<th>1</th>
<th colspan="2"><blockquote>
<p>ente donatore:</p>
</blockquote></th>
<th colspan="5">Aggiorna le disponibilità dei beni</th>
</tr>
<tr class="odd">
<th>2</th>
<th colspan="2"><blockquote>
<p>Sistema:</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>invia una notifica a chi è interessato alla categoria del bene</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="8"><strong>I Scenario/Flusso di eventi di ERRORE:</strong> Errori (Rete)</th>
</tr>
<tr class="odd">
<th colspan="2"><strong>4.1</strong></th>
<th colspan="2"><strong>Sistema:</strong></th>
<th colspan="4">Timeout o errore durante l’invio della notifica</th>
</tr>
<tr class="header">
<th colspan="2"><strong>Note</strong></th>
<th colspan="2"></th>
<th colspan="4"></th>
</tr>
<tr class="odd">
<th colspan="4"><strong>Special Requirements</strong></th>
<th colspan="4">Requisito n.f.#2 – Persistenza dei dati</th>
</tr>
<tr class="header">
<th colspan="4"></th>
<th colspan="4">Requisito n.f #5 - Protezione dei Dati e Autenticazione</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
