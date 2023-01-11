from model.organisation import Organisation


class Company(Organisation):
    def __init__(self):
        super().__init__()
        self._mission_statement: str = ""