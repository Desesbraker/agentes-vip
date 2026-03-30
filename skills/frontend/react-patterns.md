# @react-patterns

## OBJETIVO

Diseñar arquitectura de componentes React clara, reutilizable y mantenible, separando datos, estado e interfaz.

## USAR CUANDO

Hay que definir composición de componentes, extraer hooks, ordenar responsabilidades o decidir patrones de interactividad en React.

## NO USAR CUANDO

La tarea es principalmente performance de Next.js, diseño visual o tipado avanzado de TypeScript. Esos casos tienen skills más específicas.

## INSTRUCCIONES

1. Separar tipos de componente por responsabilidad: Server para datos, Client para interactividad, presentational para UI y containers solo cuando agreguen coordinación real.
2. Extraer custom hooks cuando un patrón de estado o side effects se repite y tenga una API clara para otros consumidores.
3. Usar capacidades modernas de React cuando resuelvan el problema real: useActionState para formularios, useOptimistic para feedback inmediato y use() para recursos compatibles.
4. Preferir composición sobre condicionales gigantes: compound components, slots o render props solo si aumentan claridad y no complejidad accidental.

## FORMATO DE SALIDA

- Patrón recomendado
- Estructura de componentes
- Ubicación del estado
- Hooks a extraer o evitar
- Riesgo de mantenimiento detectado

## RECURSOS RELACIONADOS

- Ver `./_playbook.md` para el flujo operativo de arquitectura frontend.
- Ver `./_templates.md` para el template de vista.
- Ver `./resources/react-nextjs-playbook.md` para composición, custom hooks, estado local y separación server/client.

## ANTI-PATRON

Prop drilling profundo, componentes gigantes con demasiadas responsabilidades, usar useEffect como parche universal o usar index como key en listas dinámicas.
