# @systematic-debugging

## OBJETIVO

Resolver bugs y fallos de tests identificando causa raíz antes de aplicar cambios, para evitar fixes cosméticos o regresiones.

## USAR CUANDO

Aparece un bug, un test falla o el sistema se comporta de forma inesperada y hace falta investigar antes de tocar código.

## NO USAR CUANDO

Ya existe evidencia concluyente y solo queda ejecutar una corrección validada. Esta skill es para investigar, no para improvisar.

## INSTRUCCIONES

1. Prohibir el quick fix inicial: leer errores completos, reproducir el problema de forma consistente y delimitar qué cambió antes de asumir nada.
2. Trazar el flujo entre capas, comparar con casos sanos y reunir evidencia suficiente para formular una hipótesis específica sobre la causa raíz.
3. Probar una hipótesis a la vez con cambio mínimo o instrumentación puntual; si el problema resiste varias correcciones superficiales, cuestionar la arquitectura o los supuestos base.
4. Convertir la reproducción en test o evidencia automatizable, aplicar la corrección única y cerrar con verificación fresca.

## FORMATO DE SALIDA

- Síntoma observado
- Evidencia reunida
- Causa raíz
- Cambio aplicado o propuesto
- Verificación fresca

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de debugging.
- Ver `./_templates.md` para el template de bug report.
- Ver `./upstream/systematic-debugging/SKILL.md` para la guía upstream principal.
- Ver `./upstream/debugging-strategies/SKILL.md` y `./upstream/debugging-strategies/resources/` para estrategias complementarias y recursos adicionales.

## ANTI-PATRON

Quick fixes, múltiples cambios simultáneos, adivinar sin evidencia, saltar la reproducción o cerrar el bug sin test o verificación fresca.
