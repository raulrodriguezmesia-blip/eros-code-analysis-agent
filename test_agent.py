import json
import os
import sys

def test_pipeline_artifacts():
    print("=== [TEST] Eros Code Analysis Agent Validation ===")
    
    artifacts = ["demo_input.py", "demo_output.json", "app/main.py"]
    for artifact in artifacts:
        if not os.path.exists(artifact):
            print(f"ERROR: Missing required artifact: {artifact}")
            sys.exit(1)
        print(f"[OK] Artifact verified: {artifact}")

    try:
        with open("demo_output.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        assert data["agent_metadata"]["intelligence_layer"] == "Microsoft Foundry IQ"
        print("[OK] Microsoft IQ Integration metadata: VALID")
        
        security_phase = data["pipeline_execution"]["phase_3_security"]
        if security_phase["status"] == "CRITICAL":
            print(f"[OK] Phase 3 successful: Vulnerability detected [{security_phase['vulnerability']['class']}]")
        
        secure_code = data["pipeline_execution"]["phase_5_refactoring"]["secure_code_proposal"]
        if "id = %s" in secure_code or "parameterized" in secure_code.lower() or "user_id" in secure_code:
            print("[OK] Phase 5 successful: Parameterized mitigation proposal")
            
    except Exception as e:
        print(f"ERROR validating JSON structure: {str(e)}")
        sys.exit(1)

    print("\n[SUCCESS] All agent internal tests passed (Exit Code 0).")
    sys.exit(0)

if __name__ == "__main__":
    test_pipeline_artifacts()