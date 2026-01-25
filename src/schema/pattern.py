from dataclasses import dataclass
from datetime import datetime

@dataclass
class BehaviorPattern:
    pattern_id: str
    pattern_type: str        # failure / cost / advice
    signal: str              # 人能看懂
    confidence: float
    evidence_count: int
    examples: list[str]
    created_at: datetime
