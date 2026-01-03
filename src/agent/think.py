from agent.state import AgentState

def think(state: AgentState) -> AgentState:
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
