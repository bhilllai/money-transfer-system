# Calculating the hash in order to add digital fingerprints to the blocks
import hashlib
import json
import PoS
import Merkle_Tree
from Node import list_node


class Blockchain:

    # This function is created to create the blockchain
    # It stores the chain in the form of a tuple owing to its immutability feature
    def __init__(self):
        self.chain = ()

    # This function is created to add blocks into the chain.
    def create_block(self, previous_hash, winner_node, tr_list):
        merkle_value = Merkle_Tree.buildTree(tr_list)
        block = {'index': len(self.chain) + 1,
                 'previous_hash': previous_hash,
                 'validator': winner_node,
                 'merkle_root': merkle_value,
                 'hash': self.hash(merkle_value+previous_hash),
                 'transactions_list': tr_list
                 }
        temp_list = list(self.chain)
        temp_list.append(block)
        self.chain = tuple(temp_list)

        return block

    # This function is created to get the last added block
    def latest_block(self):
        return self.chain[-1]

    # This function used SHA256 hashing algorithm to hash a block and return the hash value
    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # This function is used to check the validity of the chain
    def chain_valid(self, chain):
        if len(chain) == 0:
            return True

        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            valid_hash = self.hash(block['previous_hash']+block['merkle_root'])
            if block['hash'] != valid_hash:
                return False

            previous_block = block
            block_index += 1

        return True

    # This function is used to mine the block
    def mine_block(self, tr_list):
        if len(self.chain) == 0:
            previous_hash = self.hash('Group-23_Chirag')
        else:
            previous_hash = self.latest_block()['hash']
        total_amt = sum([i[1] for i in tr_list])
        winner_node = PoS.POS(list_node)
        for i in list_node:
            if i.name == winner_node:
                i.reward += 1
                i.amount += 0.001*total_amt
                break
        self.create_block(previous_hash, winner_node, tr_list)
