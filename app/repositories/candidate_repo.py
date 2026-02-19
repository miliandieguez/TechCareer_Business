from sqlalchemy.orm import Session
from app.models.candidate import Candidate


class CandidateRepository:
    def create_many(self, db: Session, candidates: list[Candidate]) -> list[Candidate]:
        db.add_all(candidates)
        db.commit()
        for c in candidates:
            db.refresh(c)
        return candidates
