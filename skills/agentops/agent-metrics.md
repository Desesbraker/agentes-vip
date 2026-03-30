# @agent-metrics

OBJETIVO: Definir métricas accionables para agentes IA que permitan detectar mejora, degradación y riesgos operativos con evidencia comparable.

USAR CUANDO: Hay que decidir qué medir en un agente, formalizar fórmulas o traducir dashboards a criterios de decisión y alertas.

NO USAR CUANDO: La tarea principal es ejecutar una evaluación completa o construir el harness. En esos casos usar @agent-evaluation o @eval-harness.

INSTRUCCIONES:

1. Elegir un set corto de métricas que realmente gobierne decisiones: calidad, costo, latencia, formato, tool success o escalación humana según el sistema.
2. Definir cada métrica con fórmula, unidad, ventana temporal, fuente de datos y umbral de acción para evitar dashboards decorativos.
3. Separar métricas de calidad, negocio y operación y explicar qué palanca mueve cada una y qué evento dispara investigación, rollback o deploy.
4. Leer siempre los números en contexto y contra baseline; un ahorro de costo que destruye factuality no cuenta como mejora.

FORMATO DE SALIDA:

- Métrica
- Fórmula y unidad
- Fuente de datos
- Umbral o target
- Acción asociada

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de baseline.
- Ver `./_templates.md` para el template de definición de métrica.

ANTI-PATRÓN: Definir métricas sin fórmula, perseguir vanity metrics, usar promedios que ocultan fallos críticos o comparar versiones sin controlar la mezcla de tareas.
