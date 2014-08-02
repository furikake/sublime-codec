import quopri

def decodestring(s, header=False):
    return quopri.decodestring(s, header)

def encodestring(s, quotetabs=False):
    return quopri.encodestring(s, quotetabs)