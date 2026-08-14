import json
from app.infrastructure.redis.client import redis_client


class ConversationMemory:

    def __init__(self):
        self.redis = redis_client.client

    def add_messages(
            self,
            session_id: str,
            role: str,
            content: str
    )-> None:
        
        key = f"conversation: {session_id}"

        message = {
            "role": role,
            "content": content
        }

        self.redis.rpush(
            key,
            json.dumps(message)
        )

    def get_history(
            self,
            session_id: str
    )-> list[dict]:
        
        key = f"conversation: {session_id}"

        messages = self.redis.lrange(
            key,
            0,
            -1
        )
        return [
            json.loads(message)
            for message in messages
        ]
    
    def clear_history(
            self,
            session_id: str
    )-> None:
        
        key = f"conversation: {session_id}"

        self.redis.delete(key)

conversation_memory = ConversationMemory()