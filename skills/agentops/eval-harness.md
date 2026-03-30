# @eval-harness

OBJETIVO: Construir harnesses automatizados que conviertan evaluaciones de agentes en gates reproducibles para cambios de prompt, modelo, contexto o tools.

USAR CUANDO: Hay que automatizar una evaluación, versionar datasets o convertir un criterio de calidad en un hard gate antes de deploy.

NO USAR CUANDO: Solo hace falta una revisión manual rápida o todavía no se definieron métricas ni baseline. En ese caso volver a @agent-evaluation o @agent-metrics.

INSTRUCCIONES:

1. Diseñar el harness alrededor de tareas y riesgos reales: inputs, expected behaviors, scoring, herramientas disponibles y formato de salida.
2. Separar datasets por tipo de riesgo y versionarlos con metadata suficiente para comparar agentes, modelos, prompts o releases.
3. Automatizar ejecución y reporte con outputs parseables para que comparar corridas no dependa de trabajo manual.
4. Integrar el harness como hard gate en cambios relevantes y dejar claro qué condiciones bloquean ship, repiten prueba o autorizan release.

FORMATO DE SALIDA:

- Objetivo del harness
- Datasets y segmentación
- Métricas y scoring
- Hard gate
- Riesgos de cobertura

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de harness.
- Ver `./_templates.md` para baseline y reporte de evaluación.

ANTI-PATRÓN: Construir harnesses con datasets muertos, scores opacos, solo casos felices o resultados imposibles de comparar entre versiones.
