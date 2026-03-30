# TypeScript Frontend Playbook

## Cuándo abrir este recurso

- Resolver errores de tipos complejos
- Modelar dominio frontend
- Mejorar compilación o ergonomía TypeScript

## Flujo operativo

1. Identificar causa raíz del problema de tipos.
2. Corregir el modelo, no silenciar el error.
3. Endurecer configuración cuando el proyecto lo soporte.
4. Revisar impacto en DX y performance del compilador.

## Baseline útil

- `strict`
- `noUncheckedIndexedAccess`
- `exactOptionalPropertyTypes` cuando sea viable
- `satisfies`
- `const assertions`

## Anti-patrones frecuentes

- `any` implícito
- assertions para tapar modelo roto
- genéricos innecesariamente complejos
- silenciar errores sin arreglar frontera de tipos

## Checklist

- [ ] Problema de tipos identificado
- [ ] Causa raíz aislada
- [ ] Cambio propuesto claro
- [ ] Tradeoff documentado
- [ ] Regla futura definida