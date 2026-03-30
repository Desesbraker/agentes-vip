# @cloud-penetration-testing

## OBJETIVO

Evaluar de forma autorizada la exposicion y los caminos de ataque en AWS, Azure o GCP para detectar configuraciones peligrosas, privilegios excesivos y riesgos de persistencia. La skill se centra en escenarios cloud y requiere disciplina operativa estricta.

## USAR CUANDO

- Existe autorizacion explicita para revisar infraestructura cloud.
- Hay que evaluar IAM, servicios expuestos, metadata, secretos o persistencia en nube.
- Se necesita una guia de assessment tecnico sobre AWS, Azure o GCP.

## NO USAR CUANDO

- No hay autorizacion escrita ni alcance delimitado.
- El objetivo es solo hardening preventivo o governance; usar security-auditor.
- La tarea exige acciones destructivas o acceso a datos de produccion real.

## INSTRUCCIONES

1. Confirmar cloud, cuentas o proyectos, scope, limites operativos y plan de limpieza posterior.
2. Enumerar identidades, permisos, servicios, secretos, artefactos publicos y configuraciones expuestas por proveedor.
3. Identificar vias de explotacion y persistencia factibles, diferenciando evidencia observada de hipotesis.
4. Entregar hallazgos con impacto, servicio afectado, remediacion y acciones de cleanup o containment.

## FORMATO DE SALIDA

- Alcance cloud evaluado.
- Hallazgos por proveedor y servicio.
- Riesgos de privilegio, exposicion o persistencia.
- Remediaciones y cleanup posterior.
- Limitaciones y evidencia observada.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./vulnerability-scanner.md
- ./upstream/cloud-penetration-testing/
- ./upstream/aws-penetration-testing/

## ANTI-PATRON

- Testear sin autorizacion escrita.
- Acceder a datos de produccion reales sin permiso.
- Ignorar trazas en CloudTrail o activity logs.
- No limpiar artefactos o persistencia dejada por la prueba.
