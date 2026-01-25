import argparse

from crew.planner import PlannerAgent
from crew.executor import ExecutorAgent
from crew.reviewer import ReviewerAgent

from orchestration.tracer import ExecutionTracer
from orchestration.crew_loop import run_agent_system

# llm 实例
class DummyLLM:
    pass

    def generate(self, prompt: str) -> str:
        return "YES. 结果符合预期。"

def parse_args():
    parser = argparse.ArgumentParser(
        description="Agent From Scratch - CLI"
    )

    parser.add_argument(
        "task",
        type=str,
        help="The task you want the agent to perform"
    )

    parser.add_argument(
        "--show-plan",
        action="store_true",
        help="Display the generated task plan"
    )

    parser.add_argument(
        "--show-trace",
        action="store_true",
        help="Display execution trace"
    )

    parser.add_argument(
        "--resume-from-task",
        type=str,
        default=None,
        help="Resume execution from given task id (e.g. 2)"
    )

    return parser.parse_args()


def print_plan(plan):
    print("\n📋 Task Plan")
    print("-" * 40)
    for t in plan.subtasks:
        print(f"[{t.id}] {t.objective} ({t.task_type})")
    print("-" * 40)


def print_trace(tracer):
    print("\n🧠 Execution Trace")
    print("-" * 40)
    for e in tracer.events:
        etype = e["type"]

        if etype == "run_start":
            print(f"▶ Run started: {e['goal']}")

        elif etype == "plan":
            print("▶ Plan generated:")
            for i, obj in enumerate(e["subtasks"], 1):
                print(f"  {i}. {obj}")

        elif etype == "task_start":
            print(f"▶ Start Task {e['task_id']}: {e['objective']}")

        elif etype == "review":
            status = "✅ PASS" if e["passed"] else "❌ FAIL"
            print(f"▶ Review Task {e['task_id']}: {status}")

        elif etype == "task_done":
            print(f"▶ Task {e['task_id']} finished [{e['status']}]")

        elif etype == "run_finish":
            print("▶ Run finished")

    print("-" * 40)


def main():
    args = parse_args()

    llm = DummyLLM()

    planner = PlannerAgent(llm)
    executor = ExecutorAgent(llm)
    reviewer = ReviewerAgent(llm)
    tracer = ExecutionTracer()

    plan, tracer, pattern = run_agent_system(
        user_input=args.task,
        planner=planner,
        executor=executor,
        reviewer=reviewer,
        tracer=tracer,
        resume_from_task_id=args.resume_from_task
    )

    if args.show_plan:
        print_plan(plan)

    if args.show_trace:
        print_trace(tracer)

    print("\n✅ Final Result")
    print("-" * 40)
    for t in plan.subtasks:
        print(f"[{t.id}] {t.status} → {t.result}")
    print("-" * 40)


if __name__ == "__main__":
    main()
