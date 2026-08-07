from app.ai.retreiver import retriever
from app.ai.prompt_builder import prompt_builder
from app.ai.memory import coversation_memory
from app.ai.evaluator import evaluator

from app.ai.llm import llm
from app.ai.llm_judge import llm_judge
from app.ai.gateway.llm_gateway import llm_gateway

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
        answer = llm_gateway.generate_response(prompt)

        context = "\n\n".join(
                 chunk["text"]
                 for chunk in retrieved_chunks
)

        evaluation = llm_judge.evaluate(
            question=query,
            answer=answer,
            context=context
        )

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
            "sources": retrieved_chunks,
            "evaluation": evaluation
        }
chat_service = ChatService()
