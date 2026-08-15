from app.graph.graph_builder import workflow
from app.memory.conversation_memory import conversation_memory


class GraphService:

    def chat(
            self,
            session_id: str,
            question: str
    ):
        history = conversation_memory.get_history(
            session_id
        )

        conversation_memory.add_messages(
            session_id=session_id,
            role="user",
            content=question
        )


        initial_state = {
             "session_id": session_id,
            "question": question,
            "intent": "",
            "answer": "",
            "sources": [],
            "evaluation": {},
            "history": history
        }

        result = workflow.invoke(
            initial_state,
            config={
                "configurable": {
                    "thread_id": session_id
                }
            })
        answer = result.get(
            "answer",
            ""
        )
        conversation_memory.add_messages(
            session_id=session_id,
            role="assistant",
            content=answer
        )

        return result
    
graph_service = GraphService()