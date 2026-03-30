# @workflow-automation

## OBJETIVO

Diseñar workflows entre agentes o procesos automatizados con patron adecuado, durabilidad razonable y observabilidad suficiente. La skill transforma coordinacion dispersa en flujo controlado y recuperable.

## USAR CUANDO

- Hay que coordinar varios agentes o pasos automatizados.
- Se debe elegir entre flujo secuencial, paralelo u orchestrator-worker.
- Existen llamadas externas, reintentos o checkpoints que necesitan diseno explicito.

## NO USAR CUANDO

- Solo se requiere un plan corto de ejecucion individual; usar planificacion-concisa.
- La solicitud aun esta en fase de entendimiento; usar brainstorming.
- No hay proceso repetible o dependencias entre pasos.

## INSTRUCCIONES

1. Seleccionar el patron de workflow segun dependencias, paralelismo y necesidad de coordinacion central.
2. Definir idempotency, timeouts, checkpoints, retries y backoff en pasos con efectos externos.
3. Diseñar logs, metricas y alertas para detectar fallos y reanudar donde corresponda.
4. Entregar el flujo con puntos de validacion, riesgos operativos y criterio de recuperacion.

## FORMATO DE SALIDA

- Patron de workflow elegido.
- Pasos y dependencias.
- Controles de durabilidad y reintento.
- Observabilidad requerida.
- Riesgos y validacion del flujo.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./planificacion-concisa.md

## ANTI-PATRON

- Omitir ejecucion durable en flujos sensibles.
- Diseñar workflows monoliticos sin checkpoints.
- No incluir observabilidad ni recuperacion.
