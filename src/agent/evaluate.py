from agent.state import AgentState

def evaluate(state: AgentState) -> AgentState:
    step = state["plan"][state["current_step"]]

    if step == "risk_detection" and not state["memory"]:
        state["step_success"] = False
        state["last_failure"] = "no_risk_found"

    state["history"].append(
        f"Evaluate: {step}, success={state['step_success']}"
    )
    return state
