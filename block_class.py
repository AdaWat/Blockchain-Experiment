import datetime
from uuid import uuid4


class Block:
    difficulty = 2
    def __init__(self, sender, recipient, amount, prev_hash):
        sender.balance -= amount    # exchange money
        recipient.balance += amount
        self.sender = sender
        self.recipient = recipient
        self.sender_balance = sender.balance
        self.recipient_balance = recipient.balance
        self.timestamp = datetime.datetime.now()    # time block was created (not when it was verified)
        self.nonce = ""
        self.prev_hash = str(prev_hash)
        self.computed_hash = None
        self.amount = amount

    def regen_nonce(self):
        self.nonce = str(uuid4())  # generate random string that may make the hash start with repeating digits

    # TODO: convert get_hash() into property/getter
    def get_hash(self):
        return abs(hash(str(self.sender.id) + str(self.recipient.id) + self.nonce + self.prev_hash + str(self.amount)))

    @property
    def is_verified(self):
        first_digits = [digit for digit in self.computed_hash[0:Block.difficulty]]   # get first few digits of hash
        if len(set(first_digits)) == 1 and self.computed_hash == str(self.get_hash()):
            return True
        return False
