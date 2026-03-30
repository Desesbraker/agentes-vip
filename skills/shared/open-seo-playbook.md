# Playbook: OpenSEO en la Agencia

## Objetivo

Usar OpenSEO como fuente verificable de datos para research SEO, contenido y análisis de demanda sin fabricar métricas ni reemplazar criterio experto.

## URL operativa

- Local recomendado para agentes: `http://open-seo.localhost:1355`

## Flujo recomendado por agente

### Orquestador

TRIGGER: La solicitud pide evidencia sobre keywords, backlinks, visibilidad orgánica, content gap, site audit o demanda por búsqueda.

1. Si pide auditoría, priorización SEO o evidencia técnica -> asignar a SEO Specialist.
2. Si pide redacción SEO con research verificable -> SEO Specialist primero, Copywriter después.
3. Si pide cuantificación de demanda, comparativas de dominios o proxies de mercado desde búsquedas -> Data Analyst con apoyo de SEO Specialist si hace falta interpretación SEO.
4. Si OpenSEO no está disponible -> reportar bloqueo parcial, continuar solo con hipótesis explícitas y sin métricas inventadas.

### SEO Specialist

TRIGGER: Hace falta evidencia real para auditoría, keywords, content gap, backlinks o domain insights.

1. Abrir OpenSEO.
2. Ejecutar el workflow más cercano al objetivo.
3. Extraer evidencia mínima: fuente, entidad analizada, dato, impacto esperado, limitación.
4. Entregar findings estructurados, no capturas ni tablas crudas.

Template mínimo:

- Issue:
- Evidence:
- Severity:
- Score Impact:
- Recommendation:

### Copywriter

TRIGGER: Hay que escribir contenido SEO con base verificable.

1. Pedir o generar research en OpenSEO.
2. Extraer keyword principal, variantes, intención, preguntas y páginas para internal linking.
3. Convertir a brief editorial antes de redactar.
4. Mantener voz de marca y evitar keyword stuffing.

Template mínimo:

- Primary keyword:
- Search intent:
- Supporting terms:
- Questions to answer:
- Internal links:
- Draft angle:

### Data Analyst

TRIGGER: Hace falta usar señales de búsqueda como proxy de demanda, benchmark competitivo o apoyo para sizing.

1. Usar OpenSEO para obtener volúmenes, clusters, dominios comparables o cambios de visibilidad.
2. Tratar esos datos como una fuente parcial, no como verdad total de mercado.
3. Cruzar con al menos otra fuente o método antes de concluir.
4. Reportar fórmula, supuestos y limitaciones del proxy usado.

Template mínimo:

- Question:
- Search-demand proxy used:
- Comparison set:
- Supporting source:
- Limitation:
- Decision implication:

## Casos rápidos

### Caso 1: Auditoría SEO de sitio

1. Orquestador -> SEO Specialist.
2. SEO Specialist usa site audit + domain insights.
3. Entrega blockers, quick wins y plan priorizado.

### Caso 2: Redactar blog post SEO

1. Orquestador -> SEO Specialist para research.
2. SEO Specialist entrega keyword pack + intent + internal links.
3. Copywriter redacta con ese brief.

### Caso 3: Estimar demanda de una categoría

1. Orquestador -> Data Analyst.
2. Data Analyst usa OpenSEO como proxy de search demand.
3. Cruza con otra fuente y entrega rango, no cifra absoluta sin contexto.

## Reglas duras

- No inventar métricas si OpenSEO falla o no está disponible.
- No usar una sola fuente para conclusiones fuertes de negocio.
- No confundir volumen de búsqueda con revenue potencial sin modelo intermedio.
- No delegar interpretación estratégica al dashboard.

## Prompts listos

- Ver `./skills/shared/open-seo-prompts.md` para invocaciones directas de Orquestador, SEO Specialist, Copywriter y Data Analyst.