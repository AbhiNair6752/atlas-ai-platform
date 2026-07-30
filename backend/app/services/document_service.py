from pathlib import Path
import shutil
from fastapi import UploadFile

from app.ai.pdf_processor import pdf_processor
from app.ai.text_chunker import text_chunker
from app.ai.embedding_service import embedding_service
from app.ai.vector_store import vector_store

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

        embeddings = embedding_service.generate_embeddings(
            chunks
        )
        vector_store.add_documents(
            chunks=chunks,
            embeddings=embeddings,
            filename=file.filename
        )
        print("=" * 80)

        print(f"Document: {file.filename}")

        print(f"Chunks: {len(chunks)}")

        print(f"Embeddings: {len(embeddings)}")

        print(f"Embedding Dimension: {len(embeddings[0])}")

        print("=" * 80)

        return {
            "filename": file.filename,
            "text": extracted_text,
            "chunks": chunks,
            "embeddings": embeddings
        }
    
document_service = DocumentService()