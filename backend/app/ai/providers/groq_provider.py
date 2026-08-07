import json

from groq import Groq
from pydantic import BaseModel, ValidationError

from app.config.settings import get_settings
from app.ai.providers.base_provider import LLMProvider

settings = get_settings()

class GroqProvider(LLMProvider):

    MODEL_NAME = "llama-3.3-70b-versatile"

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model = self.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
    
    def stream_response(self, prompt: str):
        stream = self.client.chat.completions.create(
            model = self.MODEL_NAME,
            messages = [
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

        response = self.client.chat.completions.create(
            model=self.MODEL_NAME,
            messages=[
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
                f"Structured output parsing failed: {e}\n\n"
                f"LLM Output:\n{content}"
            )
        
groq_provider = GroqProvider()