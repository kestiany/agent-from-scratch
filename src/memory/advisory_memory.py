class AdvisoryMemory:

    def __init__(self):
        self._notes = []

    def add(self, notes):
        self._notes.extend(notes)

    def query(self, context: dict):
        return [
            n for n in self._notes
            if all(context.get(k) == v for k, v in n.scope.items())
        ]
