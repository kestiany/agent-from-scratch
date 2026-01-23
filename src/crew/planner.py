from crew.base import BaseRole
from schema.task import TaskPlan, SubTask

class PlannerAgent(BaseRole):
    def __init__(self, llm):
        super().__init__(
            name="Planner",
            llm=llm
        )

    def run(self, user_input: str, run_id: str) -> TaskPlan:
        """
        第六周原则：
        - Planner 是【唯一】生成 TaskPlan 的地方
        - 先结构正确，再谈智能
        """
        # prompt: 拆解任务 + 给每个子任务目标
        subtasks = [
            SubTask(
                id="1",
                objective="理解任务背景与目标",
                task_type="understanding",
                preferred_engine="workflow"
            ),
            SubTask(
                id="2",
                objective="识别关键问题或风险点",
                task_type="analysis",
                preferred_engine="workflow"
            ),
            SubTask(
                id="3",
                objective="生成最终总结与建议",
                task_type="reporting",
                preferred_engine="workflow"
            )
        ]

        return TaskPlan(
            run_id=run_id,
            goal=user_input,
            subtasks=subtasks
        )
