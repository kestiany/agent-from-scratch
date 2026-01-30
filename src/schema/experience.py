from dataclasses import dataclass
from datetime import datetime
from result import Result, CostProfile, ReviewerSummary

class TaskSingature:
    task_type: str
    domain: str
    constraints: list[str]

@dataclass
class TaskExperience:
    task_id: str
    paln_out_line: list[TaskSingature]
    result: Result
    cost_Profile: CostProfile
    reviewer_Summary: ReviewerSummary
    created: datetime

    execution_profile: dict # retry / terminate / insufficient_info etc

