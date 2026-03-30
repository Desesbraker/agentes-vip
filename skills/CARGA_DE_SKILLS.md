# Carga de Skills para Agentes

## Objetivo

Garantizar que cada agente use la información completa de sus skills y no opere solo con el índice resumido del perfil.

## Regla operativa

El perfil del agente funciona como router L1.
La skill activada funciona como instrucción L2.

Antes de ejecutar cualquier tarea especializada, el agente debe leer completa la skill correspondiente dentro de su carpeta en `../skills/<familia>/`.

## Protocolo mínimo

1. Detectar qué skill se activa según el trigger del perfil.
2. Abrir el archivo completo de esa skill antes de responder o ejecutar.
3. Aplicar sus instrucciones y respetar su formato de salida.
4. Si la skill remite a recursos anexos, abrir también `resources/`, `examples/`, `references/`, `templates/` o `scripts/` según haga falta.
5. Si la familia tiene una capa `upstream/<skill>/`, cargar también ese árbol completo cuando la tarea exija doctrina detallada, ejemplos, assets o checklists del origen.
6. Si ninguna skill cubre bien la tarea, reportar el gap y escalar al Orquestador o al Arquitecto según corresponda.
7. Si el agente queda bloqueado, detecta un error no resuelto o identifica un gap recurrente, registrarlo en `./bitacora_agencia.md` antes del cierre.

## Estructura objetivo alineada con Antigravity

Tomar como referencia `sickn33/antigravity-awesome-skills`:

- skill principal como punto de entrada
- secciones de uso, límites, instrucciones y salida
- recursos anexos para ejemplos, checklists, playbooks o scripts
- capa opcional `upstream/<skill>/` dentro de cada familia para preservar el material completo del origen sin inflar la skill router

## Regla de calidad

Nunca ejecutar una tarea usando solo el nombre de la skill o su trigger del perfil.
Siempre cargar la skill completa primero.
Nunca cerrar un bloqueo recurrente sin dejar trazabilidad en `./bitacora_agencia.md`.