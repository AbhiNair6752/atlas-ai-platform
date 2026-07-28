from groq import Groq
from app.config.settings import get_settings

settings = get_settings()

client = Groq(
    api_key=settings.GROQ_API_KEY
)

class LLM:
    
    def generate_response(
            self,
            prompt: str,
    ) -> str:
        
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
    
llm = LLM()