import base64_example

def test_encode():
    data = b'The quick brown fox jumped over the lazy dog'
    result = base64_example.encode(data)

    assert result == b'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2c='

def test_decode():
    encoded = b'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2c='
    result = base64_example.decode(encoded)

    assert result == b'The quick brown fox jumped over the lazy dog'