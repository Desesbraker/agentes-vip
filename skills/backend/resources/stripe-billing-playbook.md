# Stripe Billing Playbook

## Cuándo abrir este recurso

- Implementar cobros, suscripciones o billing con Stripe
- Diseñar checkout, portal, webhooks y reconciliación con DB
- Validar escenarios de fallo e idempotencia

## Elegir flujo

| Necesidad | Flujo recomendado |
|---|---|
| Checkout rápido con menor superficie propia | Stripe Checkout |
| Pago controlado en UI propia | Payment Intents |
| Guardar método para cobro futuro | Setup Intents |
| Gestión self-service de suscripción | Billing Portal |

## Modelo interno mínimo

Persistir al menos:

- customer_id
- product_id o plan_id interno
- price_id
- subscription_id si aplica
- estado interno
- metadata necesaria para reconciliación

## Webhooks críticos

- `checkout.session.completed`
- `payment_intent.succeeded`
- `payment_intent.payment_failed`
- `invoice.paid`
- `invoice.payment_failed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`

## Reglas duras

- Verificar firma del webhook.
- Hacer handlers idempotentes.
- No confiar solo en la respuesta inmediata del checkout para sincronizar estado.
- No hardcodear montos, precios o monedas en lógica de negocio si existen en Stripe.

## Máquina de estados interna

Separar:

- estado Stripe
- estado de acceso o entitlement interno

Ejemplo:

| Stripe | Estado interno sugerido |
|---|---|
| active | access_granted |
| past_due | payment_at_risk |
| unpaid | suspended |
| canceled | canceled |
| incomplete | pending_payment |

## Casos de fallo obligatorios

- Evento duplicado
- Webhook fuera de orden
- Pago fallido
- Suscripción cancelada
- Cambio de price
- Portal de billing modifica el estado

## Testing mínimo

- Caso feliz de checkout
- Repetición del mismo webhook
- Firma inválida
- Pago fallido
- Upgrade/downgrade de plan
- Cancelación

## Variables y setup base

- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `STRIPE_PRICE_*` o mapping equivalente
- `APP_URL` o callback URLs

## Handoff esperado

- Flujo elegido y motivo
- Eventos críticos y handlers
- Metadata persistida
- Estado interno y reconciliación
- Plan de test y fallos cubiertos