from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    question: str


class Source(BaseModel):
    score: float
    text: str

class EvaluationResponse(BaseModel):
    grounded: bool
    retrieved_chunks: int


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]
    evaluation: EvaluationResponse

