from agent.state import AgentState, ControlDecision

def reflect(state: AgentState) -> AgentState:
    """
    Reflection answers ONE question:
    Does the current paln hypothesis still hold?
    """

    failure = state["last_failure"]

    if state["step_success"]:
        decision: ControlDecision = "continue"  
    else:
        if state["retry_count"] < state["max_retry"]:
            decision = "retry"
        else:
            #decision = "replan"
            state["terminated"] = True
            state["termination_reason"] = "retry_exceeded"

    state["control_decision"] = decision
    state["history"].append(f"[Reflection] decision={decision}, failure={failure}")

    return state

