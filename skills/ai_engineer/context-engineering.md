# @context-engineering

## OBJETIVO

Diseñar la arquitectura de contexto, memoria y compresion de un sistema IA para que sea util, predecible y costeable. La skill define reglas de entrada, permanencia y descarte de informacion.

## USAR CUANDO

- El sistema IA necesita controlar mejor su presupuesto de contexto.
- Hay que decidir entre truncacion, resumen, memoria persistente o retrieval.
- Se requiere documentar reglas de refresco y descarte de informacion.

## NO USAR CUANDO

- El sistema ya esta desplegado y el foco es optimizacion operativa before and after; escalar a AgentOps.
- Solo hace falta redactar un prompt aislado; usar prompt-engineering.
- No hay claridad sobre tipos de consulta ni informacion critica.

## INSTRUCCIONES

1. Mapear el presupuesto de contexto por zonas: system prompt, instrucciones dinamicas, historial, retrieval y salida esperada.
2. Elegir la tecnica adecuada segun el problema y el costo de perder informacion.
3. Definir reglas de persistencia, resumen, reconsulta y exclusiones por sensibilidad o costo.
4. Validar con pruebas de calidad y costo para detectar perdida funcional o ahorro irrelevante.

## FORMATO DE SALIDA

- Mapa del presupuesto de contexto.
- Estrategia elegida y por que.
- Reglas de refresco y descarte.
- Riesgos de perdida de informacion.
- Plan de validacion calidad versus costo.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./prompt-engineering.md

## ANTI-PATRON

- Meter todo el historial al prompt.
- Resumir sin medir perdida funcional.
- Aplicar una sola estrategia a todos los casos.
- Comprimir informacion sensible sin reglas claras.
