from sqlalchemy.orm import Session

from app.models.job import Job
from app.repositories.job_repo import JobRepository
from app.schemas.job import JobCreate


def _skills_list_to_text(skills: list[str]) -> str:
    # guardamos "python,sql,tableau"
    cleaned = [s.strip().lower() for s in skills if s and s.strip()]
    return ",".join(cleaned)


def _skills_text_to_list(text_value: str) -> list[str]:
    if not text_value:
        return []
    return [s.strip() for s in text_value.split(",") if s.strip()]


class JobService:
    def __init__(self):
        self.repo = JobRepository()

    def create_job(self, db: Session, payload: JobCreate) -> dict:
        job = Job(
            title=payload.title,
            description=payload.description,
            must_have_skills=_skills_list_to_text(payload.must_have_skills),
            nice_to_have_skills=_skills_list_to_text(payload.nice_to_have_skills),
            seniority_expected=payload.seniority_expected.strip().lower(),
        )
        job = self.repo.create(db, job)

        return {
            "id": job.id,
            "title": job.title,
            "description": job.description,
            "must_have_skills": _skills_text_to_list(job.must_have_skills),
            "nice_to_have_skills": _skills_text_to_list(job.nice_to_have_skills),
            "seniority_expected": job.seniority_expected,
        }

    def get_job(self, db: Session, job_id: int) -> dict | None:
        job = self.repo.get_by_id(db, job_id)
        if not job:
            return None

        return {
            "id": job.id,
            "title": job.title,
            "description": job.description,
            "must_have_skills": _skills_text_to_list(job.must_have_skills),
            "nice_to_have_skills": _skills_text_to_list(job.nice_to_have_skills),
            "seniority_expected": job.seniority_expected,
        }
