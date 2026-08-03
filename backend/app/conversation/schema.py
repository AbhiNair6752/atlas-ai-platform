from pydantic import BaseModel,Field
from typing import List, Literal

class Message(BaseModel):
    role: Literal[
        "system",
        "user",
        "assistant",
        "tool"
    ]

    content: str

class ConversationTurn(BaseModel):
    session_id: str
    messages: List[Message]
    intent: str
    selected_documents: List[str] = Field(
        default_factory=list
    )
    sources: List[str] = Field(
        default_factory=list
    )