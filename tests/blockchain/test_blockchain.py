import pytest
from blockchain.blockchain import Blockchain, Block


def test_blockchain_initialization():
    blockchain = Blockchain()
    genesis_block = blockchain.chain[0]
    assert isinstance(genesis_block, Block)
    assert genesis_block.parent_hash == "0" * 64
    assert genesis_block.beneficiary == "0" * 64
    assert genesis_block.number == 1
    assert genesis_block.timestamp == 1