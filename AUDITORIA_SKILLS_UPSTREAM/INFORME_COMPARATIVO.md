# Informe Comparativo de Adaptación de Skills

## Objetivo

Evaluar si dos perfiles locales de la agencia absorbieron suficiente información útil desde la fuente declarada del catálogo de skills:

- https://github.com/sickn33/antigravity-awesome-skills

La hipótesis a contrastar es simple: los perfiles locales están bien armados como router de activación, pero parte importante del conocimiento operativo del upstream podría haberse perdido durante la adaptación.

## Alcance de esta ronda

Perfiles auditados en esta implementación:

1. Backend
2. UI/UX

Para cada perfil se revisó:

- Perfil del agente
- Carpeta completa de skills de su familia
- Playbook auxiliar local
- Equivalentes o aproximaciones razonables en el repo upstream

## Método de comparación

Cada familia se evaluó en cinco dimensiones:

1. Conexión local entre perfil y skill
2. Cobertura temática respecto al upstream
3. Densidad operativa de la información
4. Presencia de recursos anexos útiles para ejecución real
5. Riesgo de compresión excesiva

La comparación no exige copiar todo el upstream al repo local. El criterio correcto es otro: mantener prompts compactos en el perfil, pero no perder conocimiento crítico que debería vivir en playbooks, templates, resources o ejemplos.

## Backend

### Base local revisada

- [agente_backend/perfil.md](../agente_backend/perfil.md)
- [skills/backend/_playbook.md](../skills/backend/_playbook.md)
- [skills/backend/backend-dev-guidelines.md](../skills/backend/backend-dev-guidelines.md)
- [skills/backend/api-patterns.md](../skills/backend/api-patterns.md)
- [skills/backend/api-design-principles.md](../skills/backend/api-design-principles.md)
- [skills/backend/fastapi-pro.md](../skills/backend/fastapi-pro.md)

### Fuente upstream principal usada

- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/backend-dev-guidelines/SKILL.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/nodejs-backend-patterns/resources/implementation-playbook.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/api-patterns/SKILL.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/api-design-principles/resources/implementation-playbook.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/plugins/antigravity-awesome-skills/skills/python-fastapi-development/SKILL.md

### Mapeo local vs upstream

| Local | Upstream equivalente o cercano | Estado |
|---|---|---|
| @backend-dev-guidelines | backend-dev-guidelines, nodejs-backend-patterns | Adaptación parcial |
| @api-patterns | api-patterns | Bien conectado, comprimido |
| @api-design-principles | api-design-principles | Bien conectado, comprimido |
| @database-design | database-design y recursos asociados | Parcial |
| @nodejs-best-practices | nodejs-best-practices y nodejs-backend-patterns | Parcial |
| @python-pro | python bundle y skills Python relacionadas | Parcial |
| @fastapi-pro | python-fastapi-development y fastapi resources | Parcial |
| @django-pro | skills Django del upstream | Parcial |
| @sql-pro | sql patterns y recursos SQL | Parcial |
| @postgres-best-practices | patrones Postgres dispersos en bundles y playbooks | Parcial |
| @stripe-integration | skill presente en índices upstream, sin evidencia tan rica en la búsqueda usada | Indeterminado |

### Qué está bien absorbido localmente

1. El perfil local sí enruta bien las tareas. El índice en [agente_backend/perfil.md](../agente_backend/perfil.md) separa decisiones de estilo API, contratos, base de datos, stack Python, stack Node y pagos con suficiente claridad para activar una skill concreta.
2. El playbook local en [skills/backend/_playbook.md](../skills/backend/_playbook.md) conserva disciplina estructural útil: contrato antes de endpoint, schema antes de migration, tests y rollback como cierre.
3. Varias skills locales sí preservan el espíritu del upstream como guía de decisión. Se ve bien en [skills/backend/api-patterns.md](../skills/backend/api-patterns.md) y [skills/backend/api-design-principles.md](../skills/backend/api-design-principles.md): consumidores, auth, versionado, errores y consistencia aparecen como requisitos, no como opcionales.
4. La adaptación local es clara para un agente que ya tenga contexto técnico fuerte. No hay ambigüedad sobre el rol ni sobre lo que no debe hacer.

### Información importante del upstream que se perdió o quedó muy reducida

1. En backend-dev-guidelines local se perdió doctrina operativa detallada. El upstream no solo dice separar capas; también baja esa regla a arquitectura canónica, naming estricto, dependency injection, repository rules, error boundaries, observabilidad y checklist de validación final.
2. El upstream de nodejs-backend-patterns aporta un implementation playbook de gran profundidad con middleware patterns, error handling, authentication, caching, graceful shutdown, connection pooling, health checks, testing patterns y recursos externos. Esa capa prácticamente no está presente en el repo local.
3. El upstream de api-patterns no se limita a elegir entre REST, GraphQL y tRPC. Añade checklist de decisión, response format principles, anti-patrones y criterios de documentación. Localmente quedó la versión ejecutiva, pero no el cuerpo operativo que ayuda a implementar sin improvisar.
4. En api-design-principles upstream aparecen pitfalls y recursos anexos concretos: versionado, error formats consistentes, rate limiting, guías REST, schema design, templates y checklist previo a implementación. El local preserva el concepto, pero no el nivel de aterrizaje.
5. En FastAPI el upstream disponible muestra workflow por fases: diseño, data layer, models, sessions, migrations y prompts claros de uso. La skill local [skills/backend/fastapi-pro.md](../skills/backend/fastapi-pro.md) resume muy bien la intención, pero no contiene ese recorrido operativo.
6. El upstream trabaja bastante con bundles y orquestación entre skills. Localmente casi todo quedó como piezas individuales, lo que reduce guidance para flujos complejos y deja más trabajo implícito al modelo.
7. Falta scaffolding utilizable. En la evidencia upstream aparecen templates, resources y playbooks que convierten la skill en mecanismo de ejecución real. En local hay _playbook y _templates, pero hoy funcionan más como recordatorio compacto que como reemplazo equivalente.

### Señales concretas de compresión local

1. [skills/backend/backend-dev-guidelines.md](../skills/backend/backend-dev-guidelines.md) condensa en pocas líneas lo que upstream desarrolla como estándar de backend productivo con checklist, integración entre skills y validación operativa.
2. [skills/backend/api-patterns.md](../skills/backend/api-patterns.md) y [skills/backend/api-design-principles.md](../skills/backend/api-design-principles.md) cubren bien la decisión y el contrato, pero no arrastran response formats, recursos de implementación ni reglas más finas de consistencia que sí existen en upstream.
3. [skills/backend/fastapi-pro.md](../skills/backend/fastapi-pro.md) nombra OpenAPI, async, testing y dependencias limpias, pero no hereda bundles de ejecución por fases ni ejemplos de integración que el upstream sí organiza.

### Veredicto Backend

Estado general: demasiado comprimido.

Juicio:

- El repo local sí conserva routing y guardrails.
- El repo local no conserva suficiente profundidad operativa para afirmar que absorbió bien el valor completo del upstream.
- El mayor déficit no está en el perfil, sino en la pérdida de resources, templates, implementation playbooks y bundles.

Prioridad de mejora: alta.

## UI/UX

### Base local revisada

- [agente_ui_ux/perfil.md](../agente_ui_ux/perfil.md)
- [skills/ui_ux/_playbook.md](../skills/ui_ux/_playbook.md)
- [skills/ui_ux/ui-ux-pro-max.md](../skills/ui_ux/ui-ux-pro-max.md)
- [skills/ui_ux/mobile-design.md](../skills/ui_ux/mobile-design.md)
- [skills/ui_ux/interactive-portfolio.md](../skills/ui_ux/interactive-portfolio.md)

### Fuente upstream principal usada

- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/ui-ux-pro-max/SKILL.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/mobile-design/SKILL.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/docs/users/bundles.md
- https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/README.md

### Mapeo local vs upstream

| Local | Upstream equivalente o cercano | Estado |
|---|---|---|
| @ui-ux-pro-max | ui-ux-pro-max | Bien conectado, muy resumido |
| @frontend-design | frontend-design y skills de diseño complementarias | Parcial |
| @canvas-design | canvas-design | Parcial |
| @mobile-design | mobile-design | Bien conectado, resumido |
| @interactive-portfolio | interactive-portfolio | Bien conectado, resumido |
| @algorithmic-art | algorithmic-art | Parcial |

### Qué está bien absorbido localmente

1. El perfil en [agente_ui_ux/perfil.md](../agente_ui_ux/perfil.md) tiene buen routing y un alcance claro del rol. El agente no quedó ambiguo.
2. [skills/ui_ux/ui-ux-pro-max.md](../skills/ui_ux/ui-ux-pro-max.md) sí preserva el núcleo correcto del upstream: accesibilidad, interacción, design system, riesgos y entrega lista para implementación.
3. [skills/ui_ux/mobile-design.md](../skills/ui_ux/mobile-design.md) mantiene principios esenciales valiosos del upstream: touch-first, plataforma explícita, contexto de uso, diferencias iOS y Android.
4. [skills/ui_ux/interactive-portfolio.md](../skills/ui_ux/interactive-portfolio.md) recoge una idea importante y muy concreta del upstream: el 30-Second Test y la prioridad de evidenciar valor, no solo mostrar estética.
5. El playbook local [skills/ui_ux/_playbook.md](../skills/ui_ux/_playbook.md) es razonable como capa corta de operación para un agente senior.

### Información importante del upstream que se perdió o quedó muy reducida

1. UI/UX Pro Max upstream es mucho más que una definición de objetivos. Incluye quick reference por prioridades, dominios de búsqueda, stacks disponibles, workflow detallado paso a paso, output formats, tips de uso, common rules for professional UI y pre-delivery checklist. Casi toda esa riqueza no aparece en el archivo local.
2. El upstream de ui-ux-pro-max se apoya en scripts y generadores de design system. Esa parte no se absorbió en la versión local, por lo que el agente local conoce el destino deseado, pero no el mecanismo práctico sugerido por la fuente.
3. En mobile-design upstream hay matriz explícita de qué unificar y qué divergir entre iOS y Android, defaults de plataforma y psicología táctil más desarrollada. La skill local retiene la intención, pero no ese nivel de decisión.
4. La evidencia upstream incluye checklists de entrega mucho más finos: contrastes, icons, focus, reduced motion, breakpoints, hover states, layout, floating navbars y consistencia visual. En local estos criterios quedaron más comprimidos.
5. La capa de search reference del upstream es especialmente valiosa para diseño porque enseña cómo explorar producto, estilo, tipografía, color, landing, chart, UX, React y web. Ese material no fue traducido a un recurso local equivalente.
6. La familia local mantiene bien la dirección, pero no conserva suficiente instrumentación para que un agente menos experto ejecute diseño con la misma riqueza contextual que el upstream propone.

### Señales concretas de compresión local

1. [skills/ui_ux/ui-ux-pro-max.md](../skills/ui_ux/ui-ux-pro-max.md) resume muy bien el corazón del skill, pero deja fuera casi todo el apparatus operativo del upstream: quick reference, workflow, search reference y pre-delivery checklist completo.
2. [skills/ui_ux/mobile-design.md](../skills/ui_ux/mobile-design.md) mantiene reglas fuertes de touch y plataforma, pero no absorbe tablas concretas y matrices de divergencia del upstream.
3. [skills/ui_ux/interactive-portfolio.md](../skills/ui_ux/interactive-portfolio.md) conserva bien la lógica narrativa, aunque sigue siendo una versión más corta y menos ejemplificada que la fuente original.

### Veredicto UI/UX

Estado general: bien resumido en el núcleo, pero con cobertura incompleta.

Juicio:

- El repo local sí absorbió la lógica base del routing de diseño.
- La pérdida principal está en recursos de ejecución, búsqueda guiada, criterios detallados y checklists completos.
- A diferencia de Backend, aquí la adaptación central es mejor, pero sigue faltando material auxiliar para acercarse al upstream.

Prioridad de mejora: media.

## Hallazgos transversales

| Dimensión | Local | Upstream | Impacto |
|---|---|---|---|
| Routing por skill | Bueno | Bueno | Sin problema crítico |
| Claridad del rol | Alta | Alta | Sin problema crítico |
| Playbooks auxiliares | Presentes pero cortos | Profundos y ricos | Gap real |
| Templates y resources | Escasos | Frecuentes | Gap real |
| Workflows multi-fase | Muy reducidos | Comunes | Gap real |
| Checklists operativos | Básicos | Detallados | Gap medio-alto |
| Ejemplos y guías de ejecución | Muy pocos | Abundantes | Gap alto |
| Capacidad de ejecución autónoma | Depende del seniority del agente | Más guiada por la fuente | Gap alto |

## Conclusión ejecutiva

Sí, la sospecha del usuario está bien fundada.

El repo local conserva correctamente el nivel L1 de routing:

- quién hace qué
- cuándo activar una skill
- qué no hacer
- qué checks mínimos aplicar

Pero absorbe solo una parte del valor L2 y L3 del upstream:

- playbooks detallados
- recursos anexos
- templates de implementación
- bundles o workflows multi-fase
- checklists más finos
- ejemplos y mecanismos prácticos de ejecución

Dicho de otro modo:

- Los perfiles locales sí están bien informados para enrutar.
- No siempre están suficientemente informados para ejecutar con toda la riqueza que la fuente upstream sí ofrece.

## Recomendación operativa

1. No inflar los perfiles principales. Mantenerlos compactos como router.
2. Recuperar conocimiento upstream perdido en recursos anexos por familia, no dentro de cada skill corta.
3. Priorizar Backend primero, porque hoy es donde la compresión elimina más capacidad operativa.
4. En UI/UX, priorizar playbooks, search references, checklists y criterios cross-platform antes que reescribir el perfil.
5. Convertir el patrón de adaptación en norma: skill corta como entrada, resources y playbooks como cuerpo operativo.

## Prioridad sugerida de enriquecimiento

### Prioridad alta

- Backend
- Node/Express patterns
- API implementation resources
- FastAPI workflow

### Prioridad media

- UI/UX Pro Max resources
- Mobile design matrices y defaults
- Checklists de entrega visual y accesibilidad

### Prioridad baja

- Ajustes menores de naming o redacción cuando el routing ya es claro

## Resultado de esta implementación

Se creó esta carpeta raíz para centralizar el análisis:

- [AUDITORIA_SKILLS_UPSTREAM](.)

Y este archivo como informe consolidado:

- [AUDITORIA_SKILLS_UPSTREAM/INFORME_COMPARATIVO.md](./INFORME_COMPARATIVO.md)