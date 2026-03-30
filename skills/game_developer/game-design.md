# @game-design

## OBJETIVO

Definir el core loop, las mecanicas principales y el vertical slice de un juego con suficiente claridad para prototipar sin deriva de alcance. La skill aterriza el diseno en sistemas testeables y riesgos visibles.

## USAR CUANDO

- Se esta definiendo un juego nuevo o una iteracion importante de su loop.
- Hace falta bajar una idea a GDD tecnico minimo y vertical slice.
- Hay que decidir que sistemas entran primero y cuales quedan fuera.

## NO USAR CUANDO

- El trabajo principal es implementar en un engine concreto; usar unity-developer o godot-developer.
- El foco es optimizacion de rendimiento; usar game-optimization.
- No existe pitch, target o plataforma minima definida.

## INSTRUCCIONES

1. Bloquear pitch, plataforma, jugador objetivo, condiciones de victoria o fracaso y loop de 30 segundos.
2. Traducir el diseno a sistemas concretos: input, camara, movimiento, combate, puzzle, economia, guardado y feedback segun el genero.
3. Definir un vertical slice con una escena, una meta clara y criterios medibles de validacion.
4. Documentar riesgos, trade-offs y supuestos para iterar con playtesting sin inflar alcance.

## FORMATO DE SALIDA

- Resumen del concepto y core loop.
- Sistemas incluidos en la primera iteracion.
- Definicion del vertical slice.
- Riesgos y trade-offs de diseno.
- Criterio de validacion o descarte.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./game-2d.md

## ANTI-PATRON

- Diseñar demasiadas features antes de validar el loop.
- Confundir idea de juego con una lista suelta de mecanicas.
- Prototipar sin GDD minimo ni criterio de descarte.
