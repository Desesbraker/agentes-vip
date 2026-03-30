# @typescript-expert

OBJETIVO: Mantener una base TypeScript segura y escalable en apps móviles o desktop con foco en contratos, rendimiento del compilador y DX.

USAR CUANDO: Hay que resolver errores de tipos, fijar estándares TypeScript o modelar dominio en apps React Native, Expo o tooling móvil asociado.

NO USAR CUANDO: El problema principal es arquitectura mobile, release o integración nativa. En esos casos usar la skill específica del stack.

INSTRUCCIONES:

1. Endurecer la base con strict mode, tipos explícitos y reglas que eviten regresiones silenciosas en navegación, datos y storage.
2. Modelar dominio con branded types, satisfies y const assertions antes de recurrir a casts amplios.
3. Resolver problemas de performance del tipado simplificando genéricos, intersecciones y configuraciones costosas del compilador.
4. Cerrar con criterios de module resolution, path mapping y riesgos reales de DX o build.

FORMATO DE SALIDA:

- Problema de tipos
- Causa raíz
- Cambio propuesto
- Riesgo o tradeoff
- Regla futura

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de arquitectura mobile.
- Ver `./_templates.md` para arquitectura de app.

ANTI-PATRÓN: Dejar implicit any, abusar de type assertions, crear genéricos circulares o tratar path mapping como arquitectura real del sistema.
