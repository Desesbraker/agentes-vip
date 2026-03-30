# @backend-dev-guidelines

OBJETIVO: Implementar features backend en Node.js y TypeScript con separación de capas, validación fuerte y código mantenible.

USAR CUANDO: Hay que construir o modificar endpoints, servicios, integraciones o lógica de negocio en stacks backend Node.js.

NO USAR CUANDO: La tarea principal es definir el estilo de API, diseñar DB o elegir framework Python. En esos casos activar la skill específica primero.

INSTRUCCIONES:

1. Mantener una separación clara entre routes, controllers, services, repositories y acceso a infraestructura.
2. Validar toda entrada externa con schemas explícitos, centralizar config y dependencias, y evitar que la capa HTTP decida reglas de negocio.
3. Encapsular acceso a DB y servicios externos en capas dedicadas para que testear y reemplazar dependencias sea trivial.
4. Entregar siempre con tests del path crítico, manejo de errores estructurado y observabilidad mínima para producción.

FORMATO DE SALIDA:

- Feature o endpoint
- Capas afectadas
- Validaciones y auth
- Tests mínimos
- Riesgos técnicos

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de implementación backend.
- Ver `./_templates.md` para el plan de implementación backend.
- Ver `./resources/backend-nodejs-playbook.md` para arquitectura de capas, validación, observabilidad y testing en Node.js.
- Ver `./upstream/backend-dev-guidelines/SKILL.md` para la doctrina upstream completa.
- Ver `./upstream/backend-dev-guidelines/resources/` para arquitectura, errores, validación, observabilidad, repositorios y testing sin compresión.

ANTI-PATRÓN: Poner lógica en routes o controllers, acceder a ORM desde capas incorrectas, leer secrets directo desde process.env o entregar código sin tests y validación.
