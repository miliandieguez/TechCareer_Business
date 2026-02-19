from fastapi import APIRouter
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.db_ping import router as db_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(db_router)
