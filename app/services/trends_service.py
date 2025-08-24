# app/services/trends_service.py

from app.services.groq_client import ask_llm

async def get_trends(field: str):
    """
    Fetch career or industry trends using Groq AI.
    """
    prompt = f"Provide the latest trends in {field} career/industry for students and professionals."
    response = await ask_llm(prompt)
    return response
