# app/services/nlp_parser.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_resume_with_ai(resume_text: str):
    """
    Uses OpenAI GPT model to extract structured information from resume text.
    """
    prompt = f"""
    You are an AI resume parser. Extract the following details from the resume text below.
    Return the result in strict JSON format.

    Resume text:
    {resume_text}

    JSON format:
    {{
        "name": "string",
        "email": "string",
        "phone": "string",
        "education": ["list of degrees with years"],
        "skills": ["list of skills"],
        "experience": ["list of job titles, companies, durations"]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
