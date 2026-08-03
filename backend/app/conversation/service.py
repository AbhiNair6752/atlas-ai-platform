from app.conversation.repository import conversation_repository

class ConversationService:
    
    def load_history(
            self,
            session_id: str
    ):
        return conversation_repository.load(session_id)
    
    def append_turn(
            self,
            conversation_turn: ConversationTurn
    ):
        conversation_repository.save(
            conversation_turn.session_id,
            conversation_turn
        )

conversation_service = ConversationService()

