import subprocess

def run_command(command):
    """Executes a command in the terminal and shows its output."""
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError:
        print(f"\n[ERROR] The command '{command}' failed.")

def main_menu():
    while True:
        print("\n" + "="*30)
        print("🐙 GITHUB MANAGER - ANALYTICS CUP")
        print("="*30)
        print("1. Save and upload to GitHub (Push)")
        print("2. Download from GitHub (Pull - use this when changing PC/OS)")
        print("3. Exit")
        
        choice = input("\nChoose an option (1/2/3): ")
        
        if choice == '1':
            commit_message = input("What did you change? Enter a commit message: ")
            print("\nSaving changes...")
            run_command("git add .")
            run_command(f'git commit -m "{commit_message}"')
            run_command("git push origin main")
            print("✅ Changes uploaded successfully!")
            
        elif choice == '2':
            print("\nDownloading latest updates...")
            run_command("git pull origin main")
            print("✅ Synchronization complete! Code updated.")
            
        elif choice == '3':
            print("Closing manager.")
            break
            
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()