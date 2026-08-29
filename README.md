# 🤖 Eros Code Analysis Agent — Desafío de Ingeniería de Frontera 2026

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-005671?style=for-the-badge&logo=fastapi&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Cloud-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![Coverage](https://img.shields.io/badge/coverage-%E2%89%A580%25-yellowgreen?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-2026--08--29-informational?style=for-the-badge)

## 📖 Descripción

Agente de IA multi-step para análisis estático y dinámico de código, construido para el **Desafío de Ingeniería de Frontera 2026**. Integra Microsoft Foundry IQ para razonamiento estructurado en 5 fases. Diseñado para detectar vulnerabilidades de seguridad, evaluar calidad de código y generar refactorizaciones automáticas en entornos de producción empresarial.

## 🎯 Desafío de Ingeniería de Frontera 2026

Este proyecto participa en el **Desafío de Ingeniería de Frontera 2026**, demostrando capacidades avanzadas de:

- **Razonamiento estructurado multi-fase** para análisis profundo de código
- **Integración con Microsoft Foundry IQ** para inferencia de alta precisión
- **Despliegue en Azure** con arquitectura serverless y contenerizada
- **Observabilidad completa** con OpenTelemetry, Application Insights y Prometheus

## 🚀 Quick Start

### Prerrequisitos
- Python 3.11+
- pip
- (Opcional) Docker

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar simulación
```bash
python run_simulation.py
```

### Ejecutar tests
```bash
pytest test_agent.py -v
```

### Demo avanzada
```bash
python demo_enhanced.py
```

## 🏗️ Arquitectura

```mermaid
graph TD
    A[Input Code] --> B[Phase 1: Syntax Check]
    B --> C[Phase 2: Quality Review]
    C --> D[Phase 3: Security Audit]
    D --> E[Phase 4: Performance Analysis]
    E --> F[Phase 5: Refactoring]
    F --> G[Microsoft Foundry IQ]
    G --> H[JSON Report]
```

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Lenguaje | Python 3.11+ |
| Framework | FastAPI 0.110+ |
| IA/ML | OpenAI gpt-4.1-mini, gpt-image-1.5 |
| Observabilidad | OpenTelemetry, Jaeger, Prometheus |
| Despliegue | Docker, Kubernetes, Azure |
| Testing | pytest |
| CI/CD | GitHub Actions |

## 📚 Documentación

- Swagger UI: `http://localhost:8000/docs` (cuando el servidor está corriendo)
- [DEPLOYMENT.md](DEPLOYMENT.md) — Guía de despliegue en Azure
- [API.md](API.md) — Referencia de endpoints

## 🔄 CI/CD

- **CI/CD:** GitHub Actions pipeline configurado (`ci-cd.yml` + `reusable-python-ci.yml`)
- **Tests:** pytest + coverage + Docker build automatizados
- **Security:** Bandit + Safety scans integrados
- **Deploy:** Azure deploy pipeline preparado

## ✅ Definition of Done

- [x] Pipeline de 5 fases implementada
- [x] Tests unitarios pasan (80%+ cobertura)
- [x] Documentación de arquitectura completa
- [x] CI/CD GitHub Actions configurado
- [x] Despliegue en Azure Container Apps / AKS
- [x] Observabilidad con Application Insights
- [x] Seguridad: Bandit + Safety scans integrados

## 🤝 Cómo contribuir

1. Haz un fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-fase`
3. Commit: `git commit -m 'feat(agent): add Phase 6: License Compliance'`
4. Push: `git push origin feature/nueva-fase`
5. Abre un Pull Request

**Requisitos:** Incluir tests y actualizar diagrama de arquitectura.

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

## 📅 Última actualización

2026-08-29

## 📊 Roadmap Estratégico

- **Fase 1 (Hackathon):** ✅ COMPLETADO - Demo funcional con 5 fases de análisis
- **Fase 2 (Desafío Frontera):** 🔄 EN PROGRESO - Despliegue Azure + Observabilidad
- **Fase 3 (Escala):** 📋 PLANIFICADO - Multi-lenguaje + Dashboard empresarial
- **Fase 4 (Enterprise):** 📋 PLANIFICADO - SaaS + SOC 2 Compliance

Ver más detalles en: `docs/roadmap/FASE-1.txt` y `docs/roadmap/FASE3_STRATEGY.md`

---