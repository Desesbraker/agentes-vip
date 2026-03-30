# Motion, Scroll and 3D Playbook

## Cuándo abrir este recurso

- Storytelling por scroll
- Motion significativa
- 3D web con narrativa o producto
- Necesidad de fallback y degradación segura

## Flujo operativo

1. Definir objetivo narrativo o funcional.
2. Elegir stack según complejidad.
3. Diseñar fallback desktop/mobile.
4. Validar performance y accesibilidad.

## Stack guide

| Caso | Stack |
|---|---|
| Motion simple | CSS nativo |
| Motion en React | Framer Motion |
| Coreografía compleja con scroll | GSAP ScrollTrigger |
| 3D rápido o prototipo | Spline |
| 3D profundo en React | React Three Fiber |
| Control fino y custom | Three.js |

## Reglas duras

- No scroll hijacking.
- No ocultar contenido crítico detrás de animación frágil.
- No 3D sin loading state ni fallback.
- No experiencia inmersiva solo desktop.

## Checklist

- [ ] Objetivo narrativo claro
- [ ] Stack elegido con motivo
- [ ] Fallback móvil definido
- [ ] Riesgo de performance documentado
- [ ] Degradación aceptable validada

## Entrega esperada

- Objetivo narrativo
- Efectos o stack elegidos
- Estrategia desktop/mobile
- Fallback
- Riesgo de performance o accesibilidad