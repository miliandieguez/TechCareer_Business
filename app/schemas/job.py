from pydantic import BaseModel, Field


class JobCreate(BaseModel):
    title: str = Field(min_length=2, max_length=255)
    description: str = Field(min_length=10)

    # en el API los manejamos como listas (más cómodo)
    must_have_skills: list[str] = Field(default_factory=list)
    nice_to_have_skills: list[str] = Field(default_factory=list)

    # "junior" | "mid" | "senior" | "lead" | "unknown"
    seniority_expected: str = Field(default="unknown", max_length=50)


class JobRead(BaseModel):
    id: int
    title: str
    description: str
    must_have_skills: list[str]
    nice_to_have_skills: list[str]
    seniority_expected: str

    # permite construir JobRead desde objetos ORM (más adelante nos irá bien)
    class Config:
        from_attributes = True
