from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = chat_service.chat(session_id= request.session_id,
                               query = request.question)
    
    return ChatResponse(
        question=result["question"],
        answer=result["answer"],
        sources=result["sources"],
        evaluation=result["evaluation"]
    )