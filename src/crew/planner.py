from crew.base import BaseRole
from crew.schema import TaskPlan, SubTask

class PlannerAgent(BaseRole):
    def __init__(self, llm):
        super().__init__(
            name="Planner",
            llm=llm
        )
        
    def run(self, user_input: str) -> TaskPlan:
        # prompt: 拆解任务 + 给每个子任务目标
        subTasks = [
            SubTask(
                id="1",
                objective="理解系统背景和目标",
                task_type="understanding",
                preferred_engine="workflow"
            ),
            SubTask(
                id="2",
                objective="识别系统的主要风险点",
                task_type="risk_detection",
                preferred_engine="workflow"
            ),
            SubTask(
                id="3",
                objective="给出最终总结报告",
                task_type="reporting",
                preferred_engine="workflow"
            )
        ]

        return TaskPlan(
            goal=user_input,
            subtasks=subTasks
        )
