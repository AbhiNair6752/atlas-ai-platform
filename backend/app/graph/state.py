from typing import TypedDict

class GraphState(TypedDict):
    question: str
    session_id: str
    intent: str
    answer: str
    sources: list
    evaluation: dict