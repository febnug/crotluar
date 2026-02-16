import socket

def tcp_scan(target, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports
