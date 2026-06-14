# ⚡ QUICK START — Eros Code Analysis Agent

**Get started in 2 minutes**

---

## What is Eros?

AI agent that analyzes code through 5-phase reasoning: Syntax → Quality → Security → Performance → Refactoring.

Detects vulnerabilities (SQL Injection, Auth Bypass, Data Exposure) and generates secure code proposals.

---

## 3-Step Setup

### Step 1: Install
```bash
pip install -r requirements.txt
```
**Expected:** All packages installed ✅

### Step 2: Run Demo
```bash
python run_simulation.py
```
**Expected:** 5-phase analysis with vulnerability detection ✅

### Step 3: Verify Tests
```bash
python test_agent.py
```
**Expected:** `[SUCCESS] All agent internal tests passed (Exit Code 0).` ✅

---

## Try Enhanced Demo (with code comparisons)

```bash
python demo_enhanced.py
```

Shows:
- 🔴 Vulnerable code
- 🚨 EROS analysis
- ✅ Secure code proposal

---

## Next Steps

- **Deploy to Azure:** See [DEPLOYMENT.md](DEPLOYMENT.md)
- **API Reference:** See [API.md](API.md)
- **Contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## What You'll See

```
✅ Phase 1: SYNTAX CHECK → PASSED (45ms)
⚠️  Phase 2: QUALITY REVIEW → WARNING (120ms)
❌ Phase 3: SECURITY AUDIT → CRITICAL (350ms)
   → CWE-89: SQL Injection detected
✅ Phase 4: PERFORMANCE ANALYSIS → OPTIMIZABLE (80ms)
✅ Phase 5: REFACTORING → COMPLETED (405ms)

Total time: 1,000ms | Confidence: 98% | Vulnerabilities: 9
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Unicode errors | Use `python -X utf8 run_simulation.py` |
| Tests fail | Check `demo_output.json` exists |

---

**Ready? Start with Step 1 above!** 🚀
