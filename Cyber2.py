import re, random, string, hashlib, platform, os, time, socket, json, math
from getpass import getpass
from datetime import datetime

try:
    import requests
except:
    requests = None

from colorama import Fore, init
init(autoreset=True)

OWNER = "Sahil Nikam"
USER_FILE = "user.json"
LOG_FILE = "logs.txt"

STATS = {
    "password_checks": 0,
    "scans": 0
}

# ========= UI =========
def clear():
    os.system("clear")

def banner():
    clear()
    print(Fore.GREEN + f"""
 CYBERLAB GOD MODE v2 😈
 Owner: {OWNER}
""")

# ========= LOG =========
def log(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {data}\n")

# ========= AUTH =========
def register():
    banner()
    print("🔐 Register\n")
    user = input("Username: ")
    pwd = getpass("Password: ")

    data = {"user": user, "pass": hashlib.sha256(pwd.encode()).hexdigest()}
    with open(USER_FILE, "w") as f:
        json.dump(data, f)

def login():
    if not os.path.exists(USER_FILE):
        register()

    banner()
    print("🔐 Login\n")

    user = input("Username: ")
    pwd = getpass("Password: ")

    with open(USER_FILE) as f:
        data = json.load(f)

    if user == data["user"] and hashlib.sha256(pwd.encode()).hexdigest() == data["pass"]:
        print(Fore.GREEN + "Access Granted ✅")
        time.sleep(1)
    else:
        print(Fore.RED + "Access Denied ❌")
        exit()

# ========= PASSWORD AI =========
def password_ai():
    pwd = input("Enter password: ")
    STATS["password_checks"] += 1

    charset = 0
    if re.search(r"[a-z]", pwd): charset += 26
    if re.search(r"[A-Z]", pwd): charset += 26
    if re.search(r"[0-9]", pwd): charset += 10
    if re.search(r"[!@#$%^&*]", pwd): charset += 32

    entropy = len(pwd) * math.log2(charset) if charset else 0

    print(Fore.CYAN + f"Entropy: {round(entropy,2)} bits")

    # suggestions
    if len(pwd) < 12:
        print(Fore.YELLOW + "Use 12+ chars")
    if not re.search(r"[A-Z]", pwd):
        print(Fore.YELLOW + "Add uppercase")
    if not re.search(r"[0-9]", pwd):
        print(Fore.YELLOW + "Add numbers")

    bars = int(min(entropy,100)/10)
    print(Fore.GREEN + "Strength: [" + "█"*bars + "-"*(10-bars) + "]")

    log("Password checked")

# ========= FILE =========
def file_integrity():
    path = input("File path: ")

    if not os.path.exists(path):
        print("Not found")
        return

    size = os.path.getsize(path)
    with open(path, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()

    print("Size:", size, "bytes")
    print("SHA256:", sha)

# ========= WIFI =========
def wifi_scan():
    print("\n📡 WiFi Scan\n")
    try:
        data = os.popen("termux-wifi-scaninfo").read()
        nets = json.loads(data)
        for n in nets:
            print(Fore.GREEN + f"{n.get('ssid','Hidden')} | {n.get('level')} dBm")
        STATS["scans"] += 1
    except:
        print("Install termux-api")

# ========= NETWORK =========
def ip_info():
    if requests:
        try:
            print("Public IP:", requests.get("https://api.ipify.org").text)
        except:
            print("Network error")

    print("Local IP:", socket.gethostbyname(socket.gethostname()))

def port_scan():
    print("\nScanning...\n")
    for p in range(75, 90):
        s = socket.socket()
        if s.connect_ex(("127.0.0.1", p)) == 0:
            print(Fore.GREEN + f"Port {p} OPEN")
        s.close()

# ========= SYSTEM =========
def system_info():
    print("OS:", platform.system())
    print("Machine:", platform.machine())

# ========= TOOLS =========
def tool_check():
    tools = ["nmap", "git", "python"]
    for t in tools:
        if os.system(f"which {t} > /dev/null 2>&1") == 0:
            print(Fore.GREEN + f"{t} ✔")
        else:
            print(Fore.RED + f"{t} ❌")

# ========= STATS =========
def stats():
    print("\n📊 Session Stats\n")
    print("Password checks:", STATS["password_checks"])
    print("Scans:", STATS["scans"])

# ========= LOGS =========
def view_logs():
    if os.path.exists(LOG_FILE):
        print(open(LOG_FILE).read())
    else:
        print("No logs")

# ========= MAIN =========
def main():
    while True:
        banner()
        print("""
[1] Password AI
[2] WiFi Scan
[3] IP Info
[4] Port Scan
[5] System Info
[6] File Integrity
[7] Tool Check
[8] Stats
[9] Logs
[0] Exit
""")

        ch = input("root@godv2:~# ")

        if ch == "1":
            password_ai()
        elif ch == "2":
            wifi_scan()
        elif ch == "3":
            ip_info()
        elif ch == "4":
            port_scan()
        elif ch == "5":
            system_info()
        elif ch == "6":
            file_integrity()
        elif ch == "7":
            tool_check()
        elif ch == "8":
            stats()
        elif ch == "9":
            view_logs()
        elif ch == "0":
            break
        else:
            print("Invalid")

        input("\nEnter...")

# ========= RUN =========
login()
