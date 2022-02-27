import uuid


class User:
    def __init__(self, name):
        self.name = name[0].upper() + name[1:].lower()
        self.id = uuid.uuid4()
        self.balance = 0
