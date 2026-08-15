from typing import TypedDict

class GraphState(TypedDict):
    question: str
    session_id: str
    intent: str
    answer: str
    sources: list[str]
    evaluation: dict | None
    conversation_history: list
    selected_documents: list[str]
    history: list[dict]