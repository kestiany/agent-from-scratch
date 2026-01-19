# Agent Learning Journey · Week 04 Design

> **主题**：从“能跑的 Agent”到“可被使用的 Agent”
> **阶段**：Agent Productization / Runtime Control Boundary
> **核心目标**：为单 Agent 系统引入**产品级边界、拒绝规则、不确定性表达与首个真实入口（CLI）**，让系统第一次具备“可以交给别人用而不失控”的能力。

---

## 0. One‑Sentence Goal (Week 4)

> **Define strict task boundaries, refusal policies, uncertainty semantics, and a stable IO contract, so the Agent becomes controllable, honest, and usable by real users — not just runnable by its author.**

---

## 1. Background (Week 1–3 Recap)

By the end of Week 3, the Agent system already had:

* A stable `AgentKernel` main loop
* Explicit failure handling (`retry / replan / reflect`)
* Clear execution stages:

```
understanding → risk_detection → risk_qualification → reporting
```

* Structured state, traceable history, controllable recovery

At this point, the system was:

> ✔ controllable
> ✔ explainable
> ✔ resilient

But still:

> ❌ not usable by real users
> ❌ no task boundary
> ❌ no refusal policy
> ❌ no input / output contract

It was an **engineering kernel**, not a **product prototype**.

Week 4 marks the first transition from:

> “Agent runtime design” → “Agent product design”.

---

## 2. Core Insight of Week 4

### 2.1 The Real Risk Is Not Weakness — It Is Over‑Confidence

Unlike classical systems, an LLM‑based Agent:

* Almost always produces an answer
* Often sounds confident
* Rarely admits uncertainty by default

This leads to the most dangerous failure mode:

> **The Agent answers questions it is not qualified to answer.**

Therefore, Week 4 adopts a new core principle:

> **Output confidence must never exceed input certainty.**

This week is not about making the Agent stronger.

It is about making the Agent:

* honest
* bounded
* stoppable
* trustworthy

---

## 3. Product‑Level Task Definition

### 3.1 Single Supported Task

Week 4 intentionally restricts the system to exactly one task:

> **Single‑file backend code risk analysis (static, Java only)**

Scope:

* Input: one complete Java backend source file
* Task: detect potential risks within the file
* Output: structured risk report + confidence + limitations

Non‑goals:

* No project‑level analysis
* No call‑graph / architecture inference
* No runtime simulation
* No business intent guessing

---

### 3.2 Task Output Principles

The Agent must:

* Never invent business semantics
* Never infer system‑level behavior
* Never claim performance / concurrency issues
* Never output conclusions unsupported by input

Core rule:

> **If information is insufficient, the correct behavior is refusal — not guessing.**

---

## 4. Refusal Policy (Critical Design)

Week 4 introduces the first formal **Refusal / Downgrade Policy**.

### 4.1 Explicitly Unsupported Capabilities

The Agent must reject or downgrade when asked to:

* Analyze multiple files or projects
* Infer architecture or system design
* Run or simulate code
* Perform performance / concurrency analysis
* Guess business logic

---

### 4.2 Invalid Input Handling

The Agent must immediately abort when:

* Input is not code
* Code fragment is too short / meaningless
* Language is not supported (non‑Java)

Abort behavior requirements:

* Explicit user‑visible refusal message
* Do not enter the execution loop
* Do not output any risk conclusions

---

## 5. Uncertainty & Confidence Semantics

### 5.1 Risk Classification

Every detected risk must belong to one of three categories:

* **Confirmed risk** (`confidence = high / medium`)
* **Uncertain risk** (`confidence = low`)
* **Insufficient information → abort task**

---

### 5.2 Mandatory Limitations Section

Every final report must include:

* Uncertain risk count
* A `limitations` field explaining:

  * static only
  * single file only
  * no runtime context
  * possible false positives

Design principle:

> **Uncertainty must be part of the output schema, not hidden in text.**

---

## 6. Failure Control Philosophy (Extension of Week 2–3)

Week 4 does not change the core control loop:

```
think → action → evaluate → reflect → control
```

But it adds a new layer:

> **Product‑level failure semantics**

New failure categories:

* Unsupported task → immediate abort
* Insufficient information → downgrade / stop
* Boundary violation → refusal

Retry / Replan still apply only inside valid task scope.

---

## 7. IO Contract Design (CLI Interface)

### 7.1 Why CLI First

Week 4 deliberately chooses CLI as the first public interface.

Rationale:

* Exposes real execution behavior
* Makes retries and reflections visible
* Forces traceability
* Avoids UI hiding system flaws

CLI is not the final product.

It is:

> **A microscope for system correctness.**

---

### 7.2 Input Contract

CLI accepts only:

* One full Java source file (raw text)

Prohibited:

* Multiple files
* Mixed natural language instructions
* Partial snippets without semantic context

---

### 7.3 Output Contract

Final output schema is fixed:

* `summary`
* `risk_count`
* `risks[]` (type / position / severity / confidence)
* `limitations`

Execution trace must always print:

* step history
* reflection decisions
* control transitions

---

## 8. Kernel & State Evolution

### 8.1 Control Authority Remains Unchanged

As in Week 2–3:

* Kernel never makes intelligent decisions
* Reflection produces signals only
* Kernel executes `control_decision`

---

### 8.2 New Product‑Level State Semantics

Key fields emphasized in Week 4:

* `history` → full explainability
* `last_failure` → refusal & downgrade reason
* `confidence` → risk reliability
* `done` → controlled termination

Principle:

> **All uncertainty and refusal must live in state, not only in text.**

---

## 9. Capability Boundary Summary (End of Week 4)

System now supports:

* Single‑file Java static risk analysis
* Structured risk output
* Explicit uncertainty expression
* Controlled refusal & downgrade
* Full execution trace
* Stable CLI interface

System explicitly does NOT support:

* Multi‑file reasoning
* AST deep understanding
* Call‑graph analysis
* Architecture inference
* Runtime behavior modeling

---

## 10. Transition to Week 5

Week 4 intentionally avoids capability expansion.

Week 5 evolution will focus on:

* AST‑level structured parsing
* Controlled multi‑file context
* Stronger evidence‑based reflection
* Memory as long‑term hypothesis storage

But one rule will remain invariant:

> **Never increase intelligence before increasing controllability.**

---

## 11. Final Conclusion

Week 4 marks a critical milestone:

From:

> A controllable Agent kernel

To:

> A bounded, honest, stoppable Agent prototype

The most important outcome is not technical capability, but methodology:

> **Agent engineering is not about maximizing intelligence — it is about engineering control systems around intelligence.**

This principle will govern all subsequent weeks.
