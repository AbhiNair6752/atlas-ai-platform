from enum import Enum


class LLMTask(str, Enum):
    CHAT = "chat"

    SUMMARY = "summary"

    COMPARISON = "comparison"

    PLANNER = "planner"

    DOCUMENT_SELECTOR = "document_selector"