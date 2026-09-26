import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousHoneypotCanarySentinelClient

def main():
    client = AutonomousHoneypotCanarySentinelClient()
    res = client.verify_canary_integrity()
    print("=== Autonomous Honeypot Canary Sentinel Output ===")
    print(f"Session: {res['session_id']} | Canary: {res['canary_token_inspected']}")
    print(f"Compromised: {res['canary_compromised']} (Status: {res['integrity_status']})")
    print(f"Severity: {res['threat_severity']} | Action: {res['automated_response']}")

if __name__ == '__main__':
    main()
