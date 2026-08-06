from app.ai.vector_store import vector_store
from app.ai.document_selector import document_selector
from app.schemas.knowledge import DocumentContext
from app.exceptions.knowledge import (DocumentNotFoundException, AmbiguousDocumebtException)

class KnowledgeService:

    def get_document(
            self,
            question: str
    )-> DocumentContext:
        
        """
    Selects the most relevant document
    for the user's question and loads
    all its chunks.
    """
        documents = self._select_documents(question)
        
        return self._load_document(documents[0])
    
    def _load_document(
            self,
            filename: str,
    
    ) -> DocumentContext:
        chunks = vector_store.get_document_chunks(
            filename
        )
        return DocumentContext(
            filename=filename,
            chunks=chunks
        )
    
    def _select_documents(
        self,
        question: str,
    )-> list[str]:
        available_documents = vector_store.get_uploaded_documents()

        selection = document_selector.select(
            question=question,
            available_documents=available_documents
        )

        if selection.status == "not_found":
            raise DocumentNotFoundException(
                "No matching document found"
            )
        if selection.status == "ambiguous":
            raise AmbiguousDocumebtException(
                "Multiple matching documents are found"
            )
        return selection.documents
    
    def get_documents(
            self,
            question: str,
    ) -> list[DocumentContext]:
        
        documents = self._select_documents(question)

        return [
            self._load_document(doc)
            for doc in documents
        ]

knowledge_service = KnowledgeService()