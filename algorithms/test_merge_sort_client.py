import merge_sort_client as msc

def test_sort():
    items = [50, 10, 20, 30, 40]
    expected_outcome = [10, 20, 30, 40, 50]
    merge_sort = msc.MergeSortClient(items)
    results = merge_sort.sort()

    assert len(results) == 5
    assert ''.join([str(int) for int in results]) == ''.join([str(int) for int in expected_outcome])

def test_merge():
    left = [1, 10, 100, 212]
    right = [2, 8, 101, 200]
    expected_outcome = [1,2,8,10,100,101,200,212]

    merge_sort = msc.MergeSortClient([])
    results = merge_sort._merge(left, right)

    assert len(results) == 8
    assert ''.join([str(int) for int in results]) == ''.join([str(int) for int in expected_outcome])