## PROMPT FASE 1 — "EROS Roadmap Visioning"
**Objetivo:** Crear North Star + Roadmap de 4 horizontes (H0-H3)

---

### Contexto inmutable
- **Proyecto:** EROS Code Analysis Agent
- **Estado actual:** Demo hackathon (Python, 5 fases, determinista, local)
- **Usuarios:** Primario = AppSec teams; Secundario = Tech Leads
- **Principios:** Determinismo estricto, auditabilidad, ejecución local reproducible, sin autofix ciego
- **Restricción:** Mantener pipeline de 5 fases sin cambios estructurales

### Tu rol
Eres **EROS Product Architect**. Diseña un roadmap realista que evolucione EROS desde hackathon a herramienta AppSec production.

---

### Entradas (rellena antes de ejecutar)
```
Prioridad principal:          [B = AppSec production real]
Entorno objetivo:             [CI/CD first (GitHub Actions)]
Límite de tiempo por archivo: [2 segundos (actual)]
Tamaño repo target:           [Hasta 100K LOC por análisis]
Nivel de riesgo aceptable:    [Bajo = sin autofix; Medio = fixes validated]
```

---

### Salida requerida

#### 1. North Star (no negociable)
**Visión (2 frases):**
- Frase 1: ¿Qué es EROS en 1 año?
- Frase 2: ¿Para quién y por qué?

**5 Principios no negociables:**
1. 
2. 
3. 
4. 
5. 

---

#### 2. Roadmap por horizontes

**H0: Hackathon (0–7 días)**
- **Objetivo:** Ganar evento, validar concepto
- **Entregables (5-7):** [lista concreta]
- **Riesgos (2-3):** [y mitigation]
- **Métrica de éxito:** [medible, ej: "demo ejecutable en <2s"]

**H1: Post-hackathon (2–4 semanas)**
- **Objetivo:** [ej: beta con 3 AppSec teams]
- **Entregables (5-7):** [ej: GitHub Actions integration, SARIF export, etc.]
- **Riesgos (2-3):**
- **Métrica de éxito:** [ej: "SARIF validado vs 3 herramientas diferentes"]

**H2: Escala equipo (2–3 meses)**
- **Objetivo:** [ej: MVP multi-lenguaje + panel web]
- **Entregables (5-7):** [ej: JavaScript support, policy engine, reportes agregados]
- **Riesgos (2-3):**
- **Métrica de éxito:** [ej: "JavaScript funciona con same latency que Python"]

**H3: Plataforma (6–12 meses)**
- **Objetivo:** [ej: SaaS enterprise-ready + partners]
- **Entregables (5-7):** [ej: multi-lenguaje complete, Kubernetes deployment, audit logs]
- **Riesgos (2-3):**
- **Métrica de éxito:** [ej: "3+ Fortune 500 pilots, <50ms análisis remoto"]

---

### Restricciones de calidad
- ✅ Cada entregable debe tener criterio de aceptación medible
- ✅ No inventar arquitectura — validar contra principios EROS
- ✅ Separar "must-have" (H0/H1) vs "nice-to-have" (H2/H3)
- ✅ Identificar explícitamente qué requiere AI modelo upgrade vs arquitectura

---

### Instrucciones finales
1. Mantén horizontes realistas (no prometas multi-lenguaje en H1)
2. Prioriza CI/CD integration (es blocker para adopción AppSec)
3. Para cada horizonte: risk assessment + mitigation plan
4. Métricas deben ser testables (no "better", sino "X% faster")
