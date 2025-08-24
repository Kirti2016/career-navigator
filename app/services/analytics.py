# app/services/analytics.py
from app.services.llm_service import ask_groq_json

async def resume_improvement_suggestions(resume_text: str) -> dict:
    prompt = f"""
You are an ATS optimization expert. Return JSON with:
- summary_suggestions: list[str]
- keyword_gaps: list[str]
- bullet_point_upgrades: list[str] (rewrite 3 weak bullet points)
- formatting_tips: list[str]
RESUME:
{resume_text}
"""
    return await ask_groq_json(prompt)
