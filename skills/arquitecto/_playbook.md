# Playbook de Arquitecto

## Objetivo

Convertir auditoría y construcción de agentes en procesos trazables, con gates explícitos, evidencia y contratos estructurales repetibles.

## Flujo operativo

1. Confirmar dominio, objetivos, outputs, restricciones e interacciones mínimas.
2. Evaluar o construir la estructura obligatoria antes de redactar detalle.
3. Detectar huecos, overlaps, jargon indefinido, fallos de routing y violaciones a P1-P8.
4. Entregar score, hallazgos y plan de corrección o perfil final validado.

## Mapa de upstream importado

- `./upstream/ai-agents-architect/`
- `./upstream/agent-evaluation/`
- `./upstream/architect-review/`
- `./upstream/skill-check/`

## Reglas duras

- No aprobar perfiles con items estructurales faltantes.
- No construir sobre supuestos críticos no respondidos.
- Todo score debe estar respaldado por evidencia.
- Todo output operativo debe tener template o formato claro.

## Cuándo abrir upstream

- Abrir `./upstream/ai-agents-architect/` cuando el caso exija doctrina más profunda para diseñar agentes, composición o arquitectura multiagente.
- Abrir `./upstream/agent-evaluation/` y `./upstream/architect-review/` cuando la auditoría requiera criterios adicionales de evaluación, review técnico o benchmarking estructural.
- Abrir `./upstream/skill-check/` cuando haga falta un gate más fino sobre calidad o cobertura de una skill específica.

## Wrapper local sobre upstream

- `construccion-agentes.md` sigue siendo el wrapper local que agrega entrevista mínima, gates P1-P8 y convención `perfil_<agente>.md` sobre la base más general de `ai-agents-architect`.
- `auditoria-perfiles.md` sigue siendo el wrapper local que combina evaluación upstream con la scorecard estructural propia de esta agencia.
