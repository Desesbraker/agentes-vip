# @prompt-optimization

OBJETIVO: Mejorar prompts existentes con hipótesis medibles para ganar precisión, formato, costo o latencia sin perder comparabilidad.

USAR CUANDO: Existe un prompt en uso y hay que optimizarlo con baseline y before/after controlado.

NO USAR CUANDO: Todavía se está diseñando el producto IA o la arquitectura de contexto desde cero. Eso corresponde a AI Engineer.

INSTRUCCIONES:

1. Establecer baseline del prompt actual con tasa de éxito, errores típicos, longitud, costo y latencia antes de reescribir nada.
2. Detectar el problema dominante: ambigüedad, sobreinstrucción, formato deficiente, grounding pobre, exceso de contexto o mala interacción con tools y retrieval.
3. Probar cambios con hipótesis explícitas y aisladas, comparando versiones en el mismo set de pruebas.
4. Adoptar solo cambios que mejoren el balance correcto entre calidad, costo y velocidad y documentar rollback si el experimento falla.

FORMATO DE SALIDA:

- Prompt o flujo evaluado
- Hipótesis del cambio
- Métricas objetivo
- Resultado before/after
- Decisión final

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para reglas de experimento aislado.
- Ver `./_templates.md` para experimento de prompt o contexto.

ANTI-PATRÓN: Reescribir prompts enteros sin baseline, optimizar solo por longitud o mezclar cambios de prompt con modelo, contexto y retrieval en la misma prueba.
