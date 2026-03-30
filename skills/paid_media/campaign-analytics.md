# @campaign-analytics

OBJETIVO: Leer campañas con suficiente contexto para reasignar presupuesto con criterio y distinguir si el problema está en media buying, funnel, tracking o creatividad.

USAR CUANDO: Hay que analizar resultados de campaña, mover presupuesto o explicar por qué una campaña debe pausarse, escalar o investigarse.

NO USAR CUANDO: No existe ventana mínima de lectura o el tracking está roto. Antes de optimizar, hay que validar la calidad del dato.

INSTRUCCIONES:

1. Definir el KPI principal por campaña y aclarar qué métricas son secundarias para evitar lecturas contradictorias.
2. Analizar rendimiento por nivel: campaña, ad set, anuncio, audiencia, placement y creative, buscando patrones repetidos antes de actuar.
3. Separar problemas de funnel, tracking y creatividad para no culpar a la plataforma por fallos de la landing o de la atribución.
4. Cerrar con log de decisión: qué se pausa, qué se escala, qué se investiga fuera de plataforma y por qué.

FORMATO DE SALIDA:

- KPI principal y ventana analizada
- Hallazgos por nivel
- Qué pausar, escalar o mantener
- Qué revisar fuera de plataforma
- Riesgo de sesgo, poca data o tracking roto

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de analytics.
- Ver `./_templates.md` para el template de campaign reading.

ANTI-PATRÓN: Tomar decisiones con muy poca data, optimizar solo CTR o mover presupuesto compulsivamente sin hipótesis, racional ni ventana mínima de lectura.
