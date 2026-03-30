# Prompts Operativos: OpenSEO

## Uso

Estos prompts están pensados para invocar agentes de la agencia cuando necesiten usar OpenSEO como fuente verificable.

## 1. Orquestador -> Auditoría SEO

```text
Necesito una auditoría SEO basada en evidencia para [dominio o URL].
Usa OpenSEO si está disponible.
Quiero:
- issues priorizados
- evidencia concreta
- severidad
- impacto estimado
- plan de acción por prioridad
No inventes métricas si falta configuración o acceso.
```

## 2. Orquestador -> Research + Copy SEO

```text
Necesito crear un artículo SEO para [tema o keyword tentativa].
Primero usa OpenSEO para research verificable y luego secuencia el trabajo con Copywriter.
Entregables esperados:
- keyword principal
- variantes
- search intent
- preguntas relacionadas
- internal links sugeridos
- brief de contenido
- borrador inicial
No redactes sin research o placeholders explícitos.
```

## 3. Orquestador -> Data Analyst para demanda

```text
Necesito estimar la demanda de búsqueda para [categoría, producto o problema].
Usa OpenSEO como proxy de demanda si está disponible.
Quiero:
- proxy usado
- comparación entre términos o dominios
- supuestos
- limitaciones
- implicación para negocio
No conviertas volumen de búsqueda en revenue sin modelo intermedio.
```

## 4. SEO Specialist -> Keyword research

```text
Haz keyword research con OpenSEO para [tema].
Entrega:
- keyword principal
- keywords secundarias
- search intent
- preguntas relacionadas
- prioridad
- riesgos o limitaciones de los datos
Usa evidencia verificable y evita recomendaciones sin fuente.
```

## 5. SEO Specialist -> Domain insights

```text
Analiza en OpenSEO el dominio [dominio].
Necesito:
- señales de visibilidad o pérdida
- páginas o temas relevantes
- backlinks u oportunidades si aplica
- quick wins
- blockers
Devuelve findings interpretados, no export bruto.
```

## 6. Copywriter -> Brief SEO

```text
Construye un brief SEO para escribir sobre [tema].
Usa research proveniente de OpenSEO.
Entrega:
- primary keyword
- intent
- supporting terms
- questions to answer
- internal links
- title angles
- meta description draft
Mantén voz clara y evita keyword stuffing.
```

## 7. Copywriter -> Refresh de contenido

```text
Necesito refrescar una pieza de contenido existente sobre [URL o tema].
Usa OpenSEO para detectar oportunidades de keywords, preguntas e internal links.
Entrega:
- gaps detectados
- cambios propuestos
- nuevo outline
- metas actualizadas
- CTA sugerido
No inventes datos ni cambies la voz de marca sin motivo.
```

## 8. Data Analyst -> Benchmark competitivo

```text
Haz un benchmark de demanda/visibilidad para estos dominios o categorías: [lista].
Usa OpenSEO como fuente auxiliar.
Entrega:
- comparación principal
- proxy usado
- fuente complementaria
- nivel de confianza
- implicación para la decisión
Marca claramente qué es dato observado y qué es inferencia.
```

## 9. Prompt corto de fallback

```text
Usa OpenSEO si está disponible.
Si no lo está, reporta la limitación, evita inventar métricas y continúa con alcance parcial explícito.
```

## 10. Flujo real sugerido

1. Orquestador recibe pedido.
2. Si hace falta evidencia SEO, asigna a SEO Specialist.
3. Si luego hay que redactar, secuencia a Copywriter.
4. Si la tarea es sizing o benchmark de demanda, asigna a Data Analyst.
5. QA solo entra si el entregable final requiere validación publicada o checklist final.