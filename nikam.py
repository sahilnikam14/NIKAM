import re
import random
import string
import hashlib
import platform
import os
import time
import socket
from colorama import Fore, Style, init

init(autoreset=True)

# Typing effect
def slow(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.02)
    print()

# Progress bar
def progress():
    for i in range(0, 101, 10):
        print(Fore.GREEN + f"[+] Loading {i}%", end="\r")
        time.sleep(0.2)
    print()

# Fake scan
def fake_scan():
    print(Fore.GREEN + "\n[+] Initializing...")
    time.sleep(0.5)
    print("[+] Scanning system...")
    time.sleep(0.5)
    print("[+] Gathering info...")
    time.sleep(0.5)
    print("[+] Done ✔")
    time.sleep(0.5)

# Fake IP info
def ip_info():
    print(Fore.CYAN + "\n[+] Fetching IP Info...")
    time.sleep(1)
    print("IP: 127.0.0.1")
    print("Location: Localhost")
    print("ISP: Internal Network")

# Banner
def banner():
    os.system("clear")
    print(Fore.GREEN + """
███████╗ █████╗ ██╗  ██╗██╗██╗
██╔════╝██╔══██╗██║  ██║██║██║
███████╗███████║███████║██║██║
╚════██║██╔══██║██╔══██║██║██║
███████║██║  ██║██║  ██║██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝

 💀 CYBERLAB ULTIMATE 💀
 🔥 Developed by Sahil Nikam 🔥
""")

# Password Checker
def check_password(pwd):
    fake_scan()
    score = 0
    if len(pwd) >= 12: score += 30
    if re.search(r"[A-Z]", pwd): score += 15
    if re.search(r"[a-z]", pwd): score += 15
    if re.search(r"[0-9]", pwd): score += 20
    if re.search(r"[!@#$%^&*]", pwd): score += 20

    print(Fore.CYAN + f"\nScore: {score}/100")

# Password Generator
def generate_password(length=12):
    progress()
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    print(Fore.GREEN + "\nPassword:", ''.join(random.choice(chars) for _ in range(length)))

# Hash Tool
def hash_text(text):
    progress()
    print(Fore.MAGENTA + "\nMD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

# System Info
def system_info():
    fake_scan()
    print(Fore.BLUE + "\nSystem:", platform.system())
    print("Machine:", platform.machine())

# File Analyzer
def file_info(file):
    progress()
    if os.path.exists(file):
        print(Fore.CYAN + f"\nFile size: {os.path.getsize(file)} bytes")
    else:
        print(Fore.RED + "\nFile not found")

# 🔐 Simple LOCAL Port Scanner (safe)
def port_scan():
    target = "127.0.0.1"
    print(Fore.YELLOW + f"\n[+] Scanning ports on {target}...\n")

    for port in range(75, 85):  # limited range (safe demo)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port}")
        s.close()

# MAIN LOOP
while True:
    banner()
    slow(Fore.GREEN + "[+] Booting Ultimate CyberLab...\n")

    print(Fore.YELLOW + """
[1] Password Checker
[2] Password Generator
[3] Hash Tool
[4] System Info
[5] File Analyzer
[6] IP Info (Demo)
[7] Local Port Scan (Safe)
[8] Exit
""")

    choice = input(Fore.WHITE + "root@sahil:~# ")

    if choice == "1":
        check_password(input("Enter password: "))
    elif choice == "2":
        generate_password(int(input("Length: ") or 12))
    elif choice == "3":
        hash_text(input("Enter text: "))
    elif choice == "4":
        system_info()
    elif choice == "5":
        file_info(input("Enter file path: "))
    elif choice == "6":
        ip_info()
    elif choice == "7":
        port_scan()
    elif choice == "8":
        print(Fore.GREEN + "\nShutting down...")
        break
    else:
        print(Fore.RED + "Invalid command")

    input(Fore.YELLOW + "\nPress Enter...")
