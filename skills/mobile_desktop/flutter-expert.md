# @flutter-expert

OBJETIVO: Construir apps Flutter con una base clara de estado, rendering, multiplataforma e integraciones nativas.

USAR CUANDO: El proyecto usa Flutter o se está evaluando como stack para mobile, web o desktop desde un solo codebase.

NO USAR CUANDO: La tarea es nativa iOS o requiere decisiones específicas de React Native o Expo. En esos casos usar la skill adecuada.

INSTRUCCIONES:

1. Definir primero plataformas objetivo, necesidades nativas y complejidad del dominio antes de fijar patrón de estado.
2. Elegir state management por tipo de aplicación y disciplina del equipo: Riverpod, Bloc o Provider cuando realmente baste.
3. Diseñar UI con foco en rendimiento, const constructors, keys bien ubicadas y separación entre widgets de presentación y lógica.
4. Resolver integraciones nativas con platform channels o FFI solo donde aporten valor real y acompañarlo con testing razonable.

FORMATO DE SALIDA:

- Objetivo de la app Flutter
- Patrón de estado recomendado
- Estrategia UI y performance
- Integraciones nativas previstas
- Tests y riesgos

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de arquitectura mobile.
- Ver `./_templates.md` para arquitectura de app y plan de release.

ANTI-PATRÓN: Ignorar const constructors, mezclar varios state management sin criterio, omitir golden o widget tests cuando aportan o trabajar sin null safety.
