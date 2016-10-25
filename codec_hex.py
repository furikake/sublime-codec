import re
import codecs
r_hex = re.compile(r'\\x([0-9a-fA-f]{2})')

def decode_hex(hexstring):
    def func(x):
        hexval = x.groups()[0]
        return chr(int(hexval, 16))
    return r_hex.sub(func, hexstring)

def encode_hex(string):
    for c in string:
        if ord(c) > 255:
            # non-ascii not supported yet.
            return string 
    return ''.join(('\\x{0:02x}'.format(ord(char)) for char in string))
