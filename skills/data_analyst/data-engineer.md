# @data-engineer

## OBJETIVO

Diseñar pipelines y arquitectura de datos confiables, observables e idempotentes para analytics, reporting o activación operacional.

## USAR CUANDO

Hay que construir un warehouse, un pipeline batch o streaming, una capa de transformación o gobierno de datos.

## NO USAR CUANDO

La tarea es solo análisis de negocio o diseño visual del dashboard. Esta skill resuelve infraestructura y modelado de datos.

## INSTRUCCIONES

1. Definir primero fuentes, granularidad, SLAs, sensibilidad del dato y consumidor final para elegir stack y arquitectura sin sobreingeniería.
2. Separar ingestión, transformación y serving, decidiendo batch, streaming o CDC según frescura requerida y costo operativo aceptable.
3. Incluir desde el diseño calidad, lineage, schema evolution, monitoreo e idempotencia para que el pipeline sea confiable y depurable.
4. Cerrar con modelo operativo: cloud elegido, ownership, controles de seguridad y plan de observabilidad.

## FORMATO DE SALIDA

- Objetivo del pipeline o warehouse
- Fuentes y SLA
- Arquitectura y stack
- Calidad, governance y seguridad
- Riesgo operativo principal

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de fuentes y trazabilidad.
- Ver `./_templates.md` para el template de análisis SQL o métrica.

## ANTI-PATRON

Pipelines sin monitoreo, ausencia de quality checks, PII desprotegida, ETL sin idempotencia o data products sin lineage ni ownership.
