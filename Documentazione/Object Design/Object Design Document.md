<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*OBJECT DESIGN DOCUMENT*

# Sommario

[1. **SCELTA DEI DESIGN PATTERN** [2](#scelta-dei-design-pattern)](#scelta-dei-design-pattern)

[1. **Facade Pattern** [2](#facade-pattern)](#facade-pattern)

[1.2 Funzione [2](#funzione)](#funzione)

[1.3 Perché è stato scelto [2](#perché-è-stato-scelto)](#perché-è-stato-scelto)

[**2. Bridge Pattern [2](#bridge-pattern)**](#bridge-pattern)

[2.1 Funzione [3](#funzione-1)](#funzione-1)

[2.2 Perché è stato scelto [3](#perché-è-stato-scelto-1)](#perché-è-stato-scelto-1)

# SCELTA DEI DESIGN PATTERN

## 1. Facade Pattern

### 1.2 Funzione

Il pattern *Facade* viene utilizzato per fornire un’unica interfaccia semplificata a un insieme di operazioni complesse legate alla registrazione e all’autenticazione degli utenti.

Nel sistema Map4Aid questo ruolo è svolto dalla classe **AuthFacade**, che centralizza:

- validazione dei dati di registrazione

- gestione dei pending accounts

- generazione e hashing dell’OTP

- invio dell’OTP tramite email

- creazione dell’account

- gestione del login con OTP

### 1.3 Perché è stato scelto

La registrazione e il login coinvolgono numerosi passaggi e componenti diversi (database, hashing, email, sessioni).

Senza un Facade, i controller avrebbero dovuto orchestrare manualmente tutte queste operazioni, diventando:

- più complessi

- più difficili da mantenere

- più soggetti a errori

- più accoppiati ai dettagli interni

Il pattern Facade permette di:

- nascondere la complessità interna

- offrire un unico punto di accesso semplice e coerente

- ridurre l’accoppiamento tra controller e logica di autenticazione

- rendere il sistema più estensibile

## 2. Bridge Pattern

### 2.1 Funzione

Il pattern *Bridge* viene utilizzato per separare l’astrazione del servizio email dalla sua implementazione concreta.

Nel sistema questo è realizzato tramite:

- **EmailControlBridge** (astrazione)

- **EmailControl** (implementazione concreta del servizio email)

Il controller non conosce i dettagli del provider email: invia solo comandi all’astrazione.

### 2.2 Perché è stato scelto

Il sistema invia email in diversi contesti:

- OTP per la registrazione

- conferme di prenotazione

- notifiche agli enti

- validazione delle ricette

- conferme di donazione

Il provider email potrebbe cambiare (SMTP locale, Gmail API, SendGrid, ecc.).

Senza un Bridge, ogni cambiamento richiederebbe modifiche in tutto il backend.

Il pattern Bridge permette di:

- disaccoppiare completamente il backend dal provider email

- sostituire l’implementazione senza toccare i controller

- facilitare test e mocking
