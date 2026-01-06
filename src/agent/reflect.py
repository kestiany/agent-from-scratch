from agent.state import AgentState, ControlDecision

def reflect(state: AgentState) -> AgentState:
    """
    Reflection answers ONE question:
    Does the current paln hypothesis still hold?
    """

    failure = state["last_failure"]

    if failure is None:
        decision: ControlDecision = "continue"
    elif "network" in failure:
        decision = "retry"
    else:
        decision = "replan"

    state["control_decision"] = decision
    state["history"].append(f"[Reflection] decision={decision}, failure={failure}")

    return state

