from app.graph.state import GraphState
from app.ai.llm import llm

class ComparisonNode:

    def execute(
            self,
            state: GraphState
    )-> GraphState:
        
        prompt = f"""
You are Atlas AI.

Compare the following documents.

User Request:

{state["question"]}

Explain similarities and differences.
"""
        answer = llm.generate_response(prompt)

        state["answer"] = answer
        state["sources"] = []
        state["evaluation"] = {}

        return state

comparison_node = ComparisonNode()