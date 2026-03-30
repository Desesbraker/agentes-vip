# @texturing

## OBJETIVO

Texturizar personajes 3D con consistencia visual y tecnica segun el style guide y el engine destino. La skill asegura que materiales, memoria y legibilidad se mantengan bajo control.

## USAR CUANDO

- El modelo y los bakes ya estan listos para materiales.
- Hay que elegir entre pipeline PBR, stylized o hand-painted.
- Se necesita validar materiales en condiciones similares al engine.

## NO USAR CUANDO

- Aun faltan UVs o bakes correctos; volver a 3d-modeling-pipeline.
- El trabajo es rigging o export.
- No existe budget de memoria o guia visual aprobada.

## INSTRUCCIONES

1. Elegir pipeline de materiales, mapas necesarios, resolucion y limite de memoria antes de pintar.
2. Pintar materiales manteniendo consistencia entre mapas y jerarquia visual del estilo.
3. Validar texturas con shader similar al del engine y revisar seams, compresion y lectura a distancia.
4. Exportar set final con naming claro y ajustar si el personaje pierde identidad o legibilidad en engine.

## FORMATO DE SALIDA

- Pipeline de materiales elegido.
- Estado del set de texturas.
- Riesgos de memoria, seams o compresion.
- Validacion en shader o engine.
- Criterio de aprobacion final.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./rigging-export.md

## ANTI-PATRON

- Pintar sin budget de memoria.
- Depender de iluminacion baked para que el material funcione.
- Mezclar estilos sin control.
- Aprobar texturas sin probar compresion y distancia.
