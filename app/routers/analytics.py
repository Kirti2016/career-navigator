from fastapi import APIRouter

router = APIRouter()

@router.get("/ats")
def ats_score():
    return {"ats_score": 85, "remarks": "Resume is ATS-friendly ✅"}
