# @rust-pro

OBJETIVO: Construir apps desktop con Tauri o componentes nativos en Rust manteniendo seguridad de memoria, buen rendimiento y límites claros con el frontend.

USAR CUANDO: Hay que desarrollar una app desktop ligera con Tauri o una capa Rust para alto rendimiento, bindings o procesamiento local.

NO USAR CUANDO: El problema puede resolverse completamente en una app móvil o web sin necesidad de runtime nativo ni requisitos de performance específicos.

INSTRUCCIONES:

1. Confirmar primero por qué Rust o Tauri aportan valor real frente a alternativas más simples del stack.
2. Diseñar bien la frontera entre frontend y backend Rust, incluyendo comandos, estado, filesystem y permisos.
3. Mantener disciplina con ownership, errores, async y testing para que la app no dependa de unsafe innecesario.
4. Cerrar con packaging, observabilidad local y riesgos de compatibilidad por plataforma desktop.

FORMATO DE SALIDA:

- Objetivo desktop o nativo
- Razón para usar Rust o Tauri
- Frontera frontend/backend
- Tests y packaging
- Riesgo de compatibilidad

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de arquitectura y distribución.
- Ver `./_templates.md` para decisión de stack y plan de release.

ANTI-PATRÓN: Usar unsafe sin justificar, ignorar lifetimes y errores, acoplar en exceso frontend con backend Rust o entregar sin tests ni estrategia de packaging.
