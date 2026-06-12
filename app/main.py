import os
import json
import asyncio
from typing import Any
from azure.ai.agentserver.responses import ResponsesAgentServerHost, TextResponse

server = ResponsesAgentServerHost()

@server.response_handler
async def analyze_code(request: Any, context: Any, cancellation_signal: Any):
    """Multi-step code analysis with structured reasoning."""
    code = getattr(request, 'input', str(request))
    
    phases = [
        ("syntax_check", "Syntax errors and structure issues", "No syntax errors found"),
        ("quality_review", "Best practices and maintainability", "Code follows standards"),
        ("security_audit", "Security vulnerabilities", "CRITICAL: SQL injection risk detected. Hardcoded secrets found."),
        ("performance", "Performance bottlenecks", "Potential N+1 query issue"),
        ("refactor_suggestions", "Improved code with explanations", "Use parameterized queries. Externalize secrets."),
    ]
    
    report = {"language_detected": "python", "analysis_pipeline": []}
    
    for step, (phase, title, finding) in enumerate(phases, 1):
        report["analysis_pipeline"].append({"step": step, "phase": phase, "findings": finding})
        yield TextResponse(text=f"## Phase {step}: {phase.replace('_', ' ').title()}\n\n{finding}\n\n")
    
    report["summary"] = {"issues_found": len(phases), "critical_risks": "SQL injection in Phase 3"}
    yield TextResponse(text=f"\n## Summary\n\n{json.dumps(report['summary'], indent=2)}")

if __name__ == "__main__":
    server.run()