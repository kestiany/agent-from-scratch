# Agent From Scratch

> 从 **第一性原理** 构建一个可控、可测试、可演进的 Agent 系统。

本仓库记录了一个按周推进的 Agent 架构演化过程。**到第 06 周为止**，系统已经形成一个完整、可追踪、可回放的 Agent 执行内核，而非 Demo 拼装。

🌐 **语言**：简体中文 | [English](README.md)

---

## ✨ 核心设计理念

* **内核优先**：Agent 能力来自清晰的执行循环，而不是 Prompt 技巧
* **状态显式化**：所有状态变化都可序列化、可调试
* **Plan → Execute → Review**：任何任务都必须经过评审
* **默认可追踪**：每次运行都有完整执行轨迹
* **轻框架**：避免黑盒编排

---

## 🧠 第 06 周已完成能力

### 1️⃣ Agent Kernel（执行内核）

位置：`src/agent/kernel.py`

职责：

* 驱动 Think / Act / Evaluate / Reflect 循环
* 不包含业务逻辑
* 保证执行确定性

---

### 2️⃣ Planner / Executor / Reviewer 协作闭环

* Planner 生成 `TaskPlan`
* Executor 执行子任务
* Reviewer 判断是否通过
* 未通过则进入反思或重试

这是一个**可读、可调试、可替换**的控制流，而不是 DAG 黑箱。

---

### 3️⃣ 统一状态与 Schema

* 明确的任务状态：PENDING / IN_PROGRESS / COMPLETED / FAILED
* 状态是系统唯一事实来源
* 易于持久化与恢复

---

### 4️⃣ Execution Trace（执行轨迹）

每一次运行都会记录：

* Run 生命周期
* 子任务执行情况
* Review 结果

为后续的：

* Debug
* Replay
* Resume
  打下基础。

---

## 📂 项目结构

```
src/
├── agent/            # Agent 内核与认知步骤
├── crew/             # Planner / Executor / Reviewer
├── orchestration/    # 执行循环与追踪
├── schema/           # 状态与任务定义
├── examples/         # 示例
└── main.py           # CLI 入口
```

---

## ▶️ 运行示例

```bash
python ./src/main.py  --show-plan "分析该系统的主要风险"
```

---

## 🧭 接下来（第 07 周以后）

* 基于 Trace 的中断 / 恢复
* Memory Layer（长期 / 短期）
* Tool 执行隔离
* 多方案对比

---

## 📜 License

MIT
