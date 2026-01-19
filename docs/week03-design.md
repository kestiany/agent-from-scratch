# Agent Learning Journey · Week 03 Design

> **主题**：任务可以失败，但系统不能乱
>
> **核心目标**：在已有 Agent Kernel 的基础上，引入 *Reflection / Retry / Replan*，让 Agent 在失败场景下依然保持可控、可解释。

---

## 一、为什么需要 Week 03？

在 Week 01 中，我们已经构建了一个最小可运行的 Agent Kernel：

```
Input → Think → Act → Evaluate → Output
```

它可以完成一次完整任务，但存在一个致命问题：

> **一旦中间步骤失败，系统就失去控制。**

具体表现为：

* 工具失败后直接输出错误结果
* 中间产物质量很差，但依然继续执行
* Agent 无法解释「为什么失败」「下一步该做什么」

Week 03 的设计目标正是解决这个问题。

---

## 二、Week 03 的设计原则

### 原则 1：失败是常态，而不是异常

在真实任务中，失败几乎不可避免：

* LLM 输出不符合预期
* 工具调用失败
* 信息不足导致判断失真

**正确的设计不是避免失败，而是管理失败。**

---

### 原则 2：失败处理必须系统化

失败不能靠 prompt 临时补救，而必须进入系统状态：

* 被记录
* 被评估
* 被决策

这要求我们在 Agent 架构中引入明确的控制机制。

---

## 三、核心机制一：Control Decision

### 1. 决策枚举

我们在 Week 03 中引入了一个明确的控制决策枚举：

```python
ControlDecision = Literal[
    "continue",  # 当前步骤成功，进入下一步
    "retry",     # 当前步骤失败，但值得再试一次
    "replan"     # 当前计划不成立，需要重新规划
]
```

这个枚举的作用是：

> **把“下一步做什么”的判断，从隐式逻辑变成显式状态。**

---

### 2. 决策不是由 Kernel 做出的

一个非常重要的设计选择是：

> **Kernel 不做智能判断，只执行决策。**

真正做判断的是：

* `evaluate`（结果是否成功）
* `reflect`（基于失败类型给出控制决策）

Kernel 只是忠实执行 `control_decision`。

---

## 四、核心机制二：Reflection

### 1. Reflection 的职责边界

Reflection 并不是“反思人生”，而是一个非常工程化的模块：

> **基于当前 step 的执行结果，判断系统该如何继续。**

它回答的不是：

* “我是不是很笨？”

而是：

* 这次失败是否偶发？
* 重试是否可能成功？
* 当前 plan 是否已经不成立？

---

### 2. Reflection 的输入

Reflection 只依赖于状态，不依赖外部信息：

* `step_success`
* `retry_count / max_retry`
* `last_failure`

这保证了反思逻辑的**可复现性与可测试性**。

---

### 3. Reflection 的输出

Reflection 的唯一输出是：

```python
state["control_decision"]
```

它不会直接修改 plan，也不会推进 step。

---

## 五、核心机制三：Retry Policy

### 1. 为什么 Retry 不能无限发生？

无限 retry 会导致：

* 死循环
* Token 浪费
* 难以解释的行为

因此 Retry 必须是一个**有上限的、被计数的行为**。

---

### 2. Retry 相关状态字段

在 Week 03 中，我们引入：

```python
retry_count: int
max_retry: int
last_failure: Optional[str]
```

这些字段使失败行为变得：

* 可观察
* 可分析
* 可调优

---

## 六、Kernel 在 Week 03 中的角色

一个关键判断：

> **Week 03 并没有让 Kernel 变聪明，而是让 Kernel 更可靠。**

Kernel 的职责仍然是：

* 控制主循环
* 判断是否继续
* 执行 control_decision

所有“智能”仍然分布在节点中。

---

## 七、失败场景示例（抽象级）

### 场景 1：工具调用失败

* `action` 标记 `step_success = False`
* `evaluate` 记录失败原因
* `reflect` 判断：retry
* Kernel 重试当前 step

---

### 场景 2：连续失败

* retry_count 达到上限
* reflect 输出 replan
* Kernel 清空 plan，回到起点

---

## 八、Week 03 的产出总结

完成 Week 03 后，Agent 系统具备了以下能力：

* 任务可以失败，但不会失控
* 系统行为可解释、可追踪
* 失败处理逻辑清晰、可扩展

更重要的是：

> **Agent 不再是“一次性推理器”，而是一个“运行中的系统”。**

---

## 九、对后续 Weeks 的意义

Week 03 的设计为后续所有能力奠定了基础：

* Week 03 的“可信代码分析”依赖 Reflection
* Week 04 的“用户可控体验”依赖 Retry / Replan
* Week 05 之后的多 Agent 协作，依赖清晰的失败边界

如果没有 Week 03，后续所有复杂能力都会退化为不可控的 prompt 拼接。

---

## 十、阶段性结论

> **Week 01 解决了“能不能跑”，**
> **Week 03 解决了“乱不乱”。**

这是 Agent 系统从 Demo 走向工程的第一道分水岭。
