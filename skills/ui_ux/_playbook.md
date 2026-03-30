# Playbook de UI/UX

## Cómo usar este playbook

1. Usar este archivo como capa transversal mínima.
2. Abrir después el recurso temático en `./resources/` según el tipo de trabajo.
3. No diseñar si aún no están bloqueados objetivo, audiencia, plataforma y tono.

## Mapa de resources

- `./resources/design-system-playbook.md`
- `./resources/frontend-aesthetics-playbook.md`
- `./resources/mobile-ux-playbook.md`
- `./resources/portfolio-playbook.md`
- `./resources/generative-visual-playbook.md`

## Flujo operativo

1. Bloquear objetivo, audiencia, plataforma y tono visual antes de diseñar componentes, layouts o piezas artísticas.
2. Elegir una dirección visual defendible y convertirla en reglas de sistema: tipografía, color, spacing, interacción y motion.
3. Diseñar con accesibilidad, legibilidad y viabilidad de implementación como restricciones duras, no como revisión final.
4. Cerrar con una entrega accionable para Frontend, Mobile o stakeholders, incluyendo riesgos y decisiones abiertas.

## Árbol rápido de decisión

### Si el problema es design system o auditoría general

- Elegir `@ui-ux-pro-max`
- Abrir `./resources/design-system-playbook.md`

### Si el problema es dirección estética web

- Elegir `@frontend-design`
- Abrir `./resources/frontend-aesthetics-playbook.md`

### Si el problema es mobile UX

- Elegir `@mobile-design`
- Abrir `./resources/mobile-ux-playbook.md`

### Si el problema es portfolio

- Elegir `@interactive-portfolio`
- Abrir `./resources/portfolio-playbook.md`

### Si el problema es canvas o arte generativo

- Elegir `@canvas-design` o `@algorithmic-art`
- Abrir `./resources/generative-visual-playbook.md`

## Reglas duras

- No entregar UI sin design system o reglas explícitas.
- No aprobar contrastes, focus states o targets táctiles deficientes.
- No usar plantillas genéricas disfrazadas de dirección visual.
- No diseñar mobile sin plataforma, contexto de uso y restricciones de interacción.

## Checklists rápidos

### Sistema visual

- Objetivo visual definido
- Tipografías y paleta con roles claros
- Variables o tokens documentados
- Componentes base identificados

### UX móvil

- Plataforma y navegación definidas
- Targets táctiles correctos
- Estados vacíos, error y offline contemplados
- Gestos críticos visibles o reemplazables

### Entrega final

- Accesibilidad mínima validada
- Riesgo de implementación identificado
- QA visual previsto
- No parece template intercambiable
