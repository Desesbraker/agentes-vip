# Frontend Performance Playbook

## Cuándo abrir este recurso

- LCP alto, CLS alto, interacción lenta o bundle excesivo
- Waterfalls de datos
- Hidratación costosa
- Optimizar React o Next.js con evidencia

## Orden correcto de ataque

1. Eliminar waterfalls
2. Reducir JavaScript cliente
3. Revisar estrategia de caché y render
4. Optimizar rerenders y compute
5. Revisar terceros y assets pesados

## Quick reference

### Waterfalls

- paralelizar fetches independientes
- usar Suspense cuando ayude
- evitar awaits secuenciales innecesarios

### Bundle

- imports directos
- dynamic import para módulos pesados
- mover lógica al servidor cuando sea posible
- diferir terceros no críticos

### Render/hydration

- reducir islands interactivas
- minimizar props enormes serializadas
- evitar hidratar árboles completos sin necesidad

## Qué medir

- LCP
- CLS
- tiempo de interacción
- peso JS inicial
- costo de terceros

## Checklist

- [ ] Bottleneck identificado con evidencia
- [ ] Cambio prioritario elegido
- [ ] Medición before/after definida
- [ ] Riesgo de regresión UX evaluado

## Entrega esperada

- Bottleneck principal
- Evidencia
- Cambio prioritario
- Impacto esperado
- Medición sugerida

## Anti-patrones

- microoptimizar renders antes de resolver waterfalls
- bundle monolítico
- culpar React sin revisar fetch, assets o terceros