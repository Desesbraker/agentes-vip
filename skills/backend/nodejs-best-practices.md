# @nodejs-best-practices

OBJETIVO: Tomar buenas decisiones de arquitectura Node.js según runtime, carga, equipo y restricciones operativas.

USAR CUANDO: Hay que elegir framework, organizar capas, resolver concurrencia o fijar estándares Node.js para un servicio nuevo o existente.

NO USAR CUANDO: La tarea ya está completamente centrada en una implementación concreta de feature. En ese caso usar @backend-dev-guidelines.

INSTRUCCIONES:

1. Elegir framework y runtime por contexto: edge, serverless, throughput, ecosistema del equipo y complejidad del dominio.
2. Mantener separación entre controllers, services, repositories y tareas de infraestructura para evitar acoplamiento accidental.
3. Diseñar concurrencia y async con intención: paralelizar lo independiente, aislar CPU-bound y manejar timeouts, retries y backpressure.
4. Cerrar con criterios de seguridad, configuración y observabilidad que permitan operar el servicio en producción.

FORMATO DE SALIDA:

- Contexto técnico
- Framework o runtime recomendado
- Patrón de capas
- Riesgos de concurrencia o seguridad
- Regla operativa clave

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para el flujo común backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/backend-nodejs-playbook.md` para selección de framework, concurrencia, pooling, shutdown y observabilidad.
- Ver `./upstream/nodejs-backend-patterns/SKILL.md` para la guía upstream de patrones Node.js.
- Ver `./upstream/nodejs-backend-patterns/resources/implementation-playbook.md` para el playbook detallado de implementación.

ANTI-PATRÓN: Elegir Express para edge por costumbre, usar métodos bloqueantes en producción, meter lógica en controllers o hardcodear secrets y config sensible.
