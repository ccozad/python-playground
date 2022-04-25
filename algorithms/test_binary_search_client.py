import pytest
import binary_search_client as bsc

def test_constructor_exception():
    with pytest.raises(TypeError):
        binary_search = bsc.BinarySearchClient('foo bar')

def test_constructor_success():
    items = [1, 10, 100]
    binary_search = bsc.BinarySearchClient(items)

    assert len(binary_search.items) == 3

def test_find_odd_number_of_items():
    items = [10,20,30,40,50]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(10) == 0
    assert binary_search.find(20) == 1
    assert binary_search.find(30) == 2
    assert binary_search.find(40) == 3
    assert binary_search.find(50) == 4

def test_find_even_number_of_items():
    items = [10,20,30,40]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(10) == 0
    assert binary_search.find(20) == 1
    assert binary_search.find(30) == 2
    assert binary_search.find(40) == 3

def test_find_not_found_left():
    items = [10,20,30,40,50]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(-5) is None

def test_find_not_found_middle():
    items = [10,20,30,40,50]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(35) is None

def test_find_not_found_right():
    items = [10,20,30,40,50]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(555) is None

def test_find_large_list():
    items = [x for x in range(10000)]
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(600) == 600
    assert binary_search.find(12) == 12
    assert binary_search.find(4325) == 4325

def test_find_empty_list():
    items = []
    binary_search = bsc.BinarySearchClient(items)

    assert binary_search.find(5) is None