import numpy as np


class Proficiency(float):
    """A measure of expertise in either knowledge or skill."""

    MIN = 0.0
    MAX = 1.0 # The most proficient human on Earth for a given understanding/skill

    def __new__(cls, value: float):
        if not cls.MIN <= value <= cls.MAX:
            raise ValueError(f"Proficiency must be between {cls.MIN} and {cls.MAX}")

        return super().__new__(cls, value)


Expertise = list[Proficiency]


class Person:
    def __init__(self, name: str, expertise: Expertise) -> None:
        self._name: str = name
        self._expertise: Expertise = [Proficiency(x) for x in expertise]

    def join(self, org: Organisation) -> None:
        org.enrol(self)

    def work(self, task):
        task_sum = sum(task)
        normalized_task = [x / task_sum for x in task]
        value = max(0, np.dot(self._expertise, normalized_task))
        return value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def expertise(self) -> str:
        return self._expertise

    @expertise.setter
    def expertise(self, value: str):
        self._expertise = value
