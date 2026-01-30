class PatternExtractor:

    def extract(self, experiences):
        patterns = []
        patterns += self._failure_patterns(experiences)
        patterns += self._review_advice_patterns(experiences)
        return patterns

    def _failure_patterns(self, experiences):
        # 非智能版：group + count
        counter = defaultdict(list)

        for exp in experiences:
            if exp.execution_profile.get("terminated"):
                key = "early_termination"
                counter[key].append(exp.task_id)

        patterns = []
        for k, ids in counter.items():
            patterns.append(
                BehaviorPattern(
                    pattern_id=str(uuid.uuid4()),
                    pattern_type="failure",
                    signal=k,
                    confidence=min(1.0, len(ids) / 5),
                    evidence_count=len(ids),
                    examples=ids[:3],
                    created_at=datetime.utcnow()
                )
            )
        return patterns
