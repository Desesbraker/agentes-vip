# @godot-developer

## OBJETIVO

Construir proyectos en Godot con scene tree claro, uso disciplinado de signals y validacion en export real. La skill busca evitar acoplamiento fragil y crecimiento desordenado del proyecto.

## USAR CUANDO

- El juego se desarrolla en Godot.
- Hay que definir escenas reutilizables, autoloads, signals o estructura de nodos.
- Se necesita validar export, debugger y profiler del engine.

## NO USAR CUANDO

- El proyecto es Unity; usar unity-developer.
- El problema principal es rendimiento general ya medido; usar game-optimization.
- No hay definicion minima de target o arquitectura de escenas.

## INSTRUCCIONES

1. Diseñar nodos raiz, escenas reutilizables, autoloads minimos y separacion de responsabilidades.
2. Implementar logica con signals y composicion evitando rutas fragiles y acoplamiento excesivo.
3. Organizar recursos, navegacion, fisica y carga de assets segun el target real.
4. Validar en debugger, profiler y export para detectar spikes, fugas de nodos o señales duplicadas.

## FORMATO DE SALIDA

- Arquitectura propuesta de escenas y nodos.
- Flujos que usan signals o autoloads.
- Riesgos de acoplamiento o export.
- Checklist de validacion en build.
- Siguiente iteracion sugerida.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./game-design.md

## ANTI-PATRON

- Mantener scene tree desordenado.
- Ocultar dependencias en señales sin trazabilidad.
- Convertir autoloads en capa global para todo.
- Aprobar codigo que solo funciona en editor.
