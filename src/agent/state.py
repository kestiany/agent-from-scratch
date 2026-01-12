from typing import TypedDict, List, Optional, Literal

ControlDecision = Literal["continue", "retry", "replan"]

AnalysisStep = Literal[
    "understanding",
    "risk_detection",
    "risk_qualification",
    "reporting"
]

class AgentState(TypedDict):
    # origin input
    user_input: str
    # understand task
    objective: str

    # plans
    plan: List[AnalysisStep]
    # current step
    current_step: int

    # intermediate thinking / results
    scratchpad: List[str]
    # final result
    final_output: Optional[str]
    # finish status
    done: bool

    # context for current step (rag / tools / search etc.)
    step_context: Optional[str]
    # runtime memory for current task
    memory: List[str]
    # execution history (for trace & explain)
    history: List[str]

    # step exec info
    step_success: bool
    retry_count: int
    max_retry: int
    last_failure: Optional[str]

    # reflection output
    control_decision: Optional[ControlDecision]

