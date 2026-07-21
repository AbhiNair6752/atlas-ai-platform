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
