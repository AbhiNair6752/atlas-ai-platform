from app.ai.embedding_service import embedding_service
from app.ai.vector_store import vector_store
from app.ai.reranker import reranker

class Retriever:
    def retrieve(
            self,
            query: str,
            limit: int = 10
    ):
        query_embedding = embedding_service.generate_embedding(query)

        results = vector_store.client.query_points(
            collection_name=vector_store.collection_name,
            query=query_embedding,
            limit=limit
        )

        retrieved_chunks = []
        for result in results.points:
            retrieved_chunks.append(
                {
                    "id": result.id,
                    "score": result.score,
                    "text": result.payload["text"]
                }
            )
        reranked_documents = reranker.rerank(
            query=query,
            documents=retrieved_chunks,
            top_k=3
        )
        return reranked_documents
    
retriever = Retriever()