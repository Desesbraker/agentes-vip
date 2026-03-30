# @claude-d3js-skill

## OBJETIVO

Diseñar visualizaciones D3.js personalizadas que expliquen datos con claridad, interacción útil y una estructura técnica mantenible.

## USAR CUANDO

Hay que construir gráficos interactivos o no estándar donde una librería de charting tradicional no alcanza.

## NO USAR CUANDO

El gráfico puede resolverse con una herramienta estándar sin sacrificar claridad. No introducir D3 por prestigio técnico.

## INSTRUCCIONES

1. Definir la pregunta analítica, el tipo de gráfico y el patrón de integración antes de tocar el DOM, dejando claro si el render será directo o coordinado con un framework.
2. Estructurar el gráfico en capas: dimensiones, escalas, ejes, marks y validación de datos, incluyendo responsive real y limpieza del render previo.
3. Añadir interacción solo cuando ayude a explorar o explicar: tooltips, zoom, filtros o selección, siempre con estados claros y accesibilidad mínima.
4. Elegir SVG o canvas según volumen y complejidad, documentando límites de rendimiento y mantenimiento.

## FORMATO DE SALIDA

- Pregunta o insight a visualizar
- Tipo de gráfico elegido
- Estructura técnica del render
- Interacciones o accesibilidad
- Riesgo de performance o mantenimiento

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para criterios de claridad analítica.
- Ver `./_templates.md` para el template de dashboard o análisis SQL.

## ANTI-PATRON

No limpiar renders previos, hardcodear dimensiones, interacciones decorativas, ausencia de accesibilidad o usar SVG para volúmenes que piden canvas.
