from pydantic import BaseModel
from typing import List

class DocumentContext(BaseModel):
    filename: str
    chunks: List[str]