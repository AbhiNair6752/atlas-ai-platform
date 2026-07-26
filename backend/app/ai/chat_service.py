from app.ai.llm import client
from app.ai.prompt import SYSTEM_PROMPT

class ChatService:
    
    def chat(self, message: str):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role" : "user",
                    "content": message
                },
            ],
        )

        return response.choices[0].message.content
    
chat_service = ChatService()