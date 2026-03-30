# @analytics-tracking

## OBJETIVO

Diseñar o auditar tracking analytics que sirva para decisiones reales y no para acumular eventos cosméticos.

## USAR CUANDO

Hay que definir un tracking plan, revisar calidad de señal, corregir UTMs o alinear eventos y conversiones con decisiones de negocio.

## NO USAR CUANDO

La discusión es puramente de visualización o storytelling del dato ya disponible. Esta skill resuelve captura y calidad de señal.

## INSTRUCCIONES

1. Evaluar la calidad de la señal con un marco explícito, como Signal Quality Index, revisando alineación con decisiones, claridad del modelo de eventos, precisión, conversiones, atribución y governance.
2. Diseñar eventos como cambios de estado significativos, con naming consistente y propiedades mínimas que permitan responder preguntas de negocio sin recolectar ruido.
3. Definir conversiones, reglas de conteo y UTMs con semántica estable, documentando qué cuenta, cuándo cuenta y qué no debe inflarse.
4. Validar en tiempo real, detectar duplicados, revisar estados de consentimiento y cerrar con plan de remediación si la señal está rota.

## FORMATO DE SALIDA

- Decisión o pregunta de negocio
- Veredicto de calidad de señal
- Eventos y conversiones críticas
- Reglas de validación y governance
- Riesgo o remediación propuesta

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de métricas y señal.
- Ver `./_templates.md` para el template de plan de tracking.

## ANTI-PATRON

Trackear todo, definir eventos cosméticos, meter PII en properties, inflar conversiones o dejar UTMs inconsistentes entre equipos y canales.
