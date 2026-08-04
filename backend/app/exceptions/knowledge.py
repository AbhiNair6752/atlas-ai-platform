class KnowledgeException(Exception):
    """Base exception for Knowledge service"""

class DocumentNotFoundException(KnowledgeException):
    pass

class AmbiguousDocumebtException(KnowledgeException):
    pass
