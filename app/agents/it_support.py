import os
import json
from typing import Any, Optional
from openai import OpenAI

SYSTEM_PROMPT = """You are an Advanced Reasoning Agent specializing in critical infrastructure support, 
Java/Spring Boot microservices, and AWS Cloud environments. You must execute and document these steps:

### Step 1: Observation & Classification
- Analyze user prompt and logs
- Classify root failure in: [NETWORK], [DATABASE], [CODE/APPLICATION], or [AWS INFRASTRUCTURE]

### Step 2: Hypothesis Formulation
- Generate at least two logical explanations with architecture context

### Step 3: Validation via Tools
- Use available tools to validate hypotheses
- Async API calls to Spring Boot/AWS monitoring tools

### Step 4: Resolution & Justification
- Detailed contingency plan
- Technical justification
"""

client = OpenAI(
    base_url=os.environ.get("PROJECT_ENDPOINT"),
    api_key=os.environ.get("PROJECT_KEY", "")
)

def it_support_reasoning(logs: str) -> dict[str, Any]:
    """IT Support reasoning agent with 4-phase analysis."""
    
    # Step 1: Observation
    obs_response = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "Classify logs into [NETWORK], [DATABASE], [CODE/APPLICATION], or [AWS INFRASTRUCTURE]"
        }, {
            "role": "user",
            "content": f"Logs: {logs}\n\nExtract key observations and classify the root cause category."
        }],
        max_tokens=300,
        temperature=0.1
    )
    
    # Step 2: Hypotheses
    hyp_response = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "Generate at least 2 technical hypotheses explaining the failure."
        }, {
            "role": "user",
            "content": f"For these logs: {logs}\n\nPropose 2-3 root cause hypotheses with AWS/Spring Boot context."
        }],
        max_tokens=400,
        temperature=0.2
    )
    
    # Step 3: Validation
    val_response = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "Validate hypotheses using AWS/Spring Boot monitoring data patterns."
        }, {
            "role": "user",
            "content": f"Given hypotheses: {hyp_response.choices[0].message.content}\n\nWhat AWS/CloudWatch or Spring Boot Actuator data would confirm or reject each?"
        }],
        max_tokens=500,
        temperature=0.1
    )
    
    # Step 4: Resolution
    sol_response = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "Provide step-by-step resolution plan with technical justification."
        }, {
            "role": "user",
            "content": f"For logs: {logs}\n\nBased on validated root cause, provide numbered resolution steps and justification."
        }],
        max_tokens=600,
        temperature=0.1
    )
    
    return {
        "output": json.dumps({
            "reasoning_trace": {
                "step_1_observation": obs_response.choices[0].message.content,
                "step_2_hypothesis": hyp_response.choices[0].message.content,
                "step_3_validation": val_response.choices[0].message.content,
                "step_4_resolution": sol_response.choices[0].message.content
            }
        }, indent=2),
        "status": "completed"
    }