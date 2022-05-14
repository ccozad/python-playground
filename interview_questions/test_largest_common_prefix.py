from largest_common_prefix import longest_common_prefix

def test_no_prefix():
    items = ["foo", "bar"]
    results = longest_common_prefix(items)

    assert results == ''

def test_example():
    items = ["flower","flow","flight"]
    results = longest_common_prefix(items)

    assert results == 'fl'

def test_simple():
    items = ["ab","a"]
    results = longest_common_prefix(items)

    assert results == 'a'