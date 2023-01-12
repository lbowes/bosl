class Activity:
    def __init__(self):
        self._completion: float = 0.0

    @property
    def completion(self) -> float:
        return self._completion