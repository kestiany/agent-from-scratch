from agent.state import AgentState

class AgentKernel:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps

    def run(self, user_input: str) -> AgentState:
        state: AgentState = self._init_state(user_input)

        while self._should_continue(state):
            state = self._think(state)
            state = self._act(state)
            state = self._evaluate(state)

        return self._finalize(state)
    
    def _init_state(self, user_input: str) -> AgentState:
        return {
            "user_input": user_input,
            "objective": "",
            "plan": [],
            "current_step": 0,
            "scratchpad": [],
            "final_output": None,
            "history": [],
            "done": False,
            "step_context": None,
            "memory": []
        }

    def _finalize(self, state: AgentState) -> AgentState:
        if state["current_step"] >= len(state["plan"]):
            state["final_output"] = "\n".join(state["scratchpad"])
            state["history"].append("任务完成")
        return state

    def _should_continue(self, state: AgentState) -> bool:
        return (
            not state["done"] 
            and state["current_step"] < self.max_steps
        )

    def _think(self, state: AgentState) -> AgentState:
        if not state["plan"] and not state["done"]:
            state["objective"] = state["user_input"]
            state["plan"] = [
                "理解任务",
                "拆解步骤",
                "执行任务",
                "总结结果"
            ]
            state["history"].append("生成初始计划")
        return state
    
    def _act(self, state: AgentState) -> AgentState:
        step = state["plan"][state["current_step"]]
        state["scratchpad"].append(f"正在执行：{step}")
        state["history"].append(f"执行步骤 {state['current_step']}: {step}")
        return state

    def _evaluate(self, state: AgentState) -> AgentState:
        state["current_step"] += 1
        if state["current_step"] >= len(state["plan"]):
            state["done"] = True
        return state