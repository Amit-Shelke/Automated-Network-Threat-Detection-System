# main.py
from scapy.all import sniff
from detection_rules import detect_threats

def process_packet(packet):
    detect_threats(packet)

# Replace 'eth0' with your actual interface (e.g., wlan0)
interface = "eth0"

print(f"[+] Starting packet capture on interface: {interface}")
sniff(iface=interface, prn=process_packet, store=False)
