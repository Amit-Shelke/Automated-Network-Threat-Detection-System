# logger.py

from datetime import datetime

def log_threat(threat_type, src_ip):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{now} | {threat_type} | Source IP: {src_ip}"

    print(log_entry)

    with open("threats.log", "a") as f:
        f.write(log_entry + "\n")

import subprocess

# Set to store blocked IPs in-memory
blocked_ips = set()

def block_ip(ip):
    if ip not in blocked_ips:
        print(f"[+] Blocking IP: {ip}")
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            with open("blocked_ips.txt", "a") as f:
                f.write(ip + "\n")
            blocked_ips.add(ip)
        except Exception as e:
            print(f"[!] Failed to block {ip}: {e}")
