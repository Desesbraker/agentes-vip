# @ab-test-setup

## OBJETIVO

Diseñar experimentos A/B válidos, con hipótesis verificable y reglas de decisión que eviten conclusiones falsas.

## USAR CUANDO

Hay que validar una variante de producto, landing, formulario, pricing o messaging antes de implementarla o declararla ganadora.

## NO USAR CUANDO

No hay volumen suficiente, la métrica primaria no está definida o el cambio mezcla demasiadas variables. Primero hay que simplificar el experimento.

## INSTRUCCIONES

1. Bloquear la hipótesis completa antes de diseñar el test: observación, cambio, audiencia, expectativa direccional y MDE; sin esto no existe experimento serio.
2. Validar supuestos operativos: tráfico estable, independencia de usuarios, instrumentación confiable, duración viable y ausencia de eventos externos que contaminen el resultado.
3. Definir una métrica primaria congelada, métricas secundarias de contexto y guardrails que no pueden degradarse aunque la variante suba el objetivo principal.
4. Documentar reglas de ejecución y análisis: sin peeking, sin cambios mid-test, muestra y duración precalculadas, y decisión final basada en evidencia más criterio de negocio.

## FORMATO DE SALIDA

- Hipótesis y audiencia
- Métrica primaria y guardrails
- Tamaño de muestra y duración
- Reglas de ejecución
- Criterio de decisión

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas duras de QA y cierre con evidencia.
- Ver `./_templates.md` para el template de A/B test.
- Ver `./upstream/ab-test-setup/SKILL.md` para el skill upstream completo.

## ANTI-PATRON

Hipótesis vaga, múltiples variables sin control, peeking, cambiar criterios mid-test o ignorar guardrails para declarar ganador un experimento defectuoso.
