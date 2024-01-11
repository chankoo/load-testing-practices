import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import random
from src.main import base62_encode

ID_MIN = 3844
ID_MAX = 2**31-1  # Integer max


def test_base62_encode_basic():
    assert base62_encode(0) == "0"
    assert base62_encode(9) == "9"
    assert base62_encode(61) == "Z"
    assert base62_encode(62) == "10"

    assert base62_encode(ID_MIN).isalnum()
    assert base62_encode(ID_MAX).isalnum()


def test_base62_encode_len():
    target = random.randrange(ID_MIN, ID_MAX + 1)
    assert 3 <= len(base62_encode(target)) <= 7
    assert 3 <= len(base62_encode(ID_MIN)) <= 7
    assert 3 <= len(base62_encode(ID_MAX)) <= 7
