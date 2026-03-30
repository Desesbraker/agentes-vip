# @asset-organization

## OBJETIVO

Mantener una libreria de personajes y assets 3D ordenada, reusable y trazable para arte, desarrollo y QA. La skill reduce confusion entre fuentes maestras, exports y variantes aprobadas.

## USAR CUANDO

- Se estan organizando personajes, variantes o librerias de assets 3D.
- Hace falta definir naming, versionado y metadatos minimos.
- El equipo necesita saber que asset esta realmente aprobado para produccion.

## NO USAR CUANDO

- El trabajo es crear el personaje desde cero; usar character-concept o 3d-modeling-pipeline.
- Solo se necesita resolver un bug puntual de importacion o rig.
- No existe una minima estructura de carpetas o ownership del asset.

## INSTRUCCIONES

1. Separar assets por estado y proposito: concept, source, export, textures, renders, variantes y documentacion.
2. Aplicar naming consistente para personaje, pieza, variante, LOD, material y engine.
3. Registrar metadatos minimos: version, polycount, texturas, skeleton, formato y limitaciones.
4. Marcar como reusable solo assets probados en engine o revisados con criterio tecnico equivalente.

## FORMATO DE SALIDA

- Estructura de libreria propuesta o revisada.
- Convencion de naming.
- Metadatos obligatorios por asset.
- Riesgos de duplicidad o confusion.
- Estado de aprobacion por asset o variante.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./rigging-export.md

## ANTI-PATRON

- Mezclar carpetas y estados del pipeline.
- Usar nombres ambiguos o improvisados.
- Aprobar exports sin registrar version, engine y limitaciones.
