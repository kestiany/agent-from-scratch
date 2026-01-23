import uuid
from schema.status import TaskStatus

def run_agent_system(
    user_input: str,
    planner,
    executor,
    reviewer,
    tracer,
    resume_from_task_id: str | None = None
):
    run_id = str(uuid.uuid4())

    plan = planner.run(user_input, run_id)
    tracer.start_run(run_id, user_input)
    tracer.record_plan(plan)

    while True:
        task = plan.get_next_task()
        if not task:
            break

        # Resume 支持（最小）
        if resume_from_task_id and task.id < resume_from_task_id:
            task.complete("[SKIPPED]")
            continue

        tracer.start_task(task)
        task.start()

        result = executor.run(task)
        review = reviewer.run(task, result)

        tracer.record_review(task, review)

        if review.passed:
            task.complete(result)
        else:
            task.fail(review.comments)
            tracer.task_done(task)
            break

        tracer.task_done(task)

    return plan, tracer
