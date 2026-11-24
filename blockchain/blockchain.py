from blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = [Block.forge_genesis_block()]

    def add_block(self, block):
        try:
            Block.is_valid_block(self.chain[-1], block)
            self.chain.append(block)
        except Exception as e:
            print(f"Cannot add block. Error in validating block: {e}")


def main():
    blockchain = Blockchain()
    block = Block.forge_block(blockchain.chain[-1])
    blockchain.add_block(block)
    print(f"blockchain.chain: {blockchain.chain}")


if __name__ == "__main__":
    main()