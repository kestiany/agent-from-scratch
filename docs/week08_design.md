# Week 08 Design — Strategy, Bias, and Stability

## 🎯 Week 08 定位

**从“经验可参考”走向“行为可区分”。**

在 Week 07 中，Agent 已经具备：

* 稳定的 Runtime 内核
* 结构化 Experience
* Advisory Memory（建议而非强制）

但此时 Agent 仍然是“同一种性格”的工具。

**Week 08 的目标**是让系统开始呈现：

* 不同的决策风格
* 可预测的失败处理方式
* 稳定而可测试的长期行为

换句话说：

> Agent 不再只是“会做事”，而是开始“以某种方式做事”。

---

## 🧩 Week 08 的 4 个任务

### Task 1 — 明确失败 / 成功模式（Failure & Success Patterns）

我们明确并固定了 5 种核心模式：

**Planner 必选（直接影响规划）：**

1. ❌ 过度一次性规划
2. ✅ 分步拆解优于一次性
3. ✅ 显式验证点

**Reviewer 加分（用于评估与总结）：**
4. ❌ 策略切换过频
5. ❌ 行为发散

这些模式是：

* Planner 的启发式输入
* Reviewer 的评价基准
* 后续 Bias / Strategy 的事实来源

---

### Task 2 — 最小可行 Planner（K=3 多候选）

Planner 不再只生成一个 Plan，而是：

* 同时生成 **K=3 个候选 Plan**
* 每个 Plan 都可被解释与评分
* 基于显式规则进行打分，而非黑箱 Prompt

评分维度包括：

* 步骤粒度
* 是否包含验证点
* 与历史经验的一致性

最终 Planner 输出：

* Top-1 执行 Plan
* 其余 Plan 作为对照（用于 Trace / Debug）

> 这是从“生成答案”到“做决策”的关键跃迁。

---

### Task 3 — Bias 影响 Executor 行为（最小侵入）

Bias 被定义为：

> **失败时的默认行为倾向**，而非情绪或风格描述。

我们只在 **一个位置**引入 Bias：

**当 step 失败时，Executor 如何决定 control_decision**。

示例：

* `cautious` → 默认 retry
* `balanced` → 默认 continue
* `aggressive` → 默认 replan

这一设计保证：

* 不破坏 Kernel
* 不引入新状态机
* 但真实改变系统执行路径

---

### Task 4 — 稳定性测试场景（Design-Level）

Week 08 不追求覆盖率，而是明确：

系统在以下场景中**必须行为稳定**：

1. 连续失败但信息不足
2. 多次 retry 后仍无改进
3. Planner 多方案质量接近

这些场景定义了：

* Kernel 的边界
* Bias 的价值
* Planner 决策是否可解释

---

## 🧠 Week 08 的系统变化总结

经过 Week 08：

* Planner 开始“选择”，而不是“生成”
* Executor 具备稳定、可区分的失败行为
* Agent 行为呈现出一致性与风格

系统从：

> **工具（Tool-like）**

演进为：

> **有行为连续性的 Runtime 系统**

这为 Week 09 之后的方向收敛与可用性奠定基础。

---

## 📌 设计原则回顾

* 所有智能必须显式
* 所有偏好必须可关闭
* 所有行为必须可追溯

Week 08 的所有改动，都遵循以上三点。
