# Playbook: AgentOps Core

## Objetivo

Dar una base operativa común para baseline, métricas, harnesses, optimización de prompts, auditoría de contexto y mejora continua.

## Flujo recomendado

1. Confirmar agente, objetivo, baseline y cambios bajo evaluación.
2. Separar calidad, costo, latencia, seguridad y tool use en métricas distintas.
3. Construir o actualizar harness antes de cambiar prompts, contexto o modelo en producción.
4. Ejecutar before/after con segmentos comparables y cerrar con recomendación accionable.

## Reglas duras

- No optimizar sin baseline.
- No aprobar cambios sin resultados comparables.
- No mezclar demasiadas variables en un solo experimento.
- No usar una métrica aislada para declarar mejora.
- No enviar a producción un agente nuevo sin harness o hard gate.

## Checklists rápidos

### Baseline

- Casos típicos definidos
- Edge cases incluidos
- Adversariales incluidos
- Fuera de scope marcado
- Métricas con fórmula y fuente

### Harness

- Dataset versionado
- Rúbrica clara
- Outputs parseables
- Comparación entre corridas posible
- Hard gate definido

### Prompt y contexto

- Hipótesis explícita
- Cambio aislado
- Before y after comparable
- Impacto en costo y latencia revisado
- Rollback claro