# @postgres-best-practices

OBJETIVO: Diseñar y operar PostgreSQL con foco en rendimiento real, seguridad multi-tenant y estabilidad bajo carga.

USAR CUANDO: Hay que optimizar queries, modelar schemas en Postgres o Supabase, revisar índices o diseñar reglas de seguridad y concurrencia.

NO USAR CUANDO: La tarea es genérica de base de datos sin engine definido. En ese caso usar @database-design primero.

INSTRUCCIONES:

1. Priorizar problemas por evidencia: queries lentas, conexiones, locking, seguridad o crecimiento de tablas.
2. Diseñar índices, constraints, tipos y políticas RLS a partir de queries reales y del modelo de acceso esperado.
3. Revisar pooling, observabilidad y concurrencia antes de culpar al motor o al ORM por cada degradación.
4. Entregar con hipótesis de mejora verificable y una salida clara sobre queries, índices, seguridad y riesgos pendientes.

FORMATO DE SALIDA:

- Problema principal
- Query o patrón afectado
- Índices o cambios propuestos
- Seguridad y concurrencia
- Impacto esperado

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de schema y DB.
- Ver `./_templates.md` para el template de diseño de base de datos.
- Ver `./resources/database-postgres-playbook.md` para selección de motor, RLS, pooling, observabilidad y quality gates de Postgres.
- Ver `./upstream/postgres-best-practices/SKILL.md` para la guía upstream completa.
- Ver `./upstream/postgres-best-practices/rules/` para reglas priorizadas de query, conexiones, seguridad, schema, locking y monitoreo.
- Ver `./upstream/postgres-best-practices/AGENTS.md` para la versión compilada extendida del catálogo de reglas.

ANTI-PATRÓN: Dejar queries frecuentes sin índices, ignorar connection pooling, omitir RLS en multi-tenant o optimizar sin revisar evidencia en pg_stat_statements o EXPLAIN.
