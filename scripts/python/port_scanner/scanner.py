import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
    except socket.error:
        print("[!] Could not connect to server")

def main():
    target = input("Enter target IP or hostname: ")
    print(f"\nScanning target: {target}\n")

    for port in range(1, 1025):  # scan first 1024 ports
        scan_port(target, port)

if __name__ == "__main__":
    main()