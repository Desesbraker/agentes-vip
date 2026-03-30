# @customer-support

OBJETIVO: Gestionar soporte, triage y escalación con contexto suficiente para resolver, aprender y no transferir ambigüedad al siguiente equipo.

USAR CUANDO: Hay que diseñar o ejecutar flujos de soporte reactivo, clasificar tickets o escalar casos técnicos con orden.

NO USAR CUANDO: El problema principal es debugging profundo, desarrollo o decisión de roadmap. En ese caso soporte documenta y escala, no reemplaza al especialista.

INSTRUCCIONES:

1. Diseñar intake y triage con categorías, severidad, SLA y rutas de escalación para que cada ticket entre al flujo correcto.
2. Responder usando knowledge base y contexto específico del caso, evitando promesas técnicas cuando todavía falta verificación.
3. Registrar pasos, resolución, bloqueos y patrones repetidos con suficiente detalle para reproducir el caso o mejorar playbooks.
4. Cerrar solo cuando la resolución o el siguiente paso estén claros y documentados para el equipo o responsable correspondiente.

FORMATO DE SALIDA:

- Categoría, severidad y SLA
- Contexto del caso
- Resolución o siguiente paso
- Escalación requerida y motivo
- Riesgo de recurrencia o documentación faltante

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de triage y reglas duras.
- Ver `./_templates.md` para el template de soporte o escalación.

ANTI-PATRÓN: Cerrar por velocidad, escalar sin contexto suficiente o responder con macros genéricas que no resuelven el problema real del caso.
