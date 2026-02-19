from sqlalchemy.orm import Session

from app.repositories.batch_repo import BatchRepository
from app.repositories.candidate_repo import CandidateRepository


class BatchService:
    def __init__(self):
        self.batches = BatchRepository()
        self.candidates = CandidateRepository()

    def get_batch_status(self, db: Session, batch_id: int) -> dict | None:
        batch = self.batches.get_by_id(db, batch_id)
        if not batch:
            return None

        candidates = self.candidates.list_by_batch_id(db, batch_id)

        return {
            "id": batch.id,
            "job_id": batch.job_id,
            "status": batch.status,
            "total_files": batch.total_files,
            "processed_files": batch.processed_files,
            "failed_files": batch.failed_files,
            "candidates": [
                {
                    "id": c.id,
                    "original_filename": c.original_filename,
                    "status": c.status,
                    "file_path": c.file_path,
                }
                for c in candidates
            ],
        }
