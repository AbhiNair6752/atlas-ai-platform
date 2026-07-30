import json

from app.ai.llm import llm

class LLMJudge:

    def evaluate(
            self,
            question: str,
            answer: str,
            context: str,
    ) -> dict:
        
        prompt = f"""You are an expert AI evaluator.

Your task is to evaluate whether an AI assistant answered a question correctly using ONLY the retrieved context.

Evaluate the answer on the following criteria:

1. grounded (true/false)
   - Is the answer completely supported by the retrieved context?

2. relevance (1-10)
   - Does the answer actually answer the user's question?

3. faithfulness (1-10)
   - Does the answer avoid making up information not found in the context?

4. completeness (1-10)
   - Does the answer fully answer the user's question?

5. overall_score (1-10)

6. feedback
   - Give one concise sentence explaining your evaluation.

Question:
{question}

Retrieved Context:
{context}

Answer:
{answer}

Return ONLY valid JSON.

Example:

{{
    "grounded": true,
    "relevance": 9,
    "faithfulness": 10,
    "completeness": 8,
    "overall_score": 9,
    "feedback": "The answer is accurate and fully supported by the retrieved context."
}}

Do not include markdown.
Do not include explanations.
Return only JSON.
"""
        
        response = llm.generate_response(prompt)

        try: 
            return json.loads(response)
        except json.JSONDecodeError:
             print("\nLLM Judge returned invalid JSON:")
             print(response)

            return {
                "grounded": False,
                "relevance": 0,
                "faithfulness": 0,
                "completeness": 0,
                "overall_score": 0,
                "feedback": "Judge failed to return valid JSON."
            }
llm_judge = LLMJudge()