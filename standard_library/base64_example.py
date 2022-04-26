# Base64 encoding is a way to represent binary data as plain ascii characters.
# Example usages include creating email attachments and post bodies for JSON uploads.
#
# Base64 encoding should not be confused with encryption because the encoding
# can be simply reversed as shown below.

import base64

def encode(data):
    return base64.b64encode(data)

def decode(data):
    return base64.b64decode(data)

if __name__ == "__main__":
    data = b'The quick brown fox jumped over the lazy dog'
    encoded = encode(data)
    print('Encoded value: {}'.format(encoded))
    decoded = decode(encoded)
    print('Decoded value: {}'.format(decoded))