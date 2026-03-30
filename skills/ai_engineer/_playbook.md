# Playbook de AI Engineer

## Objetivo

Estandarizar el diseno e implementacion de productos de IA aplicada con foco en caso de uso, arquitectura minima viable, evaluacion, observabilidad y costo.

## Flujo operativo

1. Confirmar caso de uso, inputs, outputs y restricciones.
2. Elegir patron de producto y componentes minimos.
3. Implementar ruta feliz medible con guardrails y observabilidad.
4. Evaluar calidad, latencia, costo y riesgos antes de escalar.

## Reglas duras

- No elegir stack antes de definir el problema.
- No llamar listo para produccion a un flujo sin evaluacion ni trazas.
- No mezclar prompt, retrieval y tools sin contratos claros.
- Cada propuesta debe explicitar costo, latencia y riesgo principal.

## Checklist rapido

- Caso de uso bloqueado.
- Patron arquitectonico elegido y justificado.
- Baseline de calidad, costo y latencia.
- Guardrails y fallback definidos.
- Siguiente evaluacion clara.
