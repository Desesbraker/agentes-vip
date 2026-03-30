# @schema-markup

OBJETIVO: Diseñar o validar structured data útil, elegible y mantenible para rich results sin caer en markup inflado o engañoso.

USAR CUANDO: Hay que implementar o revisar JSON-LD para artículos, productos, FAQs, breadcrumbs, negocio local u otros tipos elegibles.

NO USAR CUANDO: El contenido visible todavía no existe o no sustenta el schema. Primero resolver el contenido y la estructura real.

INSTRUCCIONES:

1. Calcular elegibilidad a partir de alineación contenido-schema, tipo de rich result, completitud, riesgo técnico y riesgo de spam.
2. Elegir el markup mínimo correcto según el contenido visible y la documentación vigente de Google.
3. Validar que los datos estructurados reflejen exactamente lo que el usuario puede ver y mantener a lo largo del tiempo.
4. Cerrar con Eligibility Index, riesgos de implementación y recomendación clara de implementar, corregir o no avanzar.

FORMATO DE SALIDA:

- Schema type
- Eligibility Index
- Data completeness
- Riesgo técnico o spam
- Recomendación

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de schema y tracking.
- Ver `./_templates.md` para revisión de schema.

ANTI-PATRÓN: Implementar schema que no refleja contenido visible, sobrecargar la página con markup innecesario, usar self-serving reviews o fabricar datos para intentar forzar rich results.
