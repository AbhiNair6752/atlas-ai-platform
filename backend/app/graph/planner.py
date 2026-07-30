from app.graph.state import GraphState

class Planner:

    def classify(
            self,
            state: GraphState,
    ) -> GraphState:
        
        question = state["question"].lower()

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

        return state
    
planner = Planner()