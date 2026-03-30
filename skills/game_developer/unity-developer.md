# @unity-developer

## OBJETIVO

Implementar juegos o sistemas jugables en Unity con C# mantenible, uso correcto de prefabs y datos desacoplados. La skill conecta arquitectura de proyecto, integracion de assets y validacion en build real.

## USAR CUANDO

- El proyecto corre en Unity.
- Hay que definir escenas, prefabs, ScriptableObjects, input o pipeline de assets.
- Se necesita validar integracion end-to-end en Unity LTS.

## NO USAR CUANDO

- El proyecto corre en Godot; usar godot-developer.
- La tarea es puramente de diseno o de optimizacion sin foco en Unity.
- No estan claras la plataforma destino o las restricciones de render pipeline.

## INSTRUCCIONES

1. Confirmar version de Unity, plataforma, render pipeline, input y estrategia de escenas.
2. Implementar sistemas desacoplados con prefabs reutilizables, datos separados y arquitectura proporcional al juego.
3. Integrar assets, Addressables o pooling cuando el caso lo requiera, midiendo memoria y carga desde temprano.
4. Validar escenas, input, animacion, fisicas, UI y build real antes de crecer la complejidad.

## FORMATO DE SALIDA

- Decision tecnica de stack y arquitectura Unity.
- Sistemas implementados o por implementar.
- Riesgos de assets, memoria o integracion.
- Checklist de validacion del build.
- Siguiente iteracion recomendada.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./game-design.md

## ANTI-PATRON

- Crear Monobehaviours gigantes.
- Usar singletons para todo.
- Mantener prefabs sin convencion ni ownership.
- Dejar profiling de memoria y carga para el final.
