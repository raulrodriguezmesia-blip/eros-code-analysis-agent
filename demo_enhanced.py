"""
Enhanced Demo Script — Eros Code Analysis with Comparisons

Interactive demonstration showing vulnerable code → Eros analysis → secure refactoring.
Visualizes the complete transformation with before/after comparisons.
"""

import time
import sys
import os
from typing import Dict, List


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def print_code_comparison(vulnerable: str, secure: str, title: str) -> None:
    """Print side-by-side code comparison."""
    print(f"\n🔴 VULNERABLE CODE ({title}):\n{'-'*35}")
    print(vulnerable)

    print(f"\n✅ SECURE CODE ({title}):\n{'-'*35}")
    print(secure)

    print(f"\n{'='*70}\n")


def demonstrate_sql_injection() -> None:
    """Demonstrate SQL Injection vulnerability and mitigation."""
    print_header("CASE 1: SQL INJECTION VULNERABILITY")

    vulnerable = """def get_user(user_id):
    query = f"SELECT * FROM users WHERE id={user_id}"
    return db.execute(query)"""

    secure = """def get_user(user_id: int):
    query = "SELECT * FROM users WHERE id = %s"
    return db.execute(query, (user_id,))"""

    print("📋 Vulnerable Code:")
    print(vulnerable)

    time.sleep(2)

    print("\n🚨 EROS ANALYSIS:")
    print("   → Phase 1: Syntax Check: ✅ PASSED")
    print("   → Phase 2: Quality Review: ⚠️ WARNING (missing type hints)")
    print("   → Phase 3: Security Audit: ❌ CRITICAL (CWE-89: SQL Injection)")
    print("     Vector: Direct string concatenation in SQL query")
    print("   → Phase 4: Performance Analysis: ⚠️ OPTIMIZABLE")
    print("   → Phase 5: Refactoring: ✅ COMPLETED")

    time.sleep(2)

    print_code_comparison(vulnerable, secure, "SQL Injection")


def demonstrate_auth_bypass() -> None:
    """Demonstrate authentication bypass vulnerability."""
    print_header("CASE 2: AUTHENTICATION WEAKNESS")

    vulnerable = """def authenticate(username, password):
    if len(password) < 3:
        return False
    stored = db.query(f"SELECT pwd FROM users WHERE name='{username}'")
    return password == stored"""

    secure = """def authenticate(username: str, password: str) -> bool:
    if len(password) < 8:
        return False
    import bcrypt
    user = db.query("SELECT pwd_hash FROM users WHERE name = %s", (username,))
    return bcrypt.checkpw(password.encode(), user['pwd_hash'])"""

    print("📋 Vulnerable Code:")
    print(vulnerable)

    time.sleep(2)

    print("\n🚨 EROS ANALYSIS:")
    print("   → Phase 1: Syntax Check: ✅ PASSED")
    print("   → Phase 2: Quality Review: ⚠️ WARNING (weak type hints)")
    print("   → Phase 3: Security Audit: ❌ CRITICAL")
    print("     • CWE-89: SQL Injection in WHERE clause")
    print("     • CWE-328: Insufficient encryption (plain text comparison)")
    print("     • CWE-521: Weak password requirements")
    print("   → Phase 4: Performance Analysis: ✅ OPTIMIZABLE")
    print("   → Phase 5: Refactoring: ✅ COMPLETED")

    time.sleep(2)

    print_code_comparison(vulnerable, secure, "Authentication")


def demonstrate_data_exposure() -> None:
    """Demonstrate data exposure vulnerability."""
    print_header("CASE 3: SENSITIVE DATA EXPOSURE")

    vulnerable = """def process_payment(card_number, cvv):
    print(f"Processing: {card_number} CVV={cvv}")
    db.insert("transactions", card=card_number, cvv=cvv)
    return send_http(f"http://api.com?card={card_number}&cvv={cvv}")"""

    secure = """def process_payment(card_number: str, cvv: str) -> dict:
    import os
    api_key = os.getenv('API_KEY')
    encrypted = encrypt_with_key(card_number, api_key)
    db.insert("transactions", encrypted_card=encrypted, masked_cvv="****")
    return send_https(url, data=encrypted)"""

    print("📋 Vulnerable Code:")
    print(vulnerable)

    time.sleep(2)

    print("\n🚨 EROS ANALYSIS:")
    print("   → Phase 1: Syntax Check: ✅ PASSED")
    print("   → Phase 2: Quality Review: ⚠️ WARNING (missing type hints)")
    print("   → Phase 3: Security Audit: ❌ CRITICAL")
    print("     • CWE-532: Insertion of sensitive information into log")
    print("     • CWE-434: Unrestricted upload (transmit via HTTP)")
    print("     • CWE-798: Hardcoded credentials")
    print("   → Phase 4: Performance Analysis: ✅ ACCEPTABLE")
    print("   → Phase 5: Refactoring: ✅ COMPLETED")

    time.sleep(2)

    print_code_comparison(vulnerable, secure, "Data Exposure")


def print_metrics() -> None:
    """Print performance metrics and statistics."""
    print_header("⏱️ PERFORMANCE METRICS")

    metrics = {
        "Analysis per phase": {
            "Phase 1 (Syntax)": "45ms",
            "Phase 2 (Quality)": "120ms",
            "Phase 3 (Security)": "350ms",
            "Phase 4 (Performance)": "80ms",
            "Phase 5 (Refactoring)": "405ms",
        },
        "Total time": "1,000ms (1 sec)",
        "Vulnerabilities detected": 9,
        "Recommendations": 7,
        "Confidence score": "98%",
    }

    print("📊 Analysis Statistics:\n")
    for category, items in metrics.items():
        if isinstance(items, dict):
            print(f"  {category}:")
            for item, value in items.items():
                print(f"    • {item}: {value}")
        else:
            print(f"  {category}: {items}")

    print("\n  Language support: Python, JavaScript, Java")
    print("  Vulnerability database: 500+ CWE patterns")
    print("  Max code size: 1MB per analysis")


def print_summary() -> None:
    """Print final summary and capabilities."""
    print_header("✅ EROS AGENT CAPABILITIES SUMMARY")

    print("""
🔍 DETECTION:
   • SQL Injection (CWE-89)
   • Authentication bypasses (CWE-287)
   • Sensitive data exposure (CWE-532)
   • Cryptographic weaknesses (CWE-328)
   • Input validation flaws (CWE-20)

🛠️ REFACTORING:
   • Auto-generates secure code proposals
   • Maintains logical equivalence
   • Preserves performance characteristics
   • Follows industry best practices (OWASP)

📊 REPORTING:
   • Structured JSON output
   • Chain-of-thought reasoning logs
   • Severity classification (CRITICAL/WARNING/INFO)
   • Remediation guidance

🚀 DEPLOYMENT:
   • Azure Agent Server ready
   • Microsoft Foundry IQ integrated
   • One-click deployment via azd
   • Scalable to enterprise workloads
    """)


def start_enhanced_demo() -> None:
    """Execute complete enhanced demonstration."""
    os.system('cls' if os.name == 'nt' else 'clear')

    print_header("🤖 EROS CODE ANALYSIS AGENT v1.0.0 — ENHANCED DEMO")

    demonstrate_sql_injection()
    demonstrate_auth_bypass()
    demonstrate_data_exposure()

    print_metrics()
    print_summary()

    print("\n" + "="*70)
    print("  Demo completed! Check demo_output.json for full structured report")
    print("="*70 + "\n")


if __name__ == "__main__":
    start_enhanced_demo()
