# React and Next.js Playbook

## Cuándo abrir este recurso

- Construir vistas, componentes, layouts o dashboards en React/Next.js
- Diseñar arquitectura de componentes y estado
- Traducir `@frontend-developer` y `@react-patterns` a decisiones concretas

## Flujo operativo

1. Bloquear objetivo de la vista, actor, fuente de datos y riesgo UX.
2. Decidir qué va en servidor y qué requiere cliente.
3. Diseñar jerarquía de componentes, hooks y límites de estado.
4. Cerrar con loading, empty, error, success, responsive y validación mínima.

## Doctrina base

- Server Components por defecto en Next.js.
- Client Components solo para estado local, eventos o APIs del navegador.
- Server state separado del estado UI local.
- Composición sobre condicionales gigantes.

## Arquitectura de componentes

### Capas útiles

- page/layout
- server data boundary
- client interactive island
- presentational component
- custom hooks reutilizables

### Patrones recomendados

- Compound components si mejoran claridad
- Hooks extraídos cuando hay API clara
- `useOptimistic`, `useActionState` o primitives modernos cuando resuelvan un problema real
- Zustand o Jotai para estado cliente complejo y localizado
- TanStack Query para server state fuera del modelo puro server component

## Checklist de vista

- [ ] Objetivo claro
- [ ] Server/client split decidido
- [ ] Fetching y cache decididos
- [ ] Loading, empty, error y success cubiertos
- [ ] Responsive básico validado
- [ ] Accesibilidad mínima considerada

## Handoff esperado

- Objetivo de la vista
- Estructura de componentes
- Decisiones de render y estado
- Riesgos UX o performance
- Test o validación propuesta

## Anti-patrones

- Todo como client component
- Side effects dispersos sin capa clara
- useEffect como parche universal
- Estado remoto duplicado sin necesidad