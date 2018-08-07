import base64
import os
import sys

if os.path.join(os.path.dirname(__file__), "pybase62") not in sys.path:
    print('adding pybase62 to sys.path')
    sys.path.append(os.path.join(os.path.dirname(__file__), "pybase62"))

try:
    from .pybase62 import base62
except:
    import pybase62 as base62

def _b62encode_int(s, charset=base62.CHARSET_DEFAULT):

    try:
        i = int(s)
    except ValueError:
        print('%s is not an integer' % s)
        return s

    return str(base62.encode(i, charset=charset)).encode('UTF-8')

def b62decode_int(s):

    return str(base62.decode(s.decode('UTF-8'), charset=base62.CHARSET_DEFAULT)).encode('UTF-8')

def b62encode_int(s):

    return _b62encode_int(s, charset=base62.CHARSET_DEFAULT)

def b62decode_inv_int(s):

    return str(base62.decode(s.decode('UTF-8'), charset=base62.CHARSET_INVERTED)).encode('UTF-8')

def b62encode_inv_int(s):

    return _b62encode_int(s, charset=base62.CHARSET_INVERTED)

######
# Base62 <-> Hex
######

def _b62encode_hex(s, charset=base62.CHARSET_DEFAULT):

    try:
        the_string = s.decode('UTF-8')
        b = bytes.fromhex(the_string)
    except Exception as e:
        print('%s is not in hex.' % the_string)
        return s

    retval = base62.encodebytes(b, charset=charset)

    return str(base62.encodebytes(b, charset=charset)).encode('UTF-8')

def _b62decode_hex(s, charset=base62.CHARSET_DEFAULT):

    b = bytearray(s.decode('ASCII'), 'UTF-8')

    retval = base62.decodebytes(s.decode('ASCII'), charset=charset)

    return base64.b16encode(retval)

def b62encode_hex(s):

    return _b62encode_hex(s, charset=base62.CHARSET_DEFAULT)

def b62decode_hex(s):

    return _b62decode_hex(s, charset=base62.CHARSET_DEFAULT)

def b62encode_inv_hex(s):

    return _b62encode_hex(s, charset=base62.CHARSET_INVERTED)

def b62decode_inv_hex(s):

    return _b62decode_hex(s, charset=base62.CHARSET_INVERTED)

