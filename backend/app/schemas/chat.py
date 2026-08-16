from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    question: str


class Source(BaseModel):
    score: float
    text: str

class SourceResponse(BaseModel):
    text: str
    score: float

class EvaluationResponse(BaseModel):
    grounded: bool
    relevance: int
    faithfulness: int
    completeness: int
    overall_score: int
    feedback: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse]
    evaluation: EvaluationResponse | None = None

class ApprovalRequest(BaseModel):
    session_id: str
    approved: bool

class ApprovalRequiredResponse(BaseModel):
    status: str
    session_id: str
    message: str
    question: str
    intent: str
