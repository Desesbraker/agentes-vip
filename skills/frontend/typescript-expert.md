# @typescript-expert

## OBJETIVO

Diseñar y mantener una base TypeScript segura, legible y escalable, minimizando errores de tipos y fricción de compilación.

## USAR CUANDO

Hay que resolver errores de tipos, modelar dominio, endurecer contratos, migrar código JavaScript o mejorar performance del compilador.

## NO USAR CUANDO

El problema principal es arquitectura React, UX o debugging de runtime sin relación con tipos. En esos casos usar la skill específica del dominio.

## INSTRUCCIONES

1. Endurecer la base primero: strict, noUncheckedIndexedAccess y exactOptionalPropertyTypes cuando el proyecto lo soporte.
2. Modelar dominio con tipos explícitos, branded types, satisfies y const assertions antes de recurrir a assertions manuales.
3. Si hay degradación de compilación, revisar project references, incremental y complejidad de tipos; simplificar intersecciones y genéricos antes de desactivar checks.
4. Mantener resolución moderna ESM-first con moduleResolution bundler y tratar paths como ayuda de compilación, no como frontera real de arquitectura.

## FORMATO DE SALIDA

- Problema de tipos detectado
- Causa raíz
- Cambio propuesto
- Riesgo o tradeoff
- Regla futura para evitar regresión

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist de implementación y validación frontend.
- Ver `./_templates.md` para el template de diagnóstico performance o vista según corresponda.
- Ver `./resources/typescript-frontend-playbook.md` para baseline strict, causa raíz y tradeoffs de compilación.

## ANTI-PATRON

Dejar implicit any, abusar de type assertions, crear genéricos circulares o silenciar errores de tipos en lugar de corregir el modelo.
