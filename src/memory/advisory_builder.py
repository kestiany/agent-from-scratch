class AdvisoryBuilder:

    def build(self, patterns):
        advisories = []
        for p in patterns:
            if p.evidence_count >= 2 and p.confidence >= 0.6:
                advisories.append(self._to_advisory(p))
        return advisories
