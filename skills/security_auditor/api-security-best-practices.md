# @api-security-best-practices

## OBJETIVO

Diseñar o auditar APIs seguras con controles claros sobre autenticacion, autorizacion, validacion, rate limiting y exposicion de datos. La salida debe servir para hardening inmediato o para revisar una implementacion existente.

## USAR CUANDO

- Se esta construyendo o auditando una API REST, GraphQL o WebSocket.
- Hace falta revisar auth, validacion, headers, CORS o abuso por volumen.
- Se requiere un checklist de hardening previo a produccion.

## NO USAR CUANDO

- El foco es solo UX de autenticacion en cliente; usar frontend-security-coder.
- La tarea es un assessment integral multi-capa con priorizacion completa; usar security-auditor.
- No existe definicion de endpoints, actores o datos expuestos.

## INSTRUCCIONES

1. Inventariar endpoints, actores, datos sensibles, metodos de autenticacion y superficies de abuso.
2. Revisar autenticacion y autorizacion server-side, manejo de secrets, expiracion y rotacion de tokens o llaves.
3. Evaluar validacion de input, consultas parametrizadas, rate limiting, CORS, manejo de errores y OWASP API Top 10.
4. Entregar gaps, severidad y hardening minimo con cambios concretos por endpoint o capa.

## FORMATO DE SALIDA

- Resumen de la API evaluada y su superficie de riesgo.
- Hallazgos por endpoint o control transversal.
- Checklist de hardening recomendado.
- Riesgos de abuso, fuga de datos o elevacion de privilegios.
- Validacion sugerida despues del fix.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./auth-implementation-patterns.md

## ANTI-PATRON

- Secretos hardcodeados o sin rotacion.
- Authorization checks solo en UI.
- Responses demasiado amplias o con datos innecesarios.
- Errores verbosos en produccion.
