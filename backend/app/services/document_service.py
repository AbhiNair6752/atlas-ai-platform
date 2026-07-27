from pathlib import Path
import shutil
from fastapi import UploadFile

from app.ai.pdf_processor import pdf_processor
from app.ai.text_chunker import text_chunker

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

        chunks = text_chunker.chunk_text(
            extracted_text
        )
        print("\n" + "=" * 80)
        print(f"Document: {file.filename}")
        print(f"Total chunks : {len(chunks)}")
        print("=" * 80)

        for i, chunk in enumerate(chunks, start=1):
            print(f"\n chunk{i}")
            print("-" * 80)
            print(chunk)
        print("=" * 80 + "\n")

        return {
            "filename": file.filename,
            "text": extracted_text,
            "chunks": chunks
        }
    
document_service = DocumentService()