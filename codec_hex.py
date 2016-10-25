import re
r_hex = re.compile(r'\\x([0-9a-fA-f]{2})')

def decode_hex(hexstring):
    def func(x):
        hexval = x.groups()[0]
        return chr(int(hexval, 16))
    return r_hex.sub(func, hexstring)

def encode_hex(string):
    hex_repr = string.encode('utf-8').hex()
    retval = ""
    for i in range(0, len(hex_repr), 2):
        retval = retval + '\\x' + hex_repr[i] + hex_repr[i+1]
    return retval
