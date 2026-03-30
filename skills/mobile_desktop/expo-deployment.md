# @expo-deployment

OBJETIVO: Desplegar apps Expo a producción con control de canales, OTA, monitoreo y rollback razonable.

USAR CUANDO: Hay que preparar un release Expo, configurar actualizaciones OTA o formalizar el proceso de distribución a producción.

NO USAR CUANDO: El trabajo aún está en fase de arquitectura o desarrollo local sin requisitos de distribución reales.

INSTRUCCIONES:

1. Validar pre-release: tests, versionado, variables de entorno, tamaño de bundle y estado de features críticas.
2. Definir la ruta de distribución correcta entre build de store, beta y canales OTA según riesgo del cambio.
3. Configurar rollout, rollback y observabilidad para detectar crashes, adopción y errores tras el release.
4. Documentar el plan de release de forma que cualquier miembro del equipo sepa qué se publica, dónde y cómo volver atrás.

FORMATO DE SALIDA:

- Tipo de release
- Canal o store target
- Checklist pre-release
- Monitoreo y rollback
- Riesgo principal

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de release y distribución.
- Ver `./_templates.md` para plan de release.

ANTI-PATRÓN: Publicar sin tests, usar OTA sin channels ni rollback o ignorar monitoreo posterior al deploy.
