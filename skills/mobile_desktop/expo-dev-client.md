# @expo-dev-client

OBJETIVO: Activar correctamente un Expo Dev Client cuando Expo Go ya no cubre las necesidades nativas del proyecto.

USAR CUANDO: Hay módulos nativos, targets Apple especiales, código custom o librerías que requieren build propio para desarrollo.

NO USAR CUANDO: Expo Go ya cubre el caso de uso y no existe necesidad real de capacidades nativas adicionales.

INSTRUCCIONES:

1. Confirmar primero qué dependencia o capability obliga a salir de Expo Go para no añadir complejidad innecesaria.
2. Configurar el perfil de desarrollo, credenciales y build pipeline de manera consistente con EAS y el equipo.
3. Validar el ciclo de desarrollo local o remoto con conexión al dev client y un plan claro para compartir builds internas.
4. Cerrar con reglas de versionado, credentials management y riesgos de mantenimiento del pipeline nativo.

FORMATO DE SALIDA:

- Motivo del dev client
- Configuración requerida
- Flujo local o remoto
- Riesgo de credenciales o versionado
- Validación mínima

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de release y distribución.
- Ver `./_templates.md` para plan de release.

ANTI-PATRÓN: Crear dev client cuando Expo Go basta, olvidar versionado y credentials management o abrir un pipeline nativo sin necesidad real.
