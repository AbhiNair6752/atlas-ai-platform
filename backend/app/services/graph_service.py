from app.graph.graph_builder import workflow
from app.memory.conversation_memory import conversation_memory
from langgraph.types import Command


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
        print("Graph Result:")
        print(result)

        answer = result.get(
            "answer",
            ""
        )
        conversation_memory.add_messages(
            session_id=session_id,
            role="assistant",
            content=answer
        )

        if "__interrupt__" in result:

           interrupt = result["__interrupt__"][0]

           return {
            "status": "approval_required",
            "session_id": session_id,
            "message": interrupt.value["message"],
            "question": interrupt.value["question"],
            "intent": interrupt.value["intent"],
        }

        return {
          "status": "completed",
          "session_id": session_id,
          "question": result["question"],
          "answer": result["answer"],
          "sources": result["sources"],
          "evaluation": result["evaluation"],
    }
    
    def resume(
        self,
        session_id: str,
        approved: bool
    ):
       config = {
           "configurable": {
               "thread_id": session_id
           }
       }
       
       result = workflow.invoke(
           Command(
               resume=approved
           ),
           config=config
       )
       return result
    
    
    
graph_service = GraphService()