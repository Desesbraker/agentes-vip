# @test-driven-development

## OBJETIVO

Guiar desarrollo y fixes desde tests que fallen primero, para construir comportamiento observable con menos regresiones.

## USAR CUANDO

Hay que implementar una feature nueva, un bug fix o una regla de negocio que pueda expresarse como comportamiento verificable.

## NO USAR CUANDO

El problema todavía no se entiende o no puede reproducirse. Primero se investiga con systematic-debugging y luego se vuelve a TDD.

## INSTRUCCIONES

1. Empezar siempre por un test que falle y describa un comportamiento único; si el test pasa desde el inicio, todavía no está capturando el problema.
2. Seguir el ciclo Red, Green y Refactor con cambios mínimos, verificando cada transición antes de avanzar a la siguiente.
3. Mantener los tests cercanos al comportamiento real, usando mocks solo cuando la dependencia externa lo vuelva inevitable o rompa determinismo.
4. Cerrar con la suite relevante en verde, edge cases razonables cubiertos y una evidencia clara de que el test nuevo falló antes del fix.

## FORMATO DE SALIDA

- Comportamiento objetivo
- Test que falla primero
- Cambio mínimo para pasar
- Refactor aplicado
- Verificación final

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist TDD.
- Ver `./_templates.md` para el template de verificación.
- Ver `./upstream/test-driven-development/SKILL.md` para la guía upstream completa.

## ANTI-PATRON

Code-first, tests después, mocks excesivos, saltarse el paso rojo o declarar TDD cuando nunca se vio fallar el test nuevo.
