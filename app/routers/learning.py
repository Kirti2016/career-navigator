from fastapi import APIRouter

router = APIRouter()

@router.get("/plan")
def learning_plan():
    return {"plan": ["Step 1: Learn Python", "Step 2: Learn FastAPI", "Step 3: Build Projects"]}
