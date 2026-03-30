# @docker-expert

OBJETIVO: Contenerizar aplicaciones con imágenes reproducibles, seguras y ligeras para desarrollo y producción.

USAR CUANDO: Hay que crear o revisar Dockerfiles, imágenes de runtime o configuración Compose para un servicio.

NO USAR CUANDO: El problema principal es la plataforma de despliegue, el clúster o la política de release. En esos casos usar primero la skill más específica de deployment o infraestructura.

INSTRUCCIONES:

1. Diseñar imágenes con multi-stage builds para separar dependencias, build y runtime, maximizando cache y minimizando superficie final.
2. Endurecer seguridad con usuario non-root, UID o GID explícito, imágenes base mínimas y secretos fuera de la imagen.
3. Para orquestación local usar Compose con health checks, redes claras, límites razonables y volúmenes nombrados cuando el servicio lo necesite.
4. Entregar un artefacto que priorice tamaño, reproducibilidad y operabilidad, incluyendo `.dockerignore`, health checks y riesgos abiertos si existen.

FORMATO DE SALIDA:

- Objetivo del contenedor
- Dockerfile o diseño de stages
- Config de runtime y health check
- Secretos, volúmenes y networking
- Riesgos de seguridad, tamaño o caché

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para el checklist Docker.
- Ver `./_templates.md` para el template de diseño de contenedor.

ANTI-PATRÓN: Ejecutar como root en producción, hornear secretos en capas, construir sin multi-stage, omitir `.dockerignore` o publicar una imagen sin health check ni estrategia de runtime.
