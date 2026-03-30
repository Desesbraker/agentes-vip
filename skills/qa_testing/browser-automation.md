# @browser-automation

## OBJETIVO

Automatizar flujos de navegador con aislamiento, selectores estables y evidencia útil para depurar fallos.

## USAR CUANDO

Hay que implementar browser tests, reproducir errores UI o automatizar navegación autorizada para extracción o verificación.

## NO USAR CUANDO

El problema se resuelve mejor con tests unitarios o de integración sin navegador real. No subir a browser automation por reflejo.

## INSTRUCCIONES

1. Preferir Playwright y aislar cada caso con estado fresco por test, BrowserContext propio y datos preparados para evitar contaminación entre ejecuciones.
2. Usar locators orientados al usuario, como `getByRole`, `getByLabel` o `getByText`, y dejar CSS o XPath solo como último recurso justificado.
3. Aprovechar el auto-wait del framework, activar traces o screenshots en fallos y prohibir timeouts arbitrarios que escondan problemas reales de sincronización.
4. Si la automatización no es testing sino navegación autorizada, respetar rate limits, viewport consistente, límites legales y una estrategia explícita para errores o bloqueos.

## FORMATO DE SALIDA

- Objetivo del flujo automatizado
- Herramienta y estrategia de aislamiento
- Selectores clave
- Evidencia de debugging habilitada
- Riesgo de flakiness o bloqueo

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de debugging y aislamiento.
- Ver `./_templates.md` para el plan de pruebas o bug report.
- Ver `./upstream/browser-automation/SKILL.md` para la guía upstream base.
- Ver `./upstream/e2e-testing-patterns/SKILL.md` para patrones complementarios de diseño E2E.

## ANTI-PATRON

`waitForTimeout`, selectores frágiles, contexto compartido entre tests, ausencia de traces o automatización sin respetar límites del entorno objetivo.
