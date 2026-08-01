from app.ai.document_selector import document_selector
from app.ai.llm import llm
from app.ai.vector_store import vector_store
from app.ai.prompt_builder import prompt_builder

class ComparisonService:

    def compare(
            self,
            question: str,
    ) -> dict:
        
        available_documents = vector_store.get_uploaded_documents()

        selection = document_selector.select(
            question=question,
            available_documents=available_documents
        )
        if selection.status == "not_found":
            return {
                 "answer": "I couldn't find any matching document.",
                "sources": [],
                "evaluation": None
            }
        if selection.status == "ambiguous":
            return {
                "answer":
                    "Your request is ambiguous.\n\n"
                    "Please specify one of the following documents:\n"
                    + "\n".join(selection.documents),
                "sources": selection.documents,
                "evaluation": None
            }
        if len(selection.documents) < 2:
            return {
                "answer":
                    "Please specify at least two documents to compare.",
                "sources": selection.documents,
                "evaluation": None
            }
        documents = {}

        for filename in selection.documents:
            documents[filename] = vector_store.get_document_chunks(
                filename
            )
        prompt = prompt_builder.build_comparison_prompt(documents)

        comparison = llm.generate_response(prompt)

        return {
             "answer": comparison,
            "sources": selection.documents,
            "evaluation": None
        }

comparison_service = ComparisonService()