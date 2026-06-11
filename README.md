# Code Analysis Multi-Agent Reasoning Bot

An Azure Foundry hosted agent that performs multi-step reasoning on code submissions, analyzing through 5 distinct phases.

## Features

- **Multi-step reasoning**: 5-phase analysis pipeline
- **Language agnostic**: Supports Python, JavaScript, TypeScript, C#, Java, Go
- **Structured output**: JSON report with actionable findings
- **Security-first**: Dedicated security audit phase
- **Performance insights**: Optimization recommendations

## Analysis Phases

1. **Syntax & Structure**: Syntax errors, basic code issues
2. **Quality Review**: Best practices, naming conventions, maintainability  
3. **Security Audit**: Vulnerabilities, injection risks, authentication issues
4. **Performance Analysis**: Bottlenecks, memory leaks, optimization opportunities
5. **Refactoring**: Improved code with explanations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python -m app.main

# Test
curl -X POST http://localhost:8088/responses \
  -H "Content-Type: application/json" \
  -d '{"input": "def foo(x): return x * 2"}'
```

## Deployment to Azure Foundry

```bash
azd up
```

## Architecture

[Diagram showing 5-step pipeline with feedback loops]

## License

MIT