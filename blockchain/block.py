import time
from utils.keccak_hash import keccak_hash


class Block:
    def __init__(self, parent_hash, beneficiary, number, timestamp):
        self.parent_hash = parent_hash
        self.beneficiary = beneficiary
        self.number = number
        self.timestamp = timestamp

    def __repr__(self):
        return f"Block({self.__dict__})"

    def get_block_header(self):
        return self.__dict__

    @staticmethod
    def forge_genesis_block(transaction_series=None, state=None):
        return Block(
            parent_hash="0" * 64,
            beneficiary="0" * 64,
            number=1,
            timestamp=1,
        )

    @staticmethod
    def forge_block(last_block, transaction_series=None, state=None):
        last_block_header = last_block.get_block_header()
        return Block(
            parent_hash=keccak_hash(last_block_header),
            beneficiary="---beneficiary---",
            number=last_block_header["number"] + 1,
            timestamp=time.time_ns(),
        )

    @staticmethod
    def is_valid_block(last_block, block):
        if last_block is None:
            if keccak_hash(block.get_block_header()) != keccak_hash(
                Block.forge_genesis_block().get_block_header()
            ):
                raise Exception(
                    "The genesis block hash must be the hash of the genesis block header"
                )
            else:
                return

        last_block_header = last_block.get_block_header()
        block_header = block.get_block_header()

        if keccak_hash(last_block_header) != block_header["parent_hash"]:
            raise Exception(
                "The parent hash must be the hash of the last block header"
            )

        if block_header["number"] != last_block_header["number"] + 1:
            raise Exception("The block number must only increase by 1")