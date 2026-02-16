import socket

def run(target):
    print(f"[SMB] Checking SMB on {target}")
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, 445))
        sock.close()
        print("[SMB] Port 445 open")
        return {"smb_open": True}
    except:
        print("[SMB] Port 445 closed")
        return {"smb_open": False}
