# services/roadmap.py
from app.services.llm_service import ask_llm


def build_career_roadmap(current_role: str, target_role: str, current_skills: list[str], weeks: int = 12) -> dict:
    prompt = f"""
Create an actionable {weeks}-week roadmap as JSON with keys:
- overview: short string
- milestones: list of objects: {{ "week": int, "goal": str, "tasks": [str] }}
- resources: list of objects: {{ "title": str, "type": "course|article|tool", "url": str }}
- metrics: list of strings (how to measure progress)

CURRENT_ROLE: {current_role}
TARGET_ROLE: {target_role}
CURRENT_SKILLS: {current_skills}
"""
    return ask_groq_json(prompt)
