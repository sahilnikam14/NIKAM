import os

def menu():
    print("\n======================")
    print("  MY SECURITY TOOLKIT")
    print("======================")
    print("1. IP Info")
    print("2. Domain Info")
    print("3. Password Check")
    print("4. Exit")

while True:
    os.system("clear")
    menu()

    choice = input("\nSelect: ")

    if choice == "1":
        ip = input("Enter IP: ")
        os.system(f"curl ipinfo.io/{ip}")

    elif choice == "2":
        domain = input("Enter domain: ")
        os.system(f"nslookup {domain}")

    elif choice == "3":
        pwd = input("Enter password: ")
        print("Use your password checker script")

    elif choice == "4":
        break

    else:
        print("Invalid option")
