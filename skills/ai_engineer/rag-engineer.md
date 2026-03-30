# @rag-engineer

## OBJETIVO

Construir sistemas RAG donde retrieval y generacion esten claramente separados, evaluados y alineados al corpus real. La skill evita culpar al modelo por fallos nacidos en indexacion o ranking.

## USAR CUANDO

- El producto necesita responder con conocimiento cambiante o documental.
- Hay que definir corpus, chunking, filtros, ranking o reranking.
- Se requiere evaluar retrieval y generacion por separado.

## NO USAR CUANDO

- El caso de uso puede resolverse sin retrieval; evaluar llm-app-patterns.
- Solo se necesita prompt engineering de un flujo ya estable.
- No hay corpus, criterio de verdad ni estrategia de refresh definidos.

## INSTRUCCIONES

1. Definir corpus, tipos de pregunta, criterio de verdad y politica de refresh antes de indexar.
2. Diseñar chunking, metadatos, retrieval, filtros y ranking segun como se consulta el conocimiento.
3. Construir la generacion con formato controlado y reglas para usar solo el contexto recuperado o declarar vacios.
4. Evaluar recall, precision, calidad final, latencia, costo y drift antes de iterar prompts.

## FORMATO DE SALIDA

- Estrategia de corpus e indexacion.
- Pipeline de retrieval.
- Reglas de generacion y grounding.
- Riesgos de recall, precision o drift.
- Plan de evaluacion y siguiente ajuste.

## RECURSOS RELACIONADOS

- ./_playbook.md
- ./_templates.md
- ./llm-app-patterns.md

## ANTI-PATRON

- Usar chunking fijo sin validar.
- Hacer retrieval sin filtros ni ranking adecuados.
- Ajustar prompts cuando el fallo real esta en la recuperacion.
