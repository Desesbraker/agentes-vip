# @react-native-architecture

OBJETIVO: Diseñar o migrar apps React Native y Expo con una arquitectura moderna, estable y preparada para crecimiento.

USAR CUANDO: Hay que construir una app nueva en React Native o revisar una base existente para modernizar navegación, estado, New Architecture o estrategia offline.

NO USAR CUANDO: La tarea solo pide endpoints Expo Router del lado server o configuración de distribución EAS. En esos casos usar la skill específica de Expo.

INSTRUCCIONES:

1. Confirmar si la app debe operar con New Architecture, Expo Router, deep linking y paquetes nativos antes de definir estructura interna.
2. Separar navegación, estado local, server state y almacenamiento para evitar una app monolítica difícil de evolucionar.
3. Diseñar offline-first con persistencia local, cola de sync y resolución explícita de conflictos cuando el dominio lo necesite.
4. Cerrar con type safety en navegación, device testing y riesgos de migración si existe legado.

FORMATO DE SALIDA:

- Objetivo de la app o migración
- Arquitectura RN o Expo propuesta
- Estado, storage y sync
- Riesgos de New Architecture o native modules
- Validación mínima

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de arquitectura mobile.
- Ver `./_templates.md` para decisión de stack y arquitectura de app.

ANTI-PATRÓN: Quedarse en Old Architecture sin razón, usar AsyncStorage para cargas grandes, ignorar type safety en navegación o mezclar estado, red y storage sin frontera clara.
