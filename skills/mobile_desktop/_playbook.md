# Playbook: Mobile & Desktop Core

## Objetivo

Dar una base operativa común para decidir framework, arquitectura, offline-first, release, compliance de stores y apps desktop con bindings nativos.

## Flujo recomendado

1. Bloquear plataformas objetivo, requerimientos offline, integraciones nativas, rendimiento y restricciones de distribución.
2. Elegir stack por contexto: React Native, Flutter, Swift nativo, Expo o Tauri/Rust.
3. Definir arquitectura, estado, almacenamiento y estrategia de sincronización antes de abrir features grandes.
4. Cerrar con tests en dispositivo real, accesibilidad, release plan y riesgos de store compliance o desktop packaging.

## Reglas duras

- No entregar app sin estrategia offline o manejo explícito de no conectividad.
- No asumir que Expo Go cubre casos con código nativo custom.
- No desplegar sin release channels, monitoreo y rollback razonable.
- No publicar listing sin metadatos, visuales y compliance revisados.
- No exponer secretos ni lógica sensible en cliente.

## Checklists rápidos

### Arquitectura mobile

- Plataformas objetivo definidas
- Framework y razones documentadas
- Estado y almacenamiento elegidos
- Estrategia offline definida
- Integraciones nativas identificadas

### Release y distribución

- Versionado actualizado
- Variables de entorno listas
- Build validada en dispositivo real
- Canal o store target definido
- Monitoreo y rollback definidos

### Store compliance

- Metadata revisada
- Screenshots y preview listos
- Privacidad y permisos documentados
- Guidelines de plataforma revisadas
- Riesgos de rechazo identificados