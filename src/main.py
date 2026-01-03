from agent.kernel import AgentKernel

if __name__ == "__main__":
    agent = AgentKernel()
    result = agent.run("帮我分析这个系统设计题")

    print("==== Final Output ====")
    print(result["final_output"])

    print("\n==== History ====")
    for h in result["history"]:
        print("-", h)