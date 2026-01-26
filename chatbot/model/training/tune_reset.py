import os
import shutil

def reset_tuning():
    """Rimuove tutti gli artefatti prodotti dal fine-tuning."""
    
    # Percorsi relativi alla posizione dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    paths_to_remove = [
        # Adapter finali
        os.path.join(script_dir, "qwen-aidano-final"),
        # Checkpoint temporanei
        os.path.join(script_dir, "qwen-aidano-checkpoints"),
        # Dataset espanso
        os.path.join(script_dir, "../../data/training_data_expanded.jsonl")
    ]
    
    print("=" * 50)
    print(">> RESET FINE-TUNING AIDANO")
    print("=" * 50)
    
    for path in paths_to_remove:
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path):
            try:
                if os.path.isdir(abs_path):
                    shutil.rmtree(abs_path)
                    print(f"[OK] Rimossa cartella: {os.path.basename(abs_path)}")
                else:
                    os.remove(abs_path)
                    print(f"[OK] Rimosso file: {os.path.basename(abs_path)}")
            except Exception as e:
                print(f"[!] Errore durante la rimozione di {abs_path}: {e}")
        else:
            print(f"[--] Percorso non trovato (già pulito): {os.path.basename(abs_path)}")
            
    print("-" * 50)
    print(">> Pulizia completata! Aidano è tornato alla versione originale.")
    print("=" * 50)

if __name__ == "__main__":
    reset_tuning()
