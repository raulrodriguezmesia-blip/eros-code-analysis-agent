import time
import sys
import os

def print_step(step_num, title, status, description):
    print(f"\n" + "="*60)
    print(f"🚀 [EROS AGENT] PHASE {step_num}: {title}")
    print(f"🧠 Microsoft Foundry IQ Reasoning Path...")
    time.sleep(1)
    
    # Simular efecto de escritura en la terminal
    for char in description:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    time.sleep(1.5)
    if status == "CRITICAL":
        print(f"❌ STATUS: [{status}] ⚠️ VULNERABILITY DETECTED!")
    elif status == "WARNING":
        print(f"⚠️ STATUS: [{status}]")
    else:
        print(f"✅ STATUS: [{status}]")
    print("="*60)
    time.sleep(1)

def start_simulation():
    # Limpiar la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🤖 INITIALIZING EROS CODE ANALYSIS AGENT v1.0.0...")
    print("🔗 Target Intel Layer: Microsoft Foundry IQ")
    print("📂 Loading input file: demo_input.py")
    time.sleep(2)
    
    print_step(
        1, "SYNTAX CHECK", "PASSED",
        "-> Analyzing abstract syntax tree (AST). No structural or indentation errors found."
    )
    
    print_step(
        2, "QUALITY REVIEW", "WARNING",
        "-> Checking PEP 8 compliance. Missing static type hints and docstrings detected."
    )
    
    print_step(
        3, "SECURITY AUDIT", "CRITICAL",
        "-> Scanning for OWASP Top 10 risks...\n"
        "🚨 CRITICAL ALERT: CWE-89 SQL Injection found in line 3!\n"
        "   Vector: query = 'SELECT * FROM users WHERE id=' + id"
    )
    
    print_step(
        4, "PERFORMANCE ANALYSIS", "OPTIMIZABLE",
        "-> Evaluating database query logic. 'SELECT *' is sub-optimal. Explicit columns recommended."
    )
    
    print_step(
        5, "REFACTORING & AUTO-VALIDATION", "COMPLETED",
        "-> Injecting secure parameterized code via Foundry Toolbox.\n"
        "👉 Running automated test_agent.py simulation...\n"
        "🎉 [SUCCESS] Verification passed with exit code 0!"
    )
    
    print("\n💾 Structured report exported successfully to: demo_output.json\n")

if __name__ == "__main__":
    start_simulation()
