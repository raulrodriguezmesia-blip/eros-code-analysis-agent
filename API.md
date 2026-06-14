# 📡 API Documentation — Eros Code Analysis Agent

Complete API reference for the Eros Agent Server endpoints.

---

## Base URL

```
http://localhost:8000
https://<your-deployed-service>.azurewebsites.net
```

---

## Endpoints

### 1. Analyze Code

Performs 5-phase analysis on provided source code.

**Endpoint:** `POST /analyze`

**Request Body:**

```json
{
  "language": "python",
  "code": "def process_payment(card_number, amount):\n    query = f\"UPDATE accounts SET balance = balance - {amount} WHERE card='{card_number}'\"\n    result = db.execute(query)\n    return {\"success\": True}",
  "options": {
    "include_refactoring": true,
    "severity_threshold": "CRITICAL"
  }
}
```

**Response:**

```json
{
  "analysis_id": "eros-2026-001",
  "language_detected": "python",
  "analysis_pipeline": [
    {
      "step": 1,
      "phase": "syntax_check",
      "status": "PASSED",
      "findings": "No syntax errors found"
    },
    {
      "step": 2,
      "phase": "quality_review",
      "status": "WARNING",
      "findings": "Missing type hints and docstrings"
    },
    {
      "step": 3,
      "phase": "security_audit",
      "status": "CRITICAL",
      "vulnerability": {
        "class": "SQL Injection",
        "cwe": "CWE-89",
        "severity": "CRITICAL",
        "line": 2
      }
    },
    {
      "step": 4,
      "phase": "performance_analysis",
      "status": "OPTIMIZABLE",
      "findings": "Use parameterized queries"
    },
    {
      "step": 5,
      "phase": "refactoring",
      "status": "COMPLETED",
      "secure_code_proposal": "def process_payment(card_number: str, amount: float):\n    query = 'UPDATE accounts SET balance = balance - %s WHERE card = %s'\n    return db.execute(query, (amount, card_number))"
    }
  ],
  "timestamp": "2026-06-14T10:30:00Z",
  "metadata": {
    "intelligence_layer": "Microsoft Foundry IQ",
    "processing_time_ms": 1250,
    "confidence_score": 0.98
  }
}
```

**Status Codes:**
- `200` — Analysis successful
- `400` — Invalid request (missing required fields)
- `401` — Unauthorized (invalid API key)
- `429` — Rate limited (too many requests)
- `500` — Server error

---

### 2. Health Check

Verify agent server is running.

**Endpoint:** `GET /health`

**Response:**

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "uptime_seconds": 3600,
  "foundry_iq_connected": true,
  "timestamp": "2026-06-14T10:30:00Z"
}
```

---

### 3. Batch Analysis

Analyze multiple code files in one request.

**Endpoint:** `POST /analyze/batch`

**Request Body:**

```json
{
  "files": [
    {
      "name": "payment.py",
      "language": "python",
      "code": "..."
    },
    {
      "name": "database.py",
      "language": "python",
      "code": "..."
    }
  ]
}
```

**Response:** Array of analysis results

---

### 4. Analysis History

Retrieve previous analyses.

**Endpoint:** `GET /analyses?limit=10&offset=0`

**Response:**

```json
{
  "total": 42,
  "analyses": [
    {
      "analysis_id": "eros-2026-001",
      "timestamp": "2026-06-14T10:30:00Z",
      "language": "python",
      "critical_findings": 2,
      "warnings": 5
    }
  ]
}
```

---

## Authentication

Include API key in request headers:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"code": "..."}' \
     https://api.eros-agent.com/analyze
```

---

## Rate Limits

| Plan | Requests/min | Concurrent | Storage |
|------|-------------|-----------|---------|
| Free | 10 | 1 | 1 GB |
| Pro | 100 | 10 | 100 GB |
| Enterprise | Unlimited | 50+ | Unlimited |

---

## Examples

### Python Client

```python
import requests

api_key = "your-api-key"
code = """
def vulnerable_query(user_id):
    query = f"SELECT * FROM users WHERE id={user_id}"
    return db.execute(query)
"""

response = requests.post(
    "https://api.eros-agent.com/analyze",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"language": "python", "code": code}
)

result = response.json()
print(f"Critical findings: {result['analysis_pipeline'][3]['findings']}")
```

### JavaScript/Node.js

```javascript
const axios = require('axios');

const code = `
function processPayment(cardNumber, amount) {
  const query = \`UPDATE accounts SET balance = \${amount} WHERE card='\${cardNumber}'\`;
  return db.execute(query);
}
`;

axios.post('https://api.eros-agent.com/analyze', {
  language: 'javascript',
  code: code
}, {
  headers: { 'Authorization': 'Bearer YOUR_API_KEY' }
}).then(res => console.log(res.data));
```

### cURL

```bash
curl -X POST https://api.eros-agent.com/analyze \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "python",
    "code": "SELECT * FROM users WHERE id=1"
  }'
```

---

## Error Handling

All errors include structured response:

```json
{
  "error": {
    "code": "INVALID_CODE",
    "message": "Syntax error in provided code",
    "details": "Line 5: unexpected indentation",
    "request_id": "req-123456"
  }
}
```

---

## Support

- **Documentation:** [docs.eros-agent.com](https://docs.eros-agent.com)
- **Issues:** GitHub Issues
- **Email:** support@eros-agent.com
