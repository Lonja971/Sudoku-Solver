import os, json

#---SHOW-LIST-OF-JSON-SUDOKU-BOARDS---

def list_json_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.json')]

def choose_file(files):
    print("Selecteer een bestand:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    
    while True:
        try:
            choice = int(input("Voer het bestandsnummer in: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Het ingevoerde nummer is onjuist. Probeer het opnieuw.")
        except ValueError:
            print("Voer een nummer in.")

def load_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)