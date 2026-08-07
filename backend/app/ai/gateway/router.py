from app.ai.providers.base_provider import LLMProvider
from app.ai.providers.groq_provider import groq_provider


class LLMRouter:
    """
    Decides which LLM provider should handle a request.

    Version 1:
    Always returns the Groq provider.
    """

    def get_provider(
            self,
            task: str | None = None
    ) -> LLMProvider:
        return groq_provider
    
llm_router = LLMRouter()
