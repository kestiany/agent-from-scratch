from typing import TypedDict, Literal

from agent.result import AgentResult
from crew.base import BaseRole
from schema.task import TaskPlan

class ReviewResult:
    def __init__(self, passed: bool, comments: str):
        self.passed = passed
        self.comments = comments

class ReviewerAgent(BaseRole):
    def __init__(self, llm):
        super().__init__(
            name="Reviewer",
            llm=llm
        )
        
    def run(self, task: TaskPlan, result) -> ReviewResult:
        prompt = f"""
            请评估以下任务结果是否满足目标：
            任务目标：
            {task.objective}
    
            执行结果：
            {result}

            只回答：
            - 是否通过（YES / NO）
            - 简要理由
        """

        review = self.llm.generate(prompt)

        passed = "YES" in review.upper()
        return ReviewResult(passed, review)