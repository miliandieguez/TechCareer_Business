from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.batch_status import BatchStatusRead
from app.services.batch_service import BatchService

router = APIRouter(prefix="/batches", tags=["batches"])
service = BatchService()


@router.get("/{batch_id}", response_model=BatchStatusRead)
def get_batch(batch_id: int, db: Session = Depends(get_db)):
    data = service.get_batch_status(db, batch_id)
    if not data:
        raise HTTPException(status_code=404, detail="batch not found")
    return data
