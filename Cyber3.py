import re, random, string, hashlib, platform, os, time, socket, json, math

try:
    import requests
except:
    requests = None

from colorama import Fore, init
init(autoreset=True)

OWNER = "NIKAMHACKER"
LOG_FILE = "logs.txt"

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

 CYBERLAB V10 🚀
 Owner: {OWNER}
""")

# ========= LOG =========
def log(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{data}\n")

# ========= PASSWORD AI =========
def password_ai():
    pwd = input("Enter password: ")

    charset = 0
    if re.search(r"[a-z]", pwd): charset += 26
    if re.search(r"[A-Z]", pwd): charset += 26
    if re.search(r"[0-9]", pwd): charset += 10
    if re.search(r"[!@#$%^&*]", pwd): charset += 32

    entropy = len(pwd) * math.log2(charset) if charset else 0

    print(Fore.CYAN + f"Entropy: {round(entropy,2)} bits")

    if entropy < 40:
        print(Fore.RED + "Weak ❌")
    elif entropy < 70:
        print(Fore.YELLOW + "Medium ⚠")
    else:
        print(Fore.GREEN + "Strong 🔥")

# ========= PASSWORD GENERATOR =========
def password_gen():
    length = int(input("Length: ") or 12)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    print(Fore.GREEN + ''.join(random.choice(chars) for _ in range(length)))

# ========= HASH =========
def hash_tool():
    text = input("Enter text: ")
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

# ========= HASH CRACK (DEMO) =========
def hash_crack():
    print("Demo wordlist attack (legal use only)")
    h = input("Enter MD5 hash: ")

    wordlist = ["1234", "password", "admin", "nikam", "india"]

    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == h:
            print(Fore.GREEN + f"Found: {word}")
            return

    print(Fore.RED + "Not found in demo list")

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
        try:
            print("Public IP:", requests.get("https://api.ipify.org").text)
        except:
            print("Error")

    print("Local IP:", socket.gethostbyname(socket.gethostname()))

def ping_test():
    host = input("Enter host: ")
    os.system(f"ping -c 4 {host}")

def port_scan():
    print("\nScanning localhost...\n")
    for p in range(75, 90):
        s = socket.socket()
        if s.connect_ex(("127.0.0.1", p)) == 0:
            print(Fore.GREEN + f"Port {p} OPEN")
        s.close()

# ========= WIFI =========
def wifi_scan():
    try:
        data = os.popen("termux-wifi-scaninfo").read()
        nets = json.loads(data)
        for n in nets:
            print(Fore.GREEN + f"{n.get('ssid','Hidden')} | {n.get('level')} dBm")
    except:
        print("Install termux-api")

# ========= EXTRA TOOLS =========
def username_gen():
    name = input("Base name: ")
    for _ in range(5):
        print(name + str(random.randint(100,999)))

def notes():
    note = input("Write note: ")
    with open("notes.txt","a") as f:
        f.write(note + "\n")
    print("Saved")

def subdomain_finder():
    domain = input("Domain: ")
    subs = ["www", "mail", "ftp", "api", "test"]

    for s in subs:
        url = f"{s}.{domain}"
        try:
            socket.gethostbyname(url)
            print(Fore.GREEN + url)
        except:
            pass

# ========= SYSTEM =========
def system_info():
    print("OS:", platform.system())
    print("Machine:", platform.machine())

# ========= MAIN =========
def main():
    while True:
        banner()
        print("""
[1] Password AI
[2] Password Generator
[3] Hash Tool
[4] Hash Crack (Demo)
[5] IP Info
[6] Ping Test
[7] Port Scan
[8] WiFi Scan
[9] File Info
[10] Username Generator
[11] Subdomain Finder
[12] Notes
[13] System Info
[0] Exit
""")

        ch = input("root@nikam:~# ")

        if ch == "1": password_ai()
        elif ch == "2": password_gen()
        elif ch == "3": hash_tool()
        elif ch == "4": hash_crack()
        elif ch == "5": ip_info()
        elif ch == "6": ping_test()
        elif ch == "7": port_scan()
        elif ch == "8": wifi_scan()
        elif ch == "9": file_info()
        elif ch == "10": username_gen()
        elif ch == "11": subdomain_finder()
        elif ch == "12": notes()
        elif ch == "13": system_info()
        elif ch == "0": break
        else: print("Invalid")

        input("\nEnter...")

main()
