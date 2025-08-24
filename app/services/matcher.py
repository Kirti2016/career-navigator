# services/matcher.py
from app.services.llm_service import ask_llm

def match_resume_to_job(resume_text: str, job_description: str) -> dict:
    prompt = f"""
You are an ATS assistant. Compare this resume to the job description and return JSON with:
- match_score: 0-100 (integer)
- matched_keywords: list of strings
- missing_keywords: list of strings
- summary: short string (<= 60 words)
- section_suggestions: object {{"summary": "...", "skills": "...", "experience": "..."}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""
    data = ask_groq_json(prompt)
    # Minimal normalization
    if "match_score" in data:
        try:
            data["match_score"] = int(round(float(data["match_score"])))
        except Exception:
            pass
    return data
