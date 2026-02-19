from pydantic import BaseModel


class BatchRead(BaseModel):
    id: int
    job_id: int
    status: str
    total_files: int
    processed_files: int
    failed_files: int

    class Config:
        from_attributes = True
