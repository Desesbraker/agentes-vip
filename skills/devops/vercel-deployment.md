# @vercel-deployment

OBJETIVO: Desplegar aplicaciones Next.js en Vercel con una separación correcta de entornos, runtimes y variables.

USAR CUANDO: El proyecto corre en Vercel o necesita una estrategia de preview, production y runtime para Next.js.

NO USAR CUANDO: La plataforma final no es Vercel o el problema principal es arquitectura general de frontend o backend. Resolver eso antes de optimizar el deploy.

INSTRUCCIONES:

1. Separar variables por entorno y distinguir claramente build-time versus runtime. Nunca exponer secretos en `NEXT_PUBLIC_`.
2. Elegir runtime Edge o Serverless por caso de uso, limitaciones de APIs Node y sensibilidad a latencia o cold starts.
3. Optimizar tamaño de funciones, cache de build y preview deployments para validar cambios antes de producción.
4. Entregar configuración con riesgos conocidos: CORS, caché stale, timeouts y diferencias entre preview y prod.

FORMATO DE SALIDA:

- Entornos y variables requeridas
- Runtime elegido y justificación
- Estrategia de preview y production
- Riesgos de caché, CORS o timeouts
- Validaciones post-deploy

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para checklist pre-deploy.
- Ver `./_templates.md` para el plan de deployment.

ANTI-PATRÓN: Poner secretos en `NEXT_PUBLIC_`, usar la misma base de datos para preview y prod, ignorar tamaño de funciones o desplegar sin revisar caché, CORS y límites del runtime.
