from fastapi import APIRouter
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.db_ping import router as db_router
from app.api.v1.endpoints.jobs import router as jobs_router
from app.api.v1.endpoints.file_test import router as file_test_router
from app.api.v1.endpoints.candidates_upload import router as candidates_upload_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(db_router)
api_router.include_router(jobs_router)
api_router.include_router(file_test_router)
api_router.include_router(candidates_upload_router)
