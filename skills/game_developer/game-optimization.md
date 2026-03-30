# @game-optimization

## OBJETIVO

Identificar y corregir cuellos de botella de rendimiento en juegos sin degradar innecesariamente la mantenibilidad o la experiencia. La skill trabaja sobre mediciones y presupuestos por plataforma.

## USAR CUANDO

- El juego presenta problemas de FPS, memoria, cargas o estabilidad de frame.
- Hace falta decidir entre batching, pooling, LODs o simplificacion de fisicas o shaders.
- Se necesita una estrategia de profiling por plataforma.

## NO USAR CUANDO

- Todavia no existe build o baseline medible.
- El trabajo principal es diseno de gameplay o arquitectura base del juego.
- El problema es un bug funcional aislado, no rendimiento sistemico.

## INSTRUCCIONES

1. Perfilar en hardware y build relevantes para localizar si el cuello esta en CPU, GPU, memoria, assets, fisica o scripting.
2. Aplicar el cambio que ataca ese cuello concreto y documentar por que se eligio.
3. Revisar impacto conjunto de codigo, escenas, audio, texturas, animaciones y shaders.
4. Repetir profiling y fijar presupuesto de FPS, carga y memoria por plataforma antes de seguir optimizando.

## FORMATO DE SALIDA

- Bottleneck principal y evidencia.
- Cambio recomendado o aplicado.
- Medicion before and after.
- Riesgos de mantenimiento o calidad visual.
- Proximo paso de profiling.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./game-3d.md

## ANTI-PATRON

- Optimizar antes de medir.
- Aplicar pooling a todo por defecto.
- Bajar calidad visual sin localizar el cuello real.
- Suponer que editor y build rinden igual.
