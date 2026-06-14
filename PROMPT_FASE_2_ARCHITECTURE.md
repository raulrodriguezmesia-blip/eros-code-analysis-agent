## PROMPT FASE 2 — "EROS Architecture & Quality Design"
**Objetivo:** Diseño de arquitectura escalable + estrategia de tests/seguridad

---

### Contexto
- **Input:** Output de FASE 1 (Roadmap H0-H3)
- **Scope:** Arquitectura para soportar roadmap sin romper determinismo
- **Restricción:** Determinismo estricto = temperature 0, orden fijo, versionado de reglas

### Tu rol
Eres **EROS Architecture Lead**. Diseña la evolución técnica de EROS.

---

### Salida requerida

#### 1. Backlog priorizado (tabla)
Columnas:
- **ID:** P1-001, P1-002, etc.
- **Iniciativa:** [nombre concreto]
- **Categoría:** Alcance / Análisis / Performance / Determinismo / Observabilidad / Integraciones / Seguridad / Compliance / UX
- **Impacto:** H (Alto) / M (Medio) / L (Bajo)
- **Esfuerzo:** H / M / L
- **Dependencias:** [otra iniciativa ID, o "none"]
- **Criterio de aceptación:** [testeable, ej: "SARIF válido con todas 9 vulns reportadas"]
- **Horizonte:** H0 / H1 / H2 / H3

**Iniciativas obligatorias a incluir:**
- GitHub Actions CI/CD integration (H1)
- SARIF export + CWE/OWASP mapping (H1)
- Incremental analysis + caching (H2)
- Multi-lenguaje roadmap (H2 start)
- Secrets redaction in logs (H1)
- Anti-prompt-injection hardening (H1)
- Observabilidad: métricas + trazas (H2)
- Policy packs + waivers (H3)

---

#### 2. Diagrama de arquitectura futura
Formato: **Componentes en texto** (no imagen)

Ejemplo:
```
┌─────────────────────────────────────────────┐
│ EROS Platform (H2/H3)                       │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────┐  ┌──────────────┐        │
│  │  Phase DSL   │  │ Rule Engine  │        │
│  │ (versionado) │  │ (determinista)│       │
│  └──────────────┘  └──────────────┘        │
│         ↓                  ↓                │
│  ┌──────────────────────────────────┐      │
│  │ Analysis Pipeline (5 fases)      │      │
│  │ - Syntax, Quality, Security,     │      │
│  │   Performance, Refactoring       │      │
│  └──────────────────────────────────┘      │
│         ↓                                  │
│  ┌──────────────────────────────────┐      │
│  │ Output Layer                     │      │
│  │ - JSON, SARIF, Diffs             │      │
│  │ - Evidence traces (auditable)    │      │
│  └──────────────────────────────────┘      │
│                                             │
└─────────────────────────────────────────────┘
```

**Describe:**
- Cómo se vuelven "pluggable" las fases (si aplica)
- Cómo se versiona reglas/policies/prompts (determinismo)
- Cómo se mantiene determinismo con paralelismo (si se agrega)

---

#### 3. Estrategia de tests y validación
**Golden Test Suite:**
- Qué archivos/casos son "test fixtures" que nunca cambian
- Ej: demo_input.py siempre reporta 9 vulns exactas
- Ej: demo_enhanced.py 3 casos = resultados idénticos

**Regresión:**
- Test: cada nueva fase no rompe anteriores
- Test: mismo código → mismo JSON (determinismo)

**Property-based (si aplica):**
- Ej: "Para cualquier SQL vulnerable, Phase 3 DEBE detectarlo"
- Tool sugerida: Hypothesis (Python)

**Performance budgets:**
- Phase 1: <100ms por archivo
- Phase 3: <400ms por archivo
- Total: <2s por archivo

**Validación de refactors propuestos:**
- Lint: no syntax errors
- Typecheck: tipos coinciden con original
- Tests: fixture tests pasan (si existen)

---

#### 4. Threat model resumido (Top 5)
Formato: Amenaza → Impacto → Mitigación

Ejemplo:
1. **Exfiltración de código:** Alto → Análisis local, sin cloud logs
2. **Prompt injection:** Alto → Input sanitization + contexto separado
3. **Falsos positivos masivos:** Medio → Validación determinista + chain traces
4. **Performance degradación:** Medio → Caching + budgets monitoreados
5. **Dependency supply chain:** Bajo → Pinned versions, SBOM

---

### Restricciones
- ✅ Cada iniciativa en backlog debe tener criterio testeable
- ✅ Threat model debe ser específico a EROS (no genérico)
- ✅ Arquitectura debe soportar determinismo en todos los horizontes

