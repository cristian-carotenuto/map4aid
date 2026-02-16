"""
Script per testare le "risposte preimpostate" (Knowledge Base)
senza caricare e usare il modello generativo.

Carica i dati da 'chatbot/data/training_data_expanded.jsonl' (o 'training_data.jsonl')
e cerca la domanda più simile con difflib per restituire la risposta "canonica".
"""

import json
import os
import difflib

# Percorsi relativi dei dataset
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
DATASET_FILES = [
    os.path.join(DATA_DIR, "training_data_expanded.jsonl"),
    os.path.join(DATA_DIR, "training_data.jsonl")
]

def load_qa_pairs():
    """Carica tutte le coppie (user_msg, assistant_msg) dai dataset JSONL."""
    qa_pairs = []
    
    for file_path in DATASET_FILES:
        if not os.path.exists(file_path):
            print(f"[WARN] File non trovato: {file_path}")
            continue
            
        print(f">> Caricamento da: {os.path.basename(file_path)}...")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        messages = entry.get("messages", [])
                        
                        user_msg = next((m["content"] for m in messages if m["role"] == "user"), None)
                        assistant_msg = next((m["content"] for m in messages if m["role"] == "assistant"), None)
                        
                        if user_msg and assistant_msg:
                            qa_pairs.append({
                                "question": user_msg, 
                                "answer": assistant_msg
                            })
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"[ERR] Errore leggendo {file_path}: {e}")

    print(f"[OK] Caricate {len(qa_pairs)} coppie Q&A totali.\n")
    return qa_pairs

def find_best_match(user_query, qa_pairs, threshold=0.6):
    """Trova la domanda più simile nel dataset."""
    questions = [pair["question"] for pair in qa_pairs]
    matches = difflib.get_close_matches(user_query, questions, n=1, cutoff=threshold)
    
    if matches:
        best_q = matches[0]
        # Trova la risposta associata
        for pair in qa_pairs:
            if pair["question"] == best_q:
                return pair
    return None

def main():
    print("=" * 60)
    print(">> TEST RISPOSTE PREIMPOSTATE (NO AI GENERATIVA)")
    print("Simula le risposte di Aidano cercando la domanda più simile nel dataset.")
    print("Comandi: /esci")
    print("=" * 60)
    
    qa_pairs = load_qa_pairs()
    
    if not qa_pairs:
        print("[ERR] Nessun dato caricato. Verifica i percorsi e riprova.")
        return

    while True:
        user_input = input("\nTu (Static): ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ["/esci", "esci", "exit", "quit"]:
            break
            
        match = find_best_match(user_input, qa_pairs)
        
        if match:
            print(f"Match trovato (Q: '{match['question']}')")
            print(f"Aidano (Preset): {match['answer']}")
        else:
            print(">> Nessuna corrispondenza trovata nel dataset (soglia non superata).")
            print("   (Il modello generativo avrebbe provato a rispondere comunque)")

if __name__ == "__main__":
    main()
