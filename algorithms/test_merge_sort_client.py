import merge_sort_client as msc

def test_sort():
    items = [50, 10, 20, 30, 40]
    expected_outcome = [10, 20, 30, 40, 50]
    merge_sort = msc.MergeSortClient(items)
    results = merge_sort.sort()

    assert len(results) == 5
    assert ''.join([str(int) for int in results]) == ''.join([str(int) for int in expected_outcome])
