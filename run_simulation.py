"""
Eros Code Analysis Agent - Terminal Simulation Script

This module provides an interactive terminal animation demonstrating the 5-phase
reasoning path of the Eros code analysis agent. It visualizes each analysis phase
with real-time status updates and vulnerability detection examples.
"""

import time
import sys
import os


def print_step(step_num: int, title: str, status: str, description: str) -> None:
    """
    Print a single analysis phase with animated output.

    Args:
        step_num: Phase number (1-5)
        title: Phase title (e.g., "SYNTAX CHECK")
        status: Status indicator (PASSED, WARNING, CRITICAL, etc.)
        description: Detailed findings and analysis results
    """
    print(f"\n" + "="*60)
    print(f"🚀 [EROS AGENT] PHASE {step_num}: {title}")
    print(f"🧠 Microsoft Foundry IQ Reasoning Path...")
    time.sleep(1)

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


def start_simulation() -> None:
    """
    Execute the full 5-phase Eros analysis simulation with terminal animation.

    Simulates the complete code analysis pipeline:
    1. Syntax validation
    2. Quality review
    3. Security audit (vulnerability detection)
    4. Performance analysis
    5. Refactoring and validation
    """
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
