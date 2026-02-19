from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import StorageService

router = APIRouter(tags=["files-test"])
storage = StorageService()


@router.post("/files/test-upload")
def test_upload(file: UploadFile = File(...)):
    try:
        path = storage.save_pdf(file)
        return {"saved": True, "path": path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
