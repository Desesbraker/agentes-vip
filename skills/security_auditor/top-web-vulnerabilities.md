# @top-web-vulnerabilities

## OBJETIVO

Usar un catalogo amplio de vulnerabilidades web para estructurar assessments, checklists o revisiones de superficie de ataque. La skill ayuda a no olvidar clases de fallo frecuentes ni controles base.

## USAR CUANDO

- Se necesita una checklist amplia para evaluar una aplicacion web.
- Hay que mapear findings contra OWASP y categorias de riesgo web.
- Se quiere cubrir negocio, API, cliente, configuracion y transporte en una sola pasada.

## NO USAR CUANDO

- Ya existen hallazgos concretos y solo falta priorizarlos; usar vulnerability-scanner o security-auditor.
- El trabajo es una implementacion puntual de hardening en backend o frontend.
- No hay informacion minima del stack y superficie de la aplicacion.

## INSTRUCCIONES

1. Identificar el stack, canales, auth, datos sensibles y tipo de aplicacion o API.
2. Recorrer las categorias relevantes de vulnerabilidad y mapearlas a la superficie real del sistema.
3. Marcar controles existentes, gaps probables y pruebas manuales necesarias, incluyendo business logic.
4. Entregar la checklist priorizada o los hallazgos agrupados por categoria y severidad.

## FORMATO DE SALIDA

- Cobertura del assessment por categoria.
- Hallazgos o riesgos probables por area.
- Headers y controles base requeridos.
- Pruebas manuales pendientes.
- Priorizacion para la siguiente iteracion.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./security-auditor.md
- ./upstream/top-web-vulnerabilities/
- ./upstream/web-security-testing/

## ANTI-PATRON

- Quedarse solo con scan automatizado.
- Entregar mitigaciones genericas sin adaptarlas al stack.
- Ignorar vulnerabilidades de logica de negocio.
