from fastapi import APIRouter
from app.models.profile import ProfileInput, ProfileResult
from app.services.profile_analyzer import analyze_profile

router = APIRouter()

@router.post("/", response_model=ProfileResult)
def process_profile(data: ProfileInput):
    return analyze_profile(data)
