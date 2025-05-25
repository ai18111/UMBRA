import threading
import requests
from pystyle import Colors, Colorate, Center
import time
import os
import base64
import sys
import datetime
import colorama
from tkinter import filedialog as fd
import random
import string
import secrets
import json
import pyperclip
import hashlib


os.system("title umbra v1.0 beta version")

# colors
black = "\033[1;30m"
titletext = " [umbra v1.0]"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"


logo = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡖⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⢉⣳⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣴⠋⢀⣤⣾⣶⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣟⣁⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠛⢛⠿⢦⣄⡀⠀⠀
⢹⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠠⡤⠤⠤⠤⠤⠤⣞⣁⠀⠀⠀⠰⡘⢽⣿⢿⣆⠀
⠀⡇⠀⠀⠉⠑⠢⣤⣀⠀⠀⠀⣀⠤⠒⠉⠁⢸⠀⠀⡇⠀⠀⠀⠀⠀⣀⣬⣥⠄⠀⠀⠈⠓⠭⠼⠻⣄
⠀⠸⡀⠀⡐⠀⠀⢸⠀⠉⢦⣄⠈⠉⠒⠢⠤⣈⣦⣠⣳⣀⡤⠴⠚⢹⠁⠁⠁⠀⢟⠿⣿⢛⠆⠀⠀⢿
⠀⠀⠱⡀⠀⠀⢀⠜⠀⠀⢸⠀⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠱⠟⠋⠀⣠⡶⠁
⠀⠀⠀⠹⡖⠒⠁⠀⠀⠀⡜⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠠⡤⠚⠁⠀⠀
⠀⠀⠀⠀⠈⠲⣤⠤⣴⠊⠀⡈⠒⠙⠈⣦⠤⠤⠤⠤⣀⣀⠀⠀⣀⠜⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠒⠤⢄⣀⣀⡀⠀⠘⠆⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠙⢳⣸⠀⢀⠔⠉⠆⠀⡼⠀⠀⠀⠀⣷⠀⢀⡴⢢⠀⡼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⡏⢀⡎⣴⡿⢐⡴⠉⠉⣿⣿⣶⣿⠀⡜⣰⡏⣷⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⠀⠀⡰⠧⣼⢸⢴⣡⠟⠀⠀⠀⢸⣿⣿⣿⡆⡇⣧⢢⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠔⣻⠑⡀⢙⡺⠟⠁⠀⠀⠀⠀⣼⣿⣿⡏⢧⠳⢴⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡀⡇⠀⢧⡎⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⡌⢠⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢿⡀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⠛⢣⠘⠀⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⢄⣈⣳⡄⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠺⡆⠀⠸⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⣀⣀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠂⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀
    >> Password Tool, Umbra v1.0                                       
"""

logo = Center.XCenter(logo)



#  command choices
def choice():
   print(Center.XCenter("""

   [01] Password Judger                 
   [02] Password Advancer               
   [03] Password + Email Vault                      
   [04] Password Generator             
   [05] Password Leak Check
   [06] Password Encrypter
"""))

# Print ASCII logo cuz important color
def printascii():
    print(Colorate.Horizontal(Colors.green_to_white, logo, 1))

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pause 
def pause(text: str = None):
    if text:
        print(text)
    os.system('pause >nul' if os.name == 'nt' else 'read -n 1 -s -r -p ""')

# Areas for script

def judge():
    judgeitem = input("Enter password to judge: ")
    
    errors = []
    score = 0

    if len(judgeitem) > 8:
        score += 2
    else:
        errors.append("Length < 8")

    if len(judgeitem) >= 15:
        score += 1
    else:
        errors.append("Length < 15")

    if any(c.isupper() for c in judgeitem):
        score += 2
    else:
        errors.append("Uppercase letter not found")

    if any(c.islower() for c in judgeitem):
        score += 2
    else:
        errors.append("Lowercase letter not found")

    if any(c.isdigit() for c in judgeitem):
        score += 2
    else:
        errors.append("Number not found")

    if any(c in string.punctuation for c in judgeitem):
        score += 1
    else:
        errors.append("Special character not found")

    print(f"Score: {score}/10")
    if errors:
        print("Need to fix:")
        for err in errors:
            print(f"  - {err}")
        jta = input("Do you want to improve your password? (y): ")
        if jta.lower() == "y":
            advancer()
        else:
            print("going back to main menu")
            time.sleep(1)
            main()
    else:
        jtm = input("enter to go back to main menu: ")
        if jtm == "":
            print("going back to main menu")
            time.sleep(1)
            main()
        else:           
            print("going back to main menu")
            time.sleep(1)
            main()

def advancer():
    original_pass = input("Enter password to improve: ")
    
    if not original_pass:
        print(f"{white} Please enter a password!")
        return
    
    print(f"\n{white} Analyzing your password...")
    time.sleep(0.5) 
    
   
    has_upper = any(c.isupper() for c in original_pass)
    has_lower = any(c.islower() for c in original_pass)
    has_digit = any(c.isdigit() for c in original_pass)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in original_pass)
    
    improved_pass = original_pass
    changes_made = []
    
   
    if not has_upper:
        
        pos = random.randint(1, len(improved_pass))
        upper_char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        improved_pass = improved_pass[:pos] + upper_char + improved_pass[pos:]
        changes_made.append("Added uppercase letter")
    
    if not has_lower:
        
        
        pos = random.randint(0, len(improved_pass))
        lower_char = random.choice("abcdefghijklmnopqrstuvwxyz")
        improved_pass = improved_pass[:pos] + lower_char + improved_pass[pos:]
        changes_made.append("Added lowercase letter")
    
    if not has_digit:
       
        if random.choice([True, False]):
            num = str(random.randint(10, 99))
            improved_pass += num
        else:
            num = str(random.randint(1, 9))
            improved_pass = num + improved_pass
        changes_made.append("Added numbers")
    
    if not has_symbol:
        
        sym = ["!", "@", "#", "$", "&", "*"]
        symbol = random.choice(sym)
        if random.choice([True, False]):
            improved_pass += symbol
        else:
            improved_pass = symbol + improved_pass
        changes_made.append("Added special character")
    
    
    if len(improved_pass) < 15:

        chars_needed = 15 - len(improved_pass)
        for _ in range(chars_needed):
            char_type = random.choice(["letter", "number", "symbol"])
            if char_type == "letter":
                if random.choice([True, False]):
                    char = random.choice("abcdefghijklmnopqrstuvwxyz")
                else:
                    char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            elif char_type == "number":
                char = str(random.randint(0, 9))
            else:
                char = random.choice("!@#$%^&*")
            
           
            pos = random.randint(0, len(improved_pass))
            improved_pass = improved_pass[:pos] + char + improved_pass[pos:]
        changes_made.append("Extended length for better security")

    if len(original_pass) < 8 and random.choice([True, False]):
        current_year = datetime.datetime.now().year
        year_options = [str(current_year), str(current_year-1), "2024", "2025"]
        year = random.choice(year_options)
        improved_pass += year
        changes_made.append("Added year for complexity")
    
    
    print(f"\n{white}Password Enhancement Complete!")
    print(f"\n{white}Original Password: {original_pass}")
    print(f"{white}Improved Password: {improved_pass}")
    print(f"\n{white}Changes Made:")
    for i, change in enumerate(changes_made, 1):
        print(f"  {i}. {change}")
    
   
    original_score = 0
    improved_score = 0
    
   
    if len(original_pass) >= 8: original_score += 2
    if len(improved_pass) >= 8: improved_score += 2
    
    if len(original_pass) >= 15: original_score += 1
    if len(improved_pass) >= 15: improved_score += 1

    if any(c.isupper() for c in original_pass): original_score += 2
    if any(c.isupper() for c in improved_pass): improved_score += 2
    
    if any(c.islower() for c in original_pass): original_score += 2
    if any(c.islower() for c in improved_pass): improved_score += 2
    
    if any(c.isdigit() for c in original_pass): original_score += 2
    if any(c.isdigit() for c in improved_pass): improved_score += 2
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in original_pass): original_score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in improved_pass): improved_score += 1
    
    print(f"\n{white}Strength Comparison:")
    print(f"  Original: {original_score}/10")
    print(f"  Improved: {improved_score}/10")
    print(f"  Improvement: +{improved_score - original_score} points")
    
    copyap = input(f"Do you want to copy the improved password? (y): ")
    if copyap.lower() == "y":
        pyperclip.copy(improved_pass)
        print(f" Improved password copied to clipboard!")

        atv = input(f"Do you want to go to the vault (y): ")
        if atv.lower() == "y":
            vault()
        else:
            print("Going back to main menu")
            time.sleep(1)
            main()
    else: 
        print("Going back to main menu")
        time.sleep(1)
        main()

def vault():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vault_file = os.path.join(script_dir, "credentials.json")

    try:
        if not os.path.exists(vault_file):
            with open(vault_file, 'w') as f:
                json.dump([], f)
    except PermissionError:
        print(f"{red}[!] Permission Denied: Cannot write to vault file at '{vault_file}'")
        pause("Press Enter to return to main menu...")
        return
    except Exception as e:
        print(f"{red}[!] Unexpected error while creating vault file: {e}")
        pause("Press Enter to return to main menu")
        return

            
    # Load existing vault
    try:
        with open(vault_file, 'r') as f:
            vault_data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        vault_data = []
    
    while True:
        clear()
        printascii()
        print(Center.XCenter(f"""
        {white}
        
    [1] View Stored Credentials
    [2] Add New Credentials
    [3] Delete Credentials
    [4] Search Credentials
    [5] Return to Main Menu
        """))

        choice = input(f"""        ┌──({white}vault menu)─
 └─{white}""")
        
        if choice == "1":
       
            if not vault_data:
                print(f"\n{white}[!] Vault is empty. Add some credentials first.")
                pause()
                continue
                
            print(f"\n{white}Stored Credentials")
            for i, entry in enumerate(vault_data, 1):
                print(f"\n{white}[{i}] {entry.get('service', 'Unknown Service')}")
                print(f"  {white}Email: {entry.get('email', 'N/A')}")
                print(f"  {white}Password: {'*' * len(entry.get('password', ''))}")
            
           
            show_option = input(f"\n{white}Enter credential number to reveal password (or press Enter to continue): ")
            if show_option and show_option.isdigit() and 1 <= int(show_option) <= len(vault_data):
                idx = int(show_option) - 1
                print(f"\n{white}Service: {vault_data[idx].get('service', 'Unknown Service')}")
                print(f"{white}Email: {vault_data[idx].get('email', 'N/A')}")
                print(f"{white}Password: {vault_data[idx].get('password', 'N/A')}")
            
            pause()
            
        elif choice == "2":
            
            print(f"\n{white}Add new credentials")
            
            service = input(f"{white}Service/Website Name: ")
            email = input(f"{white}Email/Username: ")
            password = input(f"{white}Password: ")
            
            if not service or not email or not password:
                print(f"\n{red}[-] All fields are required!")
                pause()
                continue
                
            new_entry = {
                "service": service,
                "email": email,
                "password": password,
                "date_added": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            vault_data.append(new_entry)
            
          
            with open(vault_file, 'w') as f:
                json.dump(vault_data, f, indent=2)
                
            print(f"\n{green}[+] Credentials saved successfully!")
            pause()
            
        elif choice == "3":
          
            if not vault_data:
                print(f"\n{white}[!] Vault is empty. Nothing to delete.")
                pause()
                continue
            print(f"\n{white}Delete Credentials")
            for i, entry in enumerate(vault_data, 1):
                print(f"{white}[{i}] {entry.get('service', 'Unknown Service')} - {entry.get('email', 'N/A')}")
                
            delete_idx = input(f"\n{white}Enter credential number to delete (or press Enter to cancel): ")
            
            if delete_idx and delete_idx.isdigit() and 1 <= int(delete_idx) <= len(vault_data):
                idx = int(delete_idx) - 1
                deleted = vault_data.pop(idx)
                
                
                with open(vault_file, 'w') as f:
                    json.dump(vault_data, f, indent=2)
                    
                print(f"\n{green}[+] Deleted: {deleted.get('service', 'Unknown Service')} - {deleted.get('email', 'N/A')}")
            else:
                print(f"\n{white}[!] Deletion cancelled or invalid selection.")
                
            pause()
            
        elif choice == "4":
            
            if not vault_data:
                print(f"\n{white}[!] Vault is empty. Nothing to search.")
                pause()
                continue
                
            print(f"\n{white}Search Credentials")
            search_term = input(f"{white}Enter service name or email to search: ").lower()
            
            if not search_term:
                print(f"\n{red}[-] Search term required!")
                pause()
                continue
                
            results = []
            for entry in vault_data:
                if (search_term in entry.get('service', '').lower() or 
                    search_term in entry.get('email', '').lower()):
                    results.append(entry)
                    
            if results:
                print(f"\n{white}Found {len(results)} matching credentials:")
                for i, entry in enumerate(results, 1):
                    print(f"\n{white}[{i}] {entry.get('service', 'Unknown Service')}")
                    print(f"  {white}Email: {entry.get('email', 'N/A')}")
                    print(f"  {white}Password: {'*' * len(entry.get('password', ''))}")
                    
               
                show_option = input(f"\n{white}Enter result number to reveal password (or press Enter to continue): ")
                if show_option and show_option.isdigit() and 1 <= int(show_option) <= len(results):
                    idx = int(show_option) - 1
                    print(f"\n{white}Service: {results[idx].get('service', 'Unknown Service')}")
                    print(f"{white}Email: {results[idx].get('email', 'N/A')}")
                    print(f"{white}Password: {results[idx].get('password', 'N/A')}")
            else:
                print(f"\n{white}[!] No matching credentials found.")
                
            pause()
            
        elif choice == "5":
            print("Going back to main menu")
            time.sleep(1)
            main()
            
        else:
            print(f"\n{red}[-] Invalid option!")
            pause()

def generator():
    genpass = secrets.token_urlsafe(22)
    print(f"""
Generated Password: {genpass}""")
    copygen = input("Do you want to copy the generated password? (y): ")
    if copygen.lower() == "y":
        pyperclip.copy(genpass)
        print(f"Generated password copied to clipboard!")
        gpctm = input("enter to go back to main menu: ")
        if gpctm == "":
            print("going back to main menu")
            time.sleep(1)
            main()
        else:
            print("going back to main menu")
            time.sleep(1)
            main()
    else:
        print("going back to main menu")
        time.sleep(1)
        main()


def leakcheck():
    """
    Check if a password has been found in known data breaches
    Uses Have I Been Pwned API with k-anonymity (only sends first 5 chars of hash)
    """

    password = input(f"{white}Enter password to check: ")
    
    if not password:
        print(f"{red}[-] Please enter a password!")
        pause()
        return
    
    print(f"\n{white}Checking password against breach databases...")

    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"

    headers = {
            'User-Agent': 'Umbra-Password-Tool-v1.0'
        }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
            
            breach_count = 0
            
            for line in response.text.splitlines():
                if ':' in line:
                    returned_suffix, count = line.split(':')
                    if returned_suffix == hash_suffix:
                        breach_count = int(count)
                        break
            #come back rq
            if breach_count > 0:
                print(f"\n{red}[!] PASSWORD COMPROMISED!")
                print(f"{red}[!] This password was found in {breach_count:,} data breaches!")
                print(f"{red}[!] You should change this password immediately!")
                
              
                generate_new = input(f"\n{white}Would you like to generate a new secure password? (y): ")
                if generate_new.lower() == 'y':
                    generator()
                else:
                    print(f"{white}Going back to main menu")
                    time.sleep(1)
                    main()

            else:
                print(f"\n{green}[+] GOOD NEWS!")
                print(f"{green}[+] This password was not found in any known data breaches.")
                print(f"{green}[+] However, make sure it's still strong!")
                
                
                check_strength = input(f"\n{white}Would you like to rate the password? (y): ")
                if check_strength.lower() == 'y':
                   judge()
                else:
                    print("Going back to main menu")
                    time.sleep(1)
                    main()

def encrypter():
    echars = " " + string.punctuation + string.digits + string.ascii_letters
    echars = list(echars)
    key = echars.copy()

    random.shuffle(key)

    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = echars.index(letter)
        cipher_text += key[index]

    print(f"original message : {plain_text}")
    print(f"encrypted message: {cipher_text}")

    etm = input("enter to go back to main menu: ")
    if etm == "":
        print("going back to main menu")
        time.sleep(1)
        main()
    else:
        main()

def error():
    print(f"""
          {red}[-]{white} Invalid input, please try again.
          """)

# Display logo and initial menu
def intromenu():
    clear()
    printascii()
    choice()

# Main execution block
if __name__ == "__main__":
    # Input area
    def main():
        intromenu()

        ch = input(f""" ┌──({white}umbra tool)─
    └─{white}""")

        if ch == "1":
            judge()
            pause()
            
        elif ch == "2":
            advancer()
            pause()

        elif ch == "3":
            vault()
            pause()

        elif ch == "4":
            generator()
            pause()

        elif ch == "5":
            leakcheck()
            pause()

        elif ch == "6":
            encrypter()
            pause()

        else:
            error()
            pause()
            main()
main()