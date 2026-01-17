# 🧠 Code Analysis Agent (Week 4)

> A **controlled, explainable, and non-hallucinating** code analysis Agent  
> Currently supports **single-file Java backend code analysis only**

🌐 **Language**: English | [简体中文](README.zh-CN.md)

---

## What is this?

This is a **single-purpose Agent** designed to analyze backend code (Java) **only within its proven capability boundaries**.

It uses an explicit **state-driven execution model** and **control decisions** to ensure that:

- It does not hallucinate
- It does not overclaim certainty
- It clearly states limitations when information is insufficient

---

## Why does this Agent exist?

Most AI-based code analysis tools suffer from:

1. **Overconfidence** under insufficient context  
2. **Lack of explainability** (black-box outputs)  
3. **Uncontrolled execution flows** after failures  

This project takes a different stance:

> **Do less — but do it reliably, traceably, and honestly.**

---

## Design Principles

- ✅ Single-task Agent (code analysis only)
- ✅ Explicit state machine (state is the source of truth)
- ✅ Failure is visible and recorded
- ✅ Uncertainty is explicitly modeled
- ❌ No business intent guessing
- ❌ No project-level analysis
- ❌ No code execution

---

## Supported Scope (Week 4)

### ✅ Supported

- Java **single-file** backend code
- Method-level / class-level risk detection
- Uncertain risk labeling (`confidence = low`)
- Structured analysis reports
- CLI-based execution

### ❌ Not Supported

- Project-level dependency analysis
- Cross-file call graph analysis
- Runtime behavior inference
- Performance benchmarking or security scanning

---

## Agent Workflow

```

understanding
↓
risk_detection
↓
risk_qualification
↓
reporting

````

Each step is:

- Explicit
- Evaluated
- Reflective
- Controllable (`continue / retry / replan`)

---

## Core Architecture

### AgentState — State is the First-Class Citizen

All behaviors are driven by state transitions.

```python
AgentState = {
  user_input,
  objective,
  plan,
  current_step,
  memory,
  scratchpad,
  history,
  step_success,
  retry_count,
  control_decision
}
````

---

### AgentKernel — Execution Controller

Execution loop:

```
think → action → evaluate → reflect → control_decision
```

Rules:

* `evaluate` cannot be skipped
* `reflect` always runs
* Control decisions are explicit and limited

---

### Risk Model

```json
{
  "id": "uuid",
  "title": "Potential Null Pointer Risk",
  "description": "...",
  "severity": "high | medium | low",
  "confidence": "high | medium | low",
  "type": "method | class",
  "position": "Class.method()"
}
```

**Important distinction:**

* `severity` = impact if true
* `confidence` = certainty of correctness

---

## Failure & Uncertainty Policy

### Returns “Insufficient Information” when:

* Input code is too trivial
* No analyzable structure exists
* Context is fundamentally missing

### Task terminates when:

* Input is not code
* Repeated failures exceed retry limit

### Confidence is downgraded when:

* Context relies on assumptions
* Behavior depends on framework conventions
* Risk is inferred but not provable

---

## CLI Usage

```bash
python src/main.py
```

Example input:

```java
User user = repository.findById(id);
return user.getName();
```

Example output (simplified):

```json
{
  "summary": "1 potential risk detected",
  "confidence": "medium",
  "limitations": "Single-file static analysis only"
}
```

---

## Project Structure

```
agent-from-scratch/
├── agent/
│   ├── kernel.py
│   ├── state.py
│   ├── think.py
│   ├── action.py
│   ├── evaluate.py
│   └── reflect.py
├── src/
│   └── main.py
├── README.md
└── README.zh-CN.md
```

---

## Week 4 Definition of Done

* [x] State-driven execution
* [x] Traceable decision history
* [x] Explicit uncertainty modeling
* [x] Controlled failure handling
* [x] CLI demonstration ready
