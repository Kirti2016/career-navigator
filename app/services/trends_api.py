# services/trends_api.py
from app.services.analytics_service import get_trends


def trending_skills(domain: str = "software", location: str = "global") -> dict:
    prompt = f"""
List top 10 trending skills for {domain} in {location} as JSON:
{{ "skills": [{{"name": str, "growth_index": int, "category": str, "note": str}}] }}
- growth_index: 1-100 where 100 = fastest growing.
"""
    return ask_groq_json(prompt)

def trending_jobs(domain: str = "software", location: str = "global") -> dict:
    prompt = f"""
List top 10 in-demand job titles for {domain} in {location} as JSON:
{{ "jobs": [{{"title": str, "demand_index": int, "why_hiring": str}}] }}
- demand_index: 1-100 where 100 = highest hiring demand.
"""
    return ask_groq_json(prompt)
