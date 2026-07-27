from app.ai.embedding_service import embedding_service
from app.ai.vector_store import vector_store

class Retriever:
    def retrieve(
            self,
            query: str,
            limit: int = 5
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
                    "score": result.score,
                    "text": result.payload["text"]
                }
            )
        return retrieved_chunks
    
retriever = Retriever()