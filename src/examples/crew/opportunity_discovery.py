# opportunity_discovery.py
import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv  import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.2,
    max_tokens=2000,
    timeout=60,
)

# ========== 定义 Agents ==========
planner_agent = Agent(
    role="AI 产品机会规划专家",
    goal="将用户需求与AI能力进行系统性匹配，规划可行的产品机会方向",
    backstory="""
你是一位资深AI产品经理与技术架构师，拥有多年AI产品设计与落地经验。
你擅长将模糊的行业问题转化为清晰的产品机会结构。
你非常关注可落地性、技术可行性与长期商业价值。
你不会提出脱离现实工程条件的产品设想。
""",
    llm=llm,
    verbose=True,
    allow_delegation=False,   # 非层级模式，强烈建议关闭
    max_iter=3,               # 防止无限推理
)

research_agent = Agent(
    role="行业与用户需求分析专家",
    goal="分析指定领域的用户核心痛点与未被满足的需求",
    backstory="""
你是一位资深行业研究员，长期研究不同行业的用户需求与痛点。
你善于从真实场景中总结高频问题与结构性矛盾。
你非常重视问题是否真实存在，而不是凭空想象需求。
你会明确区分“真实痛点”和“伪需求”。
""",
    llm=llm,
    verbose=True,
    allow_delegation=False,   # 非层级模式，强烈建议关闭
    max_iter=3,               # 防止无限推理
)

strategist_agent = Agent(
    role="AI 产品战略与创业顾问",
    goal="基于痛点与AI能力设计可落地、可盈利的AI产品方向",
    backstory="""
你是一位资深创业顾问与AI产品战略专家，辅导过多个AI产品从0到1落地。
你非常关注：
- MVP是否足够简单
- 是否有真实付费意愿
- 产品是否具备长期演进空间
你不追求炫技，而追求真实商业成功率。
""",
    llm=llm,
    verbose=True,
    allow_delegation=False,   # 非层级模式，强烈建议关闭
    max_iter=3,               # 防止无限推理
)

# ========== 定义 Tasks ==========

task_1 = Task(
    description="""
针对给定的领域，分析该领域中最核心的用户痛点与未被很好解决的问题。
重点关注：
- 高频出现的问题
- 当前解决方案明显不足的地方
- 具有长期存在性的结构性问题
""",
    expected_output="""
一个 JSON 数组，每一项包含：
- problem: 痛点描述
- target_user: 主要用户群体
- scenario: 典型使用场景
- severity: high / medium / low
""",
    agent=research_agent
)

task_2 = Task(
    description="""
基于上述领域痛点，总结当前主流AI技术与工具在该领域中可用的核心能力。
重点分析：
- 当前大模型/工具已经能稳定做到的能力
- 适合工程落地的方向
- 明显暂时不可行的方向
""",
    expected_output="""
一个 JSON 数组，每一项包含：
- ai_capability: 可用AI能力描述
- applicable_problems: 可解决的痛点编号列表
- maturity: high / medium / low
""",
    agent=planner_agent
)

task_3 = Task(
    description="""
基于前面的痛点分析与AI能力总结，
设计 3 个最具可行性的 AI 产品机会方向。
每个方向必须包含明确的问题、解决方案、MVP形态与商业模式判断。
""",
    expected_output="""
一个 JSON 数组，包含 3 个产品机会，每一项包含：
- problem: 核心问题
- target_user: 目标用户
- ai_solution: AI如何解决
- mvp: 最小可行产品形态
- monetization: 可能的收费模式
- difficulty: 实现难度（low / medium / high）
- potential: 市场潜力（low / medium / high）
""",
    agent=strategist_agent
)

# ========== 组建 Crew（顺序流水线） ==========

crew = Crew(
    agents=[research_agent, planner_agent, strategist_agent],
    tasks=[task_1, task_2, task_3],
    process=Process.sequential,
    verbose=True   # 强烈建议打开，看整个推理过程
)

# ========== 运行 ==========

result = crew.kickoff(inputs={
    "domain": "K12 少儿英语学习"
})

print(result)
