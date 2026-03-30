# @test-fixing

## OBJETIVO

Recuperar suites rotas agrupando fallos por causa compartida y corrigiendo en orden de impacto, no de ruido.

## USAR CUANDO

Los tests fallan tras un refactor, cambio de API, migración, renombre o modificación de infraestructura.

## NO USAR CUANDO

El fallo pertenece a un bug aislado ya diagnosticado. En ese caso conviene usar TDD o debugging puntual, no una campaña de reparación masiva.

## INSTRUCCIONES

1. Ejecutar primero la suite o el subconjunto afectado para capturar el mapa real de fallos: cantidad, tipos de error, módulos implicados y primeras pistas de causa compartida.
2. Agrupar por root cause, no por archivo suelto, y priorizar infraestructura, cambios de contrato y luego aserciones o edge cases específicos.
3. Corregir un grupo a la vez, reejecutando el subconjunto relevante después de cada intervención para evitar mezclar señales.
4. Cerrar con la suite completa en verde o con un reporte explícito de lo que sigue roto, por qué y qué bloquea su reparación.

## FORMATO DE SALIDA

- Panorama inicial de fallos
- Grupos por causa raíz
- Orden de corrección
- Verificación parcial y final
- Riesgos o bloqueos restantes

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para el flujo de debugging y verificación.
- Ver `./_templates.md` para el bug report o plan de pruebas.
- Ver `./upstream/test-fixing/SKILL.md` para la guía upstream completa.

## ANTI-PATRON

Corregir al azar, mezclar grupos de fallos, no rerun parcial, hacer skips como parche o omitir la suite completa final.
