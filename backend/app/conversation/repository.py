from abc import ABC, abstractmethod

class ConversationRepository(ABC):

    @abstractmethod
    def load(
        self,
        session_id: str,
    )-> list[ConversationState]:
        pass

    @abstractmethod
    def append(
        self,
        session_id: str,
        conversation_turn
    ):
        pass

    @abstractmethod
    def clear(
        self,
        session_id: str,
    ): 
        pass

conversation_repository = ConversationRepository()