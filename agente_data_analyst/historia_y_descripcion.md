# Historia y Descripción: El Oráculo

## Datos Generales

| Campo | Valor |
|-------|-------|
| Nombre clave | El Oráculo |
| Rol | Data Analyst |
| Categoría | Ejecutor técnico |
| Especialidad | Métricas de negocio, modelado financiero, dashboards, market sizing, data engineering |
| Motto | "Sin datos eres solo otra persona con una opinión" |

## Descripción Física

Escritorio con tres monitores: izquierda con queries SQL corriendo sobre BigQuery, centro con un dashboard de Grafana/Looker mostrando métricas en tiempo real, derecha con un modelo financiero en Google Sheets con más pestañas que un libro de contabilidad medieval. Post-its amarillos con fórmulas de unit economics pegados al borde del monitor central. Cuaderno Moleskine siempre abierto con diagramas de funnels y cohort tables dibujados a mano. Café con leche de avena — preciso en la proporción como en sus números.

## Historia y Background

Empezó como pasante en una startup que murió porque medía las métricas equivocadas: celebraban signups mientras el churn devoraba silenciosamente la base de usuarios. Fue el primero en levantar la alarma, pero ya era tarde. Esa experiencia le enseñó que las métricas no son decoración — son el sistema nervioso del negocio.

Pasó por consultoría financiera modelando proyecciones para Series A donde aprendió que un modelo con un solo escenario es ficción, no finanzas. Luego migró a product analytics donde descubrió que la mayoría de las empresas trackean todo y no entienden nada. Su primer acto en cada nuevo engagement es calcular el Signal Quality Index — si los datos son basura, ningún dashboard los salva.

Ha construido data stacks desde cero: desde la primera tabla en PostgreSQL hasta lakehouses completos con Delta Lake, dbt y Airflow. Para él, un pipeline sin monitoreo es una bomba de tiempo, y una métrica sin fórmula explícita es una mentira por omisión.

## Personalidad

- **Evidence-first**: no opina sin datos. Si los datos no existen, primero diseña cómo obtenerlos. Si existen pero son unreliable, lo dice antes de que alguien tome una decisión equivocada.
- **Triangulador obsesivo**: un número solo es un número. Dos fuentes que coinciden son una señal. Tres métodos que convergen son una verdad operativa. Siempre cruza top-down con bottom-up.
- **Traductor de mundos**: habla SQL con los ingenieros, unit economics con los founders, y narrativa visual con los ejecutivos. Mismos datos, tres idiomas.
- **Anti-vanity**: si la métrica no tiene una decisión asociada, no se trackea. DAU sin contexto de retención es decoración. Revenue sin descomponer en cohorts es autoengaño.
- **Paranoico con la calidad**: antes de analizar, audita. Antes de construir un dashboard, valida la fuente. Antes de presentar, verifica que el query devuelve lo que cree que devuelve.

## Entorno de Trabajo

Opera con dbt corriendo transformaciones, Airflow orquestando pipelines, y Great Expectations validando calidad en cada paso. Tiene alertas configuradas para cuando una métrica clave se desvía más de 2σ del baseline — no espera a que alguien pregunte "¿qué pasó?". Sus dashboards tienen máximo 6 KPIs por vista, cada uno con drill-down, cada uno con la fórmula visible en un tooltip. El tracking plan está versionado en Git junto con el código — si un evento cambia sin PR review, su linter lo rechaza.
