# @analytics-tracking

OBJETIVO: Diseñar o auditar tracking confiable para medir impacto SEO y conversiones sin inflar eventos ni trabajar con datos rotos.

USAR CUANDO: Hay que revisar GA4, GTM, dataLayer, eventos o conversiones para saber si las decisiones SEO están apoyadas por medición útil.

NO USAR CUANDO: El problema principal es SEO editorial o técnico sin dependencia de tracking. En ese caso no forzar un frente de analytics innecesario.

INSTRUCCIONES:

1. Evaluar alineación entre decisiones, eventos, precisión, calidad de conversiones, atribución y gobernanza antes de declarar el sistema listo.
2. Definir eventos y conversiones por intención y valor real, no por acciones triviales o vanity metrics.
3. Revisar naming, dataLayer, UTMs, consentimiento y validación cross-browser para asegurar que el dato sea utilizable.
4. Cerrar con Measurement Readiness Index, riesgos principales y acción priorizada antes de seguir usando el dato para decisiones de SEO.

FORMATO DE SALIDA:

- Measurement Readiness Index
- Eventos y conversiones críticas
- Riesgo de data quality
- Limitación o gap de gobernanza
- Siguiente acción

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de schema y tracking.
- Ver `./_templates.md` para revisión de tracking.

ANTI-PATRÓN: Trackear por si acaso, inflar conversiones, meter PII en eventos o tomar decisiones con datos no validados entre navegador, tag manager y analytics.
