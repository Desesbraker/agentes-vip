# @code-review-checklist

## OBJETIVO

Revisar cambios de código con foco en riesgo real, no en comentarios cosméticos o aprobación automática.

## USAR CUANDO

Hay que auditar una pull request, revisar un diff importante o validar si un cambio está listo para integrarse.

## NO USAR CUANDO

La revisión se limita a formato o estilo que ya cubren herramientas automáticas. La prioridad aquí es comportamiento, riesgo y mantenibilidad.

## INSTRUCCIONES

1. Entender primero el problema que intenta resolver el cambio: leer descripción, issues, alcance, CI y, si hace falta, correr el flujo localmente antes de opinar.
2. Revisar funcionalidad y seguridad: edge cases, manejo de errores, validación de inputs, secretos, auth, acceso a datos y cualquier ruta que pueda romper producción.
3. Revisar performance y calidad estructural: queries, memoria, caché, tamaño del cambio, separación de responsabilidades y claridad del código para futuros mantenedores.
4. Cerrar con hallazgos accionables y priorizados, indicando si faltan tests, docs o aclaraciones antes de aprobar o pedir cambios.

## FORMATO DE SALIDA

- Problema revisado
- Hallazgos prioritarios
- Riesgos funcionales o de seguridad
- Estado de tests y documentación
- Recomendación final

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para checklist rápido de review.
- Ver `./_templates.md` para el template de code review.
- Ver `./upstream/code-review-checklist/SKILL.md` para la checklist upstream base.
- Ver `./upstream/code-review-excellence/SKILL.md` y `./upstream/code-review-excellence/resources/` para criterios más amplios de revisión.

## ANTI-PATRON

Aprobar sin leer, feedback vago, ignorar seguridad, discutir solo estilo o hacer rubber stamp sobre cambios que no se entendieron.
