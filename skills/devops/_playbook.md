# Playbook: DevOps

## Objetivo

Dar una base operativa común para contenedores, infraestructura, despliegues, observabilidad y respuesta a incidentes sin repetir la misma explicación en cada skill.

## Flujo recomendado

1. Bloquear stack, entorno objetivo, restricciones de seguridad, presupuesto y rollback antes de proponer tooling.
2. Separar el problema principal: build local, contenedorización, IaC, despliegue, observabilidad o incidente.
3. Elegir la mínima solución operable que pueda automatizarse, observarse y revertirse.
4. Cerrar con artefactos concretos, checklist de verificación y formato de salida parseable.

## Reglas duras

- No desplegar sin rollback documentado.
- No aprobar pipelines con secretos expuestos o privilegios innecesarios.
- No usar contenedores root en producción sin justificación excepcional.
- No aplicar cambios de infraestructura sin plan review cuando el entorno lo exige.
- No cerrar incidentes sin timeline, causa raíz y acciones de seguimiento.

## Checklists rápidos

### Pre-deploy de 8 puntos

- Code quality validada
- Build reproducible y artefacto generado
- Tests críticos aprobados
- Variables de entorno verificadas
- Secretos cargados en sistema seguro
- Backup o snapshot disponible cuando aplica
- Ruta de rollback documentada
- Monitoreo y persona responsable activos durante el despliegue

### Docker

- Multi-stage build
- Usuario non-root
- `.dockerignore` presente
- Health check definido
- Secretos fuera de la imagen

### Terraform

- Backend remoto y locking
- Plan revisado
- Variables validadas
- Drift revisado
- Security scan ejecutado

### Observabilidad

- SLI definido
- SLO y error budget definidos
- Alert routing configurado
- Runbook enlazado
- Dashboards mínimos listos

### Incidentes

- Severidad asignada
- Roles activos
- Mitigación o rollback decidido
- Comunicación iniciada
- Post-mortem agendado