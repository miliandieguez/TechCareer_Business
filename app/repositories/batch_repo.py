from sqlalchemy.orm import Session
from app.models.batch import Batch


class BatchRepository:
    def create(self, db: Session, batch: Batch) -> Batch:
        db.add(batch)
        db.commit()
        db.refresh(batch)
        return batch

    def update(self, db: Session, batch: Batch) -> Batch:
        db.add(batch)
        db.commit()
        db.refresh(batch)
        return batch

    def get_by_id(self, db: Session, batch_id: int) -> Batch | None:
        return db.get(Batch, batch_id)
