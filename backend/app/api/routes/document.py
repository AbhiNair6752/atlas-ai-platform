from fastapi import APIRouter, UploadFile, File
from app.schemas.document import UploadResponse
from app.services.document_service import document_service

router = APIRouter()

@router.post("/document/upload", response_model=UploadResponse)
def upload_document(
    file: UploadFile = File()
):
    result = document_service.upload_document(
        file
    )

    return UploadResponse(
        filename=result["filename"],
        message="Document uploaded successfully."
    )