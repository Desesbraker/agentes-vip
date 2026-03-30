# @verification-before-completion

## OBJETIVO

Impedir declaraciones de completitud sin evidencia fresca que respalde el claim técnico o funcional.

## USAR CUANDO

Siempre antes de decir que un fix, build, test suite, entrega o validación está terminada.

## NO USAR CUANDO

Nunca queda fuera; esta skill aplica como gate final transversal a cualquier trabajo.

## INSTRUCCIONES

1. Identificar exactamente qué claim se quiere hacer y cuál es el comando, prueba o evidencia mínima que realmente lo valida.
2. Ejecutar esa verificación en el momento, leer output y exit code completos y no reemplazarla por intuición o reportes viejos.
3. Contrastar el resultado contra el claim: build, tests, lint, aceptación funcional, documentación o evidencia de agente delegado.
4. Si la evidencia no alcanza, reportar el límite y no declarar completitud; si alcanza, dejar trazabilidad clara del resultado.

## FORMATO DE SALIDA

- Claim validado
- Comando o prueba ejecutada
- Resultado observado
- Exit code o evidencia equivalente
- Límite o riesgo residual

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para reglas duras de cierre.
- Ver `./_templates.md` para el template de verificación.
- Ver `./upstream/verification-before-completion/SKILL.md` para la guía upstream completa.

## ANTI-PATRON

Decir “should work now”, confiar sin evidencia, verificación parcial, confundir lint con build o saltarse el gate por prisa.
