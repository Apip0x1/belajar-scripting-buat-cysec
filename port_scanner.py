import socket
import sys

url = input("input url target : ").strip().lower()

def port_scanner(host, port):
    try:
        # 2. Membuat objek socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout untuk mencegah hang

        # 3. Mencoba untuk terhubung ke host dan port
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error: {e}")

print (f"[*] Starting port scan on {url}...")

for port in range(1, 1025):
    print(f"sedang memeriksa port : {port}", end="\r")
    sys.stdout.flush()  #
    port_scanner(url, port)
print (f"[*] Port scan completed on {url}.")