import codecs
import os
import sys

if os.path.join(os.path.dirname(__file__), "idna") not in sys.path:
    # print('adding idna to sys.path')
    sys.path.append(os.path.join(os.path.dirname(__file__), "idna"))

from . import idna

def punycode_encode(s):
    return codecs.encode(s, 'punycode').decode('UTF-8')

def punycode_decode(s):
    return codecs.decode(s, 'punycode')

def idna_encode(s):
    return codecs.encode(s, 'idna').decode('UTF-8')

def idna_decode(s):
    return codecs.decode(bytearray(s, 'utf8'), 'idna')

def idna2008_encode(s):
    return idna.encode(s, strict=True, uts46=False, std3_rules=False, transitional=False).decode('UTF-8')

def idna2008_decode(s):
    return idna.decode(s, strict=True, uts46=False, std3_rules=False)

def idna2008uts46_encode(s):
    return idna.encode(s, strict=False, uts46=True, std3_rules=False, transitional=False).decode('UTF-8')

def idna2008uts46_decode(s):
    return idna.decode(s, strict=False, uts46=True, std3_rules=False)

def idna2008transitional_encode(s):
    return idna.encode(s, strict=False, uts46=True, std3_rules=True, transitional=True).decode('UTF-8')

def idna2008transitional_decode(s):
    return idna.decode(s, strict=False, uts46=True, std3_rules=True)
