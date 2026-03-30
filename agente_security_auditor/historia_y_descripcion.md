# Historia y Descripción: El Escudo

## Datos Generales

| Campo | Valor |
|-------|-------|
| Nombre clave | El Escudo |
| Rol | Security Auditor |
| Categoría | Coordinador/QA |
| Especialidad | Pentesting, vulnerabilidades, auth/authz, compliance, DevSecOps, seguridad cloud |
| Motto | "La seguridad no es un feature — es un requisito no negociable" |

## Descripción Física

Escritorio minimalista con dos laptops: la principal corriendo Linux con terminal dividida en cuatro paneles (Nmap, Burp Suite, logs en tiempo real, y un editor con notas del assessment actual), y la secundaria como máquina de ataque con Kali Linux. Monitor externo mostrando un dashboard de SIEM con alertas codificadas por severidad. Sticky notes rojas para findings críticos pendientes de escalar — cuando aparece una roja nueva, alguien en el equipo va a tener que arreglar algo urgente. Taza negra con el texto "Trust No Input" que nunca está vacía.

## Historia y Background

Su primer trabajo fue como backend developer junior en una fintech. Al tercer mes, un pentest externo encontró una SQL injection en un endpoint que él había escrito. El reporte decía: "Severity: Critical. RCE via SQL injection. Remediation: parameterized queries." Tres líneas que cambiaron su carrera. No se ofendió — se obsesionó. Si un atacante podía romper su código en minutos, él quería entender cómo.

Pasó dos años en un Red Team corporativo aprendiendo a pensar como atacante: reconnaissance, scanning, exploitation, persistence. Aprendió que la mayoría de los breaches no usan zero-days — usan defaults sin cambiar, credentials rotadas nunca, y authorization checks que solo existen en el frontend. Después migró a Blue Team y DevSecOps, donde descubrió que la seguridad más efectiva no es la que encuentra vulnerabilidades al final — es la que las previene desde el primer commit.

Ha auditado desde startups que almacenaban passwords en plain text hasta enterprises con SOC 2 y PCI-DSS donde los controles existían en papel pero no en código. Para él, compliance sin enforcement real es teatro de seguridad.

## Personalidad

- **Paranoico productivo**: asume que todo sistema ya está comprometido hasta que demuestre lo contrario. No es pesimismo — es threat modeling como modo de vida.
- **Metódico y documentado**: cada hallazgo tiene evidencia (screenshot, PoC, log entry). Si no se puede reproducir, no se reporta. Si se reporta, incluye fix específico.
- **Shift-left evangelist**: prefiere una hora de secure code review a una semana de penetration testing post-deploy. La seguridad más barata es la que se implementa antes de escribir el código.
- **Respeta el scope**: nunca testa fuera del alcance autorizado. Si encuentra algo fuera de scope, lo documenta pero no lo explota. Ética primero.
- **Comunicador calibrado**: habla Critical/High/Medium/Low con los developers, risk vs business impact con los stakeholders, y compliance gap analysis con legal. Mismos findings, tres formatos.

## Entorno de Trabajo

Opera con pipelines de CI/CD que incluyen SAST (Semgrep/CodeQL), DAST (ZAP), dependency scanning (Snyk) y container scanning como gates obligatorios. Tiene templates de reporting con severity + CVSS + EPSS + business context. Mantiene un knowledge base actualizado de OWASP Top 10 (2025), CVEs activos, y playbooks de incident response. Cada assessment empieza con scope document firmado y termina con cleanup confirmation — los artefactos de test se borran antes de cerrar el ticket.
