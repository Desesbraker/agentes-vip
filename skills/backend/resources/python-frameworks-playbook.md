# Python, FastAPI y Django Playbook

## Cuándo abrir este recurso

- Fijar estándares Python 3.12+
- Decidir entre FastAPI y Django
- Bajar a tierra estructura, testing, concurrencia y deploy
- Recuperar workflows de implementación del upstream

## Python base

### Baseline obligatorio

- `pyproject.toml` claro
- Lockfile o estrategia reproducible de dependencias
- Lint, format y typing definidos
- Tests desde el inicio

### Concurrencia

| Contexto | Modelo sugerido |
|---|---|
| I/O intensivo y APIs modernas | async |
| Scripts simples y jobs cortos | sync |
| CPU-bound | workers o multiprocessing |

## Cuándo elegir FastAPI

- APIs tipadas y async
- OpenAPI útil
- Microservicios o servicios con foco fuerte en contratos
- Menor necesidad de admin y batteries included

### Estructura sugerida FastAPI

| Capa | Responsabilidad |
|---|---|
| Routers | HTTP |
| Dependencies | Auth, validación, sesión |
| Services | Lógica de negocio |
| Models | Entidades |
| Schemas | Request/response |

### Flujo FastAPI

1. Diseñar contratos y schemas Pydantic.
2. Diseñar modelo de datos y session management.
3. Configurar SQLAlchemy async y Alembic.
4. Resolver auth y dependencias.
5. Añadir testing async y OpenAPI útil.

### Checklist FastAPI

- [ ] Async real en path crítico
- [ ] Pydantic usado en fronteras
- [ ] Alembic configurado
- [ ] OpenAPI útil
- [ ] Tests async escritos
- [ ] Riesgos de concurrencia documentados

## Cuándo elegir Django

- Producto con dominio amplio
- Admin y auth robustos
- DRF y APIs con ecosistema maduro
- Muchas necesidades estándar de negocio

### Flujo Django

1. Definir apps y límites del dominio.
2. Resolver modelo de usuario temprano.
3. Diseñar modelos y migrations.
4. Exponer APIs con DRF cuando aplique.
5. Revisar N+1 con `select_related` y `prefetch_related`.
6. Resolver permisos y seguridad por entorno.

### Checklist Django

- [ ] Apps claras
- [ ] User model decidido temprano
- [ ] Migrations revisadas
- [ ] N+1 auditado
- [ ] Permisos y auth definidos
- [ ] Tests de modelo, API y permisos escritos

## Setup base útil

### FastAPI

1. Crear entorno virtual
2. Instalar `fastapi`, `uvicorn`, `sqlalchemy`, `alembic`, `pydantic`
3. Crear `.env`
4. Aplicar migrations
5. Arrancar servidor local

### Django

1. Crear entorno virtual
2. Instalar `django`, `djangorestframework`, herramientas de calidad y test
3. Crear proyecto y apps base
4. Configurar settings por entorno
5. Ejecutar migrations y tests iniciales

## Entrega esperada

- Framework elegido y motivo
- Estructura base del proyecto
- Modelo de concurrencia
- Auth y configuración
- Estrategia de tests
- Riesgos de rendimiento o permisos