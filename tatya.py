import re
import random
import string
import hashlib
import platform
import os
import time
import socket

# safe import (requests optional)
try:
    import requests
except:
    requests = None

from colorama import Fore, init
init(autoreset=True)

OWNER = "Sahil Nikam"

# ========= UI =========
def clear():
    os.system("clear")

def banner():
    clear()
    print(Fore.GREEN + f"""
 ██████╗ ██████╗ ██████╗ ███╗   ███╗
██╔════╝██╔═══██╗██╔══██╗████╗ ████║
██║     ██║   ██║██████╔╝██╔████╔██║
██║     ██║   ██║██╔═══╝ ██║╚██╔╝██║
╚██████╗╚██████╔╝██║     ██║ ╚═╝ ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝

 CYBERLAB GOD MODE 😈
 Owner: {OWNER}
""")

def loading():
    for i in range(101):
        print(Fore.GREEN + f"\r[+] Booting... {i}%", end="")
        time.sleep(0.01)
    print("\n")

# ========= LOGIN =========
def login():
    banner()
    print(Fore.CYAN + "\n🔐 LOGIN\n")
    user = input("Username: ")
    pwd = input("Password: ")

    if user != "admin" or pwd != "1234":
        print(Fore.RED + "Access Denied ❌")
        exit()

# ========= AI PASSWORD =========
def ai_password(pwd):
    score = 0

    if len(pwd) >= 12: score += 25
    if re.search(r"[A-Z]", pwd): score += 15
    if re.search(r"[a-z]", pwd): score += 15
    if re.search(r"[0-9]", pwd): score += 15
    if re.search(r"[!@#$%^&*]", pwd): score += 15

    entropy = len(set(pwd)) * len(pwd)

    print(Fore.CYAN + f"\nScore: {score}/100")
    print(Fore.MAGENTA + f"Entropy: {entropy}")

    bars = int(score / 10)
    print(Fore.GREEN + "Strength: [" + "█"*bars + "-"*(10-bars) + "]")

    if score < 50:
        print(Fore.RED + "Weak ❌")
    elif score < 80:
        print(Fore.YELLOW + "Medium ⚠")
    else:
        print(Fore.GREEN + "Strong 🔥")

def password_menu():
    pwd = input("Enter password: ")
    ai_password(pwd)

# ========= NETWORK =========
def ip_info():
    if requests is None:
        print("Install requests to use this feature")
        return

    try:
        ip = requests.get("https://api.ipify.org").text
        print("Public IP:", ip)
    except:
        print("Error fetching IP")

def port_scan():
    print("\nScanning localhost...\n")
    for port in range(75, 90):
        s = socket.socket()
        s.settimeout(0.3)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            print(Fore.GREEN + f"Port {port} OPEN")
        s.close()

# ========= SYSTEM =========
def system_info():
    print("OS:", platform.system())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

# ========= TOOL CHECK =========
def tool_check():
    tools = ["nmap", "git", "python"]
    for t in tools:
        if os.system(f"which {t} > /dev/null 2>&1") == 0:
            print(Fore.GREEN + f"{t} OK")
        else:
            print(Fore.RED + f"{t} Missing")

# ========= MAIN =========
def main():
    while True:
        banner()
        print(Fore.CYAN + """
[1] AI Password Analyzer
[2] IP Info
[3] Port Scan
[4] System Info
[5] Tool Check
[6] Exit
""")

        ch = input("root@godmode:~# ")

        if ch == "1":
            password_menu()
        elif ch == "2":
            ip_info()
        elif ch == "3":
            port_scan()
        elif ch == "4":
            system_info()
        elif ch == "5":
            tool_check()
        elif ch == "6":
            break
        else:
            print("Invalid")

        input("\nEnter to continue...")

# ========= RUN =========
login()
loading()
main()
