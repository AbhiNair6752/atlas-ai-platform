from app.graph.state import GraphState
from app.ai.llm import llm

VALID_INTENTS = {
    "document_qa",
    "general_chat",
    "summary",
    "comparison",
    "web_search",
}

class Planner:

    def classify(
            self,
            state: GraphState,
    ) -> GraphState:
        
        prompt = f"""
You are an AI workflow planner.

Your job is to classify the user's request.

Choose ONLY ONE intent from:

document_qa

general_chat

summary

comparison

web_search

Question:

{state["question"]}

Return ONLY the intent.

Do not explain.
"""
        
        """question = state["question"].lower()

        if(
            "summarize" in question
            or "summary" in question
        ):
            state["intent"] = "summary"

        elif(
            "today" in question
            or "latest" in question
            or current in question
        ):
            state["intent"] = "web_search"

        else:
            state["intent"] = "document_qa"

        return state"""

        intent = llm.generate_response(prompt)

        intent = (intent.strip().lower().replace(" ","_"))
        if intent not in VALID_INTENTS:
            intent = "document_qa"
        state["intent"] = intent

        return state
    
planner = Planner()