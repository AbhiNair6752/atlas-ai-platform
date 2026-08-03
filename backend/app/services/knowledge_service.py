from app.ai.vector_store import vector_store
from app.ai.document_selector import document_selector
from app.schemas.knowledge import DocumentContext

class KnowledgeService:

    def get_document(
            self,
            question: str
    )-> DocumentContext:
        available_documents = vector_store.get_uploaded_documents()

        selection = document_selector.select(
            question=question,
            available_documents=available_documents
        )
        if selection.status == "not_found":
            raise ValueError(
                "No Matching document found"
            )
        
        if selection.status == "ambiguous":
            raise ValueError(
                "Multiple matching documents found"
            )
        
        filename = selection.documents[0]

        chunks = vector_store.get_document_chunks(
            filename
        )

        return DocumentContext(
            filename=filename,
            chunks=chunks
        )

knowledge_service = KnowledgeService()