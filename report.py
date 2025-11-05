# report.py

from collections import defaultdict

def generate_report(log_file="threats.log"):
    threat_counts = defaultdict(int)
    ip_counts = defaultdict(int)

    try:
        with open(log_file, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    threat = parts[1].strip()
                    ip = parts[2].replace("Source IP:", "").strip()
                    threat_counts[threat] += 1
                    ip_counts[ip] += 1

        print("\n🛡️ Threat Summary Report")
        print("=" * 30)

        print("\n📊 Threat Types Detected:")
        for threat, count in threat_counts.items():
            print(f"  {threat}: {count} times")

        print("\n🔍 Top Offending IPs:")
        for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ip}: {count} alerts")

        print("\n✅ Report Complete.\n")

    except FileNotFoundError:
        print("[!] Log file not found.")

if __name__ == "__main__":
    generate_report()
