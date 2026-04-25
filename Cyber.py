import re, random, string, hashlib, platform, os, time, socket, json, math
from datetime import datetime
from getpass import getpass

try:
    import requests
except:
    requests = None

from colorama import Fore, init
init(autoreset=True)

OWNER = "Sahil Nikam"
USER_FILE = "secure_user.json"
LOG_FILE = "logs.txt"

STATS = {"password_checks": 0, "scans": 0, "tools_used": 0}

# ========= UI =========
def clear():
    os.system("clear")

def banner():
    clear()
    print(Fore.GREEN + f"""
███╗   ██╗██╗██╗  ██╗ █████╗ ███╗   ███╗
████╗  ██║██║██║ ██╔╝██╔══██╗████╗ ████║
██╔██╗ ██║██║█████╔╝ ███████║██╔████╔██║
██║╚██╗██║██║██╔═██╗ ██╔══██║██║╚██╔╝██║
██║ ╚████║██║██║  ██╗██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

🔥 NIKAMHACKER V5 GOD+ 🚀
Owner: {OWNER}
""")

# ========= LOG =========
def log(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {data}\n")

# ========= AUTH =========
def setup_user():
    if not os.path.exists(USER_FILE):
        print("🔐 First Setup\n")
        user = input("Create Username: ")
        pwd = getpass("Create Password: ")
        data = {
            "user": user,
            "pass": hashlib.sha256(pwd.encode()).hexdigest()
        }
        with open(USER_FILE, "w") as f:
            json.dump(data, f)

def login():
    setup_user()
    banner()
    print("🔐 LOGIN\n")

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
    crack_time = 2**entropy / 1e9

    print(Fore.CYAN + f"Entropy: {round(entropy,2)} bits")
    print(Fore.MAGENTA + f"Crack Time (est): {round(crack_time,2)} sec")

    if len(pwd) < 12: print(Fore.YELLOW + "Use 12+ chars")
    if not re.search(r"[A-Z]", pwd): print(Fore.YELLOW + "Add uppercase")
    if not re.search(r"[0-9]", pwd): print(Fore.YELLOW + "Add numbers")

    bars = int(min(entropy,100)/10)
    print(Fore.GREEN + "Strength: [" + "█"*bars + "-"*(10-bars) + "]")

    log("Password checked")

# ========= GENERATOR =========
def password_generator():
    length = int(input("Length: ") or 12)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    print("Generated:", ''.join(random.choice(chars) for _ in range(length)))

# ========= HASH =========
def hash_tool():
    text = input("Enter text: ")
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

# ========= FILE =========
def file_info():
    path = input("File path: ")
    if os.path.exists(path):
        print("Size:", os.path.getsize(path))
    else:
        print("Not found")

# ========= NETWORK =========
def ip_info():
    if requests:
        print("Public IP:", requests.get("https://api.ipify.org").text)
    print("Local IP:", socket.gethostbyname(socket.gethostname()))

def port_scan():
    for p in range(75, 90):
        s = socket.socket()
        if s.connect_ex(("127.0.0.1", p)) == 0:
            print("OPEN:", p)
        s.close()

def dns_lookup():
    d = input("Domain: ")
    print("IP:", socket.gethostbyname(d))

def ping():
    os.system(f"ping -c 4 {input('Host: ')}")

# ========= WIFI =========
def wifi_scan():
    try:
        nets = json.loads(os.popen("termux-wifi-scaninfo").read())
        for n in nets:
            print(n.get("ssid"), "|", n.get("level"))
    except:
        print("Install termux-api")

# ========= SYSTEM =========
def system_info():
    print(platform.system(), platform.machine())

def tool_check():
    for t in ["nmap", "git", "python"]:
        print(t, "✔" if os.system(f"which {t} > /dev/null")==0 else "❌")

def auto_install():
    os.system("pkg update -y && pkg install nmap git python -y")

# ========= STATS =========
def stats():
    print(STATS)

def logs():
    print(open(LOG_FILE).read() if os.path.exists(LOG_FILE) else "No logs")

# ========= MAIN =========
def main():
    while True:
        banner()
        print("""
[1] Password AI
[2] Generator
[3] Hash
[4] WiFi
[5] IP
[6] Port Scan
[7] DNS
[8] Ping
[9] System
[10] File Info
[11] Tool Check
[12] Install Tools
[13] Stats
[14] Logs
[0] Exit
""")

        ch = input("root@nikamhacker:~# ")

        actions = {
            "1": password_ai, "2": password_generator, "3": hash_tool,
            "4": wifi_scan, "5": ip_info, "6": port_scan,
            "7": dns_lookup, "8": ping, "9": system_info,
            "10": file_info, "11": tool_check, "12": auto_install,
            "13": stats, "14": logs
        }

        if ch == "0":
            break
        elif ch in actions:
            STATS["tools_used"] += 1
            actions[ch]()
        else:
            print("Invalid")

        input("\nEnter...")

# ========= RUN =========
login()
main()
