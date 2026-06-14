# 🚀 Deployment Guide — Eros Code Analysis Agent

Complete step-by-step guide to deploy Eros to Azure using Microsoft Foundry.

---

## 📋 Prerequisites

- Azure subscription (free tier available)
- Azure CLI installed (`az --version`)
- Python 3.10+ installed
- Git installed

---

## 🔧 Quick Deployment (5 minutes)

### Step 1: Initialize Azure Development Environment

```bash
# Clone the repository
git clone https://github.com/raulrodriguezmesia-blip/eros-code-analysis-agent.git
cd eros-code-analysis-agent

# Login to Azure
az login

# Initialize for Python deployment
azd init --with-python
```

### Step 2: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your Azure endpoints
# Required:
# - MODEL_DEPLOYMENT: Your Azure OpenAI model name
# - PROJECT_ENDPOINT: Your Azure OpenAI endpoint
# - FOUNDRY_IQ_ENDPOINT: Your Foundry IQ service endpoint
```

### Step 3: Deploy to Azure

```bash
# Provision and deploy infrastructure
azd up

# Output will show your deployed service URL
```

---

## 🧪 Verify Deployment

```bash
# Test the deployed endpoint
curl -X POST https://<your-agent-server>/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "SELECT * FROM users WHERE id=1"}'
```

Expected response: JSON analysis report

---

## 🐛 Troubleshooting

### Issue: Authentication Failed

```bash
# Re-authenticate
az logout
az login

# Verify subscription
az account show
```

### Issue: Endpoint Not Found

- Verify `.env` file has correct endpoints
- Check Azure resource group exists: `az group list`
- Confirm Foundry IQ service is provisioned

### Issue: Dependencies Conflict

```bash
# Clean and reinstall
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Issue: Memory/Timeout Errors

- Increase Azure Function timeout in `local.settings.json`
- Use larger compute tier: `azd env set AZURE_COMPUTE_SKU standard_d2s_v3`

---

## 📊 Monitoring & Logs

```bash
# View application logs
az appservice web log tail --name <app-name> --resource-group <rg-name>

# Monitor with Azure Monitor
az monitor metrics list --resource <resource-id>

# Check agent server status
curl https://<your-agent-server>/health
```

---

## 🔐 Security

- Secrets stored in Azure Key Vault (not in `.env`)
- API endpoints use OAuth 2.0 authentication
- All traffic encrypted (TLS 1.3)
- Telemetry disabled by default

To enable Azure Key Vault:

```bash
az keyvault create --name eros-vault --resource-group <rg-name>
az keyvault secret set --vault-name eros-vault --name openai-api-key --value <key>
```

---

## 💰 Cost Optimization

| Component | Free Tier | Recommended |
|-----------|-----------|-------------|
| Azure App Service | B1 (Shared) | B2 (Basic) |
| Cosmos DB | Free tier (400 RU/s) | Standard (1K+ RU/s) |
| OpenAI API | Pay-per-use | Reserved capacity |
| Storage | 5 GB free | Depends on usage |

**Estimated monthly cost:** $20-100 depending on usage

---

## 🔄 CI/CD Pipeline

To set up automated deployment on push:

```bash
# Create GitHub Actions workflow
mkdir -p .github/workflows

# Workflow will auto-deploy on push to main
cat > .github/workflows/deploy.yml << 'EOF'
name: Deploy to Azure

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        run: azd deploy
EOF
```

---

## 📞 Support

For deployment issues:
- Check [Azure CLI documentation](https://learn.microsoft.com/cli/azure/)
- Review [Foundry documentation](https://microsoft.com/foundry)
- Open an issue on GitHub
