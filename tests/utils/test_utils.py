import pytest
import random
import string
from utils.utils import sort_character
from utils.keccak_hash import keccak_hash


@pytest.fixture
def random_data():
    data = string.printable.strip()
    random_sample_1 = "".join(random.sample(data, len(data)))
    random_sample_2 = "".join(random.sample(data, len(data)))
    return data, random_sample_1, random_sample_2


def test_sorted_character(random_data):
    _, random_sample_1, random_sample_2 = random_data
    print(f"\n**random_sample_1 --> {random_sample_1}")
    print(f"**random_sample_2 --> {random_sample_2}")
    assert random_sample_1 != random_sample_2

    sorted_data_1 = sort_character(random_sample_1)
    sorted_data_2 = sort_character(random_sample_2)
    assert sorted_data_1 == sorted_data_2


def test_keccak_hash(random_data):
    _, random_sample_1, random_sample_2 = random_data
    print(f"\n**random_sample_1 --> {random_sample_1}")
    print(f"**random_sample_2 --> {random_sample_2}")
    assert keccak_hash(random_sample_1) == keccak_hash(random_sample_2)