from pathlib import Path
import shutil
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

class DocumentService:
    def upload_document(
            self,
            file: UploadFile
    ):
        file_path = UPLOAD_DIR / file.filename
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        return file.filename
    
document_service = DocumentService()