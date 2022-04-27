import json_example

def test_encode():
    decoded = {
        'name': 'foobar'
    }
    result = json_example.encode(decoded)

    assert result == '{"name": "foobar"}'

def test_decode():
    encoded = '{"name": "foobar"}'
    result = json_example.decode(encoded)

    assert result['name'] == 'foobar'