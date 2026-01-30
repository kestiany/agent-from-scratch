from agent.bias import BiasProfile

class BiasBuilder:
    def build(self, advisories) -> BiasProfile:
        bias = BiasProfile(
            risk_tolerance=0.5,
            verification_preference=0.5,
            verbosity=0.5
        )

        for a in advisories:
            if "retry" in a.advice:
                bias.risk_tolerance -= 0.2
                bias.verification_preference += 0.3

        return bias
