from dataclasses import dataclass
from status import TaskStatus

@dataclass
class Result:
    status: TaskStatus

@dataclass
class CostProfile:
    total_tokens: int
    retry_count: int
    duration_ms: int

@dataclass
class ReviewerSummary:
    what_worked: str
    what_failed: str
    next_time_advice: str