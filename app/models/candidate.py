from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False, index=True)
    batch_id: Mapped[int] = mapped_column(ForeignKey("batches.id"), nullable=False, index=True)

    # info del archivo
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)  # ruta local donde guardamos el pdf

    # estado del procesamiento del cv (más adelante)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="UPLOADED")

    # campos para siguientes épocas (los dejamos ya previstos)
    raw_text: Mapped[str] = mapped_column(Text, nullable=False, default="")  # pdf -> texto
    extracted_skills: Mapped[str] = mapped_column(Text, nullable=False, default="")  # csv/json simple (mvp)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    batch = relationship("Batch", back_populates="candidates")
