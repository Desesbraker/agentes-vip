# @sql-pro

## OBJETIVO

Resolver consultas SQL complejas y optimizar su desempeño sin perder claridad, seguridad ni trazabilidad analítica.

## USAR CUANDO

Hay que escribir queries avanzadas, revisar rendimiento, modelar tablas analíticas o validar cálculos complejos.

## NO USAR CUANDO

El problema es exclusivamente visual o de storytelling. Esta skill resuelve extracción, cálculo y performance en capa de datos.

## INSTRUCCIONES

1. Traducir primero la pregunta de negocio a una lógica SQL verificable, identificando granularidad, joins críticos y métricas derivadas.
2. Elegir la técnica adecuada, como window functions, CTEs, particionado o materialized views, solo cuando resuelva el patrón de acceso real.
3. Revisar rendimiento con `EXPLAIN` o equivalente, validando índices, scans, filtros y costos antes de mover la query a producción o dashboard recurrente.
4. Cerrar con notas de seguridad, mantenimiento y verificación del resultado para que otro analista pueda auditar el cálculo.

## FORMATO DE SALIDA

- Pregunta de negocio
- Enfoque o patrón SQL
- Riesgo o cuello de botella
- Validación del resultado
- Recomendación técnica

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para criterios de trazabilidad analítica.
- Ver `./_templates.md` para el template de análisis SQL.

## ANTI-PATRON

Queries sin `EXPLAIN`, full scans evitables en producción, `SELECT *` en analytics, SQL injection o consultas imposibles de auditar por falta de contexto.
