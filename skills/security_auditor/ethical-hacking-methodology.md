# @ethical-hacking-methodology

## OBJETIVO

Estructurar pentests autorizados con una metodologia clara de reconocimiento, validacion, explotacion controlada y reporte. La prioridad es generar evidencia util sin cruzar limites eticos ni operativos.

## USAR CUANDO

- Se necesita un marco metodologico para pentesting autorizado.
- Hay que organizar fases, herramientas y reporting de una simulacion de ataque.
- El equipo necesita un flujo repetible y auditable para evaluaciones ofensivas.

## NO USAR CUANDO

- No existe permiso explicito o el scope es ambiguo.
- La tarea busca automatizar un scan puntual sin metodologia completa; usar vulnerability-scanner.
- El objetivo es remediacion de codigo, no pruebas ofensivas.

## INSTRUCCIONES

1. Delimitar objetivo, scope, restricciones, ventanas horarias y criterios de exito o stop.
2. Ejecutar reconocimiento, scanning y analisis de vulnerabilidades con trazabilidad suficiente.
3. Validar explotacion solo hasta obtener evidencia necesaria, evitando acciones destructivas o acceso no autorizado a datos reales.
4. Reportar resumen ejecutivo, hallazgos tecnicos, severidad, evidencia y remediacion con claridad.

## FORMATO DE SALIDA

- Scope y reglas de engagement.
- Metodologia seguida por fases.
- Hallazgos confirmados con evidencia.
- Riesgo y remediacion sugerida.
- Limitaciones, supuestos y cierre del ejercicio.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./cloud-penetration-testing.md
- ./upstream/ethical-hacking-methodology/
- ./upstream/pentest-checklist/
- ./upstream/pentest-commands/

## ANTI-PATRON

- Testear sin autorizacion.
- Trabajar fuera de scope.
- Usar exploits destructivos o exponer datos de cliente.
- Omitir el reporte final.
