# Playbook de Orquestador

## Objetivo

Estandarizar descomposición, planificación, routing y coordinación entre agentes para que cada solicitud tenga un camino claro desde intake hasta entrega validada.

## Flujo operativo

1. Entender la solicitud y bloquear incertidumbres críticas.
2. Elegir patrón: brainstorming, plan corto, workflow o routing especializado.
3. Despachar a skills o perfiles correctos con dependencias explícitas y criterio de QA.
4. Consolidar decision log, riesgos, validación y siguiente paso verificable.

## Mapa de upstream importado

- `./upstream/concise-planning/`
- `./upstream/planning-with-files/`
- `./upstream/kaizen/`
- `./upstream/workflow-automation/`
- `./upstream/multi-agent-brainstorming/`
- `./upstream/multi-advisor/`
- `./upstream/agent-orchestrator/`
- `./upstream/antigravity-skill-orchestrator/`
- `./upstream/dispatching-parallel-agents/`
- `./upstream/agent-orchestration-multi-agent-optimize/`

## Reglas duras

- No implementar durante brainstorming.
- No hacer routing con supuestos no confirmados si cambian el resultado.
- No superar el mínimo de preguntas si el contexto ya alcanza.
- Todo workflow debe tener validación, manejo de fallos y criterio de cierre.

## Cuándo abrir upstream

- Abrir `./upstream/concise-planning/` y `./upstream/planning-with-files/` cuando el plan corto necesite más doctrina operativa o persistencia documental.
- Abrir `./upstream/multi-agent-brainstorming/` y `./upstream/multi-advisor/` cuando el intake siga ambiguo o convenga explorar opciones en paralelo.
- Abrir `./upstream/workflow-automation/`, `./upstream/agent-orchestrator/`, `./upstream/antigravity-skill-orchestrator/`, `./upstream/dispatching-parallel-agents/` y `./upstream/agent-orchestration-multi-agent-optimize/` para diseñar coordinación durable, paralelismo y guardrails de sobre-orquestación.
- Abrir `./upstream/kaizen/` cuando el problema sea reincidente y ya exista evidencia suficiente para mejora continua.

## Wrapper local sin equivalente directo

- `open-seo-routing.md` permanece local porque su valor está en enrutar trabajo SEO con el setup compartido de OpenSEO y las convenciones de esta agencia, no en una skill upstream 1:1.
