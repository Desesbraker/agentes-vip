# @e2e-testing-patterns

## OBJETIVO

Diseñar suites E2E que cubran recorridos críticos de negocio con estabilidad, trazabilidad y costo operativo razonable.

## USAR CUANDO

Hay que validar journeys completos, regresiones cross-browser o integraciones donde unit e integration tests no alcanzan.

## NO USAR CUANDO

El comportamiento puede capturarse con una prueba más barata y determinista en una capa inferior. E2E no reemplaza el resto de la pirámide.

## INSTRUCCIONES

1. Priorizar journeys por impacto de negocio y riesgo, definiendo criterio de éxito observable para cada flujo antes de automatizarlo.
2. Diseñar selectores estables, datos de test dedicados e isolation entre casos para evitar suites lentas o acopladas al estado global.
3. Integrar la suite en CI con artifacts útiles, retries razonados, paralelización y matrices de navegadores solo cuando el producto realmente lo requiera.
4. Ejecutar siempre fuera de producción, con scrubbing de datos sensibles y una estrategia explícita para debugging cuando aparezca flakiness.

## FORMATO DE SALIDA

- Journeys cubiertos
- Entorno y data de test
- Estrategia de selectores y aislamiento
- Evidencia en CI
- Riesgo de flakiness o cobertura faltante

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist E2E y reglas de cierre.
- Ver `./_templates.md` para el template de plan de pruebas.
- Ver `./upstream/e2e-testing-patterns/SKILL.md` y `./upstream/e2e-testing-patterns/resources/` para la guía upstream principal.
- Ver `./upstream/e2e-testing/SKILL.md` para el workflow complementario.
- Ver `./upstream/browser-automation/SKILL.md`, `./upstream/javascript-testing-patterns/SKILL.md` y `./upstream/awt-e2e-testing/SKILL.md` para variantes por herramienta y contexto.

## ANTI-PATRON

Tests contra producción, data compartida, ausencia de artifacts, retries como parche permanente o automatizar journeys irrelevantes por volumen y no por riesgo.
