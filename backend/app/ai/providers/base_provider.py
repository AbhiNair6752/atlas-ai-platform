from abc import ABC, abstractmethod
from pydantic import BaseModel

class LLMProvider(ABC):
    """
    Base interface for all LLM providers.

    Every provider (Groq, OpenAI, Claude, Gemini, etc.)
    must implement this interface.
    """

    @abstractmethod
    def generate_response(
        self,
        prompt: str
    ) -> str:
        """
        Generate a text response from the LLM.
        """
        pass

    @abstractmethod
    def stream_response(
        self,
        prompt: str
    ):
        """
        Stream the LLM response token by token.
        """
        pass

    @abstractmethod
    def generate_structured_response(
        self,
        prompt: str,
        response_model: type[BaseModel],
    ) -> BaseModel:
        """
        Generate a structured response that matches
        the supplied Pydantic model.
        """
        pass