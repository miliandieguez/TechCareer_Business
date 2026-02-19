from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["db"])


@router.get("/db/ping")
def db_ping(db: Session = Depends(get_db)):
    value = db.execute(text("SELECT 1")).scalar_one()
    return {"db": "ok", "value": value}
