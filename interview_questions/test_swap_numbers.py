import swap_numbers

def test_swap():
    items = [3, 5]
    swap_numbers.swap(items)

    assert items[0] == 5
    assert items[1] == 3