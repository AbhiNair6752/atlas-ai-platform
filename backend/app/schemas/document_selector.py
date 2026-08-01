from typing import Literal
from pydantic import BaseModel

class DocumentSelection(BaseModel):
    status: Literal[
        "success",
        "ambiguous",
        "not found"
    ]
    documents: list[str]