# Playbook: Backend Core

## Objetivo

Dar una base operativa común para contratos API, diseño de base de datos, stacks backend y pagos sin repetir la misma explicación en cada skill.

## Cómo usar este playbook

1. Usar este archivo como capa transversal mínima.
2. Abrir luego el recurso temático en `./resources/` según el tipo de trabajo.
3. Si la tarea requiere criterio detallado, ejemplos o assets reales del origen, abrir además la carpeta correspondiente en `./upstream/`.
4. No saltar directamente a implementación si todavía falta contrato, modelo de datos o decisión de stack.

## Mapa de resources

- `./resources/backend-nodejs-playbook.md`
- `./resources/api-design-playbook.md`
- `./resources/database-postgres-playbook.md`
- `./resources/python-frameworks-playbook.md`
- `./resources/stripe-billing-playbook.md`

## Mapa de upstream importado

- `./upstream/backend-dev-guidelines/`
- `./upstream/api-patterns/`
- `./upstream/api-design-principles/`
- `./upstream/nodejs-backend-patterns/`
- `./upstream/python-fastapi-development/`
- `./upstream/stripe-integration/`
- `./upstream/database-design/`
- `./upstream/postgres-best-practices/`
- `./upstream/sql-pro/`
- `./upstream/sql-optimization-patterns/`
- `./upstream/python-pro/`
- `./upstream/django-pro/`

## Flujo recomendado

1. Bloquear problema, consumidores, datos, auth y restricciones antes de elegir framework o patrón.
2. Definir contrato y modelo de datos antes de abrir endpoints o migrations.
3. Elegir stack por contexto real: Node, Python, FastAPI, Django o Postgres según restricciones técnicas y del equipo.
4. Diseñar seguridad, observabilidad y estrategia de test antes del cierre.
5. Entregar con formato parseable, riesgos explícitos y plan de rollback si el cambio toca producción.

## Reglas duras

- No abrir endpoints sin contrato y errores definidos.
- No diseñar schema sin índices, constraints y estrategia de evolución.
- No mezclar lógica de negocio con capa HTTP.
- No integrar Stripe sin webhooks verificados e idempotencia.
- No aprobar cambios backend sin plan de test y rollback.

## Árbol rápido de decisión

### Si el problema es API

- Elegir `@api-patterns` si todavía no se decidió estilo.
- Elegir `@api-design-principles` si el estilo ya existe y falta contrato.
- Abrir `./resources/api-design-playbook.md` para checklists y formatos.
- Abrir `./upstream/api-patterns/` o `./upstream/api-design-principles/` cuando haga falta profundizar en auth, versionado, documentación, assets o checklist detallado.

### Si el problema es backend Node

- Elegir `@backend-dev-guidelines` para implementación.
- Elegir `@nodejs-best-practices` para decisiones de runtime, framework y operación.
- Abrir `./resources/backend-nodejs-playbook.md` para arquitectura, validación, observabilidad y testing.
- Abrir `./upstream/backend-dev-guidelines/` para doctrina completa de capas, BaseController, repositorios, configuración, Sentry y testing.
- Abrir `./upstream/nodejs-backend-patterns/` para el implementation playbook específico de Node.js.

### Si el problema es datos

- Elegir `@database-design` si aún no hay modelo o engine decidido.
- Elegir `@sql-pro` para queries y planes de ejecución.
- Elegir `@postgres-best-practices` para Postgres/Supabase, pooling, RLS e índices.
- Abrir `./resources/database-postgres-playbook.md` para el flujo completo.
- Abrir `./upstream/database-design/` para selección de motor, ORM, schema, índices, optimización y migrations.
- Abrir `./upstream/postgres-best-practices/` para reglas detalladas de Postgres y Supabase.
- Abrir `./upstream/sql-pro/` y `./upstream/sql-optimization-patterns/` cuando el problema sea de query tuning o EXPLAIN.

### Si el problema es backend Python

- Elegir `@python-pro` para baseline de tooling.
- Elegir `@fastapi-pro` para APIs async y contratos tipados.
- Elegir `@django-pro` para dominio amplio, admin y stack full-featured.
- Abrir `./resources/python-frameworks-playbook.md` para estructura y quality gates.
- Abrir `./upstream/python-pro/` para la doctrina Python completa.
- Abrir `./upstream/python-fastapi-development/` cuando FastAPI sea el marco elegido y haga falta la guía upstream completa.
- Abrir `./upstream/django-pro/` cuando Django sea el marco elegido y haga falta la guía upstream completa.

### Si el problema es billing

- Elegir `@stripe-integration`.
- Abrir `./resources/stripe-billing-playbook.md` para webhooks, estados y testing.
- Abrir `./upstream/stripe-integration/` para el contenido upstream íntegro del flujo Stripe.

## Checklists rápidos

### Contrato API

- Consumidores identificados
- Auth definida
- Errores y códigos programáticos definidos
- Paginación, filtros y versionado definidos
- Ejemplo request y response listos

### Schema y DB

- Entidades y relaciones explícitas
- Índices por query real
- Constraints y tipos bien elegidos
- Estrategia de migration definida
- Riesgo de N+1 o locking revisado

### Implementación backend

- Validación de input y output
- Tests para path crítico
- Logging y observabilidad mínima
- Config sin secrets hardcodeados
- Documentación técnica actualizada

### Billing con Stripe

- Flujo correcto elegido
- Webhooks con firma verificada
- Idempotencia aplicada
- Estados de pago mapeados a DB
- Escenarios de fallo y reintento definidos