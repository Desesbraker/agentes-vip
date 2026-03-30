# @support-automation

OBJETIVO: Diseñar macros, bots y automatizaciones que reduzcan carga operativa sin degradar precisión, resolución ni experiencia de soporte.

USAR CUANDO: Hay que automatizar clasificación, FAQ, routing, seguimiento o respuestas repetitivas bien entendidas.

NO USAR CUANDO: El caso requiere juicio alto, troubleshooting complejo o información todavía no validada. Ahí debe intervenir una persona.

INSTRUCCIONES:

1. Seleccionar solo casos repetitivos y bien entendidos para automatización, descartando escenarios donde el error tenga alto costo.
2. Definir trigger, datos requeridos, respuesta esperada, criterio de salida y condición de escalación a humano.
3. Validar bots y macros contra knowledge base, tono de marca y comportamiento esperado, coordinando con AI Engineer si se usa RAG o generación.
4. Cerrar con métricas de ahorro, resolución, error de clasificación y satisfacción para confirmar que la automatización realmente ayuda.

FORMATO DE SALIDA:

- Caso automatizable
- Trigger y datos requeridos
- Respuesta automática y escalación
- Métrica de éxito
- Riesgo de clasificación o mala resolución

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de automatización.
- Ver `./_templates.md` para el template de soporte automatizado.

ANTI-PATRÓN: Automatizar tickets complejos, dejar bots sin escape a humano o usar macros que reducen tiempo de respuesta pero empeoran resolución y satisfacción.
