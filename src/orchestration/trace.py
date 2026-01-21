class ExecutionTracer:
    def __init__(self):
        self.run_id = None
        self.events = []

    def start_run(self, goal):
        self.run_id = "run-001"
        self.events.append({"type": "run_start", "goal": goal})

    def record_plan(self, plan):
        self.events.append({
            "type": "plan",
            "subtasks": [t.objective for t in plan.subtasks]
        })

    def start_task(self, task):
        self.events.append({
            "type": "task_start",
            "task_id": task.id,
            "objective": task.objective
        })

    def record_execution(self, task):
        self.events.append({
            "type": "task_done",
            "task_id": task.id,
            "result": task.result
        })

    def record_review(self, task, review):
        self.events.append({
            "type": "review",
            "task_id": task.id,
            "passed": review.passed,
            "comments": review.comments
        })

    def finish_run(self):
        self.events.append({"type": "run_finish"})
