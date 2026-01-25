from dataclasses import dataclass
from datetime import datetime

@dataclass
class AdvisoryNote:
    advisory_id: str
    scope: dict               # {"domain": "...", "task_type": "..."}
    advice: str
    confidence: float
    source_patterns: list[str]
    created_at: datetime
    expires_at: datetime | None = None
