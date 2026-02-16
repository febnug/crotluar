from core.scanner import tcp_scan

COMMON_PORTS = [21,22,25,53,80,110,139,143,443,445,3389]

def run(target):
    print(f"[Recon] Scanning {target}")
    open_ports = tcp_scan(target, COMMON_PORTS)
    print(f"[Recon] Open ports: {open_ports}")
    return {"open_ports": open_ports}
