# @stripe-integration

OBJETIVO: Implementar cobros, suscripciones y billing con Stripe de forma segura, consistente y reconciliable con el sistema interno.

USAR CUANDO: Hay que añadir checkout, payment intents, setup intents, webhooks o un flujo de suscripción y facturación con Stripe.

NO USAR CUANDO: El problema principal es arquitectura general de pagos sin proveedor decidido. En ese caso resolver la estrategia antes de entrar en Stripe.

INSTRUCCIONES:

1. Elegir el flujo correcto según UX y control necesario: Checkout Session, Payment Intents, Setup Intents o Customer Portal.
2. Diseñar la integración alrededor de webhooks firmados, idempotencia y una máquina de estados interna alineada con Stripe.
3. Mapear productos, precios, suscripciones, invoices y metadata a la base propia sin hardcodear montos ni asumir estados felices.
4. Entregar con escenarios de test, eventos críticos, manejo de fallo y riesgos operativos claramente documentados.

FORMATO DE SALIDA:

- Flujo Stripe elegido
- Eventos webhook críticos
- Estados internos y metadata
- Casos de fallo y retry
- Plan de test

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de billing.
- Ver `./_templates.md` para el template de integración Stripe.
- Ver `./resources/stripe-billing-playbook.md` para flujos, webhooks críticos, máquina de estados y plan de testing.
- Ver `./upstream/stripe-integration/SKILL.md` para la guía upstream completa de integración Stripe.

ANTI-PATRÓN: Integrar sin webhooks, no verificar firma, hardcodear montos, omitir idempotencia o tocar raw card data desde el servidor sin razón y sin cumplimiento.
