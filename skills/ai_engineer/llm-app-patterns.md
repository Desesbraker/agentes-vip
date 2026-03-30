# @llm-app-patterns

## OBJETIVO

Elegir el patron correcto de aplicacion LLM para un caso de uso concreto, equilibrando costo, latencia, control y complejidad. La skill evita sobrearquitectura temprana y patrones elegidos por moda.

## USAR CUANDO

- Hay que decidir entre chat, extraction, copiloto, RAG, tools, agentes o workflow hibrido.
- Existen varias arquitecturas posibles y se necesita compararlas.
- El equipo debe justificar por que un patron es el adecuado hoy.

## NO USAR CUANDO

- El patron ya esta elegido y toca implementarlo; usar ai-engineer o rag-engineer.
- Solo se necesita optimizar prompts de un flujo puntual.
- No existe caso de uso o criterio de exito definido.

## INSTRUCCIONES

1. Clasificar el producto segun la tarea real y el nivel de accion o conocimiento requerido.
2. Comparar la arquitectura minima viable de cada patron candidato.
3. Definir inputs, outputs, estado, fuentes de verdad, herramientas y fallbacks del patron elegido.
4. Documentar por que gana hoy y que señales forzarian una migracion futura.

## FORMATO DE SALIDA

- Patrones evaluados.
- Patron recomendado y justificacion.
- Contrato operativo del patron.
- Trade-offs de costo, latencia y control.
- Señales de futura migracion.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./ai-engineer.md

## ANTI-PATRON

- Usar agentes para tareas deterministas.
- Meter RAG donde basta un indice simple o datos embebidos.
- Elegir patron por moda sin analizar failure modes.
