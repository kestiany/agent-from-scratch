from agent.kernel import AgentKernel
from agent.result import AgentResult
from schema.task import SubTask, TaskStatus
from crew.base import BaseRole

class ExecutorAgent(BaseRole):
    def __init__(self, llm):
        super().__init__(
            name="Executor",
            llm=llm
        )
        self.kernel = AgentKernel()

    def run(self, task: SubTask) -> SubTask:
        """
        路由决策
        """
        if task.preferred_engine == "workflow":
            result = self.kernel.run(task.objective)
        elif task.preferred_engine == "free_form":
            result = self.run_free_form(task)
        else:
            raise ValueError(f"Unknown preferred engine: {task.preferred_engine}")
        
        task.status = TaskStatus.COMPLETED
        task.result = result
        return task
    
    def run_free_form(self, task: SubTask):
        # 未来接 code agent / rag / tool
        return f"[FreeForm] 完成任务: {task.objective}"