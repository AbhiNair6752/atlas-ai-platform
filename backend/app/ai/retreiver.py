from app.ai.embedding_service import embedding_service
from app.ai.vector_store import vector_store
from app.ai.reranker import reranker
from qdrant_client.models import Filter,FieldCondition,MatchValue
from app.ai.keyword_search import keyword_search

class Retriever:
    def retrieve(
            self,
            query: str,
            limit: int = 10,
            filename: str | None = None
    ):
        query_embedding = embedding_service.generate_embedding(query)

        search_filter = None

        if filename:
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="filename",
                        match=MatchValue(value=filename)
                    )
                ]
            )

        results = vector_store.client.query_points(
            collection_name=vector_store.collection_name,
            query=query_embedding,
            limit=limit,
            query_filter=search_filter
        )

        retrieved_chunks = []
        for result in results.points:
            retrieved_chunks.append(
                {
                    "id": result.id,
                    "score": result.score,
                    "text": result.payload["text"],
                    "filename": result.payload["filename"],
                    "chunk_index": result.payload["chunk_index"]
                }
            )
        keyword_results = keyword_search.search(
            query=query,
            documents=retrieved_chunks
        )
        combined_results = retrieved_chunks.copy()

        for keyword_doc in keyword_results:
            if keyword_doc["id"] not in [
                doc["id"]
                for doc in combined_results
            ]:
                combined_results.append(keyword_doc) 
        reranked_documents = reranker.rerank(
            query=query,
            documents=combined_results,
            top_k=3
        )
        return reranked_documents
    
retriever = Retriever()