# @tailwind-patterns

## OBJETIVO

Implementar estilos con Tailwind de forma consistente, escalable y alineada con tokens de diseño en lugar de utilidades caóticas.

## USAR CUANDO

Hay que construir UI con Tailwind CSS, definir tokens, resolver responsividad por componente o sistematizar patrones visuales reutilizables.

## NO USAR CUANDO

La tarea requiere dirección visual, branding o decisiones UX de alto nivel. Tailwind implementa; no reemplaza diseño.

## INSTRUCCIONES

1. Trabajar con enfoque CSS-first y tokens claros, aprovechando theme y variables nativas antes de llenar el markup con valores arbitrarios.
2. Usar container queries cuando la responsividad dependa del componente y no solo del viewport completo.
3. Definir color y spacing por capas: token primitivo, semántico y de componente para evitar clases sin criterio de sistema.
4. Extraer patrones repetidos a componentes o variantes reutilizables cuando la combinación de utilidades deje de ser legible.

## FORMATO DE SALIDA

- Patrón visual a implementar
- Tokens o variables implicadas
- Estrategia responsive
- Reutilización prevista
- Riesgo de inconsistencia

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas de sistema visual y reuse.
- Ver `./_templates.md` para el template de dirección visual.
- Ver `./resources/tailwind-design-system-playbook.md` para capas de token, responsive por componente y reuse.

## ANTI-PATRON

Llenar todo de arbitrary values, abusar de important, mezclar convenciones de Tailwind v3 y v4 o usar apply como sustituto de un sistema de componentes.
