# @python-pro

OBJETIVO: Desarrollar servicios y scripts Python modernos con tooling consistente, tipado y criterios claros de calidad.

USAR CUANDO: Hay que implementar backend, jobs o utilidades en Python 3.12+ y se necesita fijar estándares del stack.

NO USAR CUANDO: La tarea requiere decisiones específicas de FastAPI o Django ya definidas. En ese caso usar la skill del framework.

INSTRUCCIONES:

1. Establecer desde el inicio tooling, lockfile, lint, format, tipado y tests como parte del proyecto, no como etapa posterior.
2. Elegir sync, async, multiprocessing o generators según el tipo de carga y no por preferencia estilística.
3. Usar validación y type hints en fronteras críticas para que inputs, outputs y DTOs no dependan de convenciones tácitas.
4. Entregar con pyproject claro, estrategia de calidad y riesgos documentados sobre rendimiento, tipado o integraciones externas.

FORMATO DE SALIDA:

- Objetivo del servicio o script
- Tooling y estructura base
- Modelo de concurrencia
- Validación y tipado
- Tests y riesgos

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de implementación backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/python-frameworks-playbook.md` para baseline Python, concurrencia y criterios de elección de framework.
- Ver `./upstream/python-pro/SKILL.md` para el skill upstream completo con tooling moderno, tipado y rendimiento.

ANTI-PATRÓN: Instalar dependencias sin lockfile, omitir type hints, confiar en debugging con prints o entregar código Python sin tests ni pyproject ordenado.
