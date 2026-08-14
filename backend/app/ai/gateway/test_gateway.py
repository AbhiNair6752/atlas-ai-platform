from pydantic import BaseModel

from app.ai.gateway.llm_gateway import llm_gateway
from app.ai.gateway.llm_task import LLMTask


class TestPlannerResponse(BaseModel):
    intent: str


# Test normal response
response = llm_gateway.generate_response(
    "Explain REST API in one sentence.",
    task=LLMTask.CHAT,
)

print("NORMAL RESPONSE:")
print(response)


# Test structured response
structured_response = llm_gateway.generate_structured_response(
    """
Classify this request.

User request:
"Please summarize the uploaded document."

Return the intent as a structured response.
The intent should be: summary
""",
    TestPlannerResponse,
    task=LLMTask.PLANNER,
)

print("\nSTRUCTURED RESPONSE:")
print(structured_response)
print("Intent:", structured_response.intent)