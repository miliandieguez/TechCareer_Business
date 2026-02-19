import os
import uuid
from pathlib import Path

from fastapi import UploadFile

from app.core.config import settings


class StorageService:
    def __init__(self):
        self.base_dir = Path(settings.storage_dir)

    def ensure_storage_dir(self) -> None:
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_pdf(self, upload: UploadFile) -> str:
        """
        Guarda un UploadFile PDF en storage/ y devuelve la ruta (string).
        Validación MVP:
        - content_type debe ser application/pdf (si viene vacío, validamos por extensión)
        - extensión .pdf
        """
        self.ensure_storage_dir()

        filename = upload.filename or ""
        ext = Path(filename).suffix.lower()

        # validación simple
        if upload.content_type and upload.content_type != "application/pdf":
            raise ValueError("only PDF files are allowed")

        if ext != ".pdf":
            # algunos clientes no envían content_type fiable, así que también exigimos extensión
            raise ValueError("file must have .pdf extension")

        safe_id = uuid.uuid4().hex
        final_name = f"{safe_id}.pdf"
        final_path = self.base_dir / final_name

        # guardado en streaming (simple y seguro para MVP)
        with open(final_path, "wb") as f:
            while True:
                chunk = upload.file.read(1024 * 1024)  # 1MB
                if not chunk:
                    break
                f.write(chunk)

        # cerramos file handle del UploadFile
        upload.file.close()

        return str(final_path)
