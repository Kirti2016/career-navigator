from fastapi import APIRouter

router = APIRouter()

@router.get("/skills")
def trending_skills():
    return {"trending_skills": ["AI", "Web3", "Robotics", "Cloud"]}
