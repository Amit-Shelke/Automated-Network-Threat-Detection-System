# detection_rules.py

from scapy.layers.inet import IP, TCP
from collections import defaultdict
import time
from logger import log_threat, block_ip

# Global dictionaries to track traffic patterns
syn_tracker = defaultdict(list)
port_scan_tracker = defaultdict(list)

# Private IP address prefixes for spoofing detection
private_ip_prefixes = ("10.", "172.", "192.168.")

# Invalid TCP flag combinations (example values)
invalid_flags = ["FPU", "SF", ""]  # FIN+PSH+URG, SYN+FIN, or nothing

def detect_threats(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags
        current_time = time.time()

        # --- SYN FLOOD DETECTION ---
        if flags == "S":
            syn_tracker[src_ip].append(current_time)
            print(f"[DEBUG] SYN from {src_ip} | Count: {len(syn_tracker[src_ip])}")

            # Keep only the last 5 seconds of data
            syn_tracker[src_ip] = [t for t in syn_tracker[src_ip] if current_time - t < 5]

            if len(syn_tracker[src_ip]) > 15:
                log_threat("POSSIBLE SYN FLOOD", src_ip)
                block_ip(src_ip)

        # --- PORT SCAN DETECTION ---
        port_scan_tracker[src_ip].append((dst_port, current_time))

        # Remove old entries
        port_scan_tracker[src_ip] = [
            (port, t) for port, t in port_scan_tracker[src_ip] if current_time - t < 5
        ]

        unique_ports = set([port for port, t in port_scan_tracker[src_ip]])

        if len(unique_ports) > 10:
            log_threat("PORT SCAN DETECTED", src_ip)
            block_ip(src_ip)

        # --- IP SPOOFING DETECTION ---
        if src_ip.startswith(private_ip_prefixes):
            log_threat("POSSIBLE IP SPOOFING", src_ip)

        # --- INVALID TCP FLAGS DETECTION ---
        flag_str = str(flags)
        if flag_str in invalid_flags:
            log_threat("INVALID TCP FLAGS DETECTED", src_ip)
