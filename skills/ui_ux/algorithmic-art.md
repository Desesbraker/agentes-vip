# @algorithmic-art

## OBJETIVO

Crear arte generativo interactivo con una lógica visual reproducible, controlable y coherente con una intención conceptual clara.

## USAR CUANDO

Hay que producir una pieza p5.js o similar donde el sistema generativo sea parte del valor artístico y no un efecto aleatorio sin dirección.

## NO USAR CUANDO

La pieza puede resolverse mejor con diseño estático o cuando no existe una intención conceptual capaz de sostener el sistema generativo.

## INSTRUCCIONES

1. Definir primero la filosofía visual y el seed conceptual que gobernará la pieza, antes de tocar parámetros o ruido aleatorio.
2. Traducir esa intención a reglas algorítmicas reproducibles: seed fija, variaciones paramétricas y límites claros para que la pieza tenga identidad.
3. Implementar la obra con controles mínimos de exploración, regeneración y export, cuidando que la interfaz no eclipse el resultado visual.
4. Cerrar con validación estética y técnica: reproducibilidad, legibilidad del sistema y calidad del output generado.

## FORMATO DE SALIDA

- Concepto y filosofía
- Sistema generativo elegido
- Controles o parámetros
- Entregables previstos
- Riesgo de pérdida de identidad

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas duras de dirección visual.
- Ver `./_templates.md` para el template de pieza artística.
- Ver `./resources/generative-visual-playbook.md` para decidir entre sistema generativo y canvas, definir seed y validar reproducibilidad.

## ANTI-PATRON

Ruido aleatorio sin control, parámetros sin interfaz, ausencia de seed reproducible o piezas que dependen del azar más que de una dirección artística.
