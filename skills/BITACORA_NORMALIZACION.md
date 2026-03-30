# Bitácora de Normalización de Skills

> **Autor:** Arquitecto de Agentes | **Fecha inicio:** 29/03/2026  
> **Referencia upstream:** [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)  
> **Norma operativa:** `./CARGA_DE_SKILLS.md` (L1 perfil → L2 skill → L3 anexos)

---

## 1. FORMATO CANON — Referencia Rápida

Cada skill DEBE contener estas 7 secciones para considerarse completa:

| # | Sección | Principio | Test de aceptación |
|---|---------|-----------|-------------------|
| 1 | **OBJETIVO** | P1 — Rol sin ambigüedad | Dice qué resuelve y por qué en ≤2 frases |
| 2 | **USAR CUANDO** | P3 — Trigger explícito | Lista escenarios concretos de activación |
| 3 | **NO USAR CUANDO** | P1+P4 — Boundaries | Redirige a skill alternativa; no deja vacío |
| 4 | **INSTRUCCIONES** | P2 — Output estructurado | 4 pasos numerados, verificables, sin jargon indefinido |
| 5 | **FORMATO DE SALIDA** | P2 — Template parseable | 5 bullets que describen el entregable esperado |
| 6 | **RECURSOS RELACIONADOS** | P6 — Skills como referencia | Link a `_playbook.md` y `_templates.md` de la familia |
| 7 | **ANTI-PATRÓN** | P4 — Fallos anticipados | ≥3 anti-patrones concretos |

Cada familia DEBE tener además:

| Anexo | Contenido |
|-------|-----------|
| `_playbook.md` | Flujo operativo, reglas duras, checklists rápidos |
| `_templates.md` | Plantillas fill-in reutilizables por el agente |

### Mapeo con upstream (antigravity-awesome-skills `skill-anatomy.md`)

| Nuestro formato | Upstream equivalente |
|-----------------|---------------------|
| OBJETIVO | Overview |
| USAR CUANDO | When to Use This Skill |
| NO USAR CUANDO | *(añadido nuestro — no tiene equivalente directo)* |
| INSTRUCCIONES | How It Works (Steps) |
| FORMATO DE SALIDA + `_templates.md` | Examples + Templates |
| RECURSOS RELACIONADOS + `_playbook.md` | Related Skills + References |
| ANTI-PATRÓN | Common Pitfalls / Best Practices (❌) |

### Ejemplo de skill normalizada (referencia)

```
skills/backend/api-design-principles.md
```

---

## 2. DASHBOARD DE ESTADO

| Familia | Skills | Canon | _playbook | _templates | Estado | Prioridad |
|---------|--------|-------|-----------|------------|--------|-----------|
| backend | 11 | ✅ 11/11 | ✅ | ✅ | COMPLETO | — |
| agentops | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| mobile_desktop | 10 | ✅ 10/10 | ✅ | ✅ | COMPLETO | — |
| seo | 11 | ✅ 11/11 | ✅ | ✅ | COMPLETO | — |
| **devops** | **10** | ✅ 10/10 | ✅ | ✅ | COMPLETO | — |
| **copywriter** | **7** | ✅ 7/7 | ✅ | ✅ | COMPLETO | — |
| product_manager | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| growth_revops | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| paid_media | 5 | ✅ 5/5 | ✅ | ✅ | COMPLETO | — |
| customer_support | 5 | ✅ 5/5 | ✅ | ✅ | COMPLETO | — |
| media_video | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| security_auditor | 9 | ✅ 9/9 | ✅ | ✅ | COMPLETO | — |
| game_developer | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| 3d_character | 5 | ✅ 5/5 | ✅ | ✅ | COMPLETO | — |
| ai_engineer | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |
| arquitecto | 2 | ✅ 2/2 | ✅ | ✅ | COMPLETO | — |
| orquestador | 5 | ✅ 5/5 | ✅ | ✅ | COMPLETO | — |
| frontend | 10 | ✅ 10/10 | ✅ | ✅ | COMPLETO | — |
| qa_testing | 9 | ✅ 9/9 | ✅ | ✅ | COMPLETO | — |
| data_analyst | 10 | ✅ 10/10 | ✅ | ✅ | COMPLETO | — |
| ui_ux | 6 | ✅ 6/6 | ✅ | ✅ | COMPLETO | — |

**Totales:** 21 familias | 151 skills | 151/151 normalizadas | 21/21 familias completas

**Ultima actualizacion:** Se completaron `frontend`, `qa_testing`, `data_analyst` y `ui_ux`. En estas cuatro familias los anexos ya existian; el cierre consistio en convertir todas las skills al canon estructural con encabezados uniformes y validar el catalogo completo sin errores.

---

## 3. CIERRE EJECUTIVO

La normalización quedó cerrada en una sola arquitectura operativa para todo el catálogo:

1. Todas las skills usan el mismo contrato de activación, ejecución y salida.
2. Todas las familias tienen anexos de apoyo (`_playbook.md` y `_templates.md`).
3. La carga queda alineada con `skills/CARGA_DE_SKILLS.md`: perfil L1, skill L2, profundidad L3.
4. El repositorio preservó su estructura original por familia, sin migración a carpetas por skill.

### 3.1 Modos de intervención aplicados

Se usaron dos modos de cierre, según el estado real de cada familia:

| Modo | Cuándo se aplicó | Resultado |
|------|------------------|-----------|
| **Reescritura completa** | Familias telegráficas o sin canon consistente | Se reescribieron skills y se crearon anexos de familia |
| **Homologación estructural** | Familias con buen contenido pero sin encabezados canon uniformes | Se mantuvo el contenido sustantivo y se normalizó la estructura |

### 3.2 Familias por tipo de intervención

| Familia | Skills | Intervención principal | Estado |
|---------|--------|------------------------|--------|
| backend | 11 | Reescritura completa | COMPLETO |
| agentops | 6 | Reescritura completa | COMPLETO |
| mobile_desktop | 10 | Reescritura completa | COMPLETO |
| seo | 11 | Reescritura completa | COMPLETO |
| devops | 10 | Reescritura completa | COMPLETO |
| copywriter | 7 | Reescritura completa + glosario operativo | COMPLETO |
| product_manager | 6 | Reescritura completa | COMPLETO |
| growth_revops | 6 | Reescritura completa | COMPLETO |
| paid_media | 5 | Reescritura completa | COMPLETO |
| customer_support | 5 | Reescritura completa | COMPLETO |
| media_video | 6 | Reescritura completa | COMPLETO |
| security_auditor | 9 | Reescritura completa | COMPLETO |
| game_developer | 6 | Reescritura completa | COMPLETO |
| 3d_character | 5 | Reescritura completa | COMPLETO |
| ai_engineer | 6 | Reescritura completa | COMPLETO |
| arquitecto | 2 | Reescritura completa | COMPLETO |
| orquestador | 5 | Reescritura completa | COMPLETO |
| frontend | 10 | Homologación estructural | COMPLETO |
| qa_testing | 9 | Homologación estructural | COMPLETO |
| data_analyst | 10 | Homologación estructural | COMPLETO |
| ui_ux | 6 | Homologación estructural | COMPLETO |

### 3.3 Correcciones de mayor valor

- Se eliminó ambigüedad de activación entre skills que antes se solapaban.
- Se hicieron explícitos los límites de uso con `NO USAR CUANDO` en todo el catálogo.
- Se volvió parseable la salida esperada de cada skill.
- Se conectaron skills con anexos y recursos relacionados, reduciendo dependencia de conocimiento implícito.
- Se corrigieron huecos operativos específicos, como checklists no enumerados, jargon sin definir y referencias compartidas rotas.

## 4. VALIDACIÓN FINAL

La validación final del catálogo cubrió:

1. Presencia de las 7 secciones canon en todas las skills normalizadas.
2. Existencia de `_playbook.md` y `_templates.md` por familia.
3. Ausencia de errores en las familias modificadas durante cada tanda.
4. Sincronización del avance con memoria de sesión y dashboard central.

## 5. RIESGOS RESIDUALES

No quedan riesgos estructurales abiertos en la normalización. Los riesgos residuales son editoriales y de mantenimiento:

1. Algunas familias siguen teniendo diferencias leves de tono porque se preservó contenido sustantivo cuando ya era bueno.
2. La bitácora dejó de ser backlog y ahora funciona como documento de cierre; si se reinicia otra ronda de cambios, conviene abrir una bitácora nueva.
3. Cualquier nueva skill agregada al catálogo deberá pasar por el mismo contrato canon para evitar regresión estructural.

## 6. REGLA DE MANTENIMIENTO

Toda skill nueva o modificada debe cumplir antes de considerarse lista:

1. `OBJETIVO` explícito en no más de dos frases.
2. `USAR CUANDO` y `NO USAR CUANDO` sin overlaps silenciosos.
3. `INSTRUCCIONES` accionables y verificables.
4. `FORMATO DE SALIDA` parseable.
5. `RECURSOS RELACIONADOS` apuntando a anexos reales.
6. `ANTI-PATRÓN` con fallos concretos.
7. Validación posterior sin errores relevantes.

## 7. CIERRE

La normalización de skills del repositorio `Agentes vip` queda cerrada con cobertura total del catálogo y una estructura homogénea alineada al estándar definido para el proyecto.
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### 3d-modeling-pipeline.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### texturing.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### rigging-export.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### asset-organization.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### Anexos 3D Character
- [ ] `_playbook.md` — Crear con: pipeline Concept→Model→Texture→Rig→Export, naming conventions, LOD strategy
- [ ] `_templates.md` — Crear con: Character sheet, Asset checklist, Texture map spec, Rig verification, Export config

---

### 3.15 P2 — AI Engineer (6 skills)

> **Auditoría pendiente.**

#### ai-engineer.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### prompt-engineering.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### context-engineering.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### llm-app-patterns.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### rag-engineer.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### llm-ops.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### Anexos AI Engineer
- [ ] `_playbook.md` — Crear con: flujo Design→Prompt→Evaluate→Deploy→Monitor, model selection criteria, RAG architecture decision tree, frontera con AgentOps
- [ ] `_templates.md` — Crear con: Prompt template card, RAG pipeline spec, LLM app architecture doc, Evaluation report, Context budget plan

---

### 3.16 P2 — Arquitecto (2 skills)

> **Auditoría pendiente. Familia propia del meta-agente.**

#### construccion-agentes.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### auditoria-perfiles.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### Anexos Arquitecto
- [ ] `_playbook.md` — Crear con: flujo Solicitud→Entrevista→Diseño→Checklist→Entrega, P1-P8 como checklist rápido, límites de prompt por categoría
- [ ] `_templates.md` — Crear con: Perfil de agente (skeleton), Checklist de auditoría, RACI entre agentes, Reporte de auditoría

---

### 3.17 P2 — Orquestador (5 skills)

> **Auditoría pendiente.**

#### planificacion-concisa.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### brainstorming.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### workflow-automation.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### mejora-continua.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### open-seo-routing.md
- [ ] OBJETIVO  - [ ] USAR CUANDO  - [ ] NO USAR CUANDO  - [ ] INSTRUCCIONES  - [ ] FORMATO DE SALIDA  - [ ] RECURSOS RELACIONADOS  - [ ] ANTI-PATRÓN

#### Anexos Orquestador
- [ ] `_playbook.md` — Crear con: flujo de routing de solicitudes, decision tree de delegación, reglas de escalamiento, handoff protocol
- [ ] `_templates.md` — Crear con: Plan de proyecto, Brainstorming output, Workflow spec, Mejora continua log, Routing decision log

---

## 4. HALLAZGOS ESPECÍFICOS DE AUDITORÍA

### 4.1 DevOps — Hallazgos críticos

| # | Archivo | Línea | Hallazgo | Principio violado | Acción correctiva |
|---|---------|-------|----------|-------------------|-------------------|
| D1 | deployment-procedures.md | 5 | "Checklist obligatorio de 8 puntos" no enumerado | P2 (output estructurado), P3 (trigger explícito) | Listar los 8 puntos en INSTRUCCIONES y mover checklist completo a `_playbook.md` |
| D2 | Todas (10/10) | 1-2 | TRIGGER fusionado con USAR CUANDO | P3 (trigger explícito) | Separar en USAR CUANDO + NO USAR CUANDO con redirección a skill alternativa |
| D3 | Todas (10/10) | — | Sin FORMATO DE SALIDA | P2 (template parseable) | Añadir 5 bullets describiendo entregable esperado |
| D4 | Todas (10/10) | — | Sin RECURSOS RELACIONADOS | P6 (skills como referencia) | Crear `_playbook.md` + `_templates.md` y referenciar |
| D5 | Todas (10/10) | — | Rango 105-130 palabras | — | Expandir a ~250-400 con secciones canon. Son recordatorios, no playbooks |

### 4.2 Copywriter — Hallazgos críticos

| # | Archivo | Línea | Hallazgo | Principio violado | Acción correctiva |
|---|---------|-------|----------|-------------------|-------------------|
| C1 | content-creator.md | 4 | Ratio 40/25/25/10 sin definir pilares | P3 (trigger explícito) | Definir: 40% educativo / 25% entretenimiento / 25% promocional / 10% comunidad (o pilares reales del proyecto) |
| C2 | copy-editing.md | 1 | Seven Sweeps nombrados sin detallar | P3 (trigger explícito) | Detallar cada sweep con qué verificar y cómo en `_playbook.md` |
| C3 | copy-editing.md | 3 | "activar voz pasiva" — probable error | P2 (output estructurado) | Corregir a "activar voz activa / eliminar voz pasiva" |
| C4 | writing-skills.md | 2 | CSO no es término estándar | P3 (trigger explícito) | Definir: Content Search Optimization = optimizar description y triggers para search del agente |
| C5 | writing-skills.md | 5 | RED-GREEN-REFACTOR sin contexto | P3 (trigger explícito) | Definir: ciclo TDD — test que falla → implementar mínimo → refactorizar |
| C6 | writing-skills.md | 1 | Tiers mencionados sin aterrizar | P3 (trigger explícito) | Aclarar: T1 <200 líneas, T2 200-1000, T3 platform 10+ productos |
| C7 | doc-coauthoring.md | 4 | "str_replace" — leak de herramienta IDE | P1 (rol sin ambigüedad) | Reemplazar por "Editar sección específica, nunca reimprimir completo" |
| C8 | doc-coauthoring.md | 5 | "80% de completitud" umbral arbitrario | P3 (trigger explícito) | Justificar o eliminar; reemplazar "slop" por término profesional |
| C9 | copywriting.md / content-creator.md | — | Overlap sin resolver para blogs | P1 (rol sin ambigüedad) | Resolver en NO USAR CUANDO: @copywriting = conversión (landing, ads), @content-creator = marca (blog, social, calendar) |
| C10 | open-seo-content-intel.md | 4 | Si DATAFORSEO_API_KEY no configurada, research bloqueada | P4 (fallos anticipados) | Documentar fallback: solicitar apoyo a SEO Specialist o declarar placeholders explícitos |

---

## 5. PROTOCOLO DE ACTUALIZACIÓN

### Cómo actualizar esta bitácora

1. **Al iniciar una familia:** Auditar cada skill leyendo contenido completo. Marcar con `[x]` las secciones presentes, `[ ]` las faltantes, `[!]` las defectuosas. Añadir notas específicas.
2. **Al normalizar una skill:** Cambiar cada `[ ]` a `[x]` conforme se añade la sección. Actualizar conteo en Dashboard (sección 2).
3. **Al crear anexos:** Marcar `[x]` en la línea de `_playbook.md` y `_templates.md` de la familia.
4. **Al completar una familia:** Cambiar Estado a `COMPLETO` en Dashboard. Dejar Prioridad como `—`.

### Validación automática

Confirmar normalización con búsquedas grep en el directorio de la familia:

```bash
# Verificar que TODAS las skills tienen las 7 secciones
grep -l "OBJETIVO" skills/<familia>/*.md | wc -l
grep -l "USAR CUANDO" skills/<familia>/*.md | wc -l
grep -l "NO USAR CUANDO" skills/<familia>/*.md | wc -l
grep -l "FORMATO DE SALIDA" skills/<familia>/*.md | wc -l
grep -l "RECURSOS RELACIONADOS" skills/<familia>/*.md | wc -l
grep -l "ANTI-PATRÓN" skills/<familia>/*.md | wc -l

# Verificar que existen anexos
ls skills/<familia>/_playbook.md skills/<familia>/_templates.md
```

### Referencias cruzadas

- Contrato de carga: `./CARGA_DE_SKILLS.md`
- Skill normalizada de referencia: `./backend/api-design-principles.md`
- Upstream: [sickn33/antigravity-awesome-skills — skill-anatomy.md](https://github.com/sickn33/antigravity-awesome-skills/blob/main/docs/contributors/skill-anatomy.md)
- Perfil del Arquitecto: `../agente_arquitecto/perfil.md` (P1-P8)
