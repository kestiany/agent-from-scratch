from agent.state import AgentState
from agent.think import think
from agent.action import action
from agent.evaluate import evaluate
from agent.reflect import reflect
from agent.result import AgentResult

class AgentKernel:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps

    def run(self, user_input: str) -> AgentResult:
        state: AgentState = self._init_state(user_input)

        while self._should_continue(state):
            state = think(state)
            state = action(state)
            state = evaluate(state)

            if self._should_reflect(state):
                state = reflect(state)
            
            state = self._apply_control_decision(state)

            if state["terminated"]:
                break

        return self._finalize(state)
    
    def _init_state(self, user_input: str) -> AgentState:
        return {
            "user_input": user_input,
            "objective": "Analyze code and identify potential risks",
            "plan": [
                "understanding",
                "risk_detection",
                "risk_qualification",
                "reporting"
            ],
            "current_step": 0,
            "scratchpad": [],
            "final_output": None,
            "done": False,
            "step_context": None,
            "memory": [],
            "history": [],
            "step_success": False,
            "retry_count": 0,
            "max_retry": 2,
            "last_failure": None,
            "control_decision": None,
            "insufficient_info": False,
            "confidence_level": 1.0,
            "terminated": False,
            "termination_reason": None
        }

    def _finalize(self, state: AgentState) -> AgentResult:
        if state["terminated"]:
            status = "terminated"
        elif state["insufficient_info"]:
            status = "insufficient_info"
        else:
            status = "completed"
        
        return {
            "status": status,
            "confidence": state["confidence_level"],
            "final_output": state["final_output"],
            "termination_reason": state["termination_reason"],
            "history": state["history"],
        }

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

