# 🛡️ Network Threat Detection System (NTDS)

A real-time Linux-based network threat detection system built using Python, Scapy, Flask, and iptables. This project captures live network traffic, detects suspicious activity like SYN floods, port scans, IP spoofing, and invalid TCP flags, and automatically blocks the attacker’s IP while providing logs, reports, and a web dashboard for monitoring.

---

## 🚀 Features

- 📡 Real-time packet sniffing using Scapy
- 🧠 Intelligent threat detection:
  - SYN Floods
  - Port Scans
  - IP Spoofing
  - Invalid TCP Flag combinations
- 🔐 Auto-blocking IPs using `iptables`
- 🗂️ Logging all threats to `threats.log`
- 📊 Terminal-based report generator
- 🌐 Flask-based web dashboard with graphs
- 📁 Clean modular architecture

---

## 🛠️ Technologies Used

| Component         | Tech Used            |
|------------------|----------------------|
| Language         | Python 3             |
| Packet Sniffing  | Scapy                |
| Web Server       | Flask                |
| Charts           | Chart.js             |
| Firewall Control | iptables (Linux)     |
| UI Styling       | Bootstrap (CDN)      |
| OS               | Kali Linux / Linux   |

---

## 📸 Architecture

![Network Threat Detection System - Architecture](./images/ntds-architecture.png)

> Diagram showing the flow of data from packet capture → threat detection → logging/blocking → report/dashboard.

---

## 📂 Project Structure

NetworkThreatDetectorSystem(NTDS)/
├── main.py                     # Starts packet sniffer

├── detection_rules.py          # Defines threat detection logic

├── logger.py                   # Handles alerts, logging, and IP blocking

├── report.py                   # Generates CLI summary from logs

├── threats.log                 # Log file for all alerts

├── blocked_ips.txt             # List of blocked attacker IPs
   |─ dashboard/
     ├── app.py                    # Flask server for web dashboard

     ├── templates/
           └── index.html              # Web dashboard UI
           └── static/                   # (Optional) Chart.js/Bootstrap assets
     └── images/
            └── ntds-architecture.png       # Diagram for README.md


---



⚙️ How It Works
1. main.py starts sniffing live packets using Scapy.

2. Each packet is sent to detection_rules.py, where rules check for SYN floods, port scans, spoofing, and bad flags.

3. If a threat is found:
    - An alert is printed and logged (threats.log)
    - The source IP is blocked via iptables and saved to blocked_ips.txt

4. The report.py can be used to generate a terminal-based report summary.

5. The dashboard/app.py (Flask) serves a live dashboard to visualize all the threats.

---

📊 Web Dashboard
Features:

Total threats detected

Bar chart of threat types

Pie chart of top attacker IPs

Auto-refresh every 10s (optional)


📸 Screenshot:


<img width="1920" height="1025" alt="Screenshot_2025-07-13_14_18_16" src="https://github.com/user-attachments/assets/86e6fa68-87c0-44b4-acf9-8dacb292efaa" />
---
<img width="1170" height="1015" alt="Screenshot_2025-07-13_14_55_58" src="https://github.com/user-attachments/assets/c74c524b-7313-453e-a8a0-34c690324d24" />
---
<img width="1920" height="1025" alt="Screenshot_2025-07-11_15_12_08" src="https://github.com/user-attachments/assets/f5cbec3c-f943-40fb-97f4-48b29b3b59f2" />

---

🔁 FULL WORKFLOW (Step-by-Step)
Here’s how your full system works from top to bottom:

                ┌──────────────────────────────┐
                │          User                │
                └────────────┬─────────────────┘
                             │
                        Run main.py
                             │
               ┌────────────▼────────────┐
               │ Scapy captures packets  │ ← (sniff)
               └────────────┬────────────┘
                             │
               ┌────────────▼────────────┐
               │ detect_threats()        │ ← detection_rules.py
               │ (SYN flood? Port scan?) │
               └────────────┬────────────┘
                             │
     ┌──────────────────────▼───────────────────────┐
     │ If threat detected:                          │
     │   ├── Print alert to terminal                │
     │   ├── Log to threats.log                     │
     │   └── Block IP using iptables                │ ← logger.py
     └──────────────────────┬───────────────────────┘
                             │
         ┌──────────────────▼─────────────────┐
         │ View logs in CLI (report.py)       │
         └──────────────────┬─────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │ View graphs in browser (dashboard/)    │ ← Flask + Chart.js
        └────────────────────────────────────────┘
        
      
        ---
        
        ⚠️ DISCLAIMER:
        The Network Threat Detection System (NTDS) is intended only for educational and ethical purposes. Do NOT use this tool on real systems, networks, or data without explicit permission. Misuse can be illegal.
        
        ---
        
        🧑‍💻 AUTHOR:
        Mohit Nigote
        CyberSec $ Linux Enthusiast
        📧 - mohitnigote461001@gmail.com (use real if public)
        💻 GitHub:- ngmohit2003.
        x-x
        MN.


