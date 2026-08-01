from app.ai.vector_store import vector_store
from app.ai.document_selector import document_selector
from app.ai.retreiver import retriever
from app.ai.llm import llm
from app.ai.prompt_builder import prompt_builder

class SummaryService:

    def summarize(
            self,
            session_id: str,
            question: str
    ) -> dict:
        
        available_documents = vector_store.get_uploaded_documents()

        selection = document_selector.select(
            question=question,
            available_documents=available_documents
        )

        if selection.status == "not_found":
            return {
                "answer": "I couldn't find a matching document",
                "sources": [],
                "evaluation": None
            }
        
        if selection.status == "ambiguous":
            return {
                "answer":
            "Multiple matching documents found. "
            "Please specify one of the following:\n\n"
            + "\n".join(selection.documents),
        "sources": selection.documents,
        "evaluation": None
            }
        
        chunks = vector_store.get_document_chunks(
            selection.documents[0]
        )
        prompt = prompt_builder.build_summary_prompt(
            chunks
        )

        summary = llm.generate_response(prompt)

        return {
            "answer": summary,
            "sources": selection.documents,
            "evaluation": None
        }