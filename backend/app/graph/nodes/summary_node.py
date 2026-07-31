from app.graph.state import GraphState
from app.ai.llm import llm

class SummaryNode:

    def execute(
            self,
            state: GraphState
    ) -> GraphState:
        
        prompt = f"""
You are Atlas AI.

Summarize the following request.

User Request:

{state["question"]}

Provide a concise summary.
"""
        answer = llm.generate_response(prompt)

        state["answer"] = answer
        state["sources"] = []
        state["evaluation"] = {}

        return state
    
summary_node = SummaryNode()