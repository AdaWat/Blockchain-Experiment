"""Mini simulation of a blockchain
    blocks can take previous block's hash and miners can compute a hash to verify that transaction
    (1 transaction per block, regardless of size)"""

from block_class import Block
from miner_class import Miner
from user_class import User


difficulty = 2  # number of initial digits that have to match

# generate unique IDs for users

john = User("john")
jane = User("jane")
jen = User("joe")


miner1 = Miner(difficulty)

blockchain = [Block(sender=jane, recipient=john, amount=10, prev_hash=0)]  # create genesis block


def add_transaction(sender, recipient, amount):
    blockchain.append(Block(sender, recipient, amount, prev_hash=blockchain[len(blockchain)-1].computed_hash))


add_transaction(john, jane, 1)
add_transaction(jen, jane, 3)

# TODO: increase difficulty depending on number of miners
# TODO: only consider blocks that have been verified

hash_list = miner1.mine(blockchain)


def display_ledger(blockchain):
    for block in blockchain:
        if block.is_verified:
            print(f"\n{block.sender.name} → {block.recipient.name}  {block.amount}₿")
            print(f"Balances: {block.sender.name}={block.sender_balance} {block.recipient.name}={block.recipient_balance}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.computed_hash}")


display_ledger(blockchain)
