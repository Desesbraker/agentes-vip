# @api-patterns

OBJETIVO: Elegir el estilo de API correcto para el problema, evitando imponer REST, GraphQL o tRPC por moda o preferencia del equipo.

USAR CUANDO: Hay que decidir cómo exponer una API nueva o revisar si el patrón actual sigue siendo correcto para los consumidores reales.

NO USAR CUANDO: El estilo ya está definido y el trabajo ahora es cerrar contratos detallados. En ese caso usar @api-design-principles.

INSTRUCCIONES:

1. Evaluar consumidores, acoplamiento, complejidad de consulta, stack del cliente y gobernanza antes de elegir estilo.
2. Usar REST para recursos y operaciones claras, GraphQL para consumo frontend-driven con necesidad de agregación y tRPC para monorepos TypeScript con contratos end-to-end.
3. Definir desde el inicio auth, rate limiting, errores, versionado y estrategia de documentación para el patrón elegido.
4. Explicar por qué se descartan las alternativas para que la decisión sea defendible y no accidental.

FORMATO DE SALIDA:

- Problema y consumidores
- Patrón recomendado
- Razón de descarte de alternativas
- Reglas de auth, rate limiting y versionado
- Riesgo principal de adopción

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para el flujo común de diseño backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/api-design-playbook.md` para matrices de decisión, formatos de respuesta y checklist de diseño.
- Ver `./upstream/api-patterns/SKILL.md` para el mapa upstream y la regla de lectura selectiva.
- Ver `./upstream/api-patterns/` para subtemas específicos: REST, GraphQL, tRPC, auth, versionado, rate limiting, documentación y security testing.

ANTI-PATRÓN: Elegir REST, GraphQL o tRPC por inercia, usar verbos como recursos REST, dejar formatos inconsistentes o abrir una API sin controles operativos mínimos.
