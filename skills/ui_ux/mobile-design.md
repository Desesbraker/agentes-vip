# @mobile-design

## OBJETIVO

Diseñar interfaces móviles que respeten contexto de uso, plataforma y restricciones táctiles antes de perseguir complejidad visual.

## USAR CUANDO

Hay que definir UX o UI para apps iOS, Android o experiencias cross-platform.

## NO USAR CUANDO

El problema es puramente web desktop o todavía no se conoce la plataforma, navegación o contexto de uso. Eso debe bloquearse primero.

## INSTRUCCIONES

1. Confirmar plataforma, navegación, offline, audiencia y dispositivos objetivo antes de dibujar pantallas o patrones de interacción.
2. Evaluar factibilidad con un marco como MFRI y simplificar interacciones si accesibilidad, performance u offline quedan comprometidos.
3. Diseñar con touch-first: zonas de pulgar, targets mínimos, feedback claro y acciones críticas visibles sin depender solo de gestos ocultos.
4. Alinear la propuesta con normas de iOS o Android, documentando diferencias cuando el diseño sea cross-platform.

## FORMATO DE SALIDA

- Plataforma y contexto de uso
- Navegación y flujos críticos
- Reglas touch y accesibilidad
- Restricciones técnicas u offline
- Riesgo de fricción móvil

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de UX móvil.
- Ver `./_templates.md` para el template de mobile UX.
- Ver `./resources/mobile-ux-playbook.md` para matrices unificar/divergir, defaults iOS/Android y checklist touch-first.

## ANTI-PATRON

Desktop reducido a mobile, sin manejo offline, hover como dependencia o ignorar normas base de la plataforma.
