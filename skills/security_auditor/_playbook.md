# Playbook de Security Auditor

## Objetivo

Estandarizar auditorias de seguridad para que cada entrega incluya alcance, evidencia, severidad, remediacion y limites operativos.

## Flujo operativo

1. Confirmar alcance, activos, entorno y autorizacion explicita.
2. Identificar la superficie: autenticacion, autorizacion, input handling, secrets, infraestructura, dependencias y observabilidad.
3. Ejecutar chequeos manuales y automatizados apropiados al stack.
4. Consolidar hallazgos con severidad, evidencia y remediacion accionable.
5. Entregar plan de correccion priorizado y riesgos residuales.

## Reglas duras

- Nunca ejecutar pruebas ofensivas sin autorizacion escrita.
- Nunca exponer datos sensibles reales en el reporte.
- No reportar findings sin ubicacion, impacto y fix concreto.
- Diferenciar hallazgos confirmados de sospechas o hipotesis.
- Priorizar riesgo explotable y valor de negocio, no solo CVSS.

## Checklist rapido de auditoria

- Alcance y entorno confirmados.
- Superficie de ataque inventariada.
- Controles preventivos revisados.
- Logs, alertas y trazabilidad revisados.
- Dependencias y supply chain evaluadas.
- Hallazgos clasificados por severidad y explotabilidad.
- Remediaciones propuestas con owner sugerido.
- Riesgo residual y siguientes pasos documentados.

## Checklist de hallazgo util

- Que vulnerabilidad es.
- Donde aparece.
- Como reproducirla o verificarla.
- Que impacto tecnico y de negocio tiene.
- Que fix minimo reduce el riesgo.
- Que validacion cierra el hallazgo.

## Severidad sugerida

- Critical: explotacion probable con alto impacto inmediato.
- High: explotacion viable con impacto serio o exposicion amplia.
- Medium: riesgo real con mitigaciones parciales o alcance acotado.
- Low: mejora recomendable o hardening sin explotacion directa clara.

## Coordinacion

- Backend y Frontend para fixes de aplicacion.
- DevOps para secretos, despliegue, cloud y observabilidad.
- Arquitecto si el problema requiere rediseño de boundaries o trust model.