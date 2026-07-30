from rank_bm25 import BM25Okapi

class BM25Search:

    def search(
            self,
            query:str,
            documents: list[dict],
            top_k: int = 5,
    ):
        corpus = [
            doc["text"].split()
            for doc in documents
        ]

        bm25 = BM25Okapi(corpus)

        tokenized_query = query.split()

        scores = bm25.get_scores(tokenized_query)

        ranked = []

        for score, doc in zip(scores, documents):
            ranked.append(
                {
                    **doc,
                    "bm25_score": float(score)
                }
            )

        ranked.sort(
            key=lambda x: x['bm25_score'],
            reverse=True
        )

        return ranked[:top_k]
    
bm25_search = BM25Search()