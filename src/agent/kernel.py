from agent.state import AgentState
from agent.think import think
from agent.action import action
from agent.evaluate import evaluate
from agent.reflect import reflect

class AgentKernel:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps

    def run(self, user_input: str) -> AgentState:
        state: AgentState = self._init_state(user_input)

        while self._should_continue(state):
            state = think(state)
            state = action(state)
            state = evaluate(state)

            if self._should_reflect(state):
                state = reflect(state)
            
            state = self._apply_control_decision(state)

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
    
    def _should_reflect(self, state: AgentState) -> bool:
        return True
    
    def _apply_control_decision(self, state: AgentState) -> AgentState:
        decision = state["control_decision"]

        if decision == "continue":
            state["current_step"] += 1
            state["retry_count"] = 0
        elif decision == "retry":
            state["retry_count"] += 1

            if state["retry_count"] >= state["max_retry"]:
                state["last_failure"] = "retry_exceeded"
                state["control_decision"] = None
            else:
                # retry current step
                pass
        elif decision == "replan":
            state["plan"] = []
            state["current_step"] = 0
            state["retry_count"] = 0
            state["control_decision"] = None
        
        return state

