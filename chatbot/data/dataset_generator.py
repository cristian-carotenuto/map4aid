import json
import os

# Template per generare varianti di domande
TEMPLATES = [
    {
        "category": "registrazione",
        "questions": ["Come mi registro?", "Voglio iscrivermi", "Procedura di registrazione", "Creare un account"],
        "answer": "La registrazione a Map4Aid avviene tramite un modulo online dove inserire nome utente, email e password. Riceverai una mail di conferma."
    },
    {
        "category": "donazioni_monetarie",
        "questions": ["Voglio donare soldi", "Come faccio una donazione in denaro?", "Metodi di pagamento per donazioni", "Posso donare fondi?"],
        "answer": "Puoi effettuare donazioni monetarie tramite il modulo di pagamento sicuro sul portale. Il sistema invierà una ricevuta via email."
    },
    {
        "category": "stock",
        "questions": ["Cos'è lo stock?", "Donare vestiti o cibo", "Gestione magazzino enti", "Come funziona la donazione di beni?"],
        "answer": "Lo stock riguarda i beni fisici come cibo e vestiti. Gli utenti possono donare beni rispondendo agli annunci degli enti o inserendo nuove offerte."
    }
]

def generate_dataset(output_file="chatbot/data/training_data.jsonl"):
    """Genera un dataset espanso partendo dai template."""
    
    # Crea la directory se non esiste
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    dataset = []
    system_prompt = "Sei Aidano, l'assistente virtuale di Map4Aid. Rispondi in modo professionale ed esaustivo basandoti sulla documentazione."
    
    for item in TEMPLATES:
        for q in item["questions"]:
            entry = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": item["answer"]}
                ]
            }
            dataset.append(entry)
            
    # Scrivi il file JSONL
    with open(output_file, "a", encoding="utf-8") as f: # Append al file esistente
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            
    print(f">> Generati {len(dataset)} nuovi campioni in {output_file}")

if __name__ == "__main__":
    generate_dataset()
