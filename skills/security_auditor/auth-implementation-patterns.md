# @auth-implementation-patterns

## OBJETIVO

Definir o auditar patrones de autenticacion y autorizacion para que el sistema tenga enforcement server-side, ciclo de vida de credenciales y controles proporcionales al riesgo. La skill prioriza decisiones de diseño aplicables a implementacion.

## USAR CUANDO

- Hay que elegir entre sesiones, JWT, OIDC, OAuth con PKCE o passwordless.
- Se necesita revisar RBAC, ABAC, ReBAC o MFA.
- Existen dudas sobre expiracion, rotacion o almacenamiento de secrets.

## NO USAR CUANDO

- Solo se requiere hardening general de una API ya definida; usar api-security-best-practices.
- El trabajo es exclusivamente UX o integracion de pantalla de login en frontend.
- No hay claridad sobre usuarios, actores o recursos protegidos.

## INSTRUCCIONES

1. Identificar actores, recursos, criticidad y flujos de autenticacion o delegacion.
2. Seleccionar el patron adecuado de auth y el modelo de autorizacion segun riesgo, experiencia y trazabilidad.
3. Definir ciclo de vida de tokens, sesiones y secrets: emision, expiracion, rotacion, revocacion y almacenamiento.
4. Entregar el esquema recomendado con controles obligatorios, riesgos y validaciones de seguridad.

## FORMATO DE SALIDA

- Patron de autenticacion recomendado y por que.
- Modelo de autorizacion y reglas de enforcement.
- Politica de ciclo de vida de tokens o sesiones.
- Requisitos de secrets, MFA y logging.
- Riesgos si se omiten controles clave.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./api-security-best-practices.md

## ANTI-PATRON

- Auth solo client-side.
- Tokens sin expiracion o refresh sin rotacion.
- Secrets en codigo, logs o repositorios.
- Paneles admin sin MFA.
