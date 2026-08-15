from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service
from app.services.graph_service import graph_service
from app.schemas.chat import ApprovalRequest

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = graph_service.chat(session_id= request.session_id,
                               question= request.question)
    evaluation = result.get("evaluation")

    if not evaluation:
        evaluation = None
    
    return ChatResponse(
        question=result["question"],
        answer=result["answer"],
        sources=result["sources"],
        evaluation=evaluation
    )

@router.post("/chat/approve")
def approve_chat(request:ApprovalRequest):

    result = graph_service.resume(
        session_id=request.session_id,
        approved=request.approved
    )
    return result