# @bash-linux

OBJETIVO: Automatizar tareas de sistema y scripting en Linux o macOS con comandos reproducibles, seguros y fáciles de depurar.

USAR CUANDO: Hay que crear scripts, automatizar flujos locales, inspeccionar procesos o administrar archivos y texto desde terminal.

NO USAR CUANDO: La tarea requiere lógica de negocio compleja, distribución multiplataforma profunda o una herramienta de configuración más robusta. En ese caso evaluar Python, Make, Ansible u otra capa adecuada.

INSTRUCCIONES:

1. Diseñar scripts con shebang, `set -euo pipefail`, funciones con nombres claros y una entrada principal legible.
2. Usar operadores y utilidades del shell de forma explícita: pipes para composición, `find` o `grep` para búsqueda y herramientas de procesos solo con filtros suficientes.
3. Tratar texto como interfaz principal: `grep`, `sed`, `awk`, `sort` y `uniq` sirven para filtrar, transformar y validar resultados antes de mutar nada.
4. Cerrar con cleanup, quoting consistente y validaciones previas a operaciones destructivas como borrado, kill o reemplazos masivos.

FORMATO DE SALIDA:

- Objetivo del script o comando
- Dependencias o precondiciones
- Script o secuencia propuesta
- Validaciones y cleanup
- Riesgos de permisos, borrado o quoting

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para reglas duras y checklist de setup.
- Ver `./_templates.md` para el template de setup de entorno.

ANTI-PATRÓN: Dejar variables sin comillas, omitir `set -euo pipefail`, usar `rm -rf` sin validar paths o escribir scripts sin cleanup, validación ni punto de entrada claro.
