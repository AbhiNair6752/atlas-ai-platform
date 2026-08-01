from app.graph.state import GraphState
from app.services.chat_service import chat_service

class DocumentNode:

    def execute(
            self,
            state: GraphState,
    ) -> GraphState:
        
        result = chat_service.chat(
            session_id = state["session_id"],
            query = state["question"]
        )

        state["answer"] = result["answer"]
        state["sources"] = result["sources"]
        state["evaluation"] = result["evaluation"]

        return state
    

document_node = DocumentNode()