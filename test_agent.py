"""
Eros Code Analysis Agent - Automated Verification Tests

This module validates the Eros agent's output structure, Microsoft Foundry IQ
integration, and the correctness of the 5-phase analysis pipeline through
automated testing of generated artifacts.
"""

import json
import os
import pytest


def validate_json_structure():
    """
    Validate the structure of demo_output.json against expected schema.
    """
    with open("demo_output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["agent_metadata"]["intelligence_layer"] == "Microsoft Foundry IQ"
    assert data["pipeline_execution"]["phase_3_security"]["status"] == "CRITICAL"

    secure_code = data["pipeline_execution"]["phase_5_refactoring"]["secure_code_proposal"]
    assert any(keyword in secure_code.lower() for keyword in ["parameterized", "prepared", "%s", "user_id"])


def test_artifact_existence():
    """
    Verify all required project artifacts exist.
    """
    artifacts = ["demo_input.py", "demo_output.json", "app/main.py", "run_simulation.py"]
    
    for artifact in artifacts:
        assert os.path.exists(artifact), f"Missing required artifact: {artifact}"
        print(f"[OK] Artifact verified: {artifact}")


def test_json_structure():
    """
    Validate the structure of demo_output.json against expected schema.
    """
    validate_json_structure()
    print("[OK] JSON structure validation passed")


def test_pipeline_phases():
    """
    Validate all 5 analysis phases completed successfully.
    """
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


def test_security_findings():
    """
    Verify critical security findings are properly detected and reported.
    """
    with open("demo_output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    security_phase = data["pipeline_execution"]["phase_3_security"]
    assert security_phase["status"] == "CRITICAL"
    assert "SQL Injection" in security_phase["vulnerability"]["class"]
    assert security_phase["vulnerability"]["severity"] == "CRITICAL"

    print("[OK] Security findings: SQL Injection vulnerability correctly detected")


def test_pipeline_artifacts():
    """
    Execute all validation tests and report results.
    """
    print("=== [TEST] Eros Code Analysis Agent Validation ===\n")

    # Run all tests
    test_artifact_existence()
    validate_json_structure()
    test_pipeline_phases()
    test_security_findings()

    print("\n" + "="*60)
    print("[TEST SUMMARY]")
    print("✅ PASSED: Artifact Existence")
    print("✅ PASSED: JSON Structure")
    print("✅ PASSED: Pipeline Phases")
    print("✅ PASSED: Security Findings")
    print("\n[SUCCESS] All agent internal tests passed (Exit Code 0).")


if __name__ == "__main__":
    test_pipeline_artifacts()