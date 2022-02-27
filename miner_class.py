

class Miner:
    def __init__(self, difficulty):
        self.difficulty = difficulty    # number of matching digits that the hash should start with

    # private method
    def __mine_block(self, block):
        # Generate a nonce that makes the hash start with a certain number of matching digits (eg. self.difficulty=2)

        block.regen_nonce()  # regenerate nonce
        block_hash = str(block.get_hash())  # get new hash
        first_digits = [digit for digit in block_hash[0:self.difficulty]]   # get first few digits of hash
        while len(set(first_digits)) != 1:  # while first few digits arent the same (sets only have distinct elements)
            block.regen_nonce()  # regen nonce
            block_hash = str(block.get_hash())  # get new hash
            first_digits = [digit for digit in block_hash[0:self.difficulty]]

        return block_hash

    def mine(self, blockchain):
        # go down block chain and mine each block
        hash_list = []
        for block in blockchain:
            block.computed_hash = self.__mine_block(block)     # set block's computed hash to the mined hash
            hash1 = block.computed_hash
            hash_list.append(hash1)
        return hash_list
