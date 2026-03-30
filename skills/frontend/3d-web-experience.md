# @3d-web-experience

## OBJETIVO

Integrar 3D en experiencias web con valor real para narrativa, producto o branding, sin comprometer carga, usabilidad ni compatibilidad.

## USAR CUANDO

Hay que incorporar escenas 3D, viewers, hero interactivo, storytelling inmersivo o elementos tridimensionales que mejoren comprensión o impacto visual.

## NO USAR CUANDO

El 3D solo agrega peso visual, no aporta al objetivo del producto o el contexto exige máxima ligereza en dispositivos modestos.

## INSTRUCCIONES

1. Elegir stack por velocidad y control: Spline para prototipos rápidos, React Three Fiber para apps React y Three.js directo cuando se necesite control fino.
2. Optimizar el asset antes de integrarlo: bajar polígonos, bakear texturas, exportar GLB y comprimir para mantener tiempos de carga razonables.
3. Integrar con loading state, fallback y controles solo si aportan a la experiencia; la escena no debe bloquear el resto de la página.
4. Ajustar calidad por dispositivo y contemplar versión reducida o estática para mobile y equipos low-end.

## FORMATO DE SALIDA

- Objetivo del 3D
- Stack elegido
- Pipeline u optimización del asset
- Estrategia de fallback
- Riesgo de performance o compatibilidad

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para criterios de performance, fallback y QA visual.
- Ver `./_templates.md` para el template de vista o dirección visual.
- Ver `./resources/motion-immersive-playbook.md` para selección Spline/R3F/Three.js, asset pipeline y fallback por dispositivo.

## ANTI-PATRON

Meter 3D por decoración, entregar solo para desktop, omitir estados de carga o montar modelos sin optimización previa.
