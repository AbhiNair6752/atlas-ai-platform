class KeywordSearch:

    def search(
            self,
            query: str,
            documents: list[dict]
    ):
        words = query.lower().split()
        results = []

        for doc in documents:
            score = 0
            text = doc["text"].lower()

            for word in words:
                if word in text:
                    score += 1

            if score > 0:
                results.append(
                    {
                        **doc,
                        "keyword_score": score
                    }
                )
            
        return sorted(
            results,
            key=lambda x: x["keyword_score"],
            reverse = True
        )
    
keyword_search = KeywordSearch()