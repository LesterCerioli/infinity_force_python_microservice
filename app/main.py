from fastapi import FastAPI
from app.api.v1.endpoints import profiles

app = FastAPI(title="Investor Profile Microservice")

app.include_router(profiles.router, prefix="/api/v1/profiles", tags=["profiles"])
