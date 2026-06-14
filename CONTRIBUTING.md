# 🤝 Contributing to Eros Code Analysis Agent

Thank you for your interest in contributing to Eros! This guide will help you get started.

---

## 🎯 Ways to Contribute

- **Report bugs** — Found an issue? Open a GitHub issue
- **Suggest features** — Have an idea? Start a discussion
- **Improve documentation** — Help clarify or expand docs
- **Submit code** — Bug fixes and features via pull requests
- **Add test cases** — Expand test coverage
- **Share use cases** — Tell us how you're using Eros

---

## 🚀 Getting Started

### Fork & Clone

```bash
git clone https://github.com/YOUR-USERNAME/eros-code-analysis-agent.git
cd eros-code-analysis-agent
```

### Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Set Up Development Environment

```bash
pip install -r requirements.txt
python -m pytest test_agent.py
```

---

## 📝 Development Workflow

### 1. Make Changes

- Edit relevant files
- Follow PEP 8 style guide
- Add docstrings to new functions
- Include type hints

### 2. Test Locally

```bash
# Run simulation
python run_simulation.py

# Run tests
python test_agent.py

# Verify formatting
python -m black .
```

### 3. Commit Changes

```bash
git add .
git commit -m "feat: Brief description of changes"
```

### 4. Push & Open PR

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub with:
- Clear title describing the change
- Description of what and why
- Link to any related issues

---

## 💡 Code Standards

### Style Guide

- **Python version:** 3.10+
- **Formatter:** Black
- **Linter:** Pylint
- **Type checking:** MyPy

```bash
# Auto-format code
python -m black app/ run_simulation.py test_agent.py

# Check types
python -m mypy app/
```

### Docstring Format

```python
def analyze_code(code: str, language: str) -> dict:
    """
    Analyze provided code and return findings.

    Args:
        code: Source code to analyze
        language: Programming language

    Returns:
        dict: Analysis results with findings

    Raises:
        ValueError: If code is empty or language unsupported
    """
```

### Type Hints

Always include type hints:

```python
# ✅ Good
def process_findings(findings: list[dict]) -> dict:
    pass

# ❌ Avoid
def process_findings(findings):
    pass
```

---

## 🧪 Testing

### Add Tests

Create tests in `test_agent.py`:

```python
def test_new_vulnerability_detection() -> bool:
    """Test detection of new vulnerability type."""
    code = "vulnerable_code_here"
    result = analyze(code)
    assert result["status"] == "CRITICAL"
    return True
```

### Run All Tests

```bash
python test_agent.py
```

Expected output: `[SUCCESS] All agent internal tests passed (Exit Code 0).`

---

## 📚 Project Structure

```
eros-code-analysis-agent/
├── app/
│   └── main.py           # Core agent logic
├── run_simulation.py      # Demo script
├── test_agent.py          # Test suite
├── demo_input*.py         # Test cases
├── requirements.txt       # Dependencies
├── DEPLOYMENT.md          # Deployment guide
├── API.md                 # API documentation
├── CONTRIBUTING.md        # This file
└── README.md              # Project overview
```

---

## 🔍 Review Process

1. **Automatic checks** run on your PR
   - Code formatting
   - Type checking
   - Tests must pass

2. **Code review** by maintainers
   - Follow feedback
   - Discuss design decisions
   - Iterate on feedback

3. **Merge** when approved
   - Squash commits if needed
   - Delete feature branch

---

## 🐛 Reporting Bugs

### Issue Template

```markdown
**Describe the bug**
Clear description of what's broken

**Steps to reproduce**
1. Run `python run_simulation.py`
2. Observe error...

**Expected behavior**
What should happen

**Environment**
- Python: 3.10+
- OS: Windows/Linux/Mac
- Error message: (copy full traceback)
```

---

## ✨ Feature Requests

### Proposal Template

```markdown
**Motivation**
Why is this feature needed?

**Proposed solution**
How should it work?

**Alternatives considered**
Any other approaches?
```

---

## 📋 PR Checklist

Before submitting:

- [ ] Tests pass locally (`python test_agent.py`)
- [ ] Code follows PEP 8 (`python -m black .`)
- [ ] Docstrings added/updated
- [ ] Type hints included
- [ ] No hardcoded secrets
- [ ] Documentation updated if needed
- [ ] Commit message is clear
- [ ] No unnecessary dependencies added

---

## 🎓 Learning Resources

- [Microsoft Foundry Docs](https://learn.microsoft.com/foundry)
- [Azure Agent Server](https://learn.microsoft.com/azure/agents)
- [OWASP Top 10](https://owasp.org/Top10/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 💬 Questions?

- Check existing issues and discussions
- Read the [README.md](README.md)
- Review [API.md](API.md) for technical details
- Open a discussion on GitHub

---

## 🙏 Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Mentioned in release notes
- Thanked in project README

---

## 📜 License

By contributing, you agree your work will be under the same license as the project.

---

**Happy contributing! 🚀**
