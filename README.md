# 🤖 Eros Code Analysis Agent — Agents League Hackathon 2026

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-005671?style=for-the-badge&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![Coverage](https://img.shields.io/badge/coverage-%E2%89%A570%25-yellowgreen?style=for-the-badge)
![Last Updated](https://img.shields.io/badge/updated-2026--07--12-informational?style=for-the-badge)

## 📖 Descripción

Agente de IA multi-step para análisis estático y dinámico de código, construido para el **Reasoning Agents Track** del Agents League Hackathon 2026. Integra Microsoft Foundry IQ para razonamiento estructurado en 5 fases.

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
- [x] Tests unitarios pasan
- [x] Cobertura de código >= 70%
- [x] Documentación de arquitectura completa
- [x] CI/CD GitHub Actions configurado
- [ ] Despliegue en Azure (azd)

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

2026-07-24

## 📊 Roadmap Estratégico

- **H0 (Hackathon):** ✅ COMPLETADO - Demo 60-90 segundos
- **H1 (Post-hackathon):** 🔄 EN PROGRESO - CI/CD + PR Security Beta
- **H2 (Escala):** 📋 PLANIFICADO - Multi-lenguaje + Dashboard
- **H3 (Enterprise):** 📋 PLANIFICADO - SaaS + SOC 2 Compliance

Ver más detalles en: `docs/roadmap/FASE-1.txt` y `docs/roadmap/FASE3_STRATEGY.md`

---