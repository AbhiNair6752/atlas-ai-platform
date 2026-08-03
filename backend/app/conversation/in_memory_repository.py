from app.conversation.repository import ConversationRepository

class InMemoryConversationRepository(
    ConversationRepository
):
    def __init__(self):

        self.store = {}

    def load(
            self,
            session_id: str
    )-> list:
        return self.store.get(
            session_id,
            []
        )
    
    def save(
            self,
            session_id: str,
            history: list
    ):
        self.store[session_id] = history

    def clear(
            self,
            session_id: str
    ):
        self.store.pop(
            session_id,
            None
        )
    
conversation_repository = InMemoryConversationRepository()