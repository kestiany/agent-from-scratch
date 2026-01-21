from crew.base import BaseRole
from crew.planner import PlannerAgent
from crew.executor import ExecutorAgent
from crew.reviewer import ReviewerAgent
from orchestration.trace import ExecutionTracer

class CrewLoop:
    def __init__(self, planner: PlannerAgent, executor: ExecutorAgent, reviewer: ReviewerAgent, trace: ExecutionTracer):
        self.planner = planner
        self.executor = executor
        self.reviewer = reviewer
        self.trace = trace

    def run(self, user_input: str):
        self.trace.start_run(user_input
                             )
        # 1. Planner 拆任务
        plan = self.planner.run(user_input)
        self.trace.record_plan(plan)

        # 2. Executor 顺序执行每个子任务（内部仍是 Week4 kernel）
        results = []
        for subtask in plan.subtasks:
            self.trace.start_task(subtask)
            result = self.executor.run(subtask)
            self.trace.record_execution(result)

            # Reviewer
            review = self.reviewer.run(plan, result)
            self.trace.record_review(result, review)

            if review.passed:
                results.append(result)
            else:
                pass
        
        self.trace.finish_run()
        return results