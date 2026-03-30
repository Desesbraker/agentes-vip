# @mobile-developer

OBJETIVO: Diseñar y construir apps móviles o multiplataforma con una base sólida de arquitectura, rendimiento, offline-first y seguridad.

USAR CUANDO: Hay que decidir o implementar una app móvil cross-platform o nativa y todavía hace falta fijar stack, arquitectura o reglas base del proyecto.

NO USAR CUANDO: El framework ya está decidido y el trabajo es específico de Expo, Flutter, iOS nativo o desktop con Rust. En esos casos usar la skill correspondiente.

INSTRUCCIONES:

1. Elegir stack por plataformas objetivo, integraciones nativas, velocidad de entrega, talento disponible y exigencia de rendimiento.
2. Definir arquitectura, estado, almacenamiento y sincronización antes de abrir features grandes; offline-first debe ser decisión explícita, no parche tardío.
3. Optimizar para startup, frames, memoria, batería y listas grandes con profiling real en dispositivo.
4. Cerrar con seguridad, accesibilidad, tests en device real y plan de release o distribución.

FORMATO DE SALIDA:

- Plataformas objetivo
- Stack y arquitectura recomendados
- Estrategia offline y de estado
- Riesgos de rendimiento o seguridad
- Validación o test mínimo

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de arquitectura mobile.
- Ver `./_templates.md` para decisión de stack y arquitectura de app.

ANTI-PATRÓN: Empezar sin estrategia offline, no probar en dispositivos reales, ignorar guidelines de plataforma o asumir que un framework sirve igual para todos los casos.
