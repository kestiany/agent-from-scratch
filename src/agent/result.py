# result.py
from typing import TypedDict, Optional, List, Literal, Dict, Any

class AgentResult(TypedDict):
    status: Literal[
        "completed",
        "insufficient_info",
        "terminated"
    ]
    confidence: float
    final_output: Optional[Any]
    termination_reason: Optional[str]
    history: List[str]

    