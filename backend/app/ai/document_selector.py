from app.ai.llm import llm
from app.schemas.document_selector import DocumentSelection

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
    
    def select(
            self,
            question: str,
            available_documents: list[str],
    ) -> DocumentSelection:
        
        prompt = f"""
You are Atlas AI's Document Selector.

Your task is to determine which uploaded document(s)
the user is referring to.

Available Documents:

{"\n".join("- " + doc for doc in available_documents)}

User Question:

{question}

Rules:

1. Return ONLY documents from the available list.

2. Never invent filenames.

3. If exactly one document matches:
status = "success"

4. If multiple documents could match:
status = "ambiguous"

5. If no document matches:
status = "not_found"

Return ONLY valid JSON.

Example:

{{
    "status": "success",
    "documents": [
        "HR Policy.pdf"
    ]
}}
"""
        return llm.generate_structured_response(
            prompt,
            DocumentSelection
        )
    
document_selector = DocumentSelector()