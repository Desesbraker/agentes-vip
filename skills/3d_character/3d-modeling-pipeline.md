# @3d-modeling-pipeline

## OBJETIVO

Llevar un personaje desde style guide aprobado hasta una malla game-ready con topologia, UVs y bakes aptos para texturizado y rig. La skill ordena el pipeline tecnico para evitar retrabajo costoso.

## USAR CUANDO

- El concept ya esta aprobado y hay que modelar para juego o avatar 3D.
- Hace falta fijar budget tecnico, retopologia, UVs y bake.
- Se necesita una validacion intermedia antes de texturing o rig.

## NO USAR CUANDO

- Todavia falta concept o style guide; usar character-concept.
- El trabajo es exclusivamente texturizado o rigging.
- No esta definido el engine o el uso del asset.

## INSTRUCCIONES

1. Fijar escala, polycount, resolucion de texturas, piezas separadas y requisitos del engine desde el style guide.
2. Construir base mesh y high-poly solo donde aporte al bake y a la lectura final.
3. Ejecutar retopologia game-ready con loops de deformacion y densidad coherente.
4. Cerrar UVs, naming y bake, luego validar export preliminar en engine antes de pasar a texturas o rig.

## FORMATO DE SALIDA

- Budget tecnico del asset.
- Estado del modelado y retopologia.
- Checklist de UVs y bake.
- Riesgos antes de texturing o rigging.
- Criterio de paso a la siguiente fase.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./texturing.md

## ANTI-PATRON

- Llevar high-poly directo al engine.
- Hacer retopologia sin loops de deformacion.
- Aprobar UVs o bakes con artefactos no revisados.
