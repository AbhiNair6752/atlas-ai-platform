from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    score: float
    text: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]