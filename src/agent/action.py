import uuid
from agent.state import AgentState

def action(state: AgentState) -> AgentState:
    step = state["plan"][state["current_step"]]

    if step == "risk_detection":
        risk = {
            "id": str(uuid.uuid4()),
            "title": "潜在空指针风险",
            "description": "某方法返回值在使用前未进行 null 判断",
            "suggestion": "在使用返回值前增加 null 判断",
            "severity": "high",
            "confidence": "low",   # 注意：初始是低
            "type": "method",
            "position": "HelloService.process()"
        }

        state["memory"].append(risk)
        state["step_success"] = True

    elif step == "risk_qualification":
        qualified = []
        for r in state["memory"]:
            r["confidence"] = "medium"
            qualified.append(r)
        state["memory"] = qualified
        state["step_success"] = True
    elif step == "reporting":
        report = build_report(state)
        state["final_output"] = report
        state["done"] = True
        state["step_success"] = True
    else:
        state["step_success"] = True

    state["history"].append(f"Action:{step}")
    return state

def build_report(state: AgentState) -> AgentState:
    risks = state["memory"]

    count = {
        "high": 0,
        "medium": 0,
        "low": 0,
        "uncertain": 0
    }

    for r in risks:
        sev = r["severity"]
        if r["confidence"] == "low":
            count["uncertain"] += 1
        else:
            count[sev] += 1

    summary = {
        f"本次代码分析共发现 {len(risks)} 个潜在风险，"
        f"其中高风险 {count['high']} 个，"
        f"中风险 {count['medium']} 个，"
        f"不确定风险 {count['uncertain']} 个。"
    }

    return {
        "summary": summary,
        "risk_count": count,
        "risks": risks,
        "limitations": (
            "该分析基于单文件静态分析，"
            "未包含运行时行为、上下文依赖及项目级调用关系，"
            "部分风险可能存在误判。"
        )
    }