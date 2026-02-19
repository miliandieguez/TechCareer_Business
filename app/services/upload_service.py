from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.batch import Batch
from app.models.candidate import Candidate
from app.repositories.batch_repo import BatchRepository
from app.repositories.candidate_repo import CandidateRepository
from app.repositories.job_repo import JobRepository
from app.services.storage_service import StorageService


class UploadService:
    def __init__(self):
        self.jobs = JobRepository()
        self.batches = BatchRepository()
        self.candidates = CandidateRepository()
        self.storage = StorageService()

    def upload_candidates(self, db: Session, job_id: int, files: list[UploadFile]) -> dict:
        # 1) comprobar job existe
        job = self.jobs.get_by_id(db, job_id)
        if not job:
            return {"error": "job_not_found"}

        if not files:
            return {"error": "no_files"}

        # 2) crear batch
        batch = Batch(
            job_id=job_id,
            status="PENDING",
            total_files=0,
            processed_files=0,
            failed_files=0,
        )
        batch = self.batches.create(db, batch)

        # 3) guardar archivos + crear candidates
        created: list[Candidate] = []
        failed: list[dict] = []

        for f in files:
            try:
                path = self.storage.save_pdf(f)
                created.append(
                    Candidate(
                        job_id=job_id,
                        batch_id=batch.id,
                        original_filename=f.filename or "unknown.pdf",
                        file_path=path,
                        status="UPLOADED",
                    )
                )
            except Exception as e:
                failed.append({"filename": f.filename, "error": str(e)})

        if created:
            self.candidates.create_many(db, created)

        # 4) actualizar batch totals
        batch.total_files = len(files)
        batch.failed_files = len(failed)
        batch.processed_files = 0  # todavía no procesamos
        batch.status = "PENDING" if len(created) > 0 else "FAILED"
        batch = self.batches.update(db, batch)

        return {
            "batch_id": batch.id,
            "job_id": job_id,
            "status": batch.status,
            "total_files": batch.total_files,
            "created_candidates": len(created),
            "failed_files": failed,
        }
