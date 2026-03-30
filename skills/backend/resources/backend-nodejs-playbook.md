# Backend y Node.js Playbook

## Cuándo abrir este recurso

- Implementar servicios Node.js/TypeScript con tráfico real
- Definir arquitectura backend mantenible
- Resolver middleware, errores, auth, observabilidad o testing
- Traducir `@backend-dev-guidelines` o `@nodejs-best-practices` a decisiones concretas

## Flujo operativo

1. Confirmar contexto: runtime, tipo de carga, latencia esperada, consumidores, despliegue, auth, SLAs.
2. Elegir framework según contexto real, no por costumbre.
3. Bloquear arquitectura: rutas, servicios, repositorios, infraestructura y límites entre capas.
4. Cerrar validación, errores, config, observabilidad y tests antes de considerar terminada la implementación.

## Selección de framework

| Contexto | Recomendación | Motivo |
|---|---|---|
| APIs CRUD y equipo familiar con Express | Express | Ecosistema amplio y curva conocida |
| Throughput alto, tipado fuerte, plugins, validación rápida | Fastify | Mejor rendimiento y contrato más rígido |
| Edge, runtimes ligeros, serverless o workers | Hono | Menor peso y mejor ajuste al edge |
| Monorepo Next.js con pocas necesidades backend separadas | Route Handlers / API Routes | Menor sobrecarga operacional |

## Doctrina de arquitectura

### Capas mínimas

- `routes` o `routers`: HTTP y wiring
- `controllers` o handlers: traducción de request/response
- `services`: reglas de negocio
- `repositories` o data access: consultas y persistencia
- `infrastructure`: SDKs, mail, colas, storage, config, observabilidad

### Reglas duras

- No poner reglas de negocio en rutas o controllers.
- No acceder al ORM directo desde handlers si el dominio ya creció.
- No mezclar validación HTTP con lógica de negocio reutilizable.
- No acoplar el modelo de API al esquema interno de DB sin decisión explícita.

## Validación y contratos

- Validar toda entrada externa.
- Estandarizar payloads de error.
- Incluir `request_id` o correlación equivalente.
- Definir idempotencia cuando haya mutaciones sensibles.

### Formato de error sugerido

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User not found",
    "details": {},
    "request_id": "req_123"
  }
}
```

## Configuración y secretos

- Cargar config desde entorno o secret manager.
- Validar config al boot.
- Separar variables requeridas de opcionales.
- Nunca leer secrets dispersos por el código si existe módulo de config central.

## Concurrencia y async

- Paralelizar solo trabajo independiente.
- No bloquear event loop con CPU-bound.
- Mover CPU intenso a colas, workers o procesos dedicados.
- Definir timeouts, retries y circuit breakers para llamadas externas críticas.

## Base de datos desde Node

- Usar connection pooling explícito.
- Manejar shutdown graceful del pool.
- En operaciones multi-escritura, usar transacciones.
- Revisar N+1 y exceso de includes antes de culpar al motor.

### Checklist de data access

- [ ] Índices alineados a queries reales
- [ ] Transacciones donde el dominio las necesita
- [ ] Límites de concurrencia razonables
- [ ] Queries instrumentadas o trazables
- [ ] Riesgo de N+1 revisado

## Observabilidad y operación

- Structured logging desde el inicio.
- Métricas por latencia, errores y throughput.
- Trazas en llamadas a DB y servicios externos si el sistema ya tiene complejidad suficiente.
- Health checks y graceful shutdown como parte del baseline.

## Testing mínimo

- Unit tests sobre servicios con lógica real.
- Integration tests sobre rutas y persistencia crítica.
- Tests de auth y permisos.
- Test de caso feliz y al menos un fallo importante por endpoint crítico.

## Handoff esperado

- Arquitectura elegida y motivo
- Framework y runtime elegidos
- Contratos y validaciones
- Riesgos operativos
- Test plan mínimo

## Quality gate

- [ ] Lógica fuera de controllers
- [ ] Input validado
- [ ] Errores estandarizados
- [ ] Config centralizada
- [ ] Logging y métricas definidos
- [ ] Tests mínimos escritos
- [ ] Shutdown y pooling considerados