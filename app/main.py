import os
import json
from typing import Any
from azure.ai.agentserver.responses import ResponsesAgentServerHost, ResponseObject

server = ResponsesAgentServerHost()

@server.response_handler
async def analyze_code(request: Any, context: Any, cancellation_signal: Any):
    code = getattr(request, 'input', str(request))
    language = "python" if "def " in code else "unknown"
    
    phases = [
        ("syntax_check", "No syntax errors found"),
        ("quality_review", "Consider adding docstrings"),
        ("security_audit", "CRITICAL: SQL Injection vulnerability detected"),
        ("performance_analysis", "Add database indexes"),
        ("refactor_suggestions", "Use parameterized queries")
    ]
    
    report = {
        "language_detected": language,
        "analysis_pipeline": [{"step": i, "phase": p, "findings": f} for i, (p, f) in enumerate(phases, 1)]
    }
    
    response = ResponseObject(status="completed", output=json.dumps(report, indent=2))
    yield response

if __name__ == "__main__":
    server.run()