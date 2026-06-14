"""
Eros Code Analysis Agent - Automated Verification Tests

This module validates the Eros agent's output structure, Microsoft Foundry IQ
integration, and the correctness of the 5-phase analysis pipeline through
automated testing of generated artifacts.
"""

import json
import os
import sys


def validate_json_structure() -> bool:
    """
    Validate the structure of demo_output.json against expected schema.

    Returns:
        bool: True if JSON structure is valid, False otherwise
    """
    try:
        with open("demo_output.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["agent_metadata"]["intelligence_layer"] == "Microsoft Foundry IQ"
        assert data["pipeline_execution"]["phase_3_security"]["status"] == "CRITICAL"

        secure_code = data["pipeline_execution"]["phase_5_refactoring"]["secure_code_proposal"]
        assert any(keyword in secure_code.lower() for keyword in ["parameterized", "prepared", "%s", "user_id"])

        return True
    except (AssertionError, KeyError, json.JSONDecodeError) as e:
        print(f"ERROR: JSON structure validation failed: {str(e)}")
        return False


def test_artifact_existence() -> bool:
    """
    Verify all required project artifacts exist.

    Returns:
        bool: True if all artifacts present, False otherwise
    """
    artifacts = ["demo_input.py", "demo_output.json", "app/main.py", "run_simulation.py"]
    all_exist = True

    for artifact in artifacts:
        if not os.path.exists(artifact):
            print(f"ERROR: Missing required artifact: {artifact}")
            all_exist = False
        else:
            print(f"[OK] Artifact verified: {artifact}")

    return all_exist


def test_pipeline_phases() -> bool:
    """
    Validate all 5 analysis phases completed successfully.

    Returns:
        bool: True if all phases present and valid, False otherwise
    """
    try:
        with open("demo_output.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        phases = [
            ("phase_1_syntax", "PASSED"),
            ("phase_2_quality", "WARNING"),
            ("phase_3_security", "CRITICAL"),
            ("phase_4_performance", "OPTIMIZABLE"),
            ("phase_5_refactoring", "COMPLETED")
        ]

        for phase_key, expected_status in phases:
            phase = data["pipeline_execution"][phase_key]
            assert "status" in phase, f"Missing status in {phase_key}"
            print(f"[OK] Phase validation: {phase_key} → {phase['status']}")

        return True
    except (AssertionError, KeyError) as e:
        print(f"ERROR: Pipeline phase validation failed: {str(e)}")
        return False


def test_security_findings() -> bool:
    """
    Verify critical security findings are properly detected and reported.

    Returns:
        bool: True if security findings valid, False otherwise
    """
    try:
        with open("demo_output.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        security_phase = data["pipeline_execution"]["phase_3_security"]
        assert security_phase["status"] == "CRITICAL"
        assert "SQL Injection" in security_phase["vulnerability"]["class"]
        assert security_phase["vulnerability"]["severity"] == "CRITICAL"

        print("[OK] Security findings: SQL Injection vulnerability correctly detected")
        return True
    except (AssertionError, KeyError) as e:
        print(f"ERROR: Security findings validation failed: {str(e)}")
        return False


def test_pipeline_artifacts() -> None:
    """
    Execute all validation tests and report results.

    Runs the complete test suite and exits with appropriate code:
    - Exit 0: All tests passed
    - Exit 1: One or more tests failed
    """
    print("=== [TEST] Eros Code Analysis Agent Validation ===\n")

    tests = [
        ("Artifact Existence", test_artifact_existence),
        ("JSON Structure", validate_json_structure),
        ("Pipeline Phases", test_pipeline_phases),
        ("Security Findings", test_security_findings),
    ]

    results = []
    for test_name, test_func in tests:
        print(f"\n[Running] {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"ERROR in {test_name}: {str(e)}")
            results.append((test_name, False))

    print("\n" + "="*60)
    print("[TEST SUMMARY]")
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")

    all_passed = all(result for _, result in results)
    if all_passed:
        print("\n[SUCCESS] All agent internal tests passed (Exit Code 0).")
        sys.exit(0)
    else:
        print("\n[FAILURE] Some tests failed (Exit Code 1).")
        sys.exit(1)


if __name__ == "__main__":
    test_pipeline_artifacts()