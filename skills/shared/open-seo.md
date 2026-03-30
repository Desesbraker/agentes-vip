# @open-seo

TRIGGER: Necesitas datos reales para keyword research, domain insights, backlinks, content gap o site audits.

## Ruta de la app

- Repositorio local: `./herramientas/open-seo`
- Setup base: `./herramientas/open-seo/README.md`
- Docker: `./herramientas/open-seo/docs/SELF_HOSTING_DOCKER.md`

## Qué resuelve

1. Keyword research con datos reales de demanda e intención.
2. Domain insights para detectar páginas con visibilidad, pérdida o ganancia.
3. Backlinks para validar autoridad, páginas enlazadas y oportunidades.
4. Site audits para hallar problemas técnicos y priorizar correcciones.

## Setup recomendado para la agencia

1. Entrar en `./herramientas/open-seo`.
2. Ejecutar `cp .env.example .env`.
3. Añadir `DATAFORSEO_API_KEY=` en `./herramientas/open-seo/.env`.
4. Levantar con `docker compose up -d`.
5. Abrir `http://localhost:3001`.

## Alternativa local sin Docker

1. Entrar en `./herramientas/open-seo`.
2. Ejecutar `cp .env.example .env.local`.
3. Añadir `DATAFORSEO_API_KEY=` en `./herramientas/open-seo/.env.local`.
4. Ejecutar `pnpm install`.
5. Ejecutar `pnpm run db:migrate:local`.
6. Ejecutar `pnpm dev:agents`.
7. Usar la URL `http://open-seo.localhost:1355` para acceder al entorno local recomendado para agentes.

## Instrucciones para SEO Specialist

1. Usar OpenSEO cuando el trabajo requiera evidencia de keywords, backlinks, domain overview o auditoría técnica.
2. Traducir resultados a: hallazgo + evidencia + severidad + impacto + acción.
3. Priorizar interpretación sobre export bruto.
4. Reportar límites: costo API, cobertura parcial, falta de PSI o backlinks si aplica.

## Instrucciones para Copywriter

1. Usar OpenSEO solo como fuente de investigación previa, no como sustituto del criterio editorial.
2. Extraer: keyword principal, variantes, intención, preguntas relacionadas, páginas candidatas para internal links.
3. Convertir datos en brief, outline, titles, metas y estructura del contenido.
4. Si faltan datos SEO, pedirlos al SEO Specialist vía Orquestador o ejecutar este setup si el entorno lo permite.

## Instrucciones para Orquestador

1. Enrutar a SEO Specialist si la solicitud menciona auditoría SEO, keywords, backlinks, domain insights, content gap o site audit.
2. Enrutar a Copywriter si la solicitud es redacción SEO y requiere research verificable para brief, outline, metas o internal links.
3. Enrutar a Data Analyst si la solicitud pide cuantificación de demanda, benchmarks de dominios o proxies de mercado basados en búsquedas.
4. Si el trabajo combina research + redacción, secuenciar: SEO Specialist primero, Copywriter después.
5. Si OpenSEO no está configurado, informar bloqueo parcial y pedir setup antes de prometer métricas o priorizaciones cuantitativas.

## Instrucciones para Data Analyst

1. Usar OpenSEO como fuente auxiliar para señales de demanda, benchmarks de dominio y proxies de mercado.
2. Cruzar siempre esos datos con al menos otra fuente o método antes de concluir.
3. Documentar fórmula, supuestos y limitaciones cuando use search volume como proxy.
4. Coordinar con SEO Specialist si hace falta interpretación SEO profunda.

## Playbook operativo

- Casos y templates: `./skills/shared/open-seo-playbook.md`
- Prompts listos para invocar agentes: `./skills/shared/open-seo-prompts.md`

## Reglas de uso

1. `DATAFORSEO_API_KEY` es obligatoria para keywords, domain y backlinks.
2. La app no reemplaza estrategia, criterio editorial ni auditoría interpretada.
3. No inventar métricas si OpenSEO no está configurado o el request falla.
4. PSI es opcional y usa una Google PageSpeed Insights API key guardada por proyecto dentro de la app.

## Anti-patrones

- Copiar pantallas o tablas sin síntesis.
- Fabricar volumen, dificultad o tendencias.
- Forzar keyword stuffing porque la herramienta mostró una variante.
- Confundir backlinks con prueba suficiente de calidad de contenido.