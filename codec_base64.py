import base64

def b64decode(s, add_padding=False, altchars=None):
    
    new_s = s

    if add_padding:
        new_s = fix_base64_padding(new_s)

    return base64.b64decode(new_s, altchars)

def urlsafe_b64decode(s, add_padding=False):

    new_s = s

    if add_padding:
        new_s = fix_base64_padding(s)

    return base64.urlsafe_b64decode(new_s)

def fix_base64_padding(s):
    new_s = s.decode("UTF-8").strip()

    return (new_s + "=" * (len(str(new_s)) % 4)).encode("UTF-8")

def fix_base32_padding(s):
    ## TODO Implement
    new_s = s.decode("UTF-8").strip()

    return (new_s + "=" * (len(str(new_s)) % 8)).encode("UTF-8")

def fix_base16_padding(s):
    ## TODO Implement
    pass
