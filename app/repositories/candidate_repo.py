from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.candidate import Candidate


class CandidateRepository:
    def create_many(self, db: Session, candidates: list[Candidate]) -> list[Candidate]:
        db.add_all(candidates)
        db.commit()
        for c in candidates:
            db.refresh(c)
        return candidates

    def list_by_batch_id(self, db: Session, batch_id: int) -> list[Candidate]:
        stmt = select(Candidate).where(Candidate.batch_id == batch_id).order_by(Candidate.id.asc())
        return list(db.execute(stmt).scalars().all())
