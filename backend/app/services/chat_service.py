from app.ai.retreiver import retriever
from app.ai.prompt_builder import prompt_builder
from app.ai.memory import coversation_memory

from app.ai.llm import llm

class ChatService:
    def chat(
            self,
            session_id: str,
            query: str
    ):
        history = coversation_memory.get_history(session_id)
        
        retrieved_chunks = retriever.retrieve(query)

        prompt = prompt_builder.build_prompt(query=query,
                                             retrieved_chunks=retrieved_chunks,
                                             history=history)
        answer = llm.generate_response(prompt)

        coversation_memory.add_message(
            session_id,
            "user",
            query
        )
        coversation_memory.add_message(
            session_id,
            "assistant",
            answer
        )

        return {
            "question": query,
            "answer": answer,
            "sources": retrieved_chunks
        }
chat_service = ChatService()
