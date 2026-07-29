from flashrank import Ranker, RerankRequest

class Reranker:

    def __init__(self):
        self.ranker = Ranker()

    def rerank(
            self,
            query: str,
            documents: list[dict],
            top_k: int = 3
    ):
        passages = []

        for doc in documents:
            passages.append(
                {
                    "id": doc["id"],
                    "text": doc["text"]
                }
            )
        request = RerankRequest(
            query=query,
            passages=passages
        )

        ranked = self.ranker.rerank(request)

        return ranked[:top_k]
    
reranker = Reranker()
