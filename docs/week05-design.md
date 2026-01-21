# Runtime Skeleton: Planner / Executor / Reviewer Architecture

## 1. Objective of Week 05

Week 05 focuses on building the **first runnable Agent Runtime Skeleton** on top of the existing AgentKernel and workflow system from Week 04.

Goals:

* Introduce role-based multi-agent structure (Planner / Executor / Reviewer)
* Preserve and reuse Week04 workflow system
* Build an end-to-end runnable pipeline with CLI entry
* Achieve traceable, explainable execution flow

This week marks the transition from *single-agent workflow* to a **multi-role agent system**.

---

## 2. Architecture Overview

High-level runtime loop:

```
User Input
   ↓
PlannerAgent  → TaskPlan (SubTask[])
   ↓
ExecutorAgent → route & execute each SubTask
   ↓
ReviewerAgent → review & finalize
   ↓
Final Output
```

Key design principle:

> Planner decides *what to do*
> Executor decides *how to do it*
> Workflow decides *how to execute specific domains*

---

## 3. Relationship to Week 04 Workflow

Week 04 introduced a domain workflow:

```
understanding → risk_detection → risk_qualification → reporting
```

In Week 05:

* Planner output **does NOT assume** this workflow
* Executor performs **routing**:

| SubTask Type                | Execution Path            |
| --------------------------- | ------------------------- |
| Matches workflow capability | AgentKernel.run(workflow) |
| Non-matching                | Free-form LLM execution   |

This allows:

* Multiple workflows in future
* Mixed reasoning + domain pipelines
* No coupling between planning and execution engine

---

## 4. Module Responsibilities

### 4.1 BaseRole

Common abstraction for all agent roles.

Responsibilities:

* Hold LLM instance
* Provide unified run() interface

---

### 4.2 PlannerAgent

Input: raw user task
Output: TaskPlan (list of SubTask)

Responsibilities:

* Decompose complex tasks
* Assign semantic task_type
* Produce ordered execution plan

---

### 4.3 ExecutorAgent

Responsibilities:

* Iterate through SubTask list
* Route each subtask to:

  * Week04 workflow (AgentKernel)
  * or free-form execution
* Collect ExecutionResult list

Routing Strategy (current version):

* If subtask.task_type in workflow_capabilities → workflow
* Else → free execution

---

### 4.4 ReviewerAgent

Responsibilities:

* Review execution outputs
* Check completeness & coherence
* Produce final response

---

## 5. Runtime Characteristics Achieved

By end of Week 05, the system has:

* Role-based architecture
* Structured planning
* Domain workflow reuse
* CLI runnable entry
* Execution trace visibility

This forms the **minimum viable Agent runtime kernel** for future extensions:

* Failure detection
* Reflection
* Retry & replan
* Multi-workflow orchestration

---

## 6. Key Engineering Takeaways

1. Planner should not be coupled with execution workflows
2. Executor is the true policy and routing layer
3. Workflow is a specialized execution backend
4. CLI entry is essential for product-level iteration
5. Traceability is mandatory for agent reliability

---

## 7. Status

Week 05 milestone achieved:

* Multi-role runtime skeleton complete
* End-to-end execution pipeline operational
* Ready for Week 06: Reflection & Retry
