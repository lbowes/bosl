# What is true of any organisation?

from model.person import Person
from model.activity import Activity


class Organisation:
    def __init__(self):
        self._members: set[Person] = set()

        # TODO: Is this correct?
        #self._activities: set[Activity] = set()

    def enrol(self, new_member: Person) -> None:
        self._members.add(new_member)