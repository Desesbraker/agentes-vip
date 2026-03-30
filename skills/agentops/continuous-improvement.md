# @continuous-improvement

OBJETIVO: Convertir datos de producción y hallazgos de evaluación en un ciclo de mejora continua atribuible y sostenible.

USAR CUANDO: Hay que priorizar fallos reales, proponer experimentos de mejora o institucionalizar aprendizajes en agentes ya operativos.

NO USAR CUANDO: Todavía no existe baseline, harness o métricas mínimas. Primero construir esa base con @agent-evaluation y @eval-harness.

INSTRUCCIONES:

1. Recolectar evidencia real de producción y priorizar por impacto, frecuencia, severidad y costo, no por anécdotas aisladas.
2. Traducir cada problema a una hipótesis concreta con un cambio aislado, una medición before/after y una condición de rollback.
3. Ejecutar iteraciones pequeñas y atribuibles para saber qué intervención produjo mejora, degradación o efecto nulo.
4. Cerrar el ciclo actualizando baseline, métricas, harnesses y documentación para que el aprendizaje se vuelva operativo y no anecdótico.

FORMATO DE SALIDA:

- Problema priorizado
- Hipótesis
- Cambio aislado
- Resultado before/after
- Decisión y siguiente paso

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para reglas duras del ciclo.
- Ver `./_templates.md` para reporte de evaluación y experimento.

ANTI-PATRÓN: Cambiar muchas variables a la vez, iterar por intuición, ignorar datos de producción o declarar mejora sin medir impacto sostenido.
