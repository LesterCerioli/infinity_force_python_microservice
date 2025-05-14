from pydantic import BaseModel
from typing import List

class ProfileInput(BaseModel):
    age: int
    risk_tolerance: str
    investment_goals: List[str]

class ProfileResult(BaseModel):
    profile_type: str
    recommended_cryptos: List[str]
