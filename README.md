# Eros Code Analysis Agent - Agents League Hackathon

Multi-step reasoning AI agent for code analysis with Microsoft IQ integration.

## Microsoft IQ Integration

✅ **Foundry IQ**: Enhanced reasoning pipeline with external knowledge querying
✅ **Multi-phase analysis**: 5 distinct phases with tool-enhanced insights
✅ **Foundry Toolbox**: Best practices search integration

## Features

- **Multi-step reasoning**: 5-phase pipeline (syntax → quality → security → performance → refactor)
- **Foundry IQ enhanced**: External knowledge context for each analysis phase
- **Language agnostic**: Python, JavaScript, TypeScript, C#, Java, Go
- **Tool integration**: Search and validation capabilities
- **Structured JSON output**: Actionable findings with source attribution
- **Security-first**: Dedicated audit phase for vulnerabilities
- **Performance insights**: Optimization recommendations

## Analysis Pipeline (Reasoning Phases)

1. **Syntax Check** (`iq_enhanced`): Errors and structure issues with Foundry IQ context
2. **Quality Review**: Best practices, naming, maintainability  
3. **Security Audit**: Injection risks, auth flaws, secrets exposure
4. **Performance Analysis**: Bottlenecks, complexity, optimization opportunities
5. **Refactoring**: Improved code with explanations

## Variants

**Three reasoning modes available:**
- `code-analysis`: 5-phase code review pipeline
- `it-support`: 4-phase IT incident resolution (AWS/Spring Boot)
- `hybrid`: Auto-routing based on input type

## 🚀 Quick Start & One-Click Deploy

Eros Code Analysis Agent is fully optimized for fast execution and deployment using the Azure Developer CLI (`azd`).

### Local Simulation (3-Step Quick Run)
Clone, install dependencies, and run the pipeline verification immediately:
```bash
# 1. Clone the repository
git clone https://github.com/raulrodriguezmesia-blip/eros-code-analysis-agent && cd eros-code-analysis-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the multi-step reasoning validation script
python test_agent.py
```

### ☁️ Cloud Deployment via Microsoft Foundry
Initialize and provision your agent infrastructure into your Azure environment instantly:
```bash
azd init --with-python
azd up
```

## Demo Example

**Input:**
```python
def get_user(id):
    query = "SELECT * FROM users WHERE id=" + id
    return db.execute(query)
```

**Output:** Full 5-phase analysis including SQL injection vulnerability detection, refactored secure code with parameterized queries.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python -m app.main

# Test (Responses API)
curl -X POST http://localhost:8088/responses \
  -H "Content-Type: application/json" \
  -d '{"input": "def foo(x): return x * 2", "language": "python"}'
```

## Environment Variables

```bash
model=gpt-4
PROJECT_ENDPOINT=https://YOUR-PROJECT.openai.azure.com/
FOUNDRY_TOOLBOX_ENDPOINT=
FOUNDRY_IQ_ENDPOINT=
```

## Deployment to Azure Foundry

```bash
azd init --with-python
azd up
```

## Hackathon Requirements Met

- ✅ Microsoft IQ Layer (Foundry IQ)
- ✅ Multi-step reasoning pipeline
- ✅ Tool integration (search, validation)
- ✅ Creative approach with security focus
- ✅ Ready for demo video (5 min max)

## License

MIT