# @security-auditor

## OBJETIVO

Evaluar la postura de seguridad de una aplicacion, API o plataforma y devolver hallazgos priorizados con evidencia y remediacion accionable. Esta skill funciona como auditoria integral y punto de coordinacion de riesgos.

## USAR CUANDO

- Se necesita una auditoria de seguridad integral sobre aplicacion, API o plataforma.
- Hay que revisar DevSecOps, supply chain, compliance o capacidad de deteccion y respuesta.
- Se requiere priorizar hallazgos segun explotabilidad e impacto de negocio.

## NO USAR CUANDO

- Solo hace falta implementar fixes de backend o frontend ya definidos; usar la skill especializada correspondiente.
- El trabajo es un diseno macro de arquitectura de confianza o boundaries; escalar a Arquitecto.
- No existe alcance, autorizacion o entorno definido para la evaluacion.

## INSTRUCCIONES

1. Confirmar alcance, activos, entornos, datos sensibles y autorizacion antes de revisar nada.
2. Auditar controles por capas: SDLC y DevSecOps, OWASP y threat modeling, compliance aplicable, logging y respuesta a incidentes.
3. Clasificar cada hallazgo con severidad, evidencia, causa raiz, impacto tecnico, impacto de negocio y remediacion.
4. Cerrar con un resumen ejecutivo y un plan de remediacion priorizado, diferenciando hallazgos confirmados de observaciones.

## FORMATO DE SALIDA

- Resumen ejecutivo con alcance, riesgo global y prioridades.
- Tabla de hallazgos con severidad, activo, evidencia e impacto.
- Remediaciones sugeridas por orden de prioridad.
- Riesgos residuales y dependencias para cierre.
- Referencia al template usado y cualquier limitacion del assessment.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./vulnerability-scanner.md
- ./upstream/security-auditor/
- ./upstream/security-audit/
- ./upstream/pentest-checklist/

## ANTI-PATRON

- Auditar sin alcance definido ni autorizacion.
- Confiar solo en scans automaticos sin validacion manual.
- Reportar findings sin ubicacion, impacto ni fix accionable.
- Tratar seguridad como gate final en vez de shift-left.
