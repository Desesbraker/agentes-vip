# @planificacion-concisa

## OBJETIVO

Convertir una solicitud nueva en un plan corto, accionable y validable sin sobrecargar al usuario con preguntas o detalle innecesario. La skill sirve para arrancar ejecucion con claridad minima suficiente.

## USAR CUANDO

- Entra una tarea nueva y el contexto ya permite planear rapido.
- Solo hay 1 o 2 bloqueos reales que deben preguntarse antes de actuar.
- Se necesita scope in or out, pasos atomicos y validacion minima.

## NO USAR CUANDO

- La solicitud sigue ambigua y requiere exploracion; usar brainstorming.
- La tarea ya esta en ejecucion y toca coordinar varios agentes; usar workflow-automation.
- Faltan demasiados inputs criticos para producir un plan honesto.

## INSTRUCCIONES

1. Escanear contexto y formular solo las preguntas bloqueantes imprescindibles.
2. Generar approach, alcance in or out, action items verb-first y validacion minima.
3. Descomponer pasos no atomicos hasta que el plan sea ejecutable.
4. Cerrar con open questions limitadas y siguiente accion clara.

## FORMATO DE SALIDA

- Approach breve.
- Scope in y out.
- Action items atomicos.
- Validacion minima.
- Open questions restantes.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./brainstorming.md
- ./upstream/concise-planning/
- ./upstream/planning-with-files/

## ANTI-PATRON

- Planificar sin contexto.
- Hacer demasiadas preguntas.
- Dejar pasos no atomicos o sin validacion.
