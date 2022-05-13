import time
from two_sum import two_sum_v1, two_sum_v2

def test_v1():
    items = [3, 1, 2, 4]
    results = two_sum_v1(items, 6)

    assert len(results) == 2
    assert results[0] == 2 or results[0] == 3
    assert results[1] == 2 or results[1] == 3

def test_v2():
    items = [3, 1, 2, 4]
    results = two_sum_v2(items, 6)

    assert len(results) == 2
    assert results[0] == 2 or results[0] == 3
    assert results[1] == 2 or results[1] == 3

def test_performance():
    items = [1,2,3,4,5,6,37,7,8,9,10,11,12,13,14,15,16]

    v1_start = time.time()
    two_sum_v1(items, 39)
    v1_end = time.time()

    v2_start = time.time()
    two_sum_v2(items, 39)
    v2_end = time.time()

    v1_elapsed = v1_end - v1_start
    v2_elapsed = v2_end - v2_start

    performance = round((v1_elapsed - v2_elapsed)/v1_elapsed * 100, 1)

    print('v2 is {}% faster than v1'.format(performance))

    assert v2_elapsed < v1_elapsed

