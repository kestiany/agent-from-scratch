from dataclasses import dataclass
from typing import TypedDict

@dataclass
class SubTask:
    id: str
    objective: str
    task_type: str          # understanding / risk_detection / risk_qualification / reporting
    preferred_engine: str   # workflow / free_form
    status: str = "pending"  # pending / in_progress / completed / failed
    result: str | None = None

@dataclass
class TaskPlan:
    goal: str
    subtasks: list[SubTask]
