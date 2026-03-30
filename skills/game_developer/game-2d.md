# @game-2d

## OBJETIVO

Diseñar e implementar la base tecnica de un juego 2D con control legible, colisiones manejables y pipeline de assets sostenible. La prioridad es una experiencia jugable estable antes de escalar contenido.

## USAR CUANDO

- El proyecto usa sprites, tilemaps o fisica 2D.
- Hace falta definir resolucion, camara, atlas y flujo de escena 2D.
- Se quiere validar el feel de gameplay 2D antes de crecer el juego.

## NO USAR CUANDO

- El proyecto es principalmente 3D; usar game-3d.
- El problema central es optimizacion o profiling avanzado; usar game-optimization.
- No esta definida la plataforma o resolucion destino.

## INSTRUCCIONES

1. Fijar resolucion objetivo, camara, densidad visual, input y convencion de sprites o atlas.
2. Implementar movimiento, colisiones e hitboxes acordes al genero priorizando respuesta y lectura.
3. Organizar tilemaps, layers, sorting, animaciones y audio basico para produccion ordenada.
4. Validar build real con pruebas de jugabilidad, jitter, cargas y consistencia visual antes de sumar contenido.

## FORMATO DE SALIDA

- Base tecnica 2D definida.
- Sistemas jugables implementados o pendientes.
- Riesgos de camara, colisiones o assets.
- Checklist de validacion del build.
- Siguiente iteracion recomendada.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./game-design.md

## ANTI-PATRON

- Mantener sprites sueltos sin atlas.
- Usar colisiones complejas para todo.
- Romper control o fisica persiguiendo pixel perfect sin plan.
