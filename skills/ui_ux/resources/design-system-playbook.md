# Design System Playbook

## Cuándo abrir este recurso

- Diseñar o auditar un design system
- Traducir una dirección visual a reglas implementables
- Recuperar la profundidad de `ui-ux-pro-max` del upstream
- Resolver accesibilidad, responsive, motion y coherencia visual

## Flujo operativo

1. Analizar requerimientos: tipo de producto, industria, tono visual, audiencia y stack objetivo.
2. Definir sistema visual: pattern, estilo, color, tipografía, componentes y motion.
3. Validar interacción, responsive y accesibilidad antes de refinar estética.
4. Entregar tokens, reglas y checklist de implementación para Frontend o Mobile.

## Categorías prioritarias

| Prioridad | Categoría | Qué revisar |
|---|---|---|
| 1 | Accesibilidad | contraste, focus, labels, teclado, reduced motion |
| 2 | Touch e interacción | targets, feedback, hover/focus, cursor, estados |
| 3 | Performance visual | imágenes, layout stability, motion, content jumping |
| 4 | Layout y responsive | breakpoints, spacing, contenedores, scroll horizontal |
| 5 | Tipografía y color | pairing, legibilidad, jerarquía, roles cromáticos |
| 6 | Animación | duración, easing, transform, loading states |
| 7 | Estilo | diferenciación, consistencia, anti-patrones visuales |

## Search reference operativo

### Dominios que conviene pensar aunque no exista script local

- `product`: tipo de producto y estructura de página
- `style`: categoría estética y efectos
- `typography`: pairing y personalidad tipográfica
- `color`: paletas y roles cromáticos
- `landing`: orden de secciones y CTA strategy
- `ux`: accesibilidad, loading, z-index, feedback
- `react` o `web`: constraints de implementación por stack

### Stacks a tener en cuenta

| Stack | Foco |
|---|---|
| html-tailwind | utilidades, responsive, a11y |
| react | estado, rendimiento, componentes |
| nextjs | SSR, imágenes, routing, app structure |
| vue | composición y estructura |
| svelte | performance y simplicidad |
| swiftui | navegación, state, animation |
| react-native | componentes, listas, navegación |
| flutter | widgets, layout, theming |
| shadcn | theming, forms, composición |

## Output esperado de un design system

- Objetivo visual y de experiencia
- Pattern de layout
- Dirección de estilo
- Paleta con roles claros
- Tipografías y jerarquía
- Tokens o variables clave
- Componentes base
- Estados interactivos
- Anti-patrones explícitos
- Riesgos de implementación

## Checklist previo a entrega

### Visual quality

- [ ] No usar emojis como iconos
- [ ] Iconografía consistente
- [ ] Hover sin layout shift
- [ ] Tipografía con personalidad y propósito
- [ ] No parece template intercambiable

### Interaction

- [ ] Todo clickable tiene feedback claro
- [ ] Focus visible
- [ ] Transiciones entre 150 y 300ms si aplica
- [ ] Targets y affordances visibles

### Layout

- [ ] Responsive validado en 375, 768, 1024 y 1440
- [ ] No hay contenido oculto por elementos fixed
- [ ] No hay scroll horizontal accidental
- [ ] Spacing consistente entre secciones

### Accessibility

- [ ] Contraste mínimo razonable
- [ ] Form inputs con labels
- [ ] Color no es único indicador
- [ ] `prefers-reduced-motion` respetado si hay motion fuerte

## Anti-patrones

- Diseñar bonito sin reglas de sistema
- Glass o efectos sin revisar contraste y legibilidad
- Dark mode o light mode rotos
- Navbar fixed que tapa contenido
- UI vistosa pero sin diferenciación real