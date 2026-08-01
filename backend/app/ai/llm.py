from groq import Groq
from app.config.settings import get_settings
from pydantic import BaseModel
import json
from pydantic import ValidationError

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
    
    def stream_response(
            self,
            prompt:str
    ):
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            stream=True
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content

            if delta:
                yield delta

    def generate_structured_response(
            self,
            prompt: str,
            response_model: type[BaseModel]
    ) -> BaseModel:
        
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        try:
            data = json.loads(content)
            return response_model.model_validate(data)
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(
                f"Structured output parsing failed: {e}\n\nLLM Output: \n{content}"
            )
        
    
llm = LLM()