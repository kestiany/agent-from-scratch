from agent.state import AgentState
from agent.think import think
from agent.action import action
from agent.evaluate import evaluate

class AgentKernel:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps

    def run(self, user_input: str) -> AgentState:
        state: AgentState = self._init_state(user_input)

        while self._should_continue(state):
            state = think(state)
            state = action(state)
            state = evaluate(state)

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

