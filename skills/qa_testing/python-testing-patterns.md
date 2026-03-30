# @python-testing-patterns

## OBJETIVO

Construir suites de testing Python legibles, mantenibles y preparadas para cubrir sync, async, datos y edge cases reales.

## USAR CUANDO

Hay que escribir o reorganizar tests Python, preparar fixtures, mejorar cobertura o endurecer la infraestructura de testing del proyecto.

## NO USAR CUANDO

El problema principal es arquitectura del sistema o un bug sin reproducir. Primero hay que entender el problema y luego elegir la estrategia de test.

## INSTRUCCIONES

1. Tomar `pytest` como base, estructurar fixtures reutilizables y usar parametrización cuando el comportamiento deba validarse sobre múltiples entradas significativas.
2. Aislar dependencias externas con mocks o doubles solo cuando haga falta, usar `pytest-asyncio` para async y mantener fixtures transaccionales o efímeras para base de datos.
3. Añadir property-based testing con Hypothesis cuando los edge cases sean amplios o poco intuitivos, especialmente en parsing, validación o transformaciones.
4. Integrar la suite en CI con markers, coverage y ejecución paralela cuando aporte velocidad sin ocultar dependencias frágiles.

## FORMATO DE SALIDA

- Tipo de suite o módulo
- Fixtures y datos de prueba
- Estrategia de mocks o async
- Edge cases cubiertos
- Integración en CI

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas duras de QA y debugging.
- Ver `./_templates.md` para el template de plan de pruebas.
- Ver `./upstream/python-testing-patterns/SKILL.md` y `./upstream/python-testing-patterns/resources/` para la guía upstream principal.

## ANTI-PATRON

Fixtures globales opacas, mocks sin entender la dependencia, tests sin markers ni criterio de aislamiento o usar la suite para esconder diseño defectuoso.
