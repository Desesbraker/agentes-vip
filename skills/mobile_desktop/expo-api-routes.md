# @expo-api-routes

OBJETIVO: Crear endpoints server-side en Expo Router con límites claros de runtime, seguridad y despliegue.

USAR CUANDO: La app Expo necesita endpoints ligeros del lado servidor dentro del mismo proyecto o una capa backend simple ligada al producto móvil.

NO USAR CUANDO: La lógica backend exige un servicio más robusto, acceso a capacidades Node no soportadas o una arquitectura separada. En ese caso escalar a Backend.

INSTRUCCIONES:

1. Definir recurso, auth, validación y contrato HTTP antes de crear la ruta file-based.
2. Diseñar el endpoint respetando el runtime disponible: sin fs ni APIs nativas de Node, solo Web APIs compatibles con EAS Hosting o runtime equivalente.
3. Mantener secrets en entorno seguro, validar inputs y devolver status codes y errores consistentes.
4. Cerrar con estrategia de deploy, variables de entorno y límites explícitos de lo que esta capa sí y no debe hacer.

FORMATO DE SALIDA:

- Endpoint o recurso
- Método y contrato
- Auth y validación
- Runtime o limitaciones
- Plan de deploy

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de release y backend ligero.
- Ver `./_templates.md` para arquitectura de app y plan de release.

ANTI-PATRÓN: Exponer API keys en cliente, omitir validación, olvidar límites del runtime o meter lógica backend compleja donde ya conviene un servicio dedicado.
