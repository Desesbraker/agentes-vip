# @prompt-engineering

## OBJETIVO

Diseñar y versionar prompts base de sistema que sean claros, testeables y compatibles con el flujo mayor donde viven. La skill busca obediencia a formato, grounding y trazabilidad de cambios.

## USAR CUANDO

- Hay que redactar o reestructurar prompts base para un producto IA.
- Se requiere versionado, pruebas adversariales o control de formato.
- El sistema necesita separar instrucciones permanentes de variables dinamicas.

## NO USAR CUANDO

- El problema principal es contexto, memoria o retrieval; usar context-engineering o rag-engineer.
- El prompt ya esta desplegado y se busca optimizacion medible before and after; escalar a AgentOps.
- No existe objetivo, input o criterio de exito del prompt.

## INSTRUCCIONES

1. Bloquear tarea, inputs, restricciones, tono, formato de salida y errores prohibidos.
2. Estructurar el prompt por capas claras y separar instrucciones permanentes de variables.
3. Probar con casos normales, ambiguos y adversariales, versionando cambios con hipotesis y resultado.
4. Validar la interaccion del prompt con retrieval, tools y memoria si forma parte de un sistema mayor.

## FORMATO DE SALIDA

- Objetivo del prompt.
- Estructura propuesta por capas.
- Riesgos de ambiguedad o alucinacion.
- Plan de pruebas y versionado.
- Cambios siguientes sugeridos.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./context-engineering.md

## ANTI-PATRON

- Crear prompts largos sin estructura.
- Mezclar reglas con datos dinamicos.
- Iterar wording sin hipotesis ni tests.
- Usar ejemplos contradictorios.
