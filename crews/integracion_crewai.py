from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List

from crewai import Agent, Crew, Process


BASE_DIR = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class AgentConfig:
    slug: str
    role: str
    goal: str
    allow_delegation: bool = False
    verbose: bool = True

    @property
    def directory(self) -> Path:
        return BASE_DIR / self.slug

    @property
    def profile_slug(self) -> str:
        return self.slug.replace("agente_", "", 1)

    @property
    def perfil_path(self) -> Path:
        return self.directory / f"perfil_{self.profile_slug}.md"

    @property
    def historia_path(self) -> Path:
        return self.directory / "historia_y_descripcion.md"


AGENT_CONFIGS: Dict[str, AgentConfig] = {
    "orquestador": AgentConfig(
        slug="agente_orquestador",
        role="Coordinador central de agencia digital",
        goal="Distribuir tareas al agente correcto, priorizar entregas y consolidar resultados con calidad",
        allow_delegation=True,
    ),
    "arquitecto": AgentConfig(
        slug="agente_arquitecto",
        role="Meta-agente de diseño de sistemas y arquitecturas de software",
        goal="Definir arquitectura técnica, límites entre agentes y criterios estructurales del sistema",
    ),
    "frontend": AgentConfig(
        slug="agente_frontend",
        role="Desarrollador de interfaces web modernas y performantes",
        goal="Implementar interfaces web responsivas, accesibles y de alto rendimiento",
    ),
    "backend": AgentConfig(
        slug="agente_backend",
        role="Desarrollador server-side de APIs y lógica de negocio",
        goal="Construir backends robustos, seguros y escalables con APIs bien definidas",
    ),
    "mobile_desktop": AgentConfig(
        slug="agente_mobile_desktop",
        role="Desarrollador multiplataforma de apps móviles y de escritorio",
        goal="Construir apps nativas y cross-platform de alta calidad para mobile y desktop",
    ),
    "copywriter": AgentConfig(
        slug="agente_copywriter",
        role="Redactor creativo y estratégico de contenido digital",
        goal="Crear copy persuasivo, contenido de marca y textos orientados a conversión",
    ),
    "seo": AgentConfig(
        slug="agente_seo",
        role="Especialista en posicionamiento orgánico y visibilidad en buscadores",
        goal="Maximizar visibilidad orgánica mediante SEO técnico, on-page y estrategia de contenido",
    ),
    "ui_ux": AgentConfig(
        slug="agente_ui_ux",
        role="Diseñador visual de experiencias digitales y branding",
        goal="Crear diseños visuales atractivos, usables y coherentes con la marca",
    ),
    "devops": AgentConfig(
        slug="agente_devops",
        role="Ingeniero de infraestructura, CI/CD y operaciones cloud",
        goal="Automatizar deployment, mantener infraestructura confiable y optimizar operación",
    ),
    "qa_testing": AgentConfig(
        slug="agente_qa_testing",
        role="Ingeniero de calidad y validación de entregas",
        goal="Garantizar calidad mediante pruebas, debugging y revisión técnica antes de entregar",
    ),
    "data_analyst": AgentConfig(
        slug="agente_data_analyst",
        role="Analista de datos, métricas financieras y visualización",
        goal="Transformar datos en insights accionables mediante análisis, métricas y visualizaciones",
    ),
    "security_auditor": AgentConfig(
        slug="agente_security_auditor",
        role="Auditor de seguridad especializado en vulnerabilidades y hardening",
        goal="Identificar, priorizar y mitigar vulnerabilidades de seguridad en código e infraestructura",
    ),
    "ai_engineer": AgentConfig(
        slug="agente_ai_engineer",
        role="Ingeniero de IA aplicada: LLM, RAG, context engineering y evals",
        goal="Diseñar y construir productos de IA en producción con evaluación rigurosa",
    ),
    "product_manager": AgentConfig(
        slug="agente_product_manager",
        role="Estratega de producto: discovery, PRDs, backlog y lanzamiento",
        goal="Definir qué construir, para quién y cómo medir éxito antes de desarrollo",
    ),
    "growth_revops": AgentConfig(
        slug="agente_growth_revops",
        role="Operador de crecimiento e ingresos: CRM, outreach y revenue operations",
        goal="Diseñar y automatizar el motor de ingresos del cliente",
    ),
    "paid_media": AgentConfig(
        slug="agente_paid_media",
        role="Especialista en publicidad paga y performance creative",
        goal="Maximizar ROI de campañas pagas con hipótesis, testing y optimización continua",
    ),
    "game_developer": AgentConfig(
        slug="agente_game_developer",
        role="Desarrollador de videojuegos: gameplay, engines y optimización",
        goal="Construir experiencias interactivas jugables y optimizadas por plataforma",
    ),
    "3d_character": AgentConfig(
        slug="agente_3d_character",
        role="Diseñador de personajes 3D: concept, modelado, texturizado y rigging",
        goal="Producir personajes 3D game-ready con pipeline de producción completo",
    ),
    "customer_support": AgentConfig(
        slug="agente_customer_support",
        role="Soporte y éxito del cliente: onboarding, knowledge base y retención",
        goal="Resolver problemas del usuario y convertir soporte en mejoras de producto",
    ),
    "media_video": AgentConfig(
        slug="agente_media_video",
        role="Producción multimedia: video, clips, repurposing y contenido social",
        goal="Producir contenido audiovisual adaptado a cada plataforma con datos de rendimiento",
    ),
    "agentops": AgentConfig(
        slug="agente_agentops",
        role="Evaluador y optimizador de agentes IA: evals, prompts y mejora continua",
        goal="Medir, evaluar y mejorar la calidad de agentes IA con datos y baselines",
    ),
}


PROJECT_COMPOSITIONS: Dict[str, List[str]] = {
    "web": [
        "orquestador",
        "arquitecto",
        "frontend",
        "backend",
        "seo",
        "copywriter",
        "ui_ux",
        "qa_testing",
        "devops",
    ],
    "mobile": [
        "orquestador",
        "arquitecto",
        "mobile_desktop",
        "backend",
        "ui_ux",
        "qa_testing",
        "devops",
    ],
    "desktop": [
        "orquestador",
        "arquitecto",
        "mobile_desktop",
        "backend",
        "qa_testing",
        "devops",
    ],
    "marketing": [
        "orquestador",
        "copywriter",
        "seo",
        "ui_ux",
        "data_analyst",
    ],
    "analytics": ["orquestador", "data_analyst"],
    "security": ["orquestador", "security_auditor", "devops"],
    "branding": ["orquestador", "ui_ux", "copywriter", "frontend"],
    "ecommerce": [
        "orquestador",
        "arquitecto",
        "frontend",
        "backend",
        "seo",
        "copywriter",
        "ui_ux",
        "qa_testing",
        "devops",
        "security_auditor",
        "data_analyst",
    ],
    "full": list(AGENT_CONFIGS.keys()),
    "ai_product": [
        "orquestador",
        "arquitecto",
        "ai_engineer",
        "backend",
        "frontend",
        "qa_testing",
        "agentops",
        "security_auditor",
    ],
    "saas": [
        "orquestador",
        "arquitecto",
        "product_manager",
        "frontend",
        "backend",
        "ui_ux",
        "seo",
        "copywriter",
        "data_analyst",
        "growth_revops",
        "paid_media",
        "customer_support",
        "qa_testing",
        "devops",
        "security_auditor",
    ],
    "videogame": [
        "orquestador",
        "arquitecto",
        "game_developer",
        "3d_character",
        "ui_ux",
        "qa_testing",
    ],
    "growth": [
        "orquestador",
        "growth_revops",
        "paid_media",
        "copywriter",
        "seo",
        "data_analyst",
        "media_video",
    ],
    "content": [
        "orquestador",
        "copywriter",
        "seo",
        "media_video",
        "ui_ux",
        "data_analyst",
    ],
}


def _read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo requerido: {path}")
    return path.read_text(encoding="utf-8").strip()


def _read_skills(agent_slug: str) -> str:
    """Lee todos los archivos de skills del agente y los concatena."""
    skills_dir = BASE_DIR / "skills" / agent_slug.replace("agente_", "")
    if not skills_dir.exists():
        return ""
    skill_files = sorted(skills_dir.glob("*.md"))
    if not skill_files:
        return ""
    parts = []
    for sf in skill_files:
        parts.append(sf.read_text(encoding="utf-8").strip())
    return "\n\n---\n\n".join(parts)


def build_backstory(config: AgentConfig) -> str:
    perfil = _read_text(config.perfil_path)
    historia = _read_text(config.historia_path)
    skills = _read_skills(config.slug)
    backstory = (
        "Tu comportamiento operativo está definido por documentos locales del proyecto. "
        "Debes tratarlos como fuente primaria de contexto y límites de actuación.\n\n"
        f"[PERFIL OPERATIVO]\n{perfil}\n\n"
        f"[HISTORIA Y DESCRIPCION]\n{historia}"
    )
    if skills:
        backstory += f"\n\n[SKILLS DETALLADAS]\n{skills}"
    return backstory


def build_agent(agent_key: str, **agent_overrides) -> Agent:
    if agent_key not in AGENT_CONFIGS:
        valid_keys = ", ".join(sorted(AGENT_CONFIGS))
        raise KeyError(f"Agente desconocido: {agent_key}. Opciones válidas: {valid_keys}")

    config = AGENT_CONFIGS[agent_key]
    payload = {
        "role": config.role,
        "goal": config.goal,
        "backstory": build_backstory(config),
        "verbose": config.verbose,
        "allow_delegation": config.allow_delegation,
    }
    payload.update(agent_overrides)
    return Agent(**payload)


def build_agents(agent_keys: Iterable[str]) -> Dict[str, Agent]:
    return {agent_key: build_agent(agent_key) for agent_key in agent_keys}


def build_full_crew(tasks: List | None = None, **crew_overrides) -> Crew:
    agents = build_agents(PROJECT_COMPOSITIONS["full"])
    orquestador = agents["orquestador"]

    payload = {
        "agents": list(agents.values()),
        "tasks": tasks or [],
        "process": Process.hierarchical,
        "manager_agent": orquestador,
        "verbose": True,
    }
    payload.update(crew_overrides)
    return Crew(**payload)


def build_project_crew(project_type: str, tasks: List | None = None, **crew_overrides) -> Crew:
    if project_type not in PROJECT_COMPOSITIONS:
        valid_types = ", ".join(sorted(PROJECT_COMPOSITIONS))
        raise KeyError(f"Tipo de proyecto desconocido: {project_type}. Opciones válidas: {valid_types}")

    agent_keys = PROJECT_COMPOSITIONS[project_type]
    agents = build_agents(agent_keys)
    orquestador = agents["orquestador"]

    payload = {
        "agents": list(agents.values()),
        "tasks": tasks or [],
        "process": Process.hierarchical,
        "manager_agent": orquestador,
        "verbose": True,
    }
    payload.update(crew_overrides)
    return Crew(**payload)


if __name__ == "__main__":
    crew = build_full_crew()
    print("Crew creado con", len(crew.agents), "agentes")
    print("Manager:", crew.manager_agent.role)