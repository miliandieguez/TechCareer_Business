from pydantic import BaseModel


class CandidateInBatch(BaseModel):
    id: int
    original_filename: str
    status: str
    file_path: str


class BatchStatusRead(BaseModel):
    id: int
    job_id: int
    status: str
    total_files: int
    processed_files: int
    failed_files: int
    candidates: list[CandidateInBatch]
