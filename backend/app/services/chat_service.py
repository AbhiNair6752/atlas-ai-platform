from app.ai.retreiver import retriever
from app.ai.prompt_builder import prompt_builder

from app.ai.llm import llm

class ChatService:
    def chat(
            self,
            query: str
    ):
        retrieved_chunks = retriever.retrieve(query)

        prompt = prompt_builder.build_prompt(query=query,
                                             retrieved_chunks=retrieved_chunks)
        answer = llm.generate_response(prompt)

        return {
            "question": query,
            "answer": answer,
            "sources": retrieved_chunks
        }
chat_service = ChatService()
