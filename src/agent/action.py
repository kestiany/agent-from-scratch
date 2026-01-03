from agent.state import AgentState

def action(state: AgentState) -> AgentState:
    step = state["plan"][state["current_step"]]
    state["scratchpad"].append(f"正在执行：{step}")
    state["history"].append(f"执行步骤 {state['current_step']}: {step}")
    return state