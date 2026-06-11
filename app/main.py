import os
import json
import requests
from typing import Any, Optional
from azure.ai.agentserver.responses import ResponsesHostServer
from openai import OpenAI

TOOLBOX_ENDPOINT = os.environ.get("FOUNDRY_TOOLBOX_ENDPOINT", "")

def search_best_practices(query: str) -> Optional[str]:
    """Search for best practices using toolbox."""
    if not TOOLBOX_ENDPOINT:
        return None
    try:
        resp = requests.post(
            TOOLBOX_ENDPOINT,
            headers={"Content-Type": "application/json"},
            json={"tool": "web_search", "query": f"{query} best practices coding standards"}
        )
        return resp.json().get("result", "") if resp.ok else None
    except:
        return None

def analyze_code_multi_step(user_message: dict[str, Any]) -> dict[str, Any]:
    """Multi-step code analysis with structured reasoning.
    
    Executes 5-phase analysis pipeline optimized for the Agents League hackathon:
    - Phase 1: Syntax validation
    - Phase 2: Code quality  
    - Phase 3: Security audit
    - Phase 4: Performance optimization
    - Phase 5: Refactoring with best practices
    """
    code = user_message.get("input", "")
    language_hint = user_message.get("language", "auto-detect")
    
    client = OpenAI(
        base_url=os.environ.get("PROJECT_ENDPOINT"),
        api_key=os.environ.get("MODEL_DEPLOYMENT")
    )
    
    analysis_report = {
        "request_id": user_message.get("id", "unknown"),
        "language_detected": language_hint,
        "analysis_pipeline": []
    }
    
    # Phase 1: Syntax & Basic Structure
    phase1 = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "You are a code linter. Identify syntax errors, undefined variables, and structural issues. Be concise."
        }, {
            "role": "user", 
            "content": f"Analyze this {language_hint} code for syntax errors:\n\n{code}"
        }],
        max_tokens=500,
        temperature=0.1
    )
    analysis_report["analysis_pipeline"].append({
        "phase": "syntax_check",
        "step": 1,
        "findings": phase1.choices[0].message.content
    })
    
    # Phase 2: Code Quality & Best Practices
    phase2 = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "You are a senior code reviewer. Check DRY violations, naming conventions, code smells, and maintainability."
        }, {
            "role": "user",
            "content": f"Code quality review for {language_hint}:\n\n{code}"
        }],
        max_tokens=600,
        temperature=0.2
    )
    analysis_report["analysis_pipeline"].append({
        "phase": "quality_review", 
        "step": 2,
        "findings": phase2.choices[0].message.content
    })
    
    # Phase 3: Security Audit
    phase3 = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "You are a security auditor. Identify SQL injection, XSS, auth flaws, secrets exposure, and insecure patterns. Prioritize critical risks."
        }, {
            "role": "user",
            "content": f"Security audit for {language_hint} code:\n\n{code}"
        }],
        max_tokens=600,
        temperature=0.1
    )
    analysis_report["analysis_pipeline"].append({
        "phase": "security_audit",
        "step": 3, 
        "findings": phase3.choices[0].message.content
    })
    
    # Phase 4: Performance Analysis
    phase4 = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "You are a performance engineer. Identify time/space complexity issues, bottlenecks, memory leaks, and optimization opportunities."
        }, {
            "role": "user",
            "content": f"Performance analysis for {language_hint}:\n\n{code}"
        }],
        max_tokens=500,
        temperature=0.2
    )
    analysis_report["analysis_pipeline"].append({
        "phase": "performance_analysis",
        "step": 4,
        "findings": phase4.choices[0].message.content
    })
    
    # Phase 5: Refactoring with Tool Integration
    best_practice_info = search_best_practices(f"{language_hint} code refactoring")
    phase5_prompt = f"Refactor this {language_hint} code incorporating all findings:\n\n{code}"
    if best_practice_info:
        phase5_prompt += f"\n\nReference best practices:\n{best_practice_info}"
    
    phase5 = client.chat.completions.create(
        model=os.environ.get("MODEL_DEPLOYMENT", "gpt-4"),
        messages=[{
            "role": "system",
            "content": "You are a principal engineer. Provide improved code with explanations. Apply fixes from all previous phases."
        }, {
            "role": "user",
            "content": phase5_prompt
        }],
        max_tokens=800,
        temperature=0.3
    )
    analysis_report["analysis_pipeline"].append({
        "phase": "refactor_suggestions",
        "step": 5,
        "findings": phase5.choices[0].message.content,
        "tool_enhanced": bool(best_practice_info)
    })
    
    # Final summary focusing on reasoning flow
    analysis_report["summary"] = {
        "total_issues_found": sum(1 for p in analysis_report["analysis_pipeline"] if p.get("findings")),
        "critical_risks": "See security_audit phase for details",
        "next_steps": "Review refactor_suggestions for improved implementation"
    }
    
    return {
        "output": json.dumps(analysis_report, indent=2),
        "status": "completed"
    }

server = ResponsesHostServer(analyze_code_multi_step)
server.run()