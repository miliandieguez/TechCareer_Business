from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router

from app.db.session import engine
from app.db.base import Base

# IMPORTANTE: importar modelos para que SQLAlchemy los registre
from app.models.job import Job  # noqa: F401
from app.models.batch import Batch  # noqa: F401
from app.models.candidate import Candidate  # noqa: F401


app = FastAPI(title=settings.app_name)
app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

