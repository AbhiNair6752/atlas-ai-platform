from dataclasses import dataclass

@dataclass
class SecurityResult:
    allowed: bool
    reason: str | None = None