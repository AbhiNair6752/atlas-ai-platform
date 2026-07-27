from pathlib import Path
import shutil
from fastapi import UploadFile

from app.ai.pdf_processor import pdf_processor

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
        extracted_text = pdf_processor.extract_text(
            str(file_path)
        )

        return {
            "filename": file.filename,
            "text": extracted_text
        }
    
document_service = DocumentService()