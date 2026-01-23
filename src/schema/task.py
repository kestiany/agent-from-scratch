from dataclasses import dataclass
from typing import Optional
from schema.status import TaskStatus

@dataclass
class SubTask:
    id: str
    objective: str
    task_type: str          # understanding / risk_detection / risk_qualification / reporting
    preferred_engine: str   # workflow / free_form
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[str] = None

    def start(self):
        self.status = TaskStatus.IN_PROGRESS

    def complete(self, result: str):
        self.status = TaskStatus.COMPLETED
        self.result = result

    def fail(self, reason: str):
        self.status = TaskStatus.FAILED
        self.result = reason

@dataclass
class TaskPlan:
    run_id: str
    goal: str
    subtasks: list[SubTask]

    def get_next_task(self) -> Optional[SubTask]:
        return next((t for t in self.subtasks if t.status == TaskStatus.PENDING), None)
    
    def all_completed(self) -> bool:
        return all(t.status == TaskStatus.COMPLETED for t in self.subtasks)
    
