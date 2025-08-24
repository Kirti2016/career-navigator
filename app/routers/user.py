from fastapi import APIRouter, Depends
from app.utils.security import get_current_user

router = APIRouter()

@router.get("/profile")
def read_profile(current_user: str = Depends(get_current_user)):
    return {"email": current_user}
