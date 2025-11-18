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
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#3</em></p></td>
<td rowspan="3"><em>Donazione monetaria</em></td>
<td colspan="2"><em>Data</em></td>
<td><em>17/11/2025</em></td>
</tr>
<tr class="even">
<td><em>Vers.</em></td>
<td colspan="2"><em>0.00.000</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Maistrini &amp; De Caro</em></td>
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
<td colspan="2"><em>0.00.000</em></td>
</tr>
<tr class="odd">
<td><em>Autore</em></td>
<td colspan="2"><em>Maistrini &amp; De Caro</em></td>
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
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC_01a</em></p></td>
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
<td colspan="2"><p><em>Giovanni Esposito</em></p>
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
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC_01b</em></p></td>
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
<td colspan="2"><p><em>Giovanni Esposito</em></p>
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
<p><em>UC-07</em></p></td>
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
<td colspan="2"><p>Giovanni Esposito</p>
<p>Nicola Luciano</p></td>
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
<tbody>
<tr class="odd">
<td colspan="4" rowspan="3"><p><strong>Identificativo</strong></p>
<p><em>UC#4</em></p></td>
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
<td colspan="2"><em>Milone e Caserta</em></td>
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
<li><blockquote>
<p>L’utente deve essere registrato o loggato come donatore</p>
</blockquote></li>
<li><blockquote>
<p>L'utente deve essere assegnato ad una determinata categoria di donazione</p>
</blockquote></li>
<li><blockquote>
<p>L’utente deve compilare un modulo, il quale varia a seconda della tipologia di donazione, ed inviarlo</p>
</blockquote></li>
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
<td colspan="2"><em>Milone e Caserta</em></td>
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
<li><blockquote>
<p>Il sistema invia un messaggio sulle scadenze di prenotazioni non ritirate o sulla disponibilità di nuovi beni compatibili con le preferenze dell’utente o compatibili con le patologie inserite.</p>
</blockquote></li>
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
