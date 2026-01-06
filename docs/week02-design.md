# Week 2 — Failure, Reflection, and Recovery

> **Theme**: Reflection / Retry / Replan
> **Stage**: Agent Runtime Design
> **Goal**: Build a controllable, explainable, and testable failure–recovery loop for a single Agent.

---

## 0. One‑Sentence Goal (Week 2)

> **Enable the Agent to detect failure, reflect on whether its current plan hypothesis still holds, and decide whether to retry or replan — without breaking control‑flow clarity.**

---

## 1. Background (Week 1 Recap)

By the end of Week 1, the Agent already had:

* A minimal `AgentState`
* A Kernel loop: **Think → Act → Evaluate**
* Sequential plan execution (`current_step`)

However, failure was only implicit:

* No explicit failure semantics
* No self‑correction
* Execution stopped only when reaching hard limits

This made the system closer to a **workflow** than a true **Agent**.

---

## 2. Core Concept of Week 2

### 2.1 Key Insight

> **The difference between a workflow and an agent is not tools or memory — it is how failure is handled.**

Week 2 focuses on completing the **single‑agent mental loop**:

```
Failure → Reflection → Decision → Continue
```

---

## 3. Failure Semantics (Day 8)

### 3.1 What Is a “Step Failure”?

Failures are classified into two categories:

#### 1. Technical Failure

Failures caused by the execution environment rather than reasoning quality:

* Network errors
* Service unavailability
* Runtime exceptions
* Environment or dependency issues

#### 2. Business (Semantic) Failure

Failures where execution succeeds but intent is not satisfied:

* Output is empty
* Output is irrelevant
* Output does not meet user expectations

---

### 3.2 Retry vs Replan Criteria

| Decision   | Meaning                                                                             |
| ---------- | ----------------------------------------------------------------------------------- |
| **Retry**  | The current plan hypothesis still holds, but execution was insufficient or unstable |
| **Replan** | The current plan hypothesis is invalid and must be replaced                         |

**Initial rules:**

* Technical failures → usually **Retry**
* Business failures → usually **Replan**

These rules are *heuristics*, not hard guarantees.

---

## 4. Making Failure Visible in State (Day 9)

### 4.1 Design Principle

> **Failure must be visible in state, not inferred from logs.**

### 4.2 State Extension (Minimal)

```python
class AgentState(TypedDict):
    ...
    history: List[str]          # execution trace
    failure_record: List[str]   # structured failure info
```

**Notes:**

* `history` is for explainability
* `failure_record` is for decision‑making
* State growth is controlled by:

  * truncation
  * summarization
  * or windowing (future work)

---

## 5. Reflection as a First‑Class Node (Day 10)

### 5.1 Reflection Is a Node, Not a Log

Reflection is treated as a **pluggable runtime node**:

```python
while should_continue(state):
    think(state)
    action(state)
    evaluate(state)

    if should_reflect(state):
        reflect(state)
```

Reflection is **not embedded** into Think / Act / Evaluate.

---

### 5.2 Responsibility of Reflection

> **Reflection answers exactly one question:**
> *Does the current plan hypothesis still hold?*

Reflection:

* Summarizes failure context
* Evaluates hypothesis validity
* Produces a **decision recommendation**

Reflection **does NOT**:

* Change control flow
* Execute retries
* Trigger replans directly

---

## 6. Retry / Replan Control Flow (Day 11)

### 6.1 Control Authority

> **Only the workflow controls execution flow.**

Reflection only produces signals.

---

### 6.2 Control States

| Control State | Behavior                                            |
| ------------- | --------------------------------------------------- |
| Continue      | Move to next step or finish                         |
| Retry         | Retry current step, increment `retry_count`         |
| Replan        | Discard plan, regenerate plan, reset `current_step` |

---

### 6.3 Retry Logic

```text
retry:
- retry_count += 1
- current_step unchanged

if retry_count >= max_retry:
    trigger re‑reflection
```

---

### 6.4 Replan Logic

```text
replan:
- clear existing plan
- inject reflection output into planning prompt
- regenerate plan
- current_step = 0
```

---

## 7. Failure → Reflection → Decision Loop (Key Insight)

Actual runtime behavior:

```text
Step fails
↓
Reflection evaluates hypothesis
↓
Control decision:
    - hypothesis valid → Retry
    - hypothesis invalid → Replan
```

**Retry and Replan are not parallel branches — they are stages of the same reasoning loop.**

---

## 8. Testing Failure Behavior (Day 12)

### Required Scenarios

1. Step fails → Retry → Success
2. Step fails repeatedly → Replan → Continue

Testing focuses on:

* State transitions
* Control decisions
* Not LLM quality

---

## 9. Architecture Review (Day 14)

### 9.1 Is Reflection Optional?

* Architecturally: **pluggable**
* In this Agent design: **essential**

What is mandatory is **hypothesis validation**, not a specific reflection implementation.

---

### 9.2 Can Retry Be Removed?

Yes.

* Agent still works using only Replan
* Cost and latency increase

Retry is an **efficiency optimization**, not a correctness requirement.

---

### 9.3 Will Tools or Memory Break Control Flow?

No.

* Tools = execution capability
* Memory = evidence source
* Control authority remains in the workflow

---

## 10. Capability Upgrade Summary

**Before Week 2:**

* Executes plans blindly
* Stops only at hard limits

**After Week 2:**

* Continuously validates plan assumptions
* Distinguishes execution failure vs plan failure
* Can recover without external intervention

> **The Agent now adapts its strategy, not just its actions.**

---

## 11. Known Limitations (Intentional)

* Reflection logic is simple
* Failure classification is heuristic‑based
* No tool / memory integration yet

These are deliberate to preserve control‑flow clarity.

---

## 12. Transition to Week 3

Week 3 will extend this architecture by adding:

* Tools as capability providers
* Memory as hypothesis evidence
* Stronger reflection signals

**The failure–reflection–decision loop remains unchanged.**
