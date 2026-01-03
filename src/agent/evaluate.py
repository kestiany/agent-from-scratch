from agent.state import AgentState

def evaluate(state: AgentState) -> AgentState:
    state["current_step"] += 1
    if state["current_step"] >= len(state["plan"]):
        state["done"] = True
    return state