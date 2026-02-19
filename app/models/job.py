from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # MVP: lo guardamos como texto. luego lo haremos mejor (tabla o json)
    must_have_skills: Mapped[str] = mapped_column(Text, nullable=False, default="")
    nice_to_have_skills: Mapped[str] = mapped_column(Text, nullable=False, default="")

    seniority_expected: Mapped[str] = mapped_column(String(50), nullable=False, default="unknown")

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
