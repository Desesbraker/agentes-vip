# @kpi-dashboard-design

## OBJETIVO

Diseñar dashboards de KPIs que faciliten decisiones periódicas sin saturar a la audiencia ni ocultar definiciones clave.

## USAR CUANDO

Hay que crear un dashboard ejecutivo, táctico u operativo, ordenar vistas de métricas o rehacer una interfaz de reporting.

## NO USAR CUANDO

La prioridad es arreglar tracking roto o definir fórmulas que todavía no existen. Primero se corrige la base de datos o la semántica de métricas.

## INSTRUCCIONES

1. Bloquear audiencia, frecuencia de uso y decisión asociada al dashboard para seleccionar pocas métricas con rol claro.
2. Elegir layout y jerarquía según nivel estratégico, táctico u operativo, manteniendo headline KPIs, tendencias y alertas sin mezclar contextos incompatibles.
3. Documentar fórmula, fuente y refresh de cada KPI, dejando drill-downs o vistas secundarias solo cuando cambien la decisión.
4. Validar legibilidad, volumen de KPIs y capacidad de acción; si el dashboard no sugiere qué hacer, todavía no está resuelto.

## FORMATO DE SALIDA

- Audiencia y decisión objetivo
- KPIs headline
- Layout y jerarquía
- Fórmulas, fuentes y refresh
- Riesgo de ruido o mala interpretación

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de dashboards.
- Ver `./_templates.md` para el template de dashboard.

## ANTI-PATRON

Más de siete KPIs por vista, vanity metrics, gráficos 3D, sin drill-down útil o métricas sin fórmula documentada.
