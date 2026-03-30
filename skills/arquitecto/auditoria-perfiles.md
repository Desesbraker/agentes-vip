# @auditoria-perfiles

## OBJETIVO

Auditar un perfil existente contra los principios P1-P8 y sus secciones obligatorias para detectar huecos de estructura, routing y entregables. La salida debe servir como plan de correccion verificable, no como opinion general.

## USAR CUANDO

- Hay que evaluar la calidad estructural de un perfil de agente.
- Se sospechan triggers ambiguos, outputs sin template o jargon no definido.
- Hace falta emitir score con evidencia y acciones correctivas.

## NO USAR CUANDO

- Se va a crear un perfil nuevo desde cero; usar construccion-agentes.
- Solo se requiere ajustar una skill puntual sin revisar el perfil completo.
- No se dispone del perfil o de los criterios de evaluacion base.

## INSTRUCCIONES

1. Evaluar el perfil contra P1-P8 usando evidencia concreta y ejemplos observables.
2. Inventariar las secciones obligatorias y marcar faltantes, overlaps o debilidades.
3. Listar outputs sin template, triggers faltantes, acronimos sin definir y anti-patrones detectados.
4. Entregar score final con plan de correccion priorizado y criterios de cierre.

## FORMATO DE SALIDA

- Resumen del perfil auditado.
- Evidencia por principio o seccion.
- Hallazgos prioritarios.
- Score final con justificacion.
- Plan de correccion.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./construccion-agentes.md

## ANTI-PATRON

- Auditar sin evidencia.
- Aprobar perfiles con huecos estructurales criticos.
- Emitir score sin criterio observable.
