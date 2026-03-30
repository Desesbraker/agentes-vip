# API Design Playbook

## Cuándo abrir este recurso

- Elegir entre REST, GraphQL y tRPC
- Diseñar contratos API consistentes
- Fijar versionado, auth, rate limiting y formatos de error
- Entregar request/response ejemplos sin improvisación

## Fase 1: Entender consumidores

Antes de diseñar:

- ¿Quién consume la API?
- ¿Web, mobile, terceros, integraciones internas o monorepo TypeScript?
- ¿Necesitan agregación compleja o recursos simples?
- ¿Hay restricciones de caché, latencia o versionado público?

## Fase 2: Elegir patrón

| Patrón | Mejor para | Riesgo principal |
|---|---|---|
| REST | Recursos claros, integración amplia, semántica HTTP | Sobre/infra-fetching |
| GraphQL | Frontend-driven, agregación compleja, evitar múltiples round trips | Complejidad operativa y de caching |
| tRPC | Monorepo TypeScript y contratos end-to-end | Acoplamiento fuerte al stack TS |

### Reglas rápidas

- Elegir REST si el dominio se expresa bien como recursos y operaciones claras.
- Elegir GraphQL si múltiples consumidores necesitan composición flexible y granular.
- Elegir tRPC si el sistema es end-to-end TypeScript y se acepta acoplamiento al stack.

## Fase 3: Bloquear contrato

Definir siempre:

- Auth
- Idempotencia
- Request shape
- Response shape
- Error codes
- Paginación y filtros
- Versionado
- Documentación

## Response format principles

Elegir y mantener consistencia:

- Envelope: `success`, `data`, `error`
- Direct resource response
- Formatos hiper-media si realmente el sistema lo necesita

### Error response

- Código programático
- Mensaje seguro para consumidor
- Detalles de validación si aplica
- `request_id`
- Nunca filtrar detalles internos sensibles

## Paginación

| Tipo | Usar cuando | Trade-off |
|---|---|---|
| Offset | Listados simples con salto de página | Degrada en datasets grandes |
| Cursor | Datasets grandes o mutables | Menos amigable para salto arbitrario |
| Keyset | Performance crítica sobre clave ordenable | Menor flexibilidad |

## Versionado

- Versionar si habrá consumidores externos o cambios incompatibles.
- Usar deprecation path en vez de ruptura silenciosa.
- Documentar qué cambia y cuándo se retira.

## Rate limiting y seguridad

- Definir límites por actor o por token si la API puede ser abusada.
- Aplicar auth antes de modelar payloads sensibles.
- Revisar exposición de errores internos.

## Checklist de decisión

- [ ] Consumidores identificados
- [ ] Patrón elegido por contexto y no por moda
- [ ] Response format decidido
- [ ] Error format consistente
- [ ] Auth definida
- [ ] Rate limiting previsto
- [ ] Versionado definido
- [ ] Documentación prevista

## Entrega esperada

- Problema y consumidores
- Patrón elegido
- Contrato resumido
- Ejemplo request
- Ejemplo response
- Error codes y status codes
- Riesgo principal

## Anti-patrones

- REST por inercia para cualquier cosa
- Verbos en endpoints REST como recurso principal
- Formatos de error distintos por endpoint
- Exponer errores internos al cliente
- Abrir mutaciones sensibles sin idempotencia