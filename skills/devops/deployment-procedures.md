# @deployment-procedures

OBJETIVO: Planificar y ejecutar despliegues con una ruta clara de validación, monitoreo y rollback para reducir riesgo operativo.

USAR CUANDO: Hay que desplegar a producción, preparar una ventana de release o definir estrategia de deployment para un servicio.

NO USAR CUANDO: Todavía no existe build reproducible, staging mínimo o una ruta de rollback. Esos prerequisitos se resuelven antes del deploy.

INSTRUCCIONES:

1. Elegir plataforma y estrategia según el sistema: estático, web app, microservicios o serverless. La decisión debe responder a riesgo, latencia, costo y complejidad operativa.
2. Ejecutar el checklist pre-deploy de 8 puntos: code quality validada, build reproducible, tests críticos aprobados, variables verificadas, secretos cargados, backup disponible, rollback documentado y monitoreo con responsable activo.
3. Seguir el workflow en cinco fases: PREPARE, BACKUP, DEPLOY, VERIFY y CONFIRM o ROLLBACK. Durante VERIFY no se abandona la ventana ni se corta el monitoreo.
4. Si hace falta zero-downtime, elegir Rolling como base, Blue-Green para rollback rápido o Canary para validar con tráfico real antes de expandir.

FORMATO DE SALIDA:

- Servicio, entorno y estrategia elegida
- Checklist pre-deploy cumplido
- Fases del deployment
- Validaciones post-deploy y señales a observar
- Ruta de rollback y riesgo principal

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para el checklist pre-deploy completo y reglas duras.
- Ver `./_templates.md` para el template de plan de deployment.

ANTI-PATRÓN: Desplegar un viernes sin necesidad, saltarse staging, omitir backup o rollback, mezclar demasiados cambios en una sola ventana o irse sin monitorear tras el deploy.
