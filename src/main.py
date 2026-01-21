import argparse

from crew.planner import PlannerAgent
from crew.executor import ExecutorAgent
from crew.reviewer import ReviewerAgent
from orchestration.crew_loop import CrewLoop
from orchestration.trace import ExecutionTracer


class DummyLLM:
    pass


def build_system():
    """
    负责组装整个 Agent 系统（产品装配线）
    """
    llm = DummyLLM()

    planner = PlannerAgent(llm)
    executor = ExecutorAgent(llm)
    reviewer = ReviewerAgent(llm)

    tracer = ExecutionTracer()

    crew = CrewLoop(
        planner=planner,
        executor=executor,
        reviewer=reviewer,
        trace=tracer
    )

    return crew, tracer


def main():
    parser = argparse.ArgumentParser(description="Agent From Scratch — Week5 CLI")

    parser.add_argument(
        "--task",
        type=str,
        required=True,
        help="输入一个复杂任务，例如：分析该系统的主要风险并给出报告"
    )

    args = parser.parse_args()

    crew, tracer = build_system()

    print("\n==============================")
    print("🚀 Agent System Started")
    print("==============================\n")

    results = crew.run(args.task)

    print("\n==============================")
    print("✅ Final Results")
    print("==============================")
    for idx, r in enumerate(results, 1):
        print(f"\n[{idx}] {r}")

    print("\n==============================")
    print("🧠 Execution Trace")
    print("==============================")

    # MVP 版本：直接打印事件
    for e in tracer.events:
        print(e)


if __name__ == "__main__":
    main()
