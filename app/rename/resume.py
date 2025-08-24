from pydantic import BaseModel
from typing import Dict

class ParsedResume(BaseModel):
    name: str | None = None
    email: str | None = None
    skills: list[str] = []
    experience: list[str] = []
    education: list[str] = []

class ATSResult(BaseModel):
    ats_score: int
    parsed_resume: ParsedResume

class AnalyzeTextIn(BaseModel):
    text: str
