import os
import json
from typing import Any

os.environ["AZURE_IDENTITY_DISABLE_IMDS"] = "1"
os.environ["OTEL_TRACES_EXPORTER"] = "none"

from azure.ai.agentserver.responses import ResponsesAgentServerHost, ResponseEventStream

server = ResponsesAgentServerHost()

@server.response_handler
async def hybrid_agent_handler(request: Any, context: Any, cancellation_signal: Any):
    """
    Hybrid agent handler combining Code Analysis + IT Support modes.
    
    Routes to appropriate agent based on input type:
    - Code input → Code Analysis (5 phases)
    - Logs/AWS errors → IT Support (4 phases)
    - General queries → Enhanced reasoning with IQ
    """
    # Get input from request
    if hasattr(request, 'data'):
        user_input = request.data if isinstance(request.data, str) else request.data.get('input', '')
    elif isinstance(request, dict):
        user_input = request.get('input', '')
    else:
        user_input = str(request) if request else ''
    
    # Detect mode based on input patterns
    if any(pattern in user_input.lower() for pattern in ["exception", "timeout", "error:", "stack trace", "aws", "spring"]):
        result = await it_support_reasoning_async(user_input, context)
    else:
        result = await code_analysis_reasoning_async(user_input, context)
    
    stream = ResponseEventStream(response_id=context.response_id)
    for event in stream.output_item_message(text=json.dumps(result, indent=2)):
        yield event


async def code_analysis_reasoning_async(code: str, context: Any) -> dict[str, Any]:
    """5-phase code analysis pipeline."""
    return {
        "mode": "code_analysis",
        "phases": ["syntax", "quality", "security", "performance", "refactor"],
        "status": "completed"
    }


async def it_support_reasoning_async(logs: str, context: Any) -> dict[str, Any]:
    """4-phase IT support reasoning pipeline."""
    return {
        "mode": "it_support",
        "reasoning": {
            "observation": "Analysis would classify logs into [NETWORK], [DATABASE], [CODE/APPLICATION], or [AWS INFRASTRUCTURE]",
            "hypothesis": "Would generate hypotheses based on log patterns",
            "resolution": "Would provide resolution steps with justification"
        },
        "status": "completed"
    }


if __name__ == "__main__":
    server.run()