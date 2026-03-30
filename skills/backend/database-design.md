# @database-design

OBJETIVO: Diseñar modelos de datos y elegir DB u ORM con criterios de uso real, rendimiento y capacidad de evolución.

USAR CUANDO: Hay que definir schema nuevo, revisar relaciones, elegir base de datos o decidir ORM o query builder.

NO USAR CUANDO: El problema principal es optimización SQL puntual en un engine ya definido. En ese caso usar @sql-pro o @postgres-best-practices.

INSTRUCCIONES:

1. Empezar por patrones de acceso, volumen, consistencia, multi-tenant y estrategia de evolución antes de elegir base de datos u ORM.
2. Elegir engine y capa de acceso por contexto: PostgreSQL para transaccional general, SQLite para simple o local-first, opciones serverless cuando el despliegue lo justifique.
3. Modelar entidades, relaciones, constraints e índices según queries reales y no solo según intuición del dominio.
4. Cerrar con plan de migration, riesgos de rendimiento y decisiones explícitas sobre normalización, JSON y N+1.

FORMATO DE SALIDA:

- Objetivo del modelo
- Engine y capa de acceso elegidos
- Entidades y relaciones
- Índices y constraints
- Riesgos de evolución o rendimiento

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de schema y DB.
- Ver `./_templates.md` para el template de diseño de base de datos.
- Ver `./resources/database-postgres-playbook.md` para selección de motor, migrations, índices y quality gates.
- Ver `./upstream/database-design/SKILL.md` para el skill upstream completo.
- Ver `./upstream/database-design/` para selección de motor, ORM, schema, índices, optimización y migrations sin compresión.

ANTI-PATRÓN: Elegir PostgreSQL para todo sin contexto, omitir índices, abusar de JSON donde conviene estructura, ignorar N+1 o diseñar sin plan de migration.
