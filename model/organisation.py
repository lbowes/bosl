# What is true of any organisation?

from model.person import Person


class Organisation:
    def __init__(self):
        self._members: set[Person] = set()

    def enrol(self, new_member: Person) -> None:
        self._members.add(new_member)