# @api-design-principles

OBJETIVO: Definir contratos API consistentes, legibles y estables para que backend, frontend y mobile trabajen sobre el mismo acuerdo técnico.

USAR CUANDO: Hay que diseñar un endpoint nuevo, revisar un contrato existente o fijar estándares API para un equipo.

NO USAR CUANDO: La decisión principal es elegir estilo de API entre REST, GraphQL o tRPC. En ese caso usar primero @api-patterns.

INSTRUCCIONES:

1. Identificar consumidores, casos de uso, auth, volumen esperado y restricciones antes de diseñar recursos o payloads.
2. Modelar contratos con inputs, outputs, errores programáticos, paginación, filtros, versionado y reglas de idempotencia cuando apliquen.
3. Validar consistencia entre endpoints: naming, envelopes, status codes, convenciones de error y semántica de mutaciones.
4. Cerrar con ejemplos concretos y una salida parseable que otros equipos puedan implementar sin adivinar comportamiento.

FORMATO DE SALIDA:

- Objetivo del contrato
- Consumidores y auth
- Request y response esperados
- Errores y status codes
- Riesgos de consistencia

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de contrato.
- Ver `./_templates.md` para el template de contrato API.
- Ver `./resources/api-design-playbook.md` para response formats, versionado, rate limiting y ejemplos de handoff.
- Ver `./upstream/api-design-principles/SKILL.md` para la guía upstream completa.
- Ver `./upstream/api-design-principles/resources/implementation-playbook.md` para patrones, checklist y templates operativos.
- Ver `./upstream/api-design-principles/references/` y `./upstream/api-design-principles/assets/` para referencias y artefactos reutilizables.

ANTI-PATRÓN: Diseñar sin conocer consumidores, mezclar convenciones entre endpoints, dejar errores ambiguos o publicar una API sin ejemplos de request y response.
