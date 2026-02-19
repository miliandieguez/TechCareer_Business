from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "TechCareer for Companies API"
    api_v1_prefix: str = "/api/v1"
    database_url: str

    # carpeta local para guardar CVs (relativa a la raíz del proyecto)
    storage_dir: str = "storage"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

