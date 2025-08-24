from pydantic import BaseModel
from typing import List

class TrendingSkill(BaseModel):
    name: str
    growth: float   # growth percentage (example: 12.5)
    demand: int     # number of job postings / mentions

class TrendingJob(BaseModel):
    title: str
    growth: float
    demand: int

class TrendResponse(BaseModel):
    skills: List[TrendingSkill]
    jobs: List[TrendingJob]
