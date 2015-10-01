
import re
r_hex = re.compile(r'\\x([0-9a-fA-f]{2})')

def decodeHex(hexstring):
    def func(x):
        hexval = x.groups()[0]
        return chr(int(hexval, 16))
    return r_hex.sub(func, hexstring)

def encodeHex(string):
    return ''.join(('\\x{0:02x}'.format(ord(char)) for char in string))

