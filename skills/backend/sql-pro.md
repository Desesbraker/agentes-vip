# @sql-pro

OBJETIVO: Escribir SQL correcto, legible y eficiente para análisis, servicios transaccionales y diagnóstico de rendimiento.

USAR CUANDO: Hay que construir queries complejas, revisar planes de ejecución o explicar por qué una consulta no escala.

NO USAR CUANDO: La decisión principal todavía es de modelado de base de datos o de engine. En ese caso usar @database-design.

INSTRUCCIONES:

1. Empezar por el objetivo de la consulta y el patrón de acceso antes de elegir joins, CTEs, ventanas o subqueries.
2. Revisar siempre el plan de ejecución y los índices relacionados antes de asumir que el problema es solo sintáctico.
3. Optimizar con evidencia: cardinalidad, estadísticas, filtros, agrupaciones, particionado o pooling según el caso.
4. Entregar la query junto con criterios de validación, riesgos de rendimiento y supuestos sobre volumen de datos.

FORMATO DE SALIDA:

- Objetivo de la query
- Query o patrón propuesto
- Índices o plan relevante
- Riesgo de rendimiento
- Validación requerida

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de schema y DB.
- Ver `./_templates.md` para el template de diseño de base de datos.
- Ver `./resources/database-postgres-playbook.md` para EXPLAIN, índices, locking, pooling y validación post-optimización.
- Ver `./upstream/sql-pro/SKILL.md` para la guía upstream base de SQL.
- Ver `./upstream/sql-optimization-patterns/SKILL.md` y `./upstream/sql-optimization-patterns/resources/implementation-playbook.md` para optimización, EXPLAIN y patrones de mejora más detallados.

ANTI-PATRÓN: Usar SELECT * en producción, ignorar EXPLAIN, asumir índices sin comprobarlos o comparar rendimiento sin estadísticas ni contexto de datos.
