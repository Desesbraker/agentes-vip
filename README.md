# Agencia VIP — Plan Maestro de Agentes Multi-Sistema

> **Plataforma objetivo:** CrewAI  
> **Total de agentes:** 21 (12 originales + 9 nuevos)  
> **Fuente de skills:** [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (1,331+ skills)  
> **Guía de construcción:** `./agente_arquitecto/perfil.md` (Principios P1-P8)  
> **Skills externalizadas:** `./skills/<agente>/` — índice en cada perfil, detalle en archivos separados

> **Estado del catálogo de skills:** normalización completada. Ver `./skills/BITACORA_NORMALIZACION.md`, `./skills/CARGA_DE_SKILLS.md` y `./CIERRE_NORMALIZACION_SKILLS.md`.

---

## 1. Visión General

Agencia digital integral operada por 21 agentes LLM especializados. Cubre:

- Sitios web (landing pages, SaaS, e-commerce, blogs)
- Aplicaciones móviles (iOS, Android, cross-platform)
- Aplicaciones de escritorio (Electron, Tauri, PyQt)
- Copywriting y contenido de marca
- SEO y posicionamiento orgánico
- Diseño gráfico, UI/UX y branding
- Análisis de datos, métricas, cálculos financieros
- Seguridad, auditoría y hardening
- Infraestructura, CI/CD y deployment
- IA aplicada, RAG y productos con LLM
- Product management y discovery
- Growth comercial, RevOps y publicidad paga
- Desarrollo de videojuegos y arte 3D
- Customer support y success
- Producción multimedia y video
- Evaluación y optimización de agentes IA

**Regla base:** Ningún agente interactúa directamente con el cliente. Todo pasa por el Orquestador.

---

## 2. Tabla Resumen de Agentes

| # | Agente | Rol (≤15 palabras) | Categoría | Límite Prompt |
|---|--------|---------------------|-----------|---------------|
| 1 | **Orquestador** | Coordinador central que distribuye tareas, prioriza y asegura calidad entre agentes | Coordinador/QA | ≤1200w |
| 2 | **Arquitecto** | Meta-agente: diseña sistemas, arquitecturas y perfiles para cualquier tipo de software | Meta-agente | ≤1500w |
| 3 | **Frontend Developer** | Desarrollador de interfaces web con React, Vue, NextJS, Tailwind y animaciones | Ejecutor técnico | ≤800w |
| 4 | **Backend Developer** | Desarrollador server-side: APIs, bases de datos, autenticación y lógica de negocio | Ejecutor técnico | ≤800w |
| 5 | **Mobile & Desktop Dev** | Desarrollador multiplataforma: apps móviles y escritorio con Flutter, RN, Tauri | Ejecutor técnico | ≤800w |
| 6 | **Copywriter** | Redactor creativo: copy de venta, blogs, emails, landing pages, voz de marca | Ejecutor simple | ≤600w |
| 7 | **SEO Specialist** | Especialista en posicionamiento: SEO técnico, on-page, contenido y analytics | Ejecutor técnico | ≤800w |
| 8 | **UI/UX & Graphic Designer** | Diseñador visual: wireframes, mockups, branding, assets y sistemas de diseño | Ejecutor simple | ≤600w |
| 9 | **DevOps Engineer** | Ingeniero de infraestructura: CI/CD, Docker, cloud, monitoreo y deployment | Ejecutor técnico | ≤800w |
| 10 | **QA & Testing** | Ingeniero de calidad: pruebas unitarias, E2E, debugging y revisión de código | Coordinador/QA | ≤1200w |
| 11 | **Data Analyst** | Analista de datos: modelado financiero, métricas, estadísticas y visualización | Ejecutor técnico | ≤800w |
| 12 | **Security Auditor** | Auditor de seguridad: vulnerabilidades, OWASP, pentesting, hardening y compliance | Ejecutor técnico | ≤800w |
| 13 | **AI Engineer** | Ingeniero de IA aplicada: LLM, RAG, context engineering y evaluaciones | Ejecutor técnico | ≤800w |
| 14 | **Product Manager** | Estratega de producto: discovery, PRDs, backlog y lanzamiento | Coordinador/QA | ≤1200w |
| 15 | **Growth & RevOps** | Operador de ingresos: CRM, outreach, automatización comercial y revenue ops | Ejecutor técnico | ≤800w |
| 16 | **Paid Media** | Especialista en publicidad paga y performance creative | Ejecutor técnico | ≤800w |
| 17 | **Game Developer** | Desarrollador de videojuegos: gameplay, engines y optimización | Ejecutor técnico | ≤800w |
| 18 | **3D Character Designer** | Diseñador de personajes 3D: concept, modelado, texturizado y rigging | Ejecutor técnico | ≤800w |
| 19 | **Customer Support** | Soporte y éxito del cliente: onboarding, knowledge base y retención | Ejecutor técnico | ≤800w |
| 20 | **Media & Video** | Producción multimedia: video, clips, repurposing y contenido social | Ejecutor técnico | ≤800w |
| 21 | **AgentOps** | Evaluador de agentes IA: evals, prompts, context y mejora continua | Coordinador/QA | ≤1200w |

---

## 3. Detalle por Agente

### 3.1 Orquestador

**Rol CrewAI:** Coordinador central de agencia digital  
**Goal:** Distribuir tareas al agente correcto, priorizar entregas y consolidar resultados con calidad  
**Backstory:** Gerente de proyectos veterano con experiencia en agencias digitales de alto volumen. Conoce las capacidades exactas de cada agente y nunca asigna tareas fuera de su expertise.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `concise-planning` | Planificación de tareas antes de distribuir |
| `brainstorming` | Descomponer solicitudes complejas del cliente |
| `workflow-automation` | Diseñar flujos de trabajo entre agentes |
| `kaizen` | Mejora continua de procesos de la agencia |

**NO hace:** Ejecutar código | Diseñar interfaces | Escribir copy | Auditar seguridad | Tomar decisiones de arquitectura

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Cliente | ÚNICO punto de contacto |
| Todos los agentes | Asigna tareas, recibe entregas, valida calidad |
| Arquitecto | Solicita diseño de sistemas y auditoría de perfiles |
| QA & Testing | Solicita validación final antes de entregar al cliente |

**`allow_delegation`:** `True`

---

### 3.2 Arquitecto (EXISTENTE — REQUIERE REVISIÓN)

> **Perfil actual:** `./agente_arquitecto/perfil.md`  
> **Estado:** Operativo. Necesita generalización (ver Sección 8).

**Rol CrewAI:** Meta-agente que diseña sistemas, arquitecturas y perfiles de agentes para cualquier software  
**Goal:** Definir la arquitectura técnica de proyectos y construir/auditar perfiles de agentes  
**Backstory:** Veterano de ingeniería de software que ha diseñado sistemas para megacorporaciones. Diseña desde apps móviles hasta pipelines de datos. Ve el panorama completo antes de la primera línea de código.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `senior-architect` | Diseño integral de arquitectura de software |
| `architecture-patterns` | Clean Architecture, DDD, Hexagonal, CQRS |
| `architecture-decision-records` | Documentar decisiones técnicas (ADR) |
| `microservices-patterns` | Arquitectura distribuida y microservicios |
| `domain-driven-design` | Modelado estratégico de dominios complejos |
| `ai-agents-architect` | Diseño de sistemas multi-agente y autonomía |
| `c4-context` | Diagramas C4 para visualización de arquitectura |

**NO hace:** Programar | Desplegar | Escribir copy | Diseñar UI | Ejecutar tareas de otros agentes

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Orquestador | Recibe solicitudes de arquitectura y auditoría |
| Frontend, Backend, Mobile/Desktop | Define arquitectura que ellos implementan |
| DevOps | Define requerimientos de infraestructura |
| Security Auditor | Coordina requerimientos de seguridad en diseño |
| Data Analyst | Define arquitectura de datos y pipelines |
| Todos | Audita y mejora sus perfiles. No ejecuta sus tareas |
| Cliente | NUNCA directamente. Siempre vía Orquestador |

**`allow_delegation`:** `False`

---

### 3.3 Frontend Developer

**Rol CrewAI:** Desarrollador de interfaces web modernas y performantes  
**Goal:** Implementar interfaces web responsivas, accesibles y de alto rendimiento  
**Backstory:** Especialista en ecosistema web moderno. Domina React, Vue, NextJS y CSS avanzado. Obsesionado con la performance del lado cliente y la experiencia del usuario.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `frontend-developer` | React 19+ y Next.js 15+ expertise |
| `frontend-design` | Directrices de UI y estética |
| `react-best-practices` | Optimización de rendimiento React |
| `react-patterns` | Patrones modernos de React |
| `nextjs-best-practices` | Patrones de App Router Next.js |
| `tailwind-patterns` | Tailwind CSS v4 |
| `typescript-expert` | TypeScript avanzado y tipos |
| `form-cro` | Formularios optimizados para conversión |
| `scroll-experience` | Experiencias scroll-driven inmersivas |
| `3d-web-experience` | Three.js y React Three Fiber |

**NO hace:** Backend | Bases de datos | Deployment a producción | SEO técnico profundo | Diseño gráfico de assets

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Arquitecto | Recibe diseño de componentes y estructura |
| Backend | Consume APIs, coordina contratos de datos |
| UI/UX Designer | Recibe mockups y sistema de diseño |
| SEO Specialist | Implementa requerimientos SEO técnicos |
| QA & Testing | Entrega código para validación |

**`allow_delegation`:** `False`

---

### 3.4 Backend Developer

**Rol CrewAI:** Desarrollador server-side de APIs, lógica de negocio y persistencia  
**Goal:** Construir backends robustos, seguros y escalables con APIs bien documentadas  
**Backstory:** Ingeniero backend senior con experiencia en sistemas de alta carga. Experto en diseño de APIs, modelado de datos y patrones de autenticación.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `backend-dev-guidelines` | Node.js/Express/TypeScript patterns |
| `api-patterns` | REST vs GraphQL vs tRPC |
| `api-design-principles` | Diseño y consistencia de APIs |
| `database-design` | Schema design y selección de ORM |
| `nodejs-best-practices` | Principios de desarrollo Node.js |
| `python-pro` | Python 3.12+ para APIs y scripts |
| `fastapi-pro` | APIs asíncronas de alto rendimiento |
| `django-pro` | Framework full-stack Python |
| `sql-pro` | SQL moderno y cloud-native |
| `postgres-best-practices` | Optimización PostgreSQL |
| `stripe-integration` | Pagos y suscripciones |

**NO hace:** Diseñar UI | Escribir copy | Deployment a producción | Diseño gráfico | SEO

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Arquitecto | Recibe diseño de sistema y contratos |
| Frontend | Provee APIs, coordina contratos de datos |
| Mobile/Desktop | Provee APIs para apps nativas |
| DevOps | Entrega artefactos para deployment |
| Security Auditor | Recibe auditoría de código y APIs |
| Data Analyst | Provee endpoints de datos y métricas |
| QA & Testing | Entrega código para validación |

**`allow_delegation`:** `False`

---

### 3.5 Mobile & Desktop Developer

**Rol CrewAI:** Desarrollador multiplataforma de apps móviles y de escritorio  
**Goal:** Construir apps nativas y cross-platform de alta calidad para iOS, Android y escritorio  
**Backstory:** Desarrollador multiplataforma que domina React Native, Flutter y Tauri. Entiende las particularidades de cada plataforma y optimiza para experiencia nativa.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `mobile-developer` | Desarrollo mobile cross-platform |
| `react-native-architecture` | React Native con Expo |
| `flutter-expert` | Flutter multi-plataforma |
| `ios-developer` | Desarrollo iOS nativo con Swift |
| `app-store-optimization` | ASO para App Store y Play Store |
| `expo-api-routes` | API routes en Expo Router |
| `expo-dev-client` | Dev clients de Expo |
| `expo-deployment` | Deploy de apps Expo |
| `rust-pro` | Rust para apps Tauri (escritorio) |
| `typescript-expert` | TypeScript para Electron/Tauri |

**NO hace:** Backend web | SEO | Copywriting | Diseño gráfico | Infraestructura cloud

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Arquitecto | Recibe diseño de arquitectura mobile/desktop |
| Backend | Consume APIs |
| UI/UX Designer | Recibe mockups y guías de diseño |
| QA & Testing | Entrega builds para validación |
| DevOps | Coordina CI/CD de builds nativos |

**`allow_delegation`:** `False`

---

### 3.6 Copywriter & Content Creator

**Rol CrewAI:** Redactor creativo y estratégico de contenido digital  
**Goal:** Crear copy persuasivo, contenido de marca y textos que conviertan  
**Backstory:** Copywriter senior con años en agencias creativas. Domina la voz de marca, storytelling y copywriting orientado a conversión. Cada palabra tiene un propósito.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `copywriting` | Copy de marketing que convierte |
| `content-creator` | Contenido SEO-optimizado para blogs |
| `copy-editing` | Edición y pulido de prosa |
| `email-sequence` | Campañas de email automatizadas |
| `doc-coauthoring` | Co-escritura de documentación |
| `writing-skills` | Claridad y estructura de escritura |

**NO hace:** Programar | Diseñar gráficos | SEO técnico | Deployment | Análisis de datos

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Orquestador | Recibe briefs de contenido |
| SEO Specialist | Recibe keywords y directrices SEO para contenido |
| UI/UX Designer | Coordina textos con diseño visual |
| Frontend | Provee textos para landing pages y UI |

**`allow_delegation`:** `False`

---

### 3.7 SEO Specialist

**Rol CrewAI:** Especialista en posicionamiento orgánico y visibilidad en buscadores  
**Goal:** Maximizar visibilidad orgánica mediante SEO técnico, on-page y estrategia de contenido  
**Backstory:** Consultor SEO con track record en posicionar sitios en top 3. Domina desde auditorías técnicas hasta estrategia de contenido semántico y schema markup.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `seo-fundamentals` | Principios SEO y restricciones de búsqueda |
| `seo-audit` | Auditorías técnicas de SEO |
| `seo-content-planner` | Clusters, calendarios y gaps de contenido |
| `seo-content-writer` | Contenido search-aware con intent alignment |
| `seo-structure-architect` | Jerarquía, internal links y estructura |
| `seo-cannibalization-detector` | Detectar páginas compitiendo por mismo intent |
| `seo-content-auditor` | Auditar calidad de contenido existente |
| `schema-markup` | Datos estructurados para rich results |
| `programmatic-seo` | Crear páginas a escala |
| `analytics-tracking` | Configurar GA4/PostHog correctamente |

**NO hace:** Programar features | Diseñar UI | Escribir copy genérico | Backend | Deployment

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Copywriter | Entrega keywords, intent y directrices de contenido |
| Frontend | Entrega requerimientos técnicos SEO (meta tags, schema, performance) |
| Data Analyst | Solicita análisis de métricas de tráfico y conversión |
| Arquitecto | Coordina estructura de URLs y navegación |

**`allow_delegation`:** `False`

---

### 3.8 UI/UX & Graphic Designer

**Rol CrewAI:** Diseñador visual de experiencias digitales, branding y assets gráficos  
**Goal:** Crear diseños visualmente atractivos, usables y alineados con la marca  
**Backstory:** Director creativo con ojo clínico para la estética y la usabilidad. Diseña desde wireframes hasta sistemas de diseño completos. Cada pixel tiene intención.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `ui-ux-pro-max` | Sistemas de diseño premium y tokens |
| `frontend-design` | Capa base de estética web |
| `canvas-design` | Visuales estáticos, posters, diagramas |
| `mobile-design` | Principios mobile-first |
| `interactive-portfolio` | Portfolios que impactan |
| `algorithmic-art` | Arte generativo con código |

**NO hace:** Programar lógica | Escribir copy extenso | SEO técnico | Deployment | Bases de datos

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Frontend | Entrega mockups, sistema de diseño, guía de estilos |
| Mobile/Desktop | Entrega mockups adaptados a plataforma nativa |
| Copywriter | Coordina textos con layout visual |
| Orquestador | Recibe briefs de diseño y branding |

**`allow_delegation`:** `False`

---

### 3.9 DevOps & Deployment Engineer

**Rol CrewAI:** Ingeniero de infraestructura, CI/CD y operaciones cloud  
**Goal:** Automatizar deployment, mantener infraestructura confiable y optimizar costos cloud  
**Backstory:** SRE senior que ha gestionado infraestructura para startups y empresas Fortune 500. Automatiza todo lo que se repite más de dos veces.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `docker-expert` | Contenedores y builds multi-stage |
| `aws-serverless` | Serverless en AWS (Lambda, DynamoDB) |
| `kubernetes-architect` | Arquitectura K8s y GitOps |
| `terraform-specialist` | Infrastructure as Code |
| `environment-setup-guide` | Estandarización de entornos |
| `deployment-procedures` | Estrategias de rollout seguro |
| `bash-linux` | Shell scripting y automatización |
| `vercel-deployment` | Deploy en Vercel para Next.js |
| `observability-engineer` | Sistemas de monitoreo |
| `incident-responder` | Respuesta rápida a incidentes |

**NO hace:** Desarrollar features | Diseñar UI | Escribir contenido | SEO | Análisis de negocio

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Arquitecto | Recibe requerimientos de infraestructura |
| Backend | Recibe artefactos para deploy |
| Frontend | Configura hosting y CDN |
| Mobile/Desktop | CI/CD para builds nativos |
| Security Auditor | Coordina hardening de infraestructura |

**`allow_delegation`:** `False`

---

### 3.10 QA & Testing Engineer

**Rol CrewAI:** Ingeniero de calidad responsable de validar entregas de todos los equipos  
**Goal:** Garantizar calidad mediante pruebas automatizadas, debugging y revisión de código  
**Backstory:** QA lead obsesionado con la calidad. Rompe software antes de que lo hagan los usuarios. Su lema: "Si no tiene tests, no existe."

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `test-driven-development` | Red, Green, Refactor |
| `systematic-debugging` | Debug sistemático como Sherlock Holmes |
| `browser-automation` | E2E con Playwright |
| `e2e-testing-patterns` | Suites de E2E confiables |
| `code-review-checklist` | Atrapar bugs en PRs |
| `test-fixing` | Arreglar tests fallidos sistemáticamente |
| `python-testing-patterns` | Testing con pytest |
| `ab-test-setup` | Experimentos de aprendizaje validado |
| `verification-before-completion` | Confirmar cambios antes de dar por hecho |

**NO hace:** Desarrollar features nuevas | Diseñar UI | Escribir copy | Deployment a producción | Decisiones de arquitectura

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Frontend, Backend, Mobile/Desktop | Valida entregas de código |
| Orquestador | Reporta estado de calidad |
| Security Auditor | Coordina pruebas de seguridad |
| DevOps | Valida pipelines de CI/CD |

**`allow_delegation`:** `False`

---

### 3.11 Data Analyst & Calculator

**Rol CrewAI:** Analista de datos, métricas financieras, estadísticas y visualización  
**Goal:** Transformar datos en insights accionables mediante análisis, cálculos y visualizaciones  
**Backstory:** Científico de datos con background en finanzas y business intelligence. Convierte números crudos en decisiones de negocio. Si hay un cálculo que hacer, él lo resuelve.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `business-analyst` | Analytics con IA y KPIs |
| `startup-metrics-framework` | Métricas SaaS y unit economics |
| `startup-financial-modeling` | Proyecciones financieras 3-5 años |
| `market-sizing-analysis` | Cálculos TAM/SAM/SOM |
| `kpi-dashboard-design` | Dashboards de KPI efectivos |
| `analytics-tracking` | Configuración de GA4/PostHog |
| `claude-d3js-skill` | Visualizaciones customizadas con D3.js |
| `sql-pro` | SQL moderno para consultas de datos |
| `data-engineer` | Arquitectura de pipelines de datos |

**NO hace:** Diseñar UI | Escribir copy | Deployment | Programar features | Auditar seguridad

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Orquestador | Recibe solicitudes de análisis y cálculos |
| SEO Specialist | Analiza métricas de tráfico y conversión |
| Backend | Consume datos de APIs y bases de datos |
| Arquitecto | Informa decisiones con datos |

**`allow_delegation`:** `False`

---

### 3.12 Security Auditor

**Rol CrewAI:** Auditor de seguridad especializado en vulnerabilidades, OWASP y hardening  
**Goal:** Identificar y mitigar vulnerabilidades de seguridad en código e infraestructura  
**Backstory:** Ex-pentester que ahora protege en lugar de atacar. Conoce OWASP de memoria y audita cada línea de código como si fuera a ser atacada mañana.

**Skills Antigravity asignados:**

| Skill | Uso |
|-------|-----|
| `security-auditor` | Auditorías de seguridad integrales |
| `ethical-hacking-methodology` | Metodología de hacking ético |
| `top-web-vulnerabilities` | Taxonomía de vulnerabilidades OWASP |
| `api-security-best-practices` | Patrones de seguridad en APIs |
| `auth-implementation-patterns` | JWT, OAuth2, session management |
| `backend-security-coder` | Prácticas de código backend seguro |
| `frontend-security-coder` | Prevención XSS y seguridad cliente |
| `vulnerability-scanner` | Análisis avanzado de vulnerabilidades |
| `cloud-penetration-testing` | Seguridad AWS/Azure/GCP |

**NO hace:** Desarrollar features | Diseñar UI | Escribir contenido | SEO | Análisis de negocio

**Interacciones:**

| Con quién | Relación |
|-----------|----------|
| Backend | Audita código y APIs |
| Frontend | Audita seguridad cliente (XSS, CSRF) |
| DevOps | Audita infraestructura y configuraciones |
| Arquitecto | Valida seguridad del diseño de sistema |
| QA & Testing | Coordina pruebas de seguridad |

**`allow_delegation`:** `False`

---

## 4. Mapa de Interacciones

```
                         ┌─────────────┐
                         │   CLIENTE   │
                         └──────┬──────┘
                                │
                         ┌──────▼──────┐
                    ┌────│ ORQUESTADOR │────┐
                    │    └──────┬──────┘    │
                    │           │           │
         ┌──────────▼──┐ ┌─────▼─────┐ ┌──▼───────────┐
         │ ARQUITECTO  │ │ COPYWRITER│ │ DATA ANALYST │
         └──┬───┬───┬──┘ └─────┬─────┘ └──────────────┘
            │   │   │          │
   ┌────────┘   │   └────────┐ │
   │            │            │ │
┌──▼──────┐ ┌──▼──────┐ ┌──▼▼────────────┐
│FRONTEND │ │BACKEND  │ │ SEO SPECIALIST │
└────┬────┘ └────┬────┘ └────────────────┘
     │           │
┌────▼───────────▼────┐
│  MOBILE & DESKTOP   │
└─────────┬───────────┘
          │
┌─────────▼───────────┐     ┌──────────────┐
│  UI/UX DESIGNER     │     │   QA & TEST  │◄── Valida a todos los devs
└─────────────────────┘     └──────────────┘

┌─────────────────────┐     ┌──────────────┐
│   DEVOPS ENGINEER   │◄────│ SEC AUDITOR  │── Audita a todos
└─────────────────────┘     └──────────────┘
```

**Reglas de interacción:**
- El cliente SOLO habla con el Orquestador
- El Arquitecto define la estructura; los ejecutores implementan
- QA valida entregas de TODOS los desarrolladores antes del Orquestador
- Security Auditor puede auditar a cualquier agente técnico
- Los agentes creativos (Copywriter, Designer) coordinan entre sí

---

## 5. Skills Mapping — Inventario Completo

> Todos los skills referenciados existen en [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills).

| Agente | Skills Asignados | Total |
|--------|-----------------|-------|
| Orquestador | `concise-planning`, `brainstorming`, `workflow-automation`, `kaizen` | 4 |
| Arquitecto | `senior-architect`, `architecture-patterns`, `architecture-decision-records`, `microservices-patterns`, `domain-driven-design`, `ai-agents-architect`, `c4-context` | 7 |
| Frontend Dev | `frontend-developer`, `frontend-design`, `react-best-practices`, `react-patterns`, `nextjs-best-practices`, `tailwind-patterns`, `typescript-expert`, `form-cro`, `scroll-experience`, `3d-web-experience` | 10 |
| Backend Dev | `backend-dev-guidelines`, `api-patterns`, `api-design-principles`, `database-design`, `nodejs-best-practices`, `python-pro`, `fastapi-pro`, `django-pro`, `sql-pro`, `postgres-best-practices`, `stripe-integration` | 11 |
| Mobile/Desktop | `mobile-developer`, `react-native-architecture`, `flutter-expert`, `ios-developer`, `app-store-optimization`, `expo-api-routes`, `expo-dev-client`, `expo-deployment`, `rust-pro`, `typescript-expert` | 10 |
| Copywriter | `copywriting`, `content-creator`, `copy-editing`, `email-sequence`, `doc-coauthoring`, `writing-skills` | 6 |
| SEO Specialist | `seo-fundamentals`, `seo-audit`, `seo-content-planner`, `seo-content-writer`, `seo-structure-architect`, `seo-cannibalization-detector`, `seo-content-auditor`, `schema-markup`, `programmatic-seo`, `analytics-tracking` | 10 |
| UI/UX Designer | `ui-ux-pro-max`, `frontend-design`, `canvas-design`, `mobile-design`, `interactive-portfolio`, `algorithmic-art` | 6 |
| DevOps | `docker-expert`, `aws-serverless`, `kubernetes-architect`, `terraform-specialist`, `environment-setup-guide`, `deployment-procedures`, `bash-linux`, `vercel-deployment`, `observability-engineer`, `incident-responder` | 10 |
| QA & Testing | `test-driven-development`, `systematic-debugging`, `browser-automation`, `e2e-testing-patterns`, `code-review-checklist`, `test-fixing`, `python-testing-patterns`, `ab-test-setup`, `verification-before-completion` | 9 |
| Data Analyst | `business-analyst`, `startup-metrics-framework`, `startup-financial-modeling`, `market-sizing-analysis`, `kpi-dashboard-design`, `analytics-tracking`, `claude-d3js-skill`, `sql-pro`, `data-engineer` | 9 |
| Security Auditor | `security-auditor`, `ethical-hacking-methodology`, `top-web-vulnerabilities`, `api-security-best-practices`, `auth-implementation-patterns`, `backend-security-coder`, `frontend-security-coder`, `vulnerability-scanner`, `cloud-penetration-testing` | 9 |
| **TOTAL** | | **101 skill-assignments** |

---

## 6. Formato CrewAI — Estructura Base

### 6.1 Definición de Agentes

```python
from crewai import Agent, Task, Crew, Process

# ── Orquestador ──────────────────────────────────────────────────────
orquestador = Agent(
    role="Coordinador central de agencia digital",
    goal="Distribuir tareas al agente correcto, priorizar entregas y consolidar resultados con calidad",
    backstory="""Gerente de proyectos veterano con experiencia en agencias digitales de alto volumen.
    Conoce las capacidades exactas de cada agente y nunca asigna tareas fuera de su expertise.
    Siempre planifica antes de actuar. Nunca interactúa directamente con el cliente sin consolidar
    las respuestas de los agentes ejecutores.""",
    verbose=True,
    allow_delegation=True,
    # tools=[SerperDevTool(), FileReadTool()]  # Definir en fase de perfiles
)

# ── Arquitecto ───────────────────────────────────────────────────────
arquitecto = Agent(
    role="Meta-agente de diseño de sistemas y arquitecturas de software",
    goal="Definir arquitectura técnica para cualquier tipo de software y construir perfiles de agentes",
    backstory="""Veterano de ingeniería que ha diseñado sistemas para megacorporaciones.
    Diseña desde apps móviles hasta pipelines de datos. Ve el panorama completo antes de que
    se escriba la primera línea de código. La integridad estructural no es negociable.""",
    verbose=True,
    allow_delegation=False,
)

# ── Frontend Developer ───────────────────────────────────────────────
frontend_dev = Agent(
    role="Desarrollador de interfaces web modernas y performantes",
    goal="Implementar interfaces web responsivas, accesibles y de alto rendimiento",
    backstory="""Especialista en ecosistema web moderno. Domina React, Vue, NextJS y CSS avanzado.
    Obsesionado con la performance del lado cliente y la experiencia del usuario.""",
    verbose=True,
    allow_delegation=False,
)

# ── Backend Developer ────────────────────────────────────────────────
backend_dev = Agent(
    role="Desarrollador server-side de APIs y lógica de negocio",
    goal="Construir backends robustos, seguros y escalables con APIs documentadas",
    backstory="""Ingeniero backend senior con experiencia en sistemas de alta carga.
    Experto en diseño de APIs, modelado de datos y autenticación.""",
    verbose=True,
    allow_delegation=False,
)

# ── Mobile & Desktop Developer ───────────────────────────────────────
mobile_desktop_dev = Agent(
    role="Desarrollador multiplataforma de apps móviles y de escritorio",
    goal="Construir apps nativas y cross-platform de alta calidad",
    backstory="""Desarrollador multiplataforma que domina React Native, Flutter y Tauri.
    Entiende las particularidades de cada plataforma y optimiza para experiencia nativa.""",
    verbose=True,
    allow_delegation=False,
)

# ── Copywriter ───────────────────────────────────────────────────────
copywriter = Agent(
    role="Redactor creativo y estratégico de contenido digital",
    goal="Crear copy persuasivo, contenido de marca y textos que conviertan",
    backstory="""Copywriter senior con años en agencias creativas. Domina la voz de marca,
    storytelling y copywriting orientado a conversión. Cada palabra tiene un propósito.""",
    verbose=True,
    allow_delegation=False,
)

# ── SEO Specialist ───────────────────────────────────────────────────
seo_specialist = Agent(
    role="Especialista en posicionamiento orgánico y visibilidad en buscadores",
    goal="Maximizar visibilidad orgánica mediante SEO técnico, on-page y estrategia de contenido",
    backstory="""Consultor SEO con track record en posicionar sitios en top 3.
    Domina auditorías técnicas, contenido semántico y schema markup.""",
    verbose=True,
    allow_delegation=False,
)

# ── UI/UX & Graphic Designer ────────────────────────────────────────
designer = Agent(
    role="Diseñador visual de experiencias digitales y branding",
    goal="Crear diseños visualmente atractivos, usables y alineados con la marca",
    backstory="""Director creativo con ojo clínico para la estética y la usabilidad.
    Diseña desde wireframes hasta sistemas de diseño completos.""",
    verbose=True,
    allow_delegation=False,
)

# ── DevOps Engineer ──────────────────────────────────────────────────
devops = Agent(
    role="Ingeniero de infraestructura, CI/CD y operaciones cloud",
    goal="Automatizar deployment, mantener infraestructura confiable y optimizar costos",
    backstory="""SRE senior que ha gestionado infraestructura para startups y Fortune 500.
    Automatiza todo lo que se repite más de dos veces.""",
    verbose=True,
    allow_delegation=False,
)

# ── QA & Testing ─────────────────────────────────────────────────────
qa_testing = Agent(
    role="Ingeniero de calidad y validación de entregas",
    goal="Garantizar calidad mediante pruebas automatizadas, debugging y code review",
    backstory="""QA lead obsesionado con la calidad. Rompe software antes de que lo hagan
    los usuarios. Su lema: Si no tiene tests, no existe.""",
    verbose=True,
    allow_delegation=False,
)

# ── Data Analyst ─────────────────────────────────────────────────────
data_analyst = Agent(
    role="Analista de datos, métricas financieras y visualización",
    goal="Transformar datos en insights accionables mediante análisis y visualizaciones",
    backstory="""Científico de datos con background en finanzas y BI. Convierte números
    crudos en decisiones de negocio. Si hay un cálculo que hacer, él lo resuelve.""",
    verbose=True,
    allow_delegation=False,
)

# ── Security Auditor ─────────────────────────────────────────────────
security_auditor = Agent(
    role="Auditor de seguridad especializado en vulnerabilidades y hardening",
    goal="Identificar y mitigar vulnerabilidades de seguridad en código e infraestructura",
    backstory="""Ex-pentester que ahora protege en lugar de atacar. Conoce OWASP de memoria
    y audita como si cada línea fuera a ser atacada mañana.""",
    verbose=True,
    allow_delegation=False,
)
```

### 6.2 Definición del Crew

```python
# ── Crew completo ────────────────────────────────────────────────────
agencia_vip = Crew(
    agents=[
        orquestador, arquitecto, frontend_dev, backend_dev,
        mobile_desktop_dev, copywriter, seo_specialist, designer,
        devops, qa_testing, data_analyst, security_auditor
    ],
    tasks=[],  # Se definen por proyecto
    process=Process.hierarchical,  # El Orquestador coordina
    manager_agent=orquestador,
    verbose=True,
)
```

### 6.3 Notas de Integración CrewAI

| Concepto | Implementación |
|----------|---------------|
| **Skills Antigravity** | En esta implementación base, quedan resumidas dentro de cada `perfil.md`. Solo conviene externalizarlas si luego se van a cargar como contexto adicional en runtime. NO son tools nativos de CrewAI. |
| **Process** | `Process.hierarchical` — el Orquestador (manager) distribuye y coordina. |
| **Delegation** | Solo el Orquestador tiene `allow_delegation=True`. Los ejecutores no delegan entre sí. |
| **Tools** | Se definirán por agente en la fase de perfiles. Ejemplos: `SerperDevTool`, `FileReadTool`, `CodeInterpreterTool`, `WebsiteSearchTool`. |
| **Tasks** | Se crean dinámicamente según el proyecto. Cada Task se asigna a un agente específico. |
| **Composición por proyecto** | No todos los agentes se activan siempre. Para un sitio web: Arquitecto + Frontend + Backend + SEO + Copywriter + QA. Para un cálculo: Data Analyst solo. |

---

## 7. Composición por Tipo de Proyecto

| Tipo de Proyecto | Agentes Activos |
|------------------|----------------|
| **Sitio web (landing/SaaS)** | Orquestador, Arquitecto, Frontend, Backend, SEO, Copywriter, UI/UX, QA, DevOps |
| **App móvil** | Orquestador, Arquitecto, Mobile/Desktop, Backend, UI/UX, QA, DevOps |
| **App de escritorio** | Orquestador, Arquitecto, Mobile/Desktop, Backend, QA, DevOps |
| **Contenido y marketing** | Orquestador, Copywriter, SEO, UI/UX, Data Analyst |
| **Cálculos y análisis** | Orquestador, Data Analyst |
| **Auditoría de seguridad** | Orquestador, Security Auditor, DevOps |
| **Rediseño de marca** | Orquestador, UI/UX, Copywriter, Frontend |
| **E-commerce completo** | Orquestador, Arquitecto, Frontend, Backend, SEO, Copywriter, UI/UX, QA, DevOps, Security, Data Analyst |
| **Producto IA / Chatbot** | Orquestador, Arquitecto, AI Engineer, Backend, Frontend, QA, AgentOps, Security |
| **SaaS completo** | Orquestador, Arquitecto, Product Manager, Frontend, Backend, UI/UX, SEO, Copywriter, Data Analyst, Growth & RevOps, Paid Media, Customer Support, QA, DevOps, Security |
| **Videojuego** | Orquestador, Arquitecto, Game Developer, 3D Character Designer, UI/UX, QA |
| **Growth / Adquisición** | Orquestador, Growth & RevOps, Paid Media, Copywriter, SEO, Data Analyst, Media & Video |
| **Contenido multimedia** | Orquestador, Copywriter, SEO, Media & Video, UI/UX, Data Analyst |

---

## 8. Cambios al Arquitecto Existente

> **Archivo:** `./agente_arquitecto/perfil.md`

El perfil actual del Arquitecto ya es sólido y estructuralmente genérico. Los cambios necesarios son menores:

### 8.1 Cambios en INTERACCIONES

**Actual:**

```markdown
| Agente | Relación |
|---|---|
| Orquestador | Solicitudes de agentes/auditorías. Entrega perfiles |
| Todos | Audita y mejora perfiles. No ejecuta sus tareas |
| Diseñador Gráfico | Valida skills: @game-art, etc. |
| Cliente | NUNCA directamente. Siempre vía Orquestador |
```

**Propuesto — Añadir:**

```markdown
| Mobile/Desktop Dev | Define arquitectura mobile/desktop que él implementa |
| Data Analyst | Define arquitectura de datos y pipelines |
| Security Auditor | Coordina requerimientos de seguridad en diseño |
| DevOps Engineer | Define requerimientos de infraestructura |
| Frontend Developer | Define arquitectura de componentes web |
| Backend Developer | Define arquitectura server-side y contratos API |
```

### 8.2 Cambios en SKILLS @construccion-agentes

Añadir en la entrevista (6 preguntas) una pregunta explícita sobre **tipo de plataforma objetivo** (web, móvil, escritorio, embebido, IA/ML, data pipeline) para que el diseño de arquitectura no asuma web por defecto.

### 8.3 Cambios en Descripción

En `./agente_arquitecto/historia_y_descripcion.md`, la línea:

> "Especialidad: Arquitectura de software, escalabilidad, y diseño de perfiles de agentes de alto rendimiento."

Cambiar a:

> "Especialidad: Arquitectura de software multiplataforma (web, móvil, escritorio, IA/datos), escalabilidad, y diseño de perfiles de agentes de alto rendimiento."

---

## 9. Estructura de Carpetas Propuesta

```
Agentes vip/
├── README.md                          ← Plan maestro
├── PROPUESTAS_NUEVOS_AGENTES.md       ← Documento estratégico de 9 nuevos agentes
├── agente_arquitecto/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_orquestador/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_frontend/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_backend/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_mobile_desktop/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_copywriter/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_seo/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_ui_ux/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_devops/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_qa_testing/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_data_analyst/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_security_auditor/
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_ai_engineer/                ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_product_manager/            ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_growth_revops/              ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_paid_media/                 ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_game_developer/             ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_3d_character/               ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_customer_support/           ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_media_video/                ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── agente_agentops/                   ← NUEVO
│   ├── perfil.md
│   └── historia_y_descripcion.md
├── skills/                            ← Skills externalizadas por agente
│   ├── arquitecto/
│   ├── orquestador/
│   ├── frontend/
│   ├── backend/
│   ├── mobile_desktop/
│   ├── copywriter/
│   ├── seo/
│   ├── ui_ux/
│   ├── devops/
│   ├── qa_testing/
│   ├── data_analyst/
│   ├── security_auditor/
│   ├── ai_engineer/
│   ├── product_manager/
│   ├── growth_revops/
│   ├── paid_media/
│   ├── game_developer/
│   ├── 3d_character/
│   ├── customer_support/
│   ├── media_video/
│   └── agentops/
├── crews/
│   └── integracion_crewai.py          ← Factory de agentes y crews
└── meta/
    ├── auditoria-reglas.md
    └── bitacora_agencia.md
```

---

## 10. Próximos Pasos

| # | Acción | Estado |
|---|--------|--------|
| 1 | Aplicar cambios al perfil del Arquitecto (Sección 8) | ✅ Completado |
| 2 | Crear `perfil.md` del Orquestador | ✅ Completado |
| 3 | Crear `perfil.md` de cada agente ejecutor (10 restantes) | ✅ Completado |
| 4 | Crear `historia_y_descripcion.md` de cada agente | ✅ Completado |
| 5 | Externalizar skills a `./skills/<agente>/` | ✅ Completado — 149 archivos |
| 6 | Crear 9 agentes nuevos (perfil + historia + skills) | ✅ Completado |
| 7 | Implementar `crews/integracion_crewai.py` con factory de agentes | ✅ Completado |
| 8 | Auditar todos los perfiles con checklist P1-P8 del Arquitecto | Pendiente |

---

## 11. Validación P1-P8

Verificación de que este plan cumple los principios del Arquitecto:

| # | Principio | Estado | Evidencia |
|---|-----------|--------|-----------|
| P1 | Rol sin ambigüedad | ✅ | Cada agente tiene rol ≤15 palabras + lista de NO hace |
| P2 | Output con estructura | ✅ | Tablas parseables, markdown estructurado |
| P3 | Triggers explícitos | ✅ | Sección 7 define cuándo se activa cada agente |
| P4 | Fallos anticipados | ⏳ | Se definirán en cada perfil individual |
| P5 | Un nivel abstracción por sección | ✅ | Estratégico (Sección 2-4) / Táctico (5-7) / Operativo (6,9) |
| P6 | Skills como referencia | ✅ | Skills en tabla, detalle en repo Antigravity (L2) |
| P7 | Sin rutas hardcodeadas | ✅ | Todas las rutas relativas a raíz del proyecto |
| P8 | Trazabilidad | ✅ | Skills mapeados a repo con links, origen documentado |
