from fastapi import APIRouter

router = APIRouter()

@router.get("/advice")
def career_advice():
    return {"advice": "Focus on AI + Web3 + Robotics for future growth"}
