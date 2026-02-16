import socket

def run(target):
    print(f"[Lateral] Checking WinRM & SSH on {target}")
    for port in [22, 5985]:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"[Lateral] Port {port} open")
            sock.close()
        except:
            pass
