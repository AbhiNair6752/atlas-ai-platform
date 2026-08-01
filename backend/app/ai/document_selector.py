from app.ai.llm import llm

class DocumentSelector:

    def select_documents(
            self,
            question: str,
            available_documents: list[str]
    ):
        documents = "\n".join(available_documents)

        prompt = f"""
You are an intelligent document selector.

The available uploaded documents are:

{documents}

User Question:

{question}

Return ONLY the matching document names.

One document per line.

If no document matches, return NONE.
"""
        response = llm.generate_response(prompt)

        selected_documents = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        if selected_documents == ["NONE"]:
            return []
        return selected_documents
    
document_selector = DocumentSelector()