# Next.js Routing and Cache Playbook

## Cuándo abrir este recurso

- Estructurar App Router
- Resolver layout, loading, error, route groups o segmentación
- Diseñar estrategia de cache y revalidación

## Flujo operativo

1. Identificar tipo de vista y requisitos de frescura.
2. Elegir render mode: static, revalidate, dynamic o no-store.
3. Estructurar segmentos con `page`, `layout`, `loading` y `error`.
4. Definir invalidación desde `revalidatePath` o `revalidateTag` si aplica.

## Reglas duras

- No usar `use client` por reflejo.
- No mezclar estrategias de cache sin razón explícita.
- No cerrar una ruta sin loading y error donde el usuario los necesite.

## Decision matrix

| Necesidad | Estrategia |
|---|---|
| Contenido estable | static |
| Frescura periódica | revalidate |
| Datos por request | dynamic |
| Sensible o sin cache | no-store |

## Quality gates

- [ ] Render strategy definida
- [ ] Cache strategy definida
- [ ] Segmentos con loading/error donde hace falta
- [ ] Mutations con invalidación clara
- [ ] Riesgo de hydration o bundle evaluado

## Entrega esperada

- Tipo de ruta o vista
- Estrategia de render
- Datos y cache
- Archivos clave
- Riesgo o edge case