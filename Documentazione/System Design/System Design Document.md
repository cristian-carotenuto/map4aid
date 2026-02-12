<img src="media/image1.png" style="width:1.32986in;height:1.32153in" />

*SYSTEM DESIGN DOCUMENT*

**1.Usabilità del sistema**: le interfacce del sistema devono essere chiare e comprensibili

**2.Sicurezza:** il sistema deve trattare i dati degli utenti in modo sicuro

**3.Privacy:** il sistema deve garantire la privacy degli utenti chiedendo solo dati essenziali

**4.Accessibilità:**il sistema deve essere accessibile da diversi dispositivi

**5.Affidabilità:** Il sistema deve garantire la correttezza delle informazioni sui beni disponibili.

**6.Scalabilità:** Il sistema deve poter gestire un gran numero di utenti e beni in modo efficiente

# 

## 

## 

## 

## 

## 

## 

## 

## 1. Usabilità vs Sicurezza

Nel progetto Map4Aid questo trade‑off è stato affrontato privilegiando la sicurezza, pur mantenendo un livello di usabilità adeguato al contesto sociale dell’applicazione.

### Scelte di sicurezza implementate

**Registrazione con OTP**: ogni nuovo account deve confermare la propria identità tramite codice monouso inviato via email.

- Questo introduce un passaggio aggiuntivo per l’utente, ma garantisce che l’indirizzo email sia reale e controllato.

**Upload del documento d’identità** per beneficiari e enti erogatori:

- aumenta la complessità della registrazione, ma permette di verificare l’autenticità dei profili e prevenire abusi.

**Ruoli e permessi rigidi** (require_roles, require_admin):

- ogni endpoint è accessibile solo alle categorie autorizzate, riducendo la superficie di attacco ma aumentando la complessità di gestione.

**Sessioni server‑side**:

- scelta più sicura rispetto ai token client‑side, ma meno comoda per l’utente e meno scalabile.

### Impatto sull’usabilità

- La registrazione richiede più passaggi rispetto a un’app tradizionale.

- L’utente deve caricare documenti e attendere approvazione.

- Alcune operazioni (es. prenotazione medicinali) richiedono conferme multiple.

### Motivazione del compromesso

Il sistema gestisce:

- dati sensibili (documenti, patologie, allergeni)

- prenotazioni di beni essenziali

- medicinali con ricetta

- enti verificati

In questo contesto, la sicurezza non è un optional ma un requisito fondamentale.

Il compromesso scelto è quindi:

> **Sicurezza elevata, anche a costo di una minore immediatezza nell’esperienza utente.**

## 2. Privacy vs Affidabilità

Trade off più evidente nel progetto, Map4Aid deve garantire che:

- i beneficiari siano reali

- gli enti siano verificati

- le prenotazioni siano corrette

- i medicinali siano distribuiti solo a chi ne ha diritto

Per farlo, il sistema deve raccogliere dati che normalmente non verrebbero richiesti in un’app generica.

### Scelte che privilegiano l’affidabilità

- **Raccolta di dati sanitari** (allergeni, patologie) per migliorare la qualità del servizio.

- **Upload della carta d’identità** per verificare l’identità del beneficiario.

- **Upload della ricetta medica** per i medicinali.

- **Geolocalizzazione precisa** per inviare segnalazioni agli enti più vicini.

- **Stati delle prenotazioni** (in_validazione → in_attesa → ritirata) per garantire tracciabilità e correttezza.

Questi elementi aumentano l’affidabilità del sistema, ma riducono la privacy dell’utente.

### Misure adottate per mitigare l’impatto sulla privacy

- Raccolta **solo dei dati strettamente necessari** al servizio.

- Nessuna condivisione dei dati con terze parti.

- Documenti salvati con nomi univoci e non riconducibili direttamente all’utente.

- Accesso ai dati limitato tramite ruoli e permessi.

- Nessuna esposizione dei dati sensibili nelle API pubbliche.

### Motivazione del compromesso

Il sistema deve garantire che:

- i beni vengano distribuiti correttamente

- i medicinali siano consegnati solo a chi ha una ricetta valida

- gli enti possano verificare l’identità dei beneficiari

Per questo motivo, la privacy non può essere assoluta:

**una parte dei dati sensibili è necessaria per garantire affidabilità e correttezza del servizio.**

# Conclusione

Nel complesso, Map4Aid adotta scelte progettuali che privilegiano:

- **Sicurezza** rispetto alla pura usabilità

- **Affidabilità** rispetto alla privacy assoluta

Questi compromessi sono coerenti con la natura del sistema, che gestisce:

- beneficiari reali

- enti verificati

- medicinali

- documenti sensibili

- prenotazioni critiche

e richiede quindi un livello di controllo superiore rispetto a un’applicazione consumer tradizionale, essendo infatti un servizio prettamente aid.

Il compromesso scelto è:

**Affidabilità e correttezza dei processi \> Minimizzazione assoluta dei dati**,

> pur mantenendo un livello di privacy adeguato e conforme al principio di necessità.

## Introduzione al Sistema

Map4Aid è una piattaforma web progettata per supportare la distribuzione di beni essenziali e medicinali a persone in difficoltà, facilitando la collaborazione tra beneficiari, donatori ed enti erogatori.

Il sistema gestisce processi critici come:

- registrazione con verifica tramite OTP

- validazione documentale dei beneficiari

- prenotazione di beni alimentari e medicinali

- validazione manuale delle ricette

- gestione dei punti di distribuzione

- gestione delle donazioni di beni

- gestione delle donazioni monetarie

- invio automatico di notifiche email

Per garantire sicurezza, modularità e manutenibilità, Map4Aid adotta un’architettura **three‑tier**, che separa nettamente interfaccia, logica applicativa e gestione dei dati.

In questo modello, **la view non può accedere direttamente al model**, ma deve sempre passare attraverso il controller e il backend Flask.

# Architettura Three‑Tier

L’architettura del sistema è suddivisa in tre livelli indipendenti:

1.  **Presentation Tier (Frontend Web)**

2.  **Application Tier (Backend Flask)**

3.  **Data Tier (Database SQLite + ORM)**

Questa separazione garantisce sicurezza, scalabilità e una chiara divisione delle responsabilità.

## 1. Presentation Tier – Frontend Web

Il frontend è sviluppato come applicazione web tradizionale, organizzata nelle cartelle:

- **html/** – pagine e template

- **css/** – fogli di stile

- **js/** – script lato client

- **imgs/** – risorse grafiche

### Responsabilità del frontend

- mostrare le informazioni provenienti dal backend

- raccogliere input tramite form (registrazione, login, prenotazioni, upload documenti)

- inviare richieste HTTP alle API REST

- gestire la sessione tramite cookie

- permettere ai donatori di effettuare donazioni monetarie tramite form dedicato

Il frontend **non accede mai direttamente al database**.

Ogni operazione passa attraverso il backend, garantendo sicurezza e controllo degli accessi.

## 2. Application Tier – Backend Flask

Il backend è il cuore logico del sistema.

È implementato in Python tramite Flask ed è organizzato in moduli coerenti e indipendenti.

La struttura include:

- **controllers/** – gestione delle richieste HTTP e orchestrazione della logica

- **models/** – definizione delle entità e delle relazioni

- **service_email/** – invio email tramite pattern Bridge

- **app.py** – configurazione dell’applicazione

- **run.py** – avvio del server

- **config.py** – configurazione generale

- **migrations/** – gestione delle migrazioni del database

### Responsabilità del backend

- autenticazione e autorizzazione (OTP, sessioni, ruoli)

- gestione delle prenotazioni di beni e medicinali

- validazione manuale delle ricette

- gestione dei pacchi alimentari

- gestione delle donazioni di beni

- gestione delle donazioni monetarie, con registrazione dell’importo e notifica all’ente

- invio email tramite EmailControlBridge

- geolocalizzazione tramite Geopy/Nominatim

- applicazione della logica di business

- protezione degli endpoint tramite middleware di permessi

Il backend è l’unico livello autorizzato a interagire con il database.

## 3. Data Tier – Database SQLite + SQLAlchemy ORM

Il livello dati utilizza:

- **SQLite** come database relazionale locale

- **SQLAlchemy** come ORM per mappare le entità Python alle tabelle SQL

### Responsabilità del Data Tier

- memorizzazione persistente dei dati

- integrità referenziale

- gestione delle relazioni tra entità

- transazioni atomiche

- nessun accesso diretto da parte del frontend

Il database contiene:

- utenti e ruoli

- pending accounts

- enti erogatori

- punti di distribuzione

- beni e sottocategorie

- pacchi alimentari

- prenotazioni

- donazioni di beni

- donazioni monetarie (importo, donatore, ente destinatario, data)

# Comunicazione tra i Livelli

La comunicazione segue rigorosamente il modello three‑tier:

Codice

Frontend → Backend → Database

Frontend ← Backend ← Database

Il backend:

1.  riceve la richiesta

2.  valida i dati

3.  applica la logica di business

4.  interroga il database

5.  restituisce una risposta JSON

Questo garantisce:

- sicurezza

- consistenza dei dati

- controllo degli accessi

- separazione delle responsabilità

# Deployment

Il sistema è eseguito in ambiente locale tramite:

Codice

flask run

con:

- backend Flask

- database SQLite

- esecuzione single‑instance

- virtual environment dedicato (venv/)

Questa configurazione è ideale per sviluppo e test, ma l’architettura three‑tier permette una futura migrazione verso:

- server dedicati

- container Docker

- database più performanti (PostgreSQL, MySQL, DJANGO)

- hosting cloud

senza modificare la struttura logica del sistema.

# Conclusione

L’architettura three‑tier adottata da Map4Aid garantisce:

- separazione chiara tra interfaccia, logica e dati

- maggiore sicurezza (il frontend non accede ai dati)

- modularità e manutenibilità

- possibilità di scalare in futuro

- integrazione naturale delle donazioni monetarie e materiali

È una scelta robusta e perfettamente adeguata alla natura del sistema, che gestisce dati sensibili, processi critici e attori con ruoli diversi.
