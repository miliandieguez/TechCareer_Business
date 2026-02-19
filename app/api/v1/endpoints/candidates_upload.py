from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.upload_service import UploadService

router = APIRouter(prefix="/jobs", tags=["candidates"])
service = UploadService()


@router.post("/{job_id}/candidates/upload")
def upload_candidates(job_id: int, files: list[UploadFile] = File(...), db: Session = Depends(get_db)):
    result = service.upload_candidates(db, job_id, files)

    if result.get("error") == "job_not_found":
        raise HTTPException(status_code=404, detail="job not found")
    if result.get("error") == "no_files":
        raise HTTPException(status_code=400, detail="no files provided")

    return result
