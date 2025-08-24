# app/services/llm_service.py
import os, json
from groq import Groq

# Make sure GROQ_API_KEY is in your environment or .env
_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# A short “JSON only” instruction helps models return valid JSON
JSON_SYSTEM_NUDGE = (
    "You are a strict JSON generator. "
    "Always return a single JSON object, no prose, no markdown, no backticks."
)

def _chat(messages, **kwargs):
    return _client.chat.completions.create(
        model=kwargs.get("model", "mixtral-8x7b-32768"),
        messages=messages,
        temperature=kwargs.get("temperature", 0.2),
        max_tokens=kwargs.get("max_tokens", 1200),
    )

async def ask_llm(prompt: str) -> str:
    """
    Free-form string response (no JSON guarantees).
    """
    r = _chat([{"role": "user", "content": prompt}])
    return r.choices[0].message.content

async def ask_groq_json(prompt: str) -> dict:
    """
    Requests JSON and parses it into a Python dict.
    If parsing fails, returns a stable error payload with the raw text.
    """
    r = _chat([
        {"role": "system", "content": JSON_SYSTEM_NUDGE},
        {"role": "user", "content": prompt + "\nReturn only a JSON object."}
    ])
    text = r.choices[0].message.content
    try:
        return json.loads(text)
    except Exception:
        return {"error": "Invalid JSON from model", "raw": text}
