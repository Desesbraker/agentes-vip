# @environment-setup-guide

OBJETIVO: Configurar entornos de desarrollo reproducibles y verificables para onboarding individual o de equipo.

USAR CUANDO: Hay que preparar una máquina desde cero, documentar onboarding técnico o estandarizar setup local.

NO USAR CUANDO: El problema es un deploy productivo o infraestructura cloud. Esta skill cubre entorno de trabajo local, no release management.

INSTRUCCIONES:

1. Inventariar requisitos: lenguaje y versión, package managers, bases de datos, herramientas de sistema, IDE y credenciales o variables necesarias.
2. Definir instalación por plataforma usando gestores adecuados y version managers cuando aplique para evitar dependencias globales frágiles.
3. Configurar archivos de entorno, shell, git, package managers e IDE a partir de ejemplos controlados, sin dejar secretos persistidos por accidente.
4. Cerrar con verificación reproducible: comandos de versión, tests mínimos, conexión a dependencias y un script de setup o bootstrap si el proyecto lo permite.

FORMATO DE SALIDA:

- Stack y requisitos base
- Pasos de instalación por plataforma
- Variables y archivos de configuración
- Comandos de verificación
- Script de setup y riesgos abiertos

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist de setup.
- Ver `./_templates.md` para el template de setup de entorno.

ANTI-PATRÓN: Asumir herramientas instaladas, saltarse la verificación final, usar `sudo` con package managers sin necesidad o depender de instalaciones globales cuando el proyecto pide aislamiento.
