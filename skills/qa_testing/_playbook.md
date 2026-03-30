# Playbook de QA & Testing

## Flujo operativo

1. Confirmar objetivo de validación, riesgo, entorno y comando de verificación antes de tocar tests o fixes.
2. Elegir la capa correcta: unit, integration, E2E, review o experimento. No subir de complejidad sin motivo.
3. Ejecutar el ciclo correspondiente con evidencia fresca: reproducir, aislar, corregir o diseñar el test, y volver a correr.
4. Cerrar solo con resultado verificable, riesgos remanentes y siguiente paso recomendado.

## Mapa de upstream importado

- `./upstream/test-driven-development/`
- `./upstream/systematic-debugging/`
- `./upstream/debugging-strategies/`
- `./upstream/browser-automation/`
- `./upstream/e2e-testing-patterns/`
- `./upstream/e2e-testing/`
- `./upstream/awt-e2e-testing/`
- `./upstream/python-testing-patterns/`
- `./upstream/javascript-testing-patterns/`
- `./upstream/code-review-checklist/`
- `./upstream/code-review-excellence/`
- `./upstream/test-fixing/`
- `./upstream/ab-test-setup/`
- `./upstream/testing-qa/`
- `./upstream/verification-before-completion/`

## Reglas duras

- Nunca declarar completitud sin ejecutar el comando que respalda el claim en ese momento.
- Nunca corregir un bug sin hipótesis y evidencia de causa raíz.
- Nunca silenciar flaky tests con skip permanente; primero aislar y clasificar la causa.
- Nunca aprobar código con feedback vago, sin revisar riesgo funcional, seguridad y cobertura.

## Cuándo abrir upstream

- Abrir `./upstream/test-driven-development/` cuando el caso requiera doctrina completa de Red-Green-Refactor.
- Abrir `./upstream/systematic-debugging/` y `./upstream/debugging-strategies/` cuando la investigación necesite métodos más detallados o recursos de apoyo.
- Abrir `./upstream/browser-automation/`, `./upstream/e2e-testing-patterns/`, `./upstream/e2e-testing/` o `./upstream/awt-e2e-testing/` para diseño E2E, aislamiento, automatización y variantes modernas del workflow.
- Abrir `./upstream/python-testing-patterns/` o `./upstream/javascript-testing-patterns/` cuando la estrategia dependa del stack de pruebas.
- Abrir `./upstream/code-review-checklist/` o `./upstream/code-review-excellence/` para revisiones con mayor profundidad.
- Abrir `./upstream/test-fixing/`, `./upstream/ab-test-setup/` y `./upstream/verification-before-completion/` para reparación masiva, experimentación y gate final de evidencia.

## Checklists rápidos

### TDD

- Test falló antes del cambio
- Cambio mínimo para pasar
- Refactor con suite en verde
- Edge cases relevantes cubiertos

### Debugging

- Reproducción consistente
- Causa raíz identificada
- Cambio único probado
- Validación fresca ejecutada

### Review

- Problema entendido
- Riesgos funcionales revisados
- Seguridad y performance revisadas
- Tests y docs evaluados
