# @nextjs-best-practices

## OBJETIVO

Diseñar aplicaciones Next.js App Router con routing, rendering y caching coherentes para producción.

## USAR CUANDO

Hay que estructurar páginas, layouts, rutas, data fetching, caching o mutations en proyectos Next.js.

## NO USAR CUANDO

La tarea solo trata de componentes React aislados, estilos o debugging de infraestructura fuera del framework.

## INSTRUCCIONES

1. Mantener Server Components por defecto y mover a Client Components solo la lógica que necesite eventos, estado local o APIs del navegador.
2. Elegir conscientemente el modo de datos: static, revalidate o no-store según frescura requerida; usar Server Actions cuando simplifiquen mutations seguras.
3. Estructurar rutas con page, layout, loading y error para que cada segmento tenga estados explícitos y recuperables.
4. Definir caching desde fetch y tags hasta revalidatePath o revalidateTag, evitando mezclar estrategias sin una razón clara.

## FORMATO DE SALIDA

- Tipo de ruta o vista
- Estrategia de render
- Estrategia de datos y cache
- Archivos clave involucrados
- Riesgo técnico o edge case

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas duras de render, cache y verificación.
- Ver `./_templates.md` para el template de vista.
- Ver `./resources/nextjs-routing-cache-playbook.md` para App Router, segmentación, render modes e invalidación.

## ANTI-PATRON

Marcar todo con use client, hacer fetch en cliente por hábito, omitir loading y error por segmento o dejar bundles grandes sin necesidad.
