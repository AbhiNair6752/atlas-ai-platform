class AtlasException(Exception):
    """
    Base exception for atlas application
    """

    def __init__(
            self,
            message: str,
            status_code: int = 500
    ):
        self.message = message
        self.status_code = status_code

        super().__init__(message)

class ResourceNotFoundException(AtlasException):
    def __init__(self, message: str):
        super().__init__(message=message,status_code=404)

class KnowledgeException(AtlasException):
    """
    Base exception for knowledge retrieval
    """
    def __init__(
            self,
            message: str,
            status_code: int = 500
    ):
        super().__init__(
            message=message,
            status_code=status_code
        )

class DocumentNotFoundException(
    KnowledgeException
):

    def __init__(
        self,
        message: str = "Document not found.",
    ):
        super().__init__(
            message=message,
            status_code=404,
        )

class AmbiguousDocumentException(
    KnowledgeException
):

    def __init__(
        self,
        message: str = "Multiple matching documents found.",
    ):
        super().__init__(
            message=message,
            status_code=400,
        )