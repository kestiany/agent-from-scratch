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
为 Debug / Replay / Resume 打下基础。

---

### 第 07 周：经验感知型 Runtime

第 07 周的核心变化是：  
**经验成为系统的一等公民**。

系统新增能力：

* 记录结构化任务经验
* 从历史执行中提取模式
* 生成可解释的经验建议
* 在规划阶段“参考经验”，但不强制执行

#### 新增模块：

* **Experience Store**：事实层，记录发生过什么
* **Pattern Extractor**：识别重复行为模式
* **Advisory Memory**：从经验中总结的建议层
* **Planner Advisory Injection**：Planner 可选择性使用建议

> ⚠️ 系统不会自动学习或自我修改。  
> 所有经验影响都必须是**显式、可解释、可关闭的**。

---

## 📂 项目结构

```
src/
├── agent/ # Agent 内核与认知步骤
├── crew/ # Planner / Executor / Reviewer
├── orchestration/ # 执行循环与运行时调度
├── memory/ # 经验存储与建议记忆
├── schema/ # 任务 / 结果 / 经验 Schema
├── examples/ # 示例
└── main.py # CLI 入口
```

---

## ▶️ 运行示例

```bash
python ./src/main.py --show-plan "分析该系统的主要风险"
```

---

## 🧭 第 08 周：策略与行为分化

第 08 周的重点不再是“增加能力”，而是：

* 多候选规划（Planner K=3）
* 显式失败 / 成功模式
* Bias 驱动的失败处理策略
* 稳定性场景定义（为长期运行做准备）

Agent 开始呈现稳定、可预测、可区分的行为风格，
从“工具”迈向“系统”。

---

## 🧭 接下来（第 09 周以后）

* 建议可信度与衰减机制
* 方向收敛（只选一个）
* 长时间运行稳定性
* 成本与错误可观测性

---

## 📜 License

MIT
