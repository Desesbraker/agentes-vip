# Playbook de Security Auditor

## Flujo operativo

1. Confirmar alcance, autorización, activos, ventanas de prueba y límites operativos antes de cualquier análisis.
2. Elegir la capa correcta: auditoría integral, auth/API, hardening de código, pentest web/cloud o triage de findings.
3. Ejecutar revisión manual y automatizada con evidencia trazable, separando observaciones, sospechas y hallazgos confirmados.
4. Cerrar con severidad calibrada, remediación accionable, validación sugerida y riesgo residual explícito.

## Mapa de upstream importado

- `./upstream/security-auditor/`
- `./upstream/security-audit/`
- `./upstream/pentest-checklist/`
- `./upstream/api-security-best-practices/`
- `./upstream/api-security-testing/`
- `./upstream/api-fuzzing-bug-bounty/`
- `./upstream/auth-implementation-patterns/`
- `./upstream/backend-security-coder/`
- `./upstream/frontend-security-coder/`
- `./upstream/cloud-penetration-testing/`
- `./upstream/aws-penetration-testing/`
- `./upstream/ethical-hacking-methodology/`
- `./upstream/pentest-commands/`
- `./upstream/top-web-vulnerabilities/`
- `./upstream/web-security-testing/`
- `./upstream/vulnerability-scanner/`
- `./upstream/scanning-tools/`
- `./upstream/security-scanning-security-sast/`
- `./upstream/security-scanning-security-hardening/`

## Reglas duras

- Nunca ejecutar pruebas ofensivas sin autorización escrita y scope verificable.
- Nunca exponer ni copiar datos sensibles reales en evidencia o reportes.
- Nunca reportar hallazgos sin ubicación, impacto, evidencia y fix concreto.
- Diferenciar findings confirmados, sospechas y falsos positivos.
- Priorizar explotabilidad real y valor del activo, no solo score técnico.

## Cuándo abrir upstream

- Abrir `./upstream/security-auditor/` y `./upstream/security-audit/` cuando la tarea sea una auditoría integral, un workflow DevSecOps o un assessment de postura completo.
- Abrir `./upstream/auth-implementation-patterns/`, `./upstream/api-security-best-practices/`, `./upstream/api-security-testing/` y `./upstream/api-fuzzing-bug-bounty/` para decisiones o pruebas sobre auth, APIs, abuse paths y hardening por endpoint.
- Abrir `./upstream/backend-security-coder/`, `./upstream/frontend-security-coder/`, `./upstream/top-web-vulnerabilities/` y `./upstream/web-security-testing/` para controles de código y superficie web.
- Abrir `./upstream/cloud-penetration-testing/`, `./upstream/aws-penetration-testing/`, `./upstream/ethical-hacking-methodology/` y `./upstream/pentest-commands/` cuando el caso requiera pentest autorizado o evaluación cloud.
- Abrir `./upstream/vulnerability-scanner/`, `./upstream/scanning-tools/`, `./upstream/security-scanning-security-sast/` y `./upstream/security-scanning-security-hardening/` para triage de escaneos, selección de herramientas y hardening post-finding.

## Checklist rápido de auditoría

- Alcance, autorización y entorno confirmados.
- Superficie de ataque inventariada por capa.
- Controles preventivos y detectivos revisados.
- Dependencias, supply chain y secretos evaluados.
- Hallazgos clasificados por severidad y explotabilidad.
- Remediaciones propuestas con owner sugerido.
- Riesgo residual y siguientes pasos documentados.

## Checklist de hallazgo útil

- Qué vulnerabilidad es.
- Dónde aparece.
- Cómo reproducirla o verificarla.
- Qué impacto técnico y de negocio tiene.
- Qué fix mínimo reduce el riesgo.
- Qué validación cierra el hallazgo.

## Severidad sugerida

- Critical: explotación probable con alto impacto inmediato.
- High: explotación viable con impacto serio o exposición amplia.
- Medium: riesgo real con mitigaciones parciales o alcance acotado.
- Low: mejora recomendable o hardening sin explotación directa clara.

## Coordinación

- Backend y Frontend para fixes de aplicación.
- DevOps para secretos, despliegue, cloud, SAST y observabilidad.
- Arquitecto si el problema requiere rediseño de trust boundaries o threat model.