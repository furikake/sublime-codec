import base64

def b64decode(s, add_padding=False, altchars=None):

    if add_padding:
        new_s = fix_base64_padding(s)
    else:
        new_s = s

    return base64.b64decode(new_s, altchars).decode('UTF-8').encode('UTF-8')

def urlsafe_b64decode(s, add_padding=False):

    if add_padding:
        new_s = fix_base64_padding(s)
    else:
        new_s = s

    return base64.urlsafe_b64decode(new_s).decode('UTF-8').encode('UTF-8')

def b32decode(s, add_padding=False, casefold=False, map01=None):
    
    if add_padding:
        new_s = fix_base32_padding(s)
    else:
        new_s = s

    return base64.b32decode(new_s).decode('UTF-8').encode('UTF-8')

def fix_base64_padding(s):
    return fix_base_padding(s, pad_size=4)

def fix_base32_padding(s):
    return fix_base_padding(s, pad_size=8)

def fix_base_padding(s, pad_size=4):
    new_s = s.decode("UTF-8").strip()

    remaining = len(str(new_s)) % pad_size
    if 0 == remaining:
        padding = 0
    else:
        padding = pad_size - remaining

    return (new_s + "=" * padding).encode("UTF-8")
