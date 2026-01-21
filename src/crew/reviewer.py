from typing import TypedDict, Literal

from agent.result import AgentResult
from crew.base import BaseRole
from crew.schema import TaskPlan

class ReviewResult:
    def __init__(self, passed: bool, comments: str, retry_suggested: bool = False):
        self.passed = passed
        self.comments = comments
        self.retry_suggested = retry_suggested

class ReviewerAgent(BaseRole):
    def __init__(self, llm):
        super().__init__(
            name="Reviewer",
            llm=llm
        )
        
    def run(self, task_plan: TaskPlan, results: list[AgentResult]) -> ReviewResult:
        """
        输入：TaskPlan（子任务列表）
        输出：ReviewResult（审核结果）
        """
        # prompt: 审核任务计划的合理性 + 给出审核意见 + 置信度评分
        return ReviewResult(
            passed=True,
            comments="Review passed - placeholder implementation"
        )