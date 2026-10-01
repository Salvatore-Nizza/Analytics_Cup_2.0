import subprocess

def esegui_comando(comando):
    """Esegue un comando nel terminale e ne mostra l'output."""
    try:
        subprocess.run(comando, check=True, shell=True)
    except subprocess.CalledProcessError:
        print(f"\n[ERRORE] Il comando '{comando}' non è andato a buon fine.")

def menu():
    while True:
        print("\n" + "="*30)
        print("🐙 GESTORE GITHUB - ANALYTICS CUP")
        print("="*30)
        print("1. Salva e carica su GitHub (Push)")
        print("2. Scarica da GitHub (Pull - usa questo quando cambi PC/OS)")
        print("3. Esci")
        
        scelta = input("\nScegli un'opzione (1/2/3): ")
        
        if scelta == '1':
            messaggio = input("Cosa hai modificato? Inserisci un messaggio: ")
            print("\nSto salvando le modifiche...")
            esegui_comando("git add .")
            esegui_comando(f'git commit -m "{messaggio}"')
            esegui_comando("git push origin main")
            print("✅ Modifiche caricate con successo!")
            
        elif scelta == '2':
            print("\nSto scaricando gli ultimi aggiornamenti...")
            esegui_comando("git pull origin main")
            print("✅ Sincronizzazione completata! Codice aggiornato.")
            
        elif scelta == '3':
            print("Chiusura del gestore.")
            break
            
        else:
            print("❌ Scelta non valida, riprova.")

if __name__ == "__main__":
    menu()