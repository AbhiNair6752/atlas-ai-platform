from qdrant_client import QdrantClient
from qdrant_client.models import (VectorParams, Distance, PointStruct)
import uuid


class VectorStore:

    def __init__(self):
        
        self.client = QdrantClient(
            host= "localhost",
            port=6333
        )
        self.collection_name = "atlas_documents"
        self._create_collection()

    def _create_collection(self):
        collections = self.client.get_collections().collections

        existing = [
            collection.name
            for collection in collections
        ]
        if self.collection_name not in existing:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size = 384,
                    distance=Distance.COSINE
                )
            )
    
    def add_documents(
            self,
            chunks: list[str],
            embeddings: list[list[float]]
    ):
        points = []
        for chunk, embedding in zip(chunks, embeddings):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "text": chunk
                    }
                )
            )
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

vector_store = VectorStore()
