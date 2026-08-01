from abc import ABC, abstractmethod

class ConversationRepository(ABC):

    @abstractmethod
    def load(
        self,
        session_id: str,
    )-> list:
        pass

    @abstractmethod
    def save(
        self,
        session_id: str,
        history: list
    ):
        pass

    @abstractmethod
    def clear(
        self,
        session_id: str,
    ): 
        pass