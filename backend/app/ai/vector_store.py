from qdrant_client import QdrantClient
from qdrant_client.models import (VectorParams, Distance, PointStruct,Filter,FieldCondition,MatchValue)
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
            embeddings: list[list[float]],
            filename: str
    ):
        points = []
        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "text": chunk,
                        "filename": filename,
                        "chunk_index": index
                    }
                )
            )
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def get_uploaded_documents(self) -> list[str]:
        points, _ = self.client.scroll(
            collection_name=self.collection_name,
            with_payload=True,
            with_vectors=False,
            limit=1000
        )

        filenames = {
            point.payload["filename"]
            for point in points
            if "filename" in point.payload
        }
        return sorted(list(filenames))
    
    def get_document_chunks(
            self,
            filename: str,
    ) -> list[str]:
        
        points, _ = self.client.scroll(
            collection_name = self.collection_name,
            scroll_filter=Filter(
                must=[
                    FieldCondition(
                        key="filename",
                        match=MatchValue(
                            value=filename
                        )
                    )
                ]
            ),
            with_payload=True,
            with_vectors=False,
            limit=10000
        )

        points.sort(
            key=lambda point: point.payload["chunk_index"]
        )
        chunks =[
            point.payload["text"]
            for point in points
        ]

        return chunks

vector_store = VectorStore()
