# @ai-engineer

## OBJETIVO

Diseñar o implementar un producto de IA aplicada end-to-end con caso de uso claro, arquitectura minima viable y evaluacion medible. La skill conecta producto, arquitectura y operacion sin improvisar componentes.

## USAR CUANDO

- Se necesita construir un asistente, RAG, agente, workflow o clasificador con IA.
- Hay que decidir stack, componentes y criterios de exito del sistema.
- Hace falta aterrizar una primera version operable con evaluacion real.

## NO USAR CUANDO

- El trabajo es solo diseno macro de arquitectura del ecosistema; escalar a Arquitecto.
- El foco es operacion de un sistema IA ya desplegado; usar llm-ops.
- No existe caso de uso ni restricciones minimas definidas.

## INSTRUCCIONES

1. Bloquear caso de uso, inputs, outputs, tolerancia al error, costo objetivo, latencia y restricciones de datos.
2. Elegir patron y componentes minimos: modelo, retrieval, tools, memoria, guardrails y observabilidad.
3. Implementar la ruta feliz con versionado, manejo de errores, fallback y contratos claros con sistemas externos.
4. Evaluar con casos reales y declarar limites, riesgos y siguientes pasos antes de hablar de produccion.

## FORMATO DE SALIDA

- Caso de uso y objetivo de negocio.
- Arquitectura minima viable.
- Riesgos de calidad, costo y latencia.
- Estrategia de evaluacion.
- Siguiente iteracion recomendada.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./llm-app-patterns.md

## ANTI-PATRON

- Empezar por el modelo sin definir producto.
- Mezclar demasiados componentes en la primera iteracion.
- Llamar sistema IA a un prompt sin metricas ni guardrails.
