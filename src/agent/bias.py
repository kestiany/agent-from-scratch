from dataclasses import dataclass

@dataclass
class BiasProfile:
    risk_tolerance: float  # 0.0 (conservative) to 1.0 (aggressive)
    verification_preference: float
    verbosity: float

# agent/bias.py
BIAS_PROFILES = {
    "cautious": {
        "on_failure": "retry"
    },
    "balanced": {
        "on_failure": "continue"
    },
    "aggressive": {
        "on_failure": "replan"
    }
}
