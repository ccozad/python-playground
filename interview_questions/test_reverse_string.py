import reverse_string

def test_reverse_string():
    s = "this.is.a.test"
    result = reverse_string.reverse_string(s)
    assert result == "test.a.is.this"