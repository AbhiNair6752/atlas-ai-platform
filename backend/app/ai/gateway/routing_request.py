from dataclasses import dataclass

from app.ai.gateway.llm_task import LLMTask

@dataclass
class LLMRoutingRequest:
    task: LLMTask
    estimated_tokens: int | None = None
    requires_structured_output: bool = False
    requires_streaming: bool = False