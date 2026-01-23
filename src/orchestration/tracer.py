import time
from typing import List, Dict

class ExecutionTracer:
    def __init__(self):
        self.run_id = None
        self.events: List[Dict] = []

    def start_run(self, run_id: str, goal: str):
        self.run_id = run_id
        self.events.append({
            "type": "run_start",
            "run_id": run_id,
            "goal": goal,
            "ts": time.time()
        })

    def record_plan(self, plan):
        self.events.append({
            "type": "plan",
            "subtasks": [t.objective for t in plan.subtasks],
            "ts": time.time()
        })

    def start_task(self, task):
        self.events.append({
            "type": "task_start",
            "task_id": task.id,
            "objective": task.objective,
            "ts": time.time()
        })

    def task_done(self, task):
        self.events.append({
            "type": "task_done",
            "task_id": task.id,
            "status": task.status,
            "result": task.result,
            "ts": time.time()
        })

    def record_review(self, task, review):
        self.events.append({
            "type": "review",
            "task_id": task.id,
            "passed": review.passed,
            "comments": review.comments,
            "ts": time.time()
        })

    def last_completed_task_id(self):
        for e in reversed(self.events):
            if e["type"] == "task_done" and e["status"] == "completed":
                return e["task_id"]
        return None
