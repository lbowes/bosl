# TODO: This file should define a language with which all real organisations can
# be described.


class Organisation():
    def __init__(self):
        self._mission_statement = ""
        self._members = list()


class Member():
    def __init__(self, name):
        self._name = name