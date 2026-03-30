# Playbook de Frontend

## Cómo usar este playbook

1. Usar este archivo como capa transversal mínima.
2. Abrir luego el recurso temático en `./resources/` según el problema.
3. No empezar a codificar si aún no están definidos objetivo, datos, render y riesgo UX/performance.

## Mapa de resources

- `./resources/react-nextjs-playbook.md`
- `./resources/performance-playbook.md`
- `./resources/nextjs-routing-cache-playbook.md`
- `./resources/tailwind-design-system-playbook.md`
- `./resources/forms-cro-playbook.md`
- `./resources/motion-immersive-playbook.md`
- `./resources/typescript-frontend-playbook.md`

## Flujo operativo

1. Bloquear objetivo de la vista, usuario, dispositivo dominante y estado de datos antes de escribir componentes.
2. Decidir render, estado y contratos primero; luego elegir patrón React, Next.js, Tailwind o TypeScript que resuelva el problema con menor complejidad.
3. Implementar con accesibilidad mínima, estados vacíos y de error, responsive real y presupuesto de performance razonable.
4. Verificar en desktop y mobile, revisar hydration, bundle, errores visibles y cobertura o prueba manual según el riesgo.

## Árbol rápido de decisión

### Si el problema es construcción de vistas o componentes

- Elegir `@frontend-developer`
- Abrir `./resources/react-nextjs-playbook.md`

### Si el problema es arquitectura React

- Elegir `@react-patterns`
- Abrir `./resources/react-nextjs-playbook.md`

### Si el problema es performance

- Elegir `@react-best-practices`
- Abrir `./resources/performance-playbook.md`

### Si el problema es Next.js App Router o caché

- Elegir `@nextjs-best-practices`
- Abrir `./resources/nextjs-routing-cache-playbook.md`

### Si el problema es Tailwind o sistema visual implementado

- Elegir `@tailwind-patterns`
- Abrir `./resources/tailwind-design-system-playbook.md`

### Si el problema es formulario o conversión

- Elegir `@form-cro`
- Abrir `./resources/forms-cro-playbook.md`

### Si el problema es scroll, motion o 3D

- Elegir `@scroll-experience` o `@3d-web-experience`
- Abrir `./resources/motion-immersive-playbook.md`

### Si el problema es tipado o compilación TS

- Elegir `@typescript-expert`
- Abrir `./resources/typescript-frontend-playbook.md`

## Reglas duras

- Server Components por defecto en Next.js; mover al cliente solo lo que requiera eventos, estado local o APIs del navegador.
- No diseñar experiencia scroll, 3D o motion sin fallback mobile y degradación aceptable.
- No introducir direction visual genérica; cada interfaz debe tener propósito, jerarquía y restricciones explícitas.
- No cerrar una vista sin estados loading, empty, error y success cuando el flujo los requiera.

## Checklists rápidos

### Vista React o Next.js

- Objetivo de la vista definido
- Render server/client decidido
- Data fetching y cache explícitos
- Estados críticos cubiertos
- Validación o test propuesto

### Performance

- Bottleneck identificado
- Waterfalls eliminados o justificados
- JS cliente minimizado
- Terceros diferidos o removidos
- Riesgo medido o plan de medición

### Dirección visual

- Tipografía principal y secundaria definidas
- Paleta con roles claros
- Reglas de spacing, contraste y motion documentadas
- No parece plantilla genérica
