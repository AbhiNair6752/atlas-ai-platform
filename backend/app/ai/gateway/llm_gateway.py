from app.ai.llm import llm
from pydantic import BaseModel

class LLMGateway:

    def generate_response(
            self,
            prompt: str
    ) -> str:
        return llm.generate_response(prompt)
    
    def stream_response(
            self,
            prompt: str
    ) -> str:
        return llm.stream_response(prompt)
    
    def generate_structured_response(
            self,
            prompt: str,
            response_model: type[BaseModel]
    ) -> BaseModel:
        return llm.generate_structured_response(
            prompt,
            response_model
        )
llm_gateway = LLMGateway()