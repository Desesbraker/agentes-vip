# @scroll-experience

## OBJETIVO

Diseñar experiencias guiadas por scroll que aporten narrativa y percepción de calidad sin sacrificar claridad, accesibilidad ni rendimiento.

## USAR CUANDO

Hay que construir storytelling visual, parallax, secciones sticky, secuencias de reveal o interacción ligada al desplazamiento.

## NO USAR CUANDO

El contenido principal depende de animaciones complejas para entenderse o el proyecto necesita máxima simplicidad y velocidad sin valor narrativo extra.

## INSTRUCCIONES

1. Elegir stack según complejidad: CSS nativo para casos simples, Framer Motion para React y GSAP ScrollTrigger cuando la coreografía exija control fino.
2. Diseñar la secuencia como narrativa con beats claros y jerarquía visual, no como una colección de efectos desconectados.
3. Usar sticky, parallax u horizontales solo cuando ayuden a guiar la atención y mantengan legible el contenido principal.
4. Simplificar en mobile, probar degradación graciosa y asegurar que el contenido crítico siga visible sin depender de una animación perfecta.

## FORMATO DE SALIDA

- Objetivo narrativo
- Efectos o patrones elegidos
- Estrategia desktop y mobile
- Riesgo de performance o accesibilidad
- Fallback propuesto

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para criterios de degradación y validación cross-device.
- Ver `./_templates.md` para el template de dirección visual.
- Ver `./resources/motion-immersive-playbook.md` para stack guide, degradación mobile y quality gates de motion.

## ANTI-PATRON

Hacer scroll hijacking, saturar la interfaz con animaciones, entregar una experiencia solo desktop o esconder contenido clave detrás de coreografías frágiles.
