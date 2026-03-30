# Database y Postgres Playbook

## Cuándo abrir este recurso

- Diseñar schema y elegir motor
- Optimizar SQL o Postgres
- Definir migrations, índices y constraints
- Resolver pooling, locking o RLS

## Fase 1: Elegir motor por contexto

| Opción | Mejor para | Trade-off |
|---|---|---|
| PostgreSQL | Transaccional general, joins complejos, madurez | Operación más pesada |
| Neon | PostgreSQL serverless, branching, previews | Misma complejidad conceptual de PG |
| SQLite | Apps simples, embebidas, local-first | Single-writer y límites de concurrencia |
| Turso | Edge y baja latencia global con SQLite | Limitaciones propias de SQLite |
| PlanetScale/MySQL | Escala global MySQL | Trade-offs con FKs y ecosistema |

### Preguntas obligatorias

1. ¿Dónde se desplegará?
2. ¿Qué tan complejas son las queries?
3. ¿Importa edge/serverless?
4. ¿Habrá multi-tenant?
5. ¿Se necesita branching o entornos efímeros?

## Fase 2: Diseñar schema

- Diseñar entidades y relaciones a partir de queries reales.
- Definir constraints temprano.
- Diseñar índices por patrón de acceso real.
- Decidir normalización vs JSON con intención explícita.

### Decision checklist

- [ ] Engine elegido por contexto
- [ ] Relaciones definidas
- [ ] Índices para queries críticas
- [ ] Estrategia de migration definida
- [ ] Riesgo de N+1 revisado

## Migrations

- Toda migration debe ser reversible o al menos tener plan de rollback.
- Separar cambios peligrosos en etapas si hay tablas grandes.
- Probar migrations en staging o snapshot antes de producción.
- Considerar backfills y locks al diseñar cambios sobre tablas calientes.

## SQL y optimización

- Empezar por `EXPLAIN` o `EXPLAIN ANALYZE`.
- Revisar cardinalidad y estadísticas.
- Evitar `SELECT *` en producción.
- Validar si el problema es índice, join, filter order, scan type o falta de stats.

### Checklist de análisis

- [ ] Plan de ejecución revisado
- [ ] Índices existentes auditados
- [ ] Volumen de datos considerado
- [ ] Locking y concurrencia observados
- [ ] Hipótesis de mejora verificable

## Postgres específico

### Pooling y conexiones

- Definir pool explícito.
- Revisar agotamiento de conexiones antes de tunear queries a ciegas.
- Cerrar conexiones con graceful shutdown.

### Seguridad multi-tenant

- Aplicar RLS cuando el modelo lo requiera.
- Diseñar políticas a partir del actor y no solo del endpoint.
- No confiar solo en filtros de aplicación si la DB debe imponer aislamiento.

### Observabilidad

- Revisar `pg_stat_statements` o equivalente.
- Medir tiempo, frecuencia y rows.
- Distinguir problema de query vs problema de pool vs problema de storage.

## Quality gates

- [ ] Schema revisado por queries reales
- [ ] Migrations probadas
- [ ] Benchmarks mínimos hechos para paths críticos
- [ ] Backups definidos
- [ ] Monitoreo definido
- [ ] Documentación técnica actualizada

## Entrega esperada

- Motor y capa de acceso elegidos
- Entidades y relaciones
- Índices y constraints
- Estrategia de migration
- Querys o planes críticos
- Riesgos de concurrencia, seguridad o escala