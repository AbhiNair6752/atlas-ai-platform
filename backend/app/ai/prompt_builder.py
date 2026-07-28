class PromptBuilder:

    def build_prompt(
            self,
            query: str,
            retrieved_chunks: list[dict]
    ) -> str:
        context = "\n\n".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )

        prompt = f"""
          You are Atlas AI.

          You are an intelligent enterprise AI assistant.

          Answer ONLY using the provided context.

          If the answer cannot be found in the context, say:

          I couldn't find that information in the uploaded documents.
          --------------------
Context
--------------------

{context}

--------------------
Question
--------------------

{query}

--------------------
Answer
--------------------"""
        return prompt.strip()
    
prompt_builder = PromptBuilder()