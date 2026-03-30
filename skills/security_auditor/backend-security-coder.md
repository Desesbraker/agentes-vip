# @backend-security-coder

## OBJETIVO

Implementar o revisar backend seguro contra vulnerabilidades comunes de input handling, auth, acceso a datos y fugas de informacion. La entrega debe aterrizar fixes concretos en codigo o checklist de remediacion.

## USAR CUANDO

- Hay endpoints o servicios backend que necesitan hardening.
- Se sospechan inyecciones, SSRF, fugas de errores o controles server-side incompletos.
- Se requiere una guia concreta para escribir codigo backend mas seguro.

## NO USAR CUANDO

- El foco es el diseno global de auth; usar auth-implementation-patterns.
- El trabajo es una auditoria integral con compliance y threat modeling; usar security-auditor.
- Solo se necesita proteger el cliente o el DOM; usar frontend-security-coder.

## INSTRUCCIONES

1. Revisar entradas, sinks y superficies criticas: queries, comandos, requests salientes, sesiones, cookies y manejo de errores.
2. Verificar defensas de input, prepared statements, privilegios minimos, cifrado, CSRF, headers y chequeos server-side.
3. Identificar vulnerabilidades explotables y mapearlas a archivo, endpoint o componente afectado.
4. Entregar cambios recomendados con prioridad, validacion posterior y riesgos residuales.

## FORMATO DE SALIDA

- Resumen del backend evaluado y superficie sensible.
- Hallazgos con ubicacion tecnica y tipo de vulnerabilidad.
- Fix minimo recomendado por hallazgo.
- Checklist de validacion despues del cambio.
- Riesgos residuales o dependencias externas.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./api-security-best-practices.md

## ANTI-PATRON

- Concatenar strings en queries.
- Ejecutar eval o exec con input de usuario.
- Loggear secrets o detalles sensibles.
- Silenciar errores sin observabilidad.
