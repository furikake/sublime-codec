import xml.sax.saxutils

def escape(input, entities={}):
    entity_map = {
        '"':'&quot;',
        '\'': '&apos;'
    }
    new_entities = entity_map.copy()
    new_entities.update(entities)
    return xml.sax.saxutils.escape(input, new_entities)

def unescape(input, entities={}):
    entity_map = {
        '&quot;': '"',
        '&apos;': '\''
    }
    new_entities = entity_map.copy()
    new_entities.update(entities)
    return xml.sax.saxutils.unescape(input, new_entities)
