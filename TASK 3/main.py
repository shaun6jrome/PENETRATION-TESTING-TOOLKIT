from modules import port_scanner, brute_forcer

def main():
    print("📦 Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. FTP Brute-Forcer")
    choice = input("Choose a module (1 or 2): ")

    if choice == "1":
        host = input("Enter target host (e.g., 127.0.0.1): ")
        ports = range(20, 1025)
        result = port_scanner.scan_ports(host, ports)
        if result:
            print(f"✅ Open ports: {result}")
        else:
            print("❌ No open ports found.")
    elif choice == "2":
        host = input("Enter FTP host (e.g., ftp.example.com): ")
        username = input("Enter FTP username: ")
        try:
            with open("passwords.txt", "r") as f:
                passwords = f.readlines()
            brute_forcer.brute_force_ftp(host, username, passwords)
        except FileNotFoundError:
            print("❌ 'passwords.txt' file not found.")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()