# 🤖 Eros Code Analysis Agent — Agents League Hackathon 2026

Multi-step reasoning AI agent for advanced static and dynamic code analysis, built for the **Reasoning Agents Track** in the Agents League Hackathon.

[![Tests Passing](https://img.shields.io/badge/tests-passing%20✓-brightgreen)](test_agent.py)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Azure Ready](https://img.shields.io/badge/azure-ready-0078d4)](DEPLOYMENT.md)
[![MIT License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Quality](https://img.shields.io/badge/quality-professional-informational)](#-code-standards)

## 🎬 Demo Video
👉 **[Watch the 3-Minute Technical Demo Here](https://youtu.be/aKqzT4fn4WY)**

---

## 🧠 Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│   Eros Code Analysis Agent (Azure Agent Server)     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌────────────────────────────────────────────┐   │
│  │  5-Phase Structured Reasoning Pipeline     │   │
│  ├────────────────────────────────────────────┤   │
│  │ 1️⃣  Phase 1: Syntax Check (AST Parse)    │   │
│  │ 2️⃣  Phase 2: Quality Review (PEP 8)      │   │
│  │ 3️⃣  Phase 3: Security Audit (OWASP)      │   │
│  │ 4️⃣  Phase 4: Performance Analysis        │   │
│  │ 5️⃣  Phase 5: Refactoring & Validation    │   │
│  └────────────────────────────────────────────┘   │
│                      ↓                             │
│  ┌────────────────────────────────────────────┐   │
│  │ Microsoft Foundry IQ (Intelligence Layer) │   │
│  │ + Foundry Toolbox (Code Generation)      │   │
│  └────────────────────────────────────────────┘   │
│                      ↓                             │
│  ┌────────────────────────────────────────────┐   │
│  │ Structured JSON Report + Mitigation Code  │   │
│  └────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 📋 Analysis Pipeline Phases

Eros decouples complex code security diagnostics by integrating with **Microsoft Foundry IQ** and **Foundry Toolbox**. Instead of linear prompting, it follows a strict multi-step clinical reasoning path:

| Phase | Component | Purpose | Output |
|-------|-----------|---------|--------|
| **1** | Syntax Check | Validate AST integrity | Structural errors, indentation issues |
| **2** | Quality Review | PEP 8 compliance, type hints | Code quality recommendations |
| **3** | Security Audit | OWASP Top 10, CWE scanning | Vulnerability findings (e.g., CWE-89 SQL Injection) |
| **4** | Performance Analysis | Database I/O, query bottlenecks | Optimization suggestions |
| **5** | Refactoring | Secure code generation | Parameterized code proposals |

---

## 🚀 Quick Start & One-Click Deploy

Eros is fully optimized for fast execution and deployment using the Azure Developer CLI (`azd`).

### Local Simulation (3-Step Quick Run)

Clone the repository, install dependencies, and run the multi-step reasoning simulation in your terminal:

```bash
# 1. Clone the repository
git clone https://github.com/raulrodriguezmesia-blip/eros-code-analysis-agent.git
cd eros-code-analysis-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the automated simulation script
python run_simulation.py

# Optional: Enhanced demo with before/after comparisons
python demo_enhanced.py
```

### ☁️ Cloud Deployment via Microsoft Foundry

Initialize and provision your agent infrastructure into your Azure environment instantly:

```bash
azd init --with-python
azd up
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed step-by-step instructions.

### 🧪 Verify Installation

Run the automated test suite to validate the agent setup:

```bash
python test_agent.py
```

Expected output: `[SUCCESS] All agent internal tests passed (Exit Code 0).`

---

## 📁 Repository Structure

```
eros-code-analysis-agent/
├── app/
│   └── main.py                 # Azure Agent Server handler & pipeline orchestration
├── run_simulation.py           # Terminal animation showcasing 5-phase reasoning
├── demo_enhanced.py            # Enhanced demo with before/after code comparisons
├── test_agent.py               # Comprehensive automated verification tests
├── demo_input.py               # Vulnerable code sample #1 (SQL Injection)
├── demo_input_2.py             # Vulnerable code sample #2 (Auth/Access Control)
├── demo_input_3.py             # Vulnerable code sample #3 (Data Exposure)
├── demo_output.json            # Structured analysis report with findings
├── requirements.txt            # Python dependencies (pinned versions)
├── .env.example                # Configuration template
├── .vscode/
│   └── tasks.json             # VS Code run commands for development
├── DEPLOYMENT.md               # Step-by-step Azure deployment guide
├── API.md                      # API documentation & endpoints
├── CONTRIBUTING.md             # Contribution guidelines
└── README.md                   # This file
```

### Key Files Explained

- **`app/main.py`** — Azure Agent Server implementation that handles incoming analysis requests and orchestrates the 5-phase pipeline
- **`run_simulation.py`** — Interactive terminal simulation demonstrating the complete analysis workflow
- **`demo_enhanced.py`** — Advanced demo showing vulnerable → secure code transformation with metrics
- **`test_agent.py`** — Multi-function test suite validating JSON structure, pipeline phases, and security findings
- **`demo_input*.py`** — Example vulnerable code samples for different vulnerability categories
- **`demo_output.json`** — Final structured report with Chain-of-Thought reasoning logs

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and configure your Azure endpoints:

```bash
cp .env.example .env
```

Key environment variables:
- `MODEL_DEPLOYMENT` — Azure OpenAI model (e.g., `gpt-4`)
- `PROJECT_ENDPOINT` — Azure OpenAI endpoint URL
- `FOUNDRY_IQ_ENDPOINT` — Microsoft Foundry IQ service endpoint
- `FOUNDRY_TOOLBOX_ENDPOINT` — Foundry Toolbox service endpoint

---

## 🏆 Hackathon Requirements Met

✅ **Reasoning Agent Track** — Implements deep multi-step thinking using Microsoft Foundry  
✅ **Microsoft IQ Layer** — Integrated with Foundry IQ and Foundry Toolbox  
✅ **Structured Output** — Delivers deterministic, actionable JSON finding sheets  
✅ **Reliability** — Validated via comprehensive automated test suites  
✅ **Professional Quality** — Production-ready code with docstrings, type hints, and error handling  

---

## 📚 Development

### Running Individual Components

```bash
# Run the terminal simulation
python run_simulation.py

# Run the Azure Agent Server
python app/main.py

# Run verification tests
python test_agent.py
```

### VS Code Integration

All run commands are pre-configured in `.vscode/tasks.json`:
- **Install dependencies** (auto-runs on worktree creation)
- **Run simulation** (interactive terminal demo)
- **Run main app** (start the agent server)

Press `Ctrl + `` in VS Code to open the terminal and run commands.

---

## 🔐 Security

- All dependencies use pinned versions for reproducibility
- No hardcoded credentials in source code
- Use `.env` file for sensitive configuration
- Telemetry disabled by default (see `app/main.py`)

---

## 📝 License

Built for the Agents League Hackathon 2026
