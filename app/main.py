import os
# Disable telemetry BEFORE importing azure SDK
os.environ["AZURE_IDENTITY_DISABLE_IMDS"] = "1"
os.environ["OTEL_TRACES_EXPORTER"] = "none"

import json
from typing import Any
from azure.ai.agentserver.responses import ResponsesAgentServerHost, ResponseEventStream

server = ResponsesAgentServerHost()

@server.response_handler
async def analyze_code(request: Any, context: Any, cancellation_signal: Any):
    report = {
        "language_detected": "python",
        "analysis_pipeline": [
            {"step": 1, "phase": "syntax_check", "findings": "No syntax errors found"},
            {"step": 2, "phase": "quality_review", "findings": "Consider adding docstrings"},
            {"step": 3, "phase": "security_audit", "findings": "CRITICAL: SQL Injection vulnerability detected"},
            {"step": 4, "phase": "performance_analysis", "findings": "Add database indexes"},
            {"step": 5, "phase": "refactor_suggestions", "findings": "Use parameterized queries"}
        ]
    }
    
    stream = ResponseEventStream(response_id=context.response_id)
    for event in stream.output_item_message(text=json.dumps(report, indent=2)):
        yield event

if __name__ == "__main__":
    server.run()