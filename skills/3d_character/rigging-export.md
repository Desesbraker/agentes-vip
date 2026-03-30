# @rigging-export

## OBJETIVO

Preparar un personaje 3D para deformacion y export game-ready con skeleton, skinning e importacion real validados. La skill evita entregar rigs teoricos que fallan al entrar al engine.

## USAR CUANDO

- El modelo ya esta listo para rigging.
- Hace falta definir skeleton, pesos y formato de export.
- Se debe probar la importacion real en Unity, Godot, Unreal u otro pipeline cerrado.

## NO USAR CUANDO

- La topologia aun no sirve para deformacion; volver a 3d-modeling-pipeline.
- Todavia falta texturing o style guide segun el caso.
- El engine destino sigue completamente indefinido.

## INSTRUCCIONES

1. Confirmar escala, naming, topologia, pivotes y engine destino antes de riggear.
2. Construir skeleton y bones extra solo donde aporten al personaje o al gameplay.
3. Resolver skinning y poses de prueba para hombros, codos, rodillas, pelvis, manos y cuello.
4. Exportar al formato compatible y validar import real, ejes, pose base, sockets, materiales y deformacion.

## FORMATO DE SALIDA

- Estado del rig y skeleton.
- Validacion de skinning y poses.
- Resultado de la importacion real en engine.
- Fallos detectados y su causa.
- Accion siguiente para cierre.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ../game_developer/game-3d.md

## ANTI-PATRON

- Riggear mallas sin retopologia apta.
- Dejar bones mal orientados o pesos sucios.
- Exportar sin probar importacion real.
