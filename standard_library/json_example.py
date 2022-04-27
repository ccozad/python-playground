# JSON or JavaScript Object Notation is a key value data format that is
# widely supported across a wide variety of languages. It is a convenient
# way to serialize and deserialize a nearly universal data exchange format
# that is most often used with

import json

def encode(data, indent = None):
    return json.dumps(data, indent=indent)

def decode(data):
    return json.loads(data)

if __name__ == "__main__":
    # We can use a python dictionary directly to have syntax that looks
    # like JSON before we've even encoded anything
    data = {
        'firstName': 'Jane',
        'lastName': 'Doe',
        'age': 35,
        'address': {
            'street': '1234 Main Street',
            'city': 'Salem',
            'state': 'OR',
            'zip': '97301'
        },
        'tags': ['pro', 'designer']
    }
    encoded = encode(data, indent=4)
    print('Encoded value:\n{}'.format(encoded))
    decoded = decode(encoded)
    print('Decoded value: {}'.format(decoded))

    print('We can access a few fields in the dictionary')
    print('firstName: {}'.format(decoded['firstName']))
    print('street: {}'.format(decoded['address']['street']))
    print('2nd tag: {}'.format(decoded['tags'][1]))