import pytest
import hamming_distance as hd

def test_calculate_exception():
    with pytest.raises(ValueError):
        hamming_distance = hd.HammingDistance()
        hamming_distance.calculate("elephant", "mouse")

def test_calculate():
    hamming_distance = hd.HammingDistance()
    outcome1 = hamming_distance.calculate("karolin", "kathrin")
    outcome2 = hamming_distance.calculate("karolin", "kerstin")
    outcome3 = hamming_distance.calculate("kathrin", "kerstin")

    assert outcome1 == 3
    assert outcome2 == 3
    assert outcome3 == 4