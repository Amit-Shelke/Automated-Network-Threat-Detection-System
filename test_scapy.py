# test_scapy.py
from scapy.all import sniff

def simple_print(packet):
    print(packet.summary())

# Replace "eth0" with your interface if needed (e.g., wlan0)
sniff(iface="eth0", prn=simple_print, count=5)
