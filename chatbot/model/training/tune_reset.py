import os
import shutil


def reset_tuning(remove_datasets: bool = False):
    """
    Rimuove tutti gli artefatti prodotti dal fine-tuning (incluse le tranche LoRA).

    remove_datasets=False (default):
      - cancella adapter e output temporanei
      - NON cancella i dataset (così non perdi i jsonl)

    remove_datasets=True:
      - cancella anche i dataset generati (expanded + intent + answerable)
    """

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.abspath(os.path.join(script_dir, "../../data"))

    # Artefatti di training (sempre rimossi)
    paths_to_remove = [
        os.path.join(script_dir, "qwen-aidano-adapters"),
        os.path.join(script_dir, "qwen-aidano-final"),
        os.path.join(script_dir, "tmp-trainer-output"),
        os.path.join(script_dir, "qwen-aidano-checkpoints"),
    ]

    # Dataset (rimossi solo se richiesto)
    dataset_paths = [
        os.path.join(data_dir, "training_data_expanded.jsonl"),
        os.path.join(data_dir, "training_intent.jsonl"),
        os.path.join(data_dir, "training_answerable.jsonl"),
        os.path.join(data_dir, "aidano_runtime_config.json"),
    ]

    if remove_datasets:
        paths_to_remove.extend(dataset_paths)

    print("=" * 60)
    print(">> RESET FINE-TUNING AIDANO")
    print("=" * 60)
    print(f">> remove_datasets = {remove_datasets}")
    print("-" * 60)

    for path in paths_to_remove:
        abs_path = os.path.abspath(path)
        base_name = os.path.basename(abs_path)

        if os.path.exists(abs_path):
            try:
                if os.path.isdir(abs_path):
                    shutil.rmtree(abs_path)
                    print(f"[OK] Rimossa cartella: {base_name}")
                else:
                    os.remove(abs_path)
                    print(f"[OK] Rimosso file: {base_name}")
            except Exception as e:
                print(f"[!] Errore durante la rimozione di {abs_path}: {e}")
        else:
            print(f"[--] Percorso non trovato (già pulito): {base_name}")

    print("-" * 60)
    print(">> Pulizia completata! Riparti da base model.")
    print("=" * 60)


if __name__ == "__main__":
    reset_tuning(remove_datasets=True)
