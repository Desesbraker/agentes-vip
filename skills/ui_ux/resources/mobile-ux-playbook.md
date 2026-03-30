# Mobile UX Playbook

## Cuándo abrir este recurso

- Diseñar iOS, Android o cross-platform
- Resolver navegación, touch, offline y restricciones de pantalla
- Recuperar matrices y defaults del upstream de mobile design

## Flujo operativo

1. Confirmar plataforma, tipo de app, contexto de uso y conectividad.
2. Definir navegación y flujos críticos.
3. Diseñar touch-first, no desktop reducido.
4. Decidir qué se unifica y qué diverge entre plataformas.

## Unify vs Diverge

| Unificar | Divergir |
|---|---|
| lógica de negocio | navegación |
| contratos API | gestos |
| validación | iconografía |
| semántica de error | tipografía |
| estados de dominio | pickers, sheets y dialogs |

## Platform defaults

| Elemento | iOS | Android |
|---|---|---|
| Tipografía base | SF Pro | Roboto |
| Touch mínimo | 44pt | 48dp |
| Back | edge swipe | system back |
| Sheets | bottom sheet | dialog o sheet |
| Iconos | SF Symbols | Material Icons |

## Mobile psychology

- Finger no es cursor
- Alcance importa más que precisión
- No depender de hover
- Las acciones primarias viven en thumb zone
- Las destructivas deben quedar alejadas y explícitas

## Checklist móvil

- [ ] Plataforma definida
- [ ] Navegación definida
- [ ] Targets táctiles correctos
- [ ] Estados vacíos, error y offline contemplados
- [ ] Gestos críticos visibles o reemplazables
- [ ] Diferencias iOS/Android documentadas

## Entrega esperada

- Plataforma y contexto
- Navegación y flujos críticos
- Reglas touch y accesibilidad
- Estados offline y error
- Riesgo de fricción o divergencia cross-platform

## Anti-patrones

- Desktop reducido a mobile
- Hover como dependencia
- Gestos ocultos sin affordance
- Cross-platform que ignora convenciones de sistema