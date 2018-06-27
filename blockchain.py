import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
    def _init_(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
    # creates a new block and adds it to the chain
    pass

    def new_transaction(self):
    # Adds a new transaction to the list of transactions
    pass

    def proof_of_work(selfself, last_proof):

        """
    Simple Proof of Work Algorithm:
        -Find a number p' such that hash(pp') contains leading 4 zeros where
        -p is the previosu proof, and p' is the new proof

        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self valid_proof(last_proof, proof) is False:
            proof += 1

            return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha3_256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(block):
    # hashes a block
    pass

    @property
    def last_block(self):
        # returns the last block in the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """

        Creates a new transaction to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })


        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):

        """
        Creates a SHA-256 hash of a block

        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()