# @llm-ops

## OBJETIVO

Operacionalizar sistemas LLM en produccion con observabilidad, versionado, guardrails y optimizacion continua basada en metricas. La skill convierte un demo funcional en un servicio operable.

## USAR CUANDO

- Un sistema LLM ya existe y debe pasar a produccion o madurar su operacion.
- Hay que definir logging, trazas, cache, fallback, rate limits o alarmas.
- Se necesita medir costo, latencia, calidad y drift de forma continua.

## NO USAR CUANDO

- El producto aun esta en fase de descubrimiento arquitectonico; usar ai-engineer.
- Solo hace falta mejorar el prompt o el contexto sin baseline operativo.
- No existe un flujo desplegado o al menos una ruta feliz medible.

## INSTRUCCIONES

1. Establecer baseline de modelo, throughput, latencia, costo, volumen y tasa de error.
2. Diseñar pipeline operativo con versionado de prompts, logging estructurado, trazas, cache y manejo de fallos del proveedor.
3. Implementar guardrails, retries razonados, circuit breakers, alarmas y politicas de datos sensibles.
4. Medir costo, latencia, calidad y drift para decidir optimizaciones con impacto real.

## FORMATO DE SALIDA

- Baseline operativo.
- Controles y observabilidad requeridos.
- Riesgos operativos detectados.
- Metricas a monitorear.
- Siguiente iteracion de optimizacion.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./context-engineering.md

## ANTI-PATRON

- Pasar un demo a produccion sin logging.
- Depender de un solo modelo sin fallback.
- Optimizar solo tokens ignorando calidad y operabilidad.
