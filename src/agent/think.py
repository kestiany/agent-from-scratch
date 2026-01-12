from agent.state import AgentState

def think(state: AgentState) -> AgentState:
    if not state["plan"] and not state["done"]:
        step = state["plan"][state["current_setp"]]

        if step == "understanding":
            state["scratchpad"].append("理解代码结构、语言和上下文")
        elif step == "risk_detection":
            state["scratchpad"].append("扫描潜在风险点(逻辑 / 安全 / 可维护性)")
        elif step == "risk_qualification":
            state["scratchpad"].append("判断风险是否确定, 是否需要降级为不确定风险")
        elif step == "reporting":
            state["scratchpad"].append("整理结构化风险报告")

        state["history"].append(f"Think: {step}")
    return state
