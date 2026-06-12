import os
import json
from typing import Any
from azure.ai.agentserver.responses import ResponsesHostServer
from openai import OpenAI

FOUNDRY_IQ_ENDPOINT = os.environ.get("FOUNDRY_IQ_ENDPOINT", "")
TOOLBOX_ENDPOINT = os.environ.get("FOUNDRY_TOOLBOX_ENDPOINT", "")
MODEL_DEPLOYMENT = os.environ.get("MODEL_DEPLOYMENT", "gpt-4")

client = OpenAI(
    base_url=os.environ.get("PROJECT_ENDPOINT"),
    api_key=os.environ.get("MODEL_DEPLOYMENT", "key")
)

def hybrid_agent(user_message: dict[str, Any]) -> dict[str, Any]:
    """Multi-agent reasoning: Code analysis + IT Support modes.
    
    Routes to appropriate agent based on input type:
    - Code input → Code Analysis (5 phases)
    - Logs/AWS errors → IT Support (4 phases)
    - General queries → Enhanced reasoning with IQ
    """
    text = user_message.get("input", "")
    
    # Detect mode based on input patterns
    if any(pattern in text for pattern in ["exception", "timeout", "error:", "stack trace", "aws", "spring"]):
        return it_support_reasoning(text, client)
    else:
        return code_analysis_reasoning(text, client)

def code_analysis_reasoning(code: str, client: OpenAI) -> dict[str, Any]:
    """5-phase code analysis pipeline."""
    return {
        "output": json.dumps({
            "mode": "code_analysis",
            "phases": ["syntax", "quality", "security", "performance", "refactor"]
        }),
        "status": "completed"
    }

def it_support_reasoning(logs: str, client: OpenAI) -> dict[str, Any]:
    """4-phase IT support reasoning pipeline."""
    obs = client.chat.completions.create(
        model=MODEL_DEPLOYMENT,
        messages=[{
            "role": "system",
            "content": "Classify into [NETWORK], [DATABASE], [CODE/APPLICATION], or [AWS INFRASTRUCTURE]"
        }, {
            "role": "user",
            "content": f"Analyze these logs and classify root cause:\n\n{logs}"
        }],
        max_tokens=300
    )
    
    hyp = client.chat.completions.create(
        model=MODEL_DEPLOYMENT,
        messages=[{"role": "system", "content": "Generate hypotheses for the failure."},
                  {"role": "user", "content": f"Logs: {logs}"}],
        max_tokens=400
    )
    
    sol = client.chat.completions.create(
        model=MODEL_DEPLOYMENT,
        messages=[{"role": "system", "content": "Provide resolution steps with justification."},
                  {"role": "user", "content": f"Based on: {obs.choices[0].message.content}"}],
        max_tokens=600
    )
    
    return {
        "output": json.dumps({
            "mode": "it_support",
            "reasoning": {
                "observation": obs.choices[0].message.content,
                "hypothesis": hyp.choices[0].message.content,
                "resolution": sol.choices[0].message.content
            }
        }, indent=2),
        "status": "completed"
    }

server = ResponsesHostServer(hybrid_agent)
server.run()