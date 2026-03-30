# @fastapi-pro

OBJETIVO: Construir APIs FastAPI rápidas, bien tipadas y listas para producción con foco en async, validación y documentación.

USAR CUANDO: Hay que levantar APIs Python de alto rendimiento, integraciones async o servicios con contratos claros y OpenAPI útil.

NO USAR CUANDO: El sistema necesita un framework full-featured con admin, ORM acoplado y mucha lógica de producto tradicional. En ese caso usar @django-pro.

INSTRUCCIONES:

1. Diseñar la API alrededor de schemas Pydantic, dependencias explícitas y rutas con contratos claros desde el inicio.
2. Mantener async real en todo el path crítico, evitando mezclar código bloqueante en endpoints declarados como async.
3. Resolver auth, config, acceso a datos y servicios externos con dependencias limpias y testing asíncrono desde el principio.
4. Entregar con OpenAPI útil, tests, strategy de deploy y riesgos documentados sobre concurrencia, validación y observabilidad.

FORMATO DE SALIDA:

- Objetivo del servicio
- Rutas y schemas clave
- Auth y dependencias
- Tests y deploy base
- Riesgo de concurrencia o I/O

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de implementación backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/python-frameworks-playbook.md` para estructura FastAPI, fases de implementación, Alembic y testing async.
- Ver `./upstream/python-fastapi-development/SKILL.md` para el skill upstream completo.

ANTI-PATRÓN: Mezclar código sync en endpoints async, saltarse validación Pydantic, exponer rutas sin OpenAPI útil o entregar un servicio sin tests async.
