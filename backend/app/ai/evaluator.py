class Evaluator:

    def evaluate(
        self,
        question: str,
        answer: str,
        retrieved_chunks: list[dict]
    ):
        context = " ".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )

        grounded = answer.lower() in context.lower()

        return {
            "grounded": grounded,
            "retrieved_chunks": len(retrieved_chunks)
        }
evaluator = Evaluator()