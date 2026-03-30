# @frontend-security-coder

## OBJETIVO

Reducir riesgos client-side como XSS, clickjacking, almacenamiento inseguro y redirecciones abiertas mediante practicas concretas de frontend seguro. La skill aterriza controles verificables en interfaces y codigo de cliente.

## USAR CUANDO

- Se esta implementando o auditando frontend con manejo de contenido dinamico.
- Hay dudas sobre CSP, token storage, redirects o seguridad del DOM.
- Se necesita una revision de hardening del cliente antes de publicar.

## NO USAR CUANDO

- El problema principal esta en auth o autorizacion server-side; usar auth-implementation-patterns o backend-security-coder.
- Solo se requiere UX o accesibilidad sin componente de seguridad.
- Se necesita una auditoria integral de postura de seguridad.

## INSTRUCCIONES

1. Revisar fuentes de contenido dinamico, navegacion, auth client-side y superficie del DOM.
2. Verificar prevencion de XSS, politicas CSP, proteccion contra clickjacking y manejo seguro de redirects o storage.
3. Identificar flujos donde el cliente expone informacion o asume enforcement que deberia estar en servidor.
4. Entregar hallazgos con cambio recomendado y forma de validarlos en navegador y build real.

## FORMATO DE SALIDA

- Riesgos client-side detectados.
- Ubicacion o flujo afectado.
- Cambio recomendado en codigo o configuracion.
- Validacion sugerida en navegador.
- Dependencias con backend o auth server-side.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./auth-implementation-patterns.md

## ANTI-PATRON

- Renderizar user input con innerHTML.
- CSP con unsafe-inline o unsafe-eval sin justificacion fuerte.
- Guardar tokens sensibles en localStorage.
- Redirecciones abiertas sin validacion.
