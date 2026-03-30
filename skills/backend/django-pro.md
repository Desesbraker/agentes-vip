# @django-pro

OBJETIVO: Construir aplicaciones y APIs con Django de forma segura, mantenible y preparada para crecimiento de producto.

USAR CUANDO: Hay que implementar backend full-featured con Django, DRF, admin, auth, background jobs o un stack Python con mucho dominio de negocio.

NO USAR CUANDO: La prioridad es una API async liviana y de alto rendimiento con mínima capa de framework. En ese caso usar @fastapi-pro.

INSTRUCCIONES:

1. Estructurar el proyecto con apps claras, modelos bien definidos y una estrategia consciente para ORM, admin, APIs y background tasks.
2. Usar DRF para APIs, optimizar ORM con select_related y prefetch_related, y dejar migrations y modelo de usuario resueltos desde temprano.
3. Resolver seguridad y permisos como parte del diseño: auth, CSRF o JWT, permisos por objeto cuando aplique y configuración segura por entorno.
4. Entregar con tests, profiling básico y salida clara sobre modelos, endpoints, tareas asíncronas y riesgos de N+1 o permisos.

FORMATO DE SALIDA:

- Objetivo de la aplicación o módulo
- Apps, modelos y endpoints implicados
- Auth, permisos y tareas async
- Tests y profiling mínimos
- Riesgos técnicos

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de implementación backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/python-frameworks-playbook.md` para estructura Django, DRF, modelo de usuario, permisos y N+1.
- Ver `./upstream/django-pro/SKILL.md` para la guía upstream completa de Django.

ANTI-PATRÓN: Dejar N+1 sin revisar, poner lógica de negocio en views, postergar migrations críticas o usar SQL raw sin parametrización ni razón fuerte.
