# Week 07 Design — Experience-Aware Agent Runtime

## 1. 本周定位

Week 07 是整个 Agent 系统从「可执行」迈向「可演进」的关键节点。

在前 6 周中，系统已经具备：

- 明确的 Agent Kernel
- 可控的 Planner / Executor / Reviewer 协作闭环
- 可追踪、可回放的执行 Trace
- 确定性的运行时行为

但此时的 Agent 仍然是**一次性执行系统**：

> 每次运行都像“第一次做这件事”。

Week 07 的目标不是让 Agent 更聪明，而是让系统具备一种更接近真实工程系统的能力：

> **从历史执行中总结经验，并将其以“可解释建议”的形式反馈给未来决策。**

---

## 2. 设计目标

### 核心目标

构建一条清晰、可控的经验反馈链路：

```

Execution → Experience → Pattern → Advisory → Planning

```

使系统具备以下能力：

- 记住做过什么（Experience）
- 发现重复问题（Pattern）
- 总结经验性建议（Advisory）
- 在规划阶段参考历史，而非强制执行

### 明确不做的事情

为避免系统失控，本周 **刻意不引入**：

- 自动参数学习
- Planner 逻辑自修改
- 隐式行为调整
- 黑盒记忆注入

所有经验影响必须满足：

> **显式、可解释、可关闭、可回溯**

---

## 3. 核心设计原则

### 3.1 Experience ≠ Intelligence

Experience 只是事实记录，不包含推理或决策。

系统必须能够回答：

- 发生了什么？
- 结果如何？
- 代价是多少？
- Reviewer 如何评价？

但 **不回答**：

- 下次一定要怎么做

---

### 3.2 Advisory ≠ Rule

经验只能生成**建议（Advisory）**，而不能生成规则。

原因：

- 经验是局部的
- 任务上下文是变化的
- 过拟合历史会导致系统退化

Planner 永远保留最终决策权。

---

### 3.3 Runtime 主干不被侵蚀

Week 07 的所有能力均以「旁路」形式存在：

- 不改变 Kernel 行为
- 不破坏 Crew Loop
- 不引入隐式控制流

如果关闭 Experience / Advisory，系统行为应退化回 Week 06。

---

## 4. 系统结构概览

Week 07 引入的核心模块位于 Runtime 主干之外：

```

Agent Runtime
├── Execution Loop (unchanged)
│   ├── Planner
│   ├── Executor
│   └── Reviewer
│
├── Experience Layer
│   ├── Experience Store
│   └── Experience Schema
│
├── Pattern Layer
│   └── Pattern Extractor
│
└── Advisory Layer
├── Advisory Builder
└── Advisory Memory

```

Execution Loop 是“现在”，  
Experience / Pattern / Advisory 是“过去对未来的影响”。

---

## 5. Experience Layer 设计

### 5.1 TaskExperience

`TaskExperience` 是本周新增的核心事实对象。

它记录一次完整任务运行的**总结性结果**，而非细粒度 Trace。

包含但不限于：

- 任务签名（类型 / 领域 / 约束）
- Planner 生成的任务结构摘要
- 最终执行结果状态
- Token / 时间 / 重试次数等成本信息
- Reviewer 的文字总结

设计要点：

- 结构化 + 人可读
- 不依赖 LLM 才能理解
- 可序列化、可持久化

---

### 5.2 Experience Store

Experience Store 是一个**事实数据库**：

- 只负责存储与查询
- 不做推理
- 不做聚合决策

它为 Pattern Extraction 提供稳定输入。

---

## 6. Pattern Extraction 设计

Pattern Extractor 的职责是：

> 从大量 TaskExperience 中，发现“重复出现的现象”。

例如：

- 某类任务经常失败
- 某种计划结构成本异常高
- Reviewer 反复给出相同建议

设计特点：

- 基于规则 / 统计，而非生成式推理
- 输出 Pattern 是中间产物，不直接影响决策
- 可独立测试

Pattern 本身仍然是“观察结论”，而非行动建议。

---

## 7. Advisory Layer 设计

### 7.1 Advisory 的定义

Advisory 是 Pattern 的“人话版本”。

它具备：

- 明确的适用范围（scope）
- 建议内容（suggestion）
- 来源（哪些 Pattern 触发）
- 可选置信度或权重

Advisory 的形式应当满足：

> 人类工程师读完后，会说：“嗯，这个提醒是有道理的。”

---

### 7.2 Advisory Memory

Advisory Memory 是 Planner 可查询的建议集合。

特点：

- 可按任务签名过滤
- 可配置是否启用
- 可被 Reviewer 回溯验证

它是系统中**唯一允许“经验影响决策”的入口**。

---

## 8. Planner Advisory Injection

Planner 在生成 TaskPlan 时，可以：

- 查询 Advisory Memory
- 将建议作为额外上下文输入
- 明确区分：哪些建议被采纳，哪些被忽略

重要约束：

- Advisory 永远不是 hard constraint
- Planner 逻辑不依赖 Advisory 的存在
- Planner 必须在无 Advisory 情况下正常工作

---

## 9. 运行时行为总结

引入 Week 07 能力后，系统行为变化为：

- 执行流程保持不变
- 每次完整运行都会沉淀 Experience
- 系统逐渐形成“经验库”
- 未来任务规划开始具备历史参考

但系统依然是：

> **确定性内核 + 显式经验反馈**

---

## 10. 取舍与后果

### 获得的能力

- 行为稳定性提升
- 重复失败概率下降
- 系统具备“工程级记忆”

### 明确的限制

- 不自动学习
- 不保证最优策略
- 经验质量依赖 Reviewer

这些限制是**刻意保留的安全边界**。

---

## 11. 为 Week 08 做好的铺垫

Week 07 的设计为后续演进提供了基础：

- Advisory 可引入置信度与衰减
- Pattern 可升级为更复杂的分析
- Planner 可进行多方案对比
- Reviewer 可反向校正 Advisory

但所有这些，都必须建立在：

> **Week 07 的“经验 → 建议 → 决策分离”结构之上**

---

## 12. 小结

Week 07 并没有让 Agent “更聪明”。

它让系统变得：

- 更像一个长期运行的工程系统
- 更接近真实团队的复盘与决策方式
- 更适合被扩展、被维护、被信任

这是 Agent 从 Demo 走向 Runtime 的分水岭。