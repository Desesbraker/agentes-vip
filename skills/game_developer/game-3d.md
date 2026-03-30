# @game-3d

## OBJETIVO

Construir la base de un juego 3D con decisiones coherentes de camara, escala, iluminacion, colisiones y presupuesto visual. La skill prioriza legibilidad espacial y rendimiento real por plataforma.

## USAR CUANDO

- El proyecto requiere escena, gameplay o assets 3D.
- Hay que fijar presupuesto visual y pipeline tecnico para mundo 3D.
- Se necesita validar una escena minima antes de escalar contenido.

## NO USAR CUANDO

- El proyecto es 2D; usar game-2d.
- Solo hace falta optimizacion de un build ya estable; usar game-optimization.
- No esta cerrada la plataforma o el engine objetivo.

## INSTRUCCIONES

1. Definir camara, escala, input, plataforma y limite de fidelidad visual realista para el target.
2. Implementar escena minima con navegacion clara, colisiones simples, iluminacion razonable y materiales consistentes.
3. Integrar assets, LODs, colliders y shaders con disciplina tecnica segun el budget.
4. Perfilar temprano en build o engine real y ajustar luces, materiales, fisica y distancia de camara segun bottleneck.

## FORMATO DE SALIDA

- Base tecnica 3D y supuestos de plataforma.
- Escena minima o slice definido.
- Riesgos de rendimiento o legibilidad.
- Pipeline recomendado para assets 3D.
- Siguiente validacion requerida.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ../3d_character/3d-modeling-pipeline.md

## ANTI-PATRON

- Usar mesh colliders para todo.
- Aprobar sombras o shaders caros sin budget.
- Reutilizar una sola malla para todas las distancias sin LOD.
