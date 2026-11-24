import pytest
from blockchain.block import Block
from utils.keccak_hash import keccak_hash


@pytest.fixture
def last_block():
    return Block.forge_genesis_block()


@pytest.fixture
def new_block(last_block):
    return Block.forge_block(last_block)


def test_forge_gensis_block():
    genesis_block = Block.forge_genesis_block()
    assert genesis_block.parent_hash == "0" * 64
    assert genesis_block.beneficiary == "0" * 64
    assert genesis_block.number == 1
    assert genesis_block.timestamp == 1


def test_forge_block_success(last_block):
    forged_block = Block.forge_block(last_block)
    assert forged_block.parent_hash == keccak_hash(last_block.get_block_header())
    assert forged_block.beneficiary == "---beneficiary---"
    assert forged_block.number == last_block.number + 1
    assert isinstance(forged_block.timestamp, int)


def test_is_valid_block_genesis():
    assert Block.is_valid_block(None, Block.forge_genesis_block()) is None


def test_is_valid_block_success(last_block, new_block):
    assert Block.is_valid_block(last_block, new_block) is None


def test_is_valid_block_invalid_parent_hash(last_block, new_block):
    new_block.parent_hash = "invalid parent hash"
    with pytest.raises(
        Exception, match="The parent hash must be the hash of the last block header"
    ):
        Block.is_valid_block(last_block, new_block)


def test_is_valid_block_invalid_block_number(last_block, new_block):
    new_block.number = last_block.number
    with pytest.raises(
        Exception, match="The block number must only increase by 1"
    ):
        Block.is_valid_block(last_block, new_block)