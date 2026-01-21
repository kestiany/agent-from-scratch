class BaseRole:
    def __init__(self, name: str, llm):
        self.name = name
        self.llm = llm

    def run(self, context: dict) -> dict:
        raise NotImplementedError("Subclasses must implement this method")