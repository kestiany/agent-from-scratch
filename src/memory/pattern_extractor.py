class PatternExtractor:

    def extract(self, experiences):
        patterns = []
        patterns += self._failure_patterns(experiences)
        patterns += self._review_advice_patterns(experiences)
        return patterns

    def _failure_patterns(self, experiences):
        # 非智能版：group + count
        ...
