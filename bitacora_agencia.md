# Bitácora de Agencia

## Objetivo

Registrar bloqueos, errores no resueltos, gaps de skills, límites de herramientas y fallos recurrentes para convertirlos en mejoras concretas del sistema.

## Regla operativa

Registrar una entrada SIEMPRE que ocurra cualquiera de estos casos:

- un agente no puede completar una tarea por falta de skill, contexto o herramienta
- aparece un error que el agente no logra resolver de forma autónoma
- una tarea debe escalarse a otro agente o al Orquestador
- se detecta un patrón repetido que sugiere crear nueva skill, nuevo agente o nueva regla

## Plantilla de entrada

```markdown
### [AAAA-MM-DD] Incidente: [titulo breve]
- Agente: [nombre]
- Tarea: [resumen]
- Tipo: [bloqueo|error_no_resuelto|gap_skill|gap_agente|limitacion_externa|falta_input]
- Sintoma: [que fallo o que no se pudo hacer]
- Causa probable: [si se conoce]
- Impacto: [que quedo bloqueado o degradado]
- Escalado a: [orquestador|arquitecto|otro agente|nadie]
- Siguiente accion: [paso concreto]
- Requiere sistema nuevo: [si|no]
- Propuesta: [nueva skill|nuevo agente|nueva regla|mejor documentacion|mejor tooling|pendiente]
- Estado: [abierto|mitigado|resuelto|descartado]
```

## Registro activo

Pendiente de primeras entradas.

## Backlog de remediacion

## Revision del Arquitecto

### Criterio de priorizacion

- P0: bloquea entregas o afecta multiples agentes
- P1: se repite y degrada calidad, tiempo o precision
- P2: mejora preventiva con impacto claro pero no urgente

### Propuestas priorizadas

#### P0

Pendiente.

#### P1

Pendiente.

#### P2

Pendiente.

### Nuevas skills candidatas

Pendiente.

### Nuevos agentes candidatos

Pendiente.

### Reglas o playbooks a reforzar

Pendiente.

## Ritual de revision

- El Orquestador registra el bloqueo o error cuando afecta una entrega o una delegacion.
- El agente ejecutor registra detalles tecnicos si detecta la causa antes de escalar.
- El Arquitecto revisa patrones recurrentes y decide si la solucion es nueva skill, nuevo agente, ajuste de perfil o regla operativa.
- El Arquitecto mueve propuestas a P0, P1 o P2 y define owner de remediacion.
