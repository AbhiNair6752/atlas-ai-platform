from app.graph.state import GraphState
from app.ai.llm import llm

class GeneralChatNode:

    def execute(
            self,
            state: GraphState
    ) -> GraphState:
        prompt = f"""
You are Atlas AI.

Answer the user's question.

Question:

{state["question"]}
"""
        answer = llm.generate_response(prompt)

        state["answer"] = answer
        state["sources"] = []
        state["evaluation"] = {}

        return state
    
general_chat_node = GeneralChatNode()
