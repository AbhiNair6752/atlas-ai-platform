from fastapi import APIRouter

from app.schemas.chat import chatRequest, ChatResponse
from app.ai.chat_service import chat_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: chatRequest):

    response = chat_service.chat(
        request.message
    )
    return ChatResponse(
        response=response
    )