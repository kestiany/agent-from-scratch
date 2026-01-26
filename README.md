# Agent From Scratch

> Build an **agent system from first principles** — controllable, testable, and evolvable.

This repository documents a week-by-week construction of an Agent kernel without relying on heavyweight frameworks (e.g. LangGraph). By **Week 06**, the system reaches a *closed-loop, reviewable, traceable* execution architecture.

🌐 **Language**: English | [简体中文](README.zh-CN.md)

---

## ✨ Design Philosophy

* **Kernel-first**: agent capability emerges from a small, explicit execution loop
* **Single Source of Truth**: state transitions are explicit and serializable
* **Plan → Execute → Review**: every task must pass through review
* **Traceable by default**: every run produces a replayable trace
* **Framework-light**: avoid black-box orchestration

---

## 🧠 Week 06: What Is Completed

By the end of Week 06, the system achieves:

### 1. Explicit Agent Kernel

Located in `src/agent/kernel.py`

Responsibilities:

* Drive the **Think → Act → Evaluate → Reflect** loop
* Enforce execution boundaries
* Never embed business logic

The kernel is deterministic given `(state, action)`.

---

### 2. Task Planning & Crew Loop

Located in `src/crew` and `src/orchestration/crew_loop.py`

* `Planner` produces a `TaskPlan`
* `Executor` runs subtasks
* `Reviewer` validates outputs
* Loop continues until all subtasks are completed or failed

This replaces LangGraph-style DAGs with a **linear, inspectable control loop**.

---

### 3. Unified State & Schema

Located in `src/schema` and `src/agent/state.py`

* Task status is explicit (`PENDING / IN_PROGRESS / COMPLETED / FAILED`)
* State is serializable
* No hidden side effects

---

### 4. Execution Tracing

Located in `src/orchestration/tracer.py`

Each run records:

* Run start / finish
* Task start / completion
* Review results

This enables:

* Debugging
* Replay
* Future resumability

---
### Week 07 — Experience-Aware Runtime

Week 07 introduces **experience as a first-class runtime concept**.

The system now:

* Records structured task experiences
* Extracts behavior patterns from past runs
* Generates advisory knowledge (not hard rules)
* Injects experience-based suggestions into planning — optionally

#### Key additions:

* **Experience Store**  
  Persistent, factual records of task executions

* **Pattern Extraction**  
  Identifies repeated failure, inefficiency, or success patterns

* **Advisory Memory**  
  Human-readable, explainable suggestions derived from experience

* **Planner Advisory Injection**  
  Planner may consult advisory memory, but is never forced to follow it

> ⚠️ The system does **not** self-modify or auto-learn.  
> Experience influences decisions **only through explicit, inspectable context**.

---

## 📂 Project Structure

```
src/
├── agent/ # Agent kernel & cognitive steps
│ ├── think.py
│ ├── action.py
│ ├── evaluate.py
│ ├── reflect.py
│ ├── kernel.py
│ └── state.py
│
├── crew/ # Planner / Executor / Reviewer roles
│
├── orchestration/ # Execution loop, tracer, runtime glue
│
├── memory/ # Experience store & advisory memory
│
├── schema/ # Typed task, result, experience schemas
│
├── examples/ # Minimal runnable demos
│
└── main.py # CLI entry point
```

---

## ▶️ Running an Example

```bash
python ./src/main.py --show-plan "Analyze risks of this system"
```

---

## 🧭 What Comes Next (Week 08+)

* Advisory confidence & decay
* Multi-plan comparison
* Tool execution sandbox
* Controlled self-improvement loops

---

## 📜 License

MIT
