import json

def encode(input, ensure_ascii=False):
    result = json.dumps(input, ensure_ascii=ensure_ascii)
    return result

def encode_ensure_ascii(input):
    return encode(input, ensure_ascii=True)

def decode(input):
    result = json.loads(input, encoding="UTF-8")
    return result