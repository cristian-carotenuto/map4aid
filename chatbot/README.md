# 🤖 Chatbot Aidano per Map4Aid

Aidano è un chatbot knowledge-based basato su **Qwen 2.5-3B** per l'assistenza agli utenti della piattaforma Map4Aid. 
È ottimizzato con quantizzazione a **4-bit (QLoRA)** per funzionare su hardware consumer con VRAM limitata (<6GB).

## 🚀 Funzionalità principali
- **Consapevolezza temporale**: Sa che giorno è e risponde in base all'orario.
- **Memoria Conversazionale**: Ricorda gli ultimi 10 messaggi scambiati per mantenere il contesto.
- **Conoscenza Specifica**: Addestrato sui documenti RAD e Use Case di Map4Aid.

---

## 🛠️ Setup e Installazione

### 1. Requisiti di sistema
- Python 3.10+
- GPU NVIDIA con almeno 6GB VRAM (consigliata per l'inferenza fluida)
- CUDA Toolkit installato

### 2. Installazione
Dalla cartella radice del progetto:
```powershell
cd chatbot
pip install -r requirements.txt
```

### 3. Scaricare il modello
```powershell
python model/inference/download_model.py
```

---

## 🧪 Test e Utilizzo

Abbiamo diviso i test in due categorie:

### Test Base (Modello Originale + Memory)
Verifica che il bot sia in grado di parlare in italiano, ricordare la cronologia e conoscere l'ora.
```powershell
python model/inference/test_qwen_basic.py
```

### Test Fine-Tuning (Conoscenza Map4Aid)
Verifica che il bot conosca i dettagli del progetto Map4Aid (donazioni, stock, enti).
```powershell
python model/inference/test_qwen_tuning.py
```

---

## 🧠 Addestramento (Fine-Tuning)

Se vuoi migliorare la conoscenza di Aidano o aggiornare i suoi dati:

### 1. Preparare il dataset
Modifica `data/training_data.jsonl` o usa il generatore per creare varianti:
```powershell
python data/dataset_generator.py
```

### 2. Installare dipendenze di training
```powershell
pip install -r model/training/requirements-train.txt
```

### 3. Avviare il training
```powershell
python model/training/fine_tune.py
```
Il modello addestrato verrà salvato nella cartella `qwen-aidano-final`.

---

## 📁 Struttura Cartelle
- `model/inference/`: Client principale e test di esecuzione.
- `model/training/`: Script per l'addestramento e configurazioni LoRA.
- `data/`: Dataset di addestramento e KB locale.
- `requirements.txt`: Dipendenze base per l'uso del bot.
```
