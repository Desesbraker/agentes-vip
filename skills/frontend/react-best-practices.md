# @react-best-practices

## OBJETIVO

Mejorar rendimiento y estabilidad de interfaces React y Next.js atacando primero los cuellos de botella con mayor impacto.

## USAR CUANDO

Hay lentitud de render, waterfalls de datos, bundles grandes, hidratación costosa o interacción degradada en React o Next.js.

## NO USAR CUANDO

El problema principal es modelado de componentes, tipos o diseño visual. En esos casos usar la skill específica y volver aquí para performance.

## INSTRUCCIONES

1. Priorizar por impacto: eliminar waterfalls, reducir bundle y luego optimizar trabajo en servidor o hidratación.
2. Resolver fetches independientes en paralelo, usar Suspense donde tenga sentido y evitar cadenas de await innecesarias.
3. Reducir JavaScript enviado al cliente con imports directos, carga diferida de módulos pesados y postergación de terceros no críticos.
4. Minimizar datos y cómputo en cliente; definir estrategia explícita de cache y revisar si el costo viene de render, datos o librerías.

## FORMATO DE SALIDA

- Bottleneck principal
- Evidencia o síntoma
- Cambio prioritario
- Impacto esperado
- Riesgo o medición sugerida

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de performance frontend.
- Ver `./_templates.md` para el template de diagnóstico performance.
- Ver `./resources/performance-playbook.md` para waterfalls, bundle, hydration, medición y orden correcto de ataque.

## ANTI-PATRON

Barrel imports indiscriminados, bundle monolítico, fetch sin estrategia de cache o microoptimizar renders antes de resolver waterfalls evidentes.
