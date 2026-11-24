from Crypto.Hash import keccak
from utils.utils import sort_character

def keccak_hash(data):
    sorted_data = sort_character(data)
    return keccak.new(digest_bits=256).update(sorted_data.encode("utf-8")).hexdigest()