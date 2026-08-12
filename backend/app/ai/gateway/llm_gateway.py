from app.ai.llm import llm
from pydantic import BaseModel
from app.ai.gateway.router import llm_router
from app.ai.gateway.llm_task import LLMTask
from app.ai.gateway.routing_request import LLMRoutingRequest

class LLMGateway:

    def generate_response(
            self,
            prompt: str,
            task: LLMTask | None = None,
            estimated_tokens: int | None = None
    ) -> str:
        request_routing = LLMRoutingRequest(
            task=task,
            estimated_tokens=estimated_tokens
        )
        
        provider = llm_router.get_provider(request_routing)
        return provider.generate_response(prompt)
    
    def stream_response(
            self,
            prompt: str,
            task: LLMTask | None = None,
    ) -> str:
        routing_request = LLMRoutingRequest(
            task=task,
            requires_streaming=True
        )
        provider = llm_router.get_provider(routing_request)
        return provider.stream_response(prompt)
    
    def generate_structured_response(
            self,
            prompt: str,
            response_model: type[BaseModel],
            task: LLMTask | None = None,
            
    ) -> BaseModel:
        
        routing_request = LLMRoutingRequest(
            task=task,
            requires_structured_output=True
        ) 
        provider = llm_router.get_provider(routing_request)
        return provider.generate_structured_response(
            prompt,
            response_model
        )
llm_gateway = LLMGateway()