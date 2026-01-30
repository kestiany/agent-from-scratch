from dataclasses import dataclass
from typing import List
from schema.task import TaskPlan, SubTask

@dataclass
class ScoredPlan:
    plan: TaskPlan
    score: float
    rationale: str

class ScoredPlanner:
    """
    Week 8 核心：
    - Planner 生成多个候选
    - 用规则打分
    - 选最稳的那个
    """

    def __init__(self, base_planner):
        self.base_planner = base_planner

    def run(self, user_input: str, run_id: str) -> TaskPlan:
        candidates = self._generate_candidates(user_input, run_id)
        scored = [self._score(p) for p in candidates]
        scored.sort(key=lambda x: x.score, reverse=True)
        return scored[0].plan

    def _generate_candidates(self, user_input, run_id) -> List[TaskPlan]:
        # Week 8：最小可行 K=3
        return [
            self.base_planner.run(user_input, run_id),
            self._conservative_plan(user_input, run_id),
            self._aggressive_plan(user_input, run_id),
        ]

    def _score(self, plan: TaskPlan) -> ScoredPlan:
        score = 1.0
        rationale = []

        if len(plan.subtasks) > 5:
            score -= 0.3
            rationale.append("too_many_steps")

        if any(t.task_type == "reporting" for t in plan.subtasks[:-1]):
            score -= 0.2
            rationale.append("early_reporting")

        return ScoredPlan(plan, score, ",".join(rationale))
