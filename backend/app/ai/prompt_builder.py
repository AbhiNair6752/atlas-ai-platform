class PromptBuilder:

    def build_prompt(
            self,
            query: str,
            retrieved_chunks: list[dict],
            history: list[dict]
    ) -> str:
        context = "\n\n".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )
        conversation = ""

        for message in history:
            conversation += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        prompt = f"""
          You are Atlas AI.

          You are an intelligent enterprise AI assistant.

          Answer ONLY using the provided context.

          If the answer cannot be found in the context, say:

          I couldn't find that information in the uploaded documents.
         ---------------------------------
Conversation History
---------------------------------

{conversation}

---------------------------------
Retrieved Context
---------------------------------

{context}

---------------------------------
Current Question
---------------------------------

{query}

---------------------------------
Answer
---------------------------------
"""
        return prompt.strip()
    
    def build_summary_prompt(
            self,
            chunks: list[str]
    ) -> str:
        
        document = "\n\n".join(chunks)
        prompt = f"""
You are Atlas AI.

You are an expert document analyst.

Your task is to summarize the document provided below.

Instructions:

- Produce a concise but complete summary.
- Preserve the important policies, procedures and key points.
- Do not invent information.
- Do not omit important sections.
- Use clear bullet points where appropriate.
- Keep the summary well structured.

Document:

{document}
"""
        return prompt
    
    def build_comparison_prompt(
            self,
            documents: dict[str, list[str]]

    ) -> str:
        document_context = ""

        for filename, chunks in documents.items():
            document_context += f"""
            Document:
{filename}

{"".join(chunks)}

-------------------------------------

"""
            prompt = f"""
You are Atlas AI.

You are an expert document analyst.

Compare the following documents.

Instructions:

- Highlight similarities.
- Highlight differences.
- Mention unique information.
- Keep the comparison concise.
- Use a markdown table whenever appropriate.
- Do not invent information.
- Base your answer only on the provided documents.

Documents:

{document_context}
"""
            return prompt
    
prompt_builder = PromptBuilder()