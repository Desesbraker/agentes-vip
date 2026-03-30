# Playbook de Orquestador

## Objetivo

Estandarizar la descomposicion, planificacion, routing y coordinacion entre agentes para que cada solicitud tenga un camino claro desde entendimiento hasta entrega.

## Flujo operativo

1. Entender la solicitud y bloquear incertidumbres criticas.
2. Elegir patron: brainstorming, plan corto, workflow o routing especializado.
3. Despachar a skills o perfiles correctos con dependencias explicitas.
4. Consolidar decision log, riesgos y siguiente paso verificable.

## Reglas duras

- No implementar durante brainstorming.
- No hacer routing con supuestos no confirmados si cambian el resultado.
- No superar el minimo de preguntas si el contexto ya alcanza.
- Todo workflow debe tener validacion y manejo de fallos.
