# @agent-evaluation

OBJETIVO: Diseñar evaluaciones reproducibles para saber si un agente mejora, empeora o sigue inestable después de cada cambio.

USAR CUANDO: Hay que medir calidad de respuestas, uso de herramientas, formato, costo, latencia, seguridad o readiness antes de liberar un agente.

NO USAR CUANDO: Solo hace falta diseñar prompts iniciales o definir arquitectura de contexto. Eso pertenece a AI Engineer; AgentOps entra cuando ya existe un baseline evaluable.

INSTRUCCIONES:

1. Crear baseline con casos representativos, edge cases, adversariales y fuera de scope antes de tocar prompts, tools o contexto.
2. Definir rúbrica multidimensional por tarea: completion, factuality, formato, seguridad, tool use, costo y latencia; medir outcomes, no intuiciones.
3. Ejecutar varias corridas si hay no determinismo y registrar distribución, fallos recurrentes y degradaciones frente al baseline.
4. Cerrar cada eval con decisiones accionables: cambio propuesto, hipótesis, hard gates y criterio explícito para aprobar, repetir o bloquear deploy.

FORMATO DE SALIDA:

- Objetivo de la evaluación
- Dataset o casos usados
- Métricas y rúbrica
- Resultado vs baseline
- Recomendación: ship, iterar o bloquear

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de baseline y hard gates.
- Ver `./_templates.md` para baseline y reporte de evaluación.

ANTI-PATRÓN: Optimizar sin baseline, evaluar una sola corrida, medir una sola métrica o aprobar un agente porque se siente mejor sin evidencia reproducible.
