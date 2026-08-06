from app.graph.graph_builder import workflow

class GraphService:

    def chat(
            self,
            session_id: str,
            question: str
    ):
        initial_state = {
             "session_id": session_id,
            "question": question,
            "intent": "",
            "answer": "",
            "sources": [],
            "evaluation": {},
        }

        result = workflow.invoke(
            initial_state,
            config={
                "configurable": {
                    "thread_id": session_id
                }
            })

        return result
    
graph_service = GraphService()