from app.ai.llm import llm
from pydantic import BaseModel
from app.ai.gateway.router import llm_router

class LLMGateway:

    def generate_response(
            self,
            prompt: str,
            task: str | None = None
    ) -> str:
        
        provider = llm_router.get_provider(task)
        return provider.generate_response(prompt)
    
    def stream_response(
            self,
            prompt: str,
            task: str | None = None
    ) -> str:
        provider = llm_router.get_provider(task)
        return provider.stream_response(prompt)
    
    def generate_structured_response(
            self,
            prompt: str,
            response_model: type[BaseModel],
            task: str | None = None
    ) -> BaseModel:
        
        provider = llm_router.get_provider(task)
        return provider.generate_structured_response(
            prompt,
            response_model
        )
llm_gateway = LLMGateway()