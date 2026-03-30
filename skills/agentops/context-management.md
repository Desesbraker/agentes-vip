# @context-management

OBJETIVO: Auditar y optimizar el uso de ventana de contexto para reducir costo y latencia sin degradar calidad ni grounding.

USAR CUANDO: Hay que revisar prompts de sistema, historial, retrieval, memoria o tool outputs en agentes ya instrumentados.

NO USAR CUANDO: La tarea exige rediseñar la arquitectura base del sistema o del producto IA. En ese caso devolver a AI Engineer o Arquitecto.

INSTRUCCIONES:

1. Medir qué entra al contexto, cuánto pesa y qué función cumple cada bloque antes de recomendar compresión o recorte.
2. Detectar desperdicio real: duplicados, historial irrelevante, retrieval redundante, outputs enormes o memoria persistente sin valor actual.
3. Proponer estrategia por bloque: recorte, resumen, routing selectivo, compresión estructurada o reordenamiento con impacto esperado en costo, latencia y calidad.
4. Validar con probes funcionales y before/after comparable; si baja tokens pero empeora decisiones, la optimización no se aprueba.

FORMATO DE SALIDA:

- Bloques de contexto auditados
- Tokens o peso por bloque
- Cambio recomendado
- Impacto esperado
- Riesgo de pérdida de información

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de cambios aislados.
- Ver `./_templates.md` para experimento de prompt o contexto.

ANTI-PATRÓN: Recortar a ciegas, mezclar memoria con retrieval sin gobernanza o celebrar ahorro de tokens cuando el agente pierde información crítica.
