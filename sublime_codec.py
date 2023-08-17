# -*- coding: utf-8 -*-
import base64
import hashlib
import sublime, sublime_plugin
import sys

PYTHON = sys.version_info[0]

if 3 == PYTHON:
    # Python 3 and ST3
    from urllib import parse
    from . import codec_base62
    from . import codec_base64
    from . import codec_xml
    from . import codec_json
    from . import codec_quopri
    from . import codec_hex
    from . import codec_idn
else:
    # Python 2 and ST2
    import urllib
    import codec_base62
    import codec_base64
    import codec_xml
    import codec_json
    import codec_quopri
    import codec_hex
    import codec_idn

SETTINGS_FILE = "Codec.sublime-settings"

"""
Pick up all the selections which are not empty.
If no selection, make all the text in return selection.
"""
def selected_regions(view):
    sels = [sel for sel in view.sel() if not sel.empty()]

    if not sels:
        sels = [sublime.Region(0, view.size())]
    else:
        sels = view.sel()

    return sels


"""
Sublime Text 3 Base64 Codec
Assumes UTF-8 encoding

日本語 encodes to base64 as 5pel5pys6Kqe
subjects?abcd encodes to url safe base64 as c3ViamVjdHM_YWJjZA==

>>> view.run_command('base64_encode', {'encode_type': 'b64encode'})

"""
class Base64EncodeCommand(sublime_plugin.TextCommand):

    ENCODE_TYPE = {
        'b64decode': codec_base64.b64decode,
        'urlsafe_b64decode': base64.urlsafe_b64decode,
    }

    def run(self, edit, encode_type='b64encode'):

        fix_base32_padding = sublime.load_settings(SETTINGS_FILE).get("base32_fix_padding", False)
        print("Codec: fix base32 padding? %s" % str(fix_base32_padding))
        fix_base64_padding = sublime.load_settings(SETTINGS_FILE).get("base64_fix_padding", False)
        print("Codec: fix base64 padding? %s" % str(fix_base64_padding))

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                if 'b64encode' == encode_type:
                    encoded_string = base64.b64encode(original_string.encode("UTF-8"))
                elif 'b64decode' == encode_type:
                    encoded_string = codec_base64.b64decode(original_string.encode("UTF-8"), add_padding=fix_base64_padding)                    
                elif 'urlsafe_b64encode' == encode_type:
                    encoded_string = base64.urlsafe_b64encode(original_string.encode("UTF-8"))
                elif 'urlsafe_b64decode' == encode_type:
                    encoded_string = codec_base64.urlsafe_b64decode(original_string.encode("UTF-8"), add_padding=fix_base64_padding)
                elif 'b32encode' == encode_type:
                    encoded_string = base64.b32encode(original_string.encode("UTF-8"))
                elif 'b32decode' == encode_type:
                    encoded_string = codec_base64.b32decode(original_string.encode("UTF-8"), add_padding=fix_base32_padding)
                elif 'b16encode' == encode_type:
                    encoded_string = base64.b16encode(original_string.encode("UTF-8"))
                elif 'b16decode' == encode_type:
                    encoded_string = base64.b16decode(original_string.encode("UTF-8"), casefold=True)
                else:
                    print("unsupported operation %s" % (encode_type,))
                    break

                # print("string encoded: " + str(encoded_string.decode("UTF-8")))
                self.view.replace(edit, region, encoded_string.decode("UTF-8"))

"""
Sublime Text 3 URL Encoding (Percentage Encoding) Codec 

日本語 encodes to %E6%97%A5%E6%9C%AC%E8%AA%9E
"something with a space" encodes to "something%20with%20a%20space"

>>> view.run_command('url_encode', {'encode_type': 'quote'})

"""
class UrlEncodeCommand(sublime_plugin.TextCommand):

    if 2 == PYTHON:
        ENCODE_TYPE = {
            'quote': urllib.quote,
            'unquote': urllib.unquote,
            'quote_plus': urllib.quote_plus,
            'unquote_plus': urllib.unquote_plus
        }
    else:
        ENCODE_TYPE = {
            'quote': parse.quote,
            'unquote': parse.unquote,
            'quote_plus': parse.quote_plus,
            'unquote_plus': parse.unquote_plus
        }

    def run(self, edit, encode_type='quote'):
        safe_characters = str(sublime.load_settings(SETTINGS_FILE).get("url_encoding_safe", "/"))
        print("Codec: safe url characters? %s" % str(safe_characters))

        urlencode_method = UrlEncodeCommand.ENCODE_TYPE[encode_type]
        # print("using url encode method: " + str(urlencode_method))

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string.encode("UTF-8"))
                # print("string encoded: " + encoded_string)
                if 2 == PYTHON:
                    try:
                        encoded_string = urlencode_method(original_string.encode("UTF-8"), safe=safe_characters)
                    except TypeError:
                        # FIXME - time to separate quote and unquote to avoid this kind of errors.
                        encoded_string = urlencode_method(original_string.encode("UTF-8"))
                    self.view.replace(edit, region, encoded_string.decode("UTF-8"))
                else:
                    try:
                        encoded_string = urlencode_method(original_string, safe=safe_characters)
                    except TypeError:
                        # FIXME - time to separate quote and unquote to avoid this kind of errors.
                        encoded_string = urlencode_method(original_string)
                    self.view.replace(edit, region, encoded_string)

"""
Sublime Text 3 Secure Hash Codec 

日本語 hashes to SHA-256 as 77710aedc74ecfa33685e33a6c7df5cc83004da1bdcef7fb280f5c2b2e97e0a5

>>> view.run_command('secure_hash', {'secure_hash_type': 'sha256'})

"""
class SecureHashCommand(sublime_plugin.TextCommand):

    SECURE_HASH_TYPE = {
        'md5': 'md5',
        'sha1': 'sha1',
        'sha224': 'sha224',
        'sha256': 'sha256',
        'sha384': 'sha384',
        'sha512': 'sha512'
    }

    def run(self, edit, secure_hash_type='sha256'):
        secure_hash_type = SecureHashCommand.SECURE_HASH_TYPE[secure_hash_type]
        # print("using secure hash algorithm: " + secure_hash_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                hash_obj = hashlib.new(secure_hash_type)
                hash_obj.update(original_string.encode("UTF-8"))
                encoded_string = hash_obj.hexdigest()
                # print("string encoded: " + str(encoded_string))
                self.view.replace(edit, region, str(encoded_string))

"""
Sublime Text 3 Secure Hash Codec 

doSomething(); hashes to SHA-256 as RFWPLDbv2BY+rCkDzsE+0fr8ylGr2R2faWMhq4lfEQc=

>>> view.run_command('binary_secure_hash', {'secure_hash_type': 'sha256'})

"""
class BinarySecureHashCommand(sublime_plugin.TextCommand):

    SECURE_HASH_TYPE = {
        'sha256': 'sha256',
        'sha384': 'sha384',
        'sha512': 'sha512'
    }

    def run(self, edit, secure_hash_type='sha256'):
        secure_hash_type = SecureHashCommand.SECURE_HASH_TYPE[secure_hash_type]
        # print("using secure hash algorithm: " + secure_hash_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                hash_obj = hashlib.new(secure_hash_type)
                hash_obj.update(original_string.encode("UTF-8"))
                encoded_string = base64.b64encode(hash_obj.digest()).decode('UTF-8')
                # print("string encoded: " + str(encoded_string))
                self.view.replace(edit, region, str(encoded_string))

"""
Escapes and unescapes the 5 standard XML predefined entities

<hello>T'was a dark & "stormy" night</hello>
escapes to
&lt;hello&gt;T&apos;was a dark &amp; &quot;stormy&quot; night&lt;/hello&gt;

>>> view.run_command('xml', {'encode_type': 'escape'})
"""
class XmlCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='escape'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                new_string = method(original_string)
                self.view.replace(edit, region, new_string)

    def get_method(self, encode_type):
        if 'escape' == encode_type:
            return codec_xml.escape
        elif 'unescape' == encode_type:
            return codec_xml.unescape
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))

"""
Encodes and decodes Quoted-Printable strings

This is a really long line to test whether "quoted-printable" works correctly when using 日本語 and 英語
encodes to
This is a really long line to test whether "quoted-printable" works correct=
ly when using =E6=97=A5=E6=9C=AC=E8=AA=9E and =E8=8B=B1=E8=AA=9E

>>> view.run_command('quoted_printable', {'encode_type': 'encode'})
"""
class QuotedPrintableCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='encode'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                encoded_string = method(original_string.encode("UTF-8"))
                self.view.replace(edit, region, encoded_string.decode("UTF-8"))

    def get_method(self, encode_type):
        if 'encode' == encode_type:
            return codec_quopri.encodestring
        elif 'decode' == encode_type:
            return codec_quopri.decodestring
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))

"""
Encodes and decodes JSON

T'was a dark & "stormy" night in 日本
encodes to
"T'was a dark & \"stormy\" night in 日本"

>>> view.run_command('json', {'encode_type': 'encode'})
"""
class JsonCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='encode'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                new_string = method(original_string)
                self.view.replace(edit, region, new_string)

    def get_method(self, encode_type):
        if 'encode' == encode_type:
            return codec_json.encode
        elif 'encode_ensure_ascii' == encode_type:
            return codec_json.encode_ensure_ascii
        elif 'decode' == encode_type:
            return codec_json.decode
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))


"""
Encodes and decodes C-style hex representations of bytes

Hello, my good friend
encodes to
\\x48\\x65\\x6c\\x6c\\x6f\\x2c\\x20\\x6d\\x79\\x20\\x67\\x6f\\x6f\\x64\\x20\\x66\\x72\\x69\\x65\\x6e\\x64\\x21

>>> view.run_command('c_hex', {'encode_type': 'encode'})
"""
class HexCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='encode'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                new_string = method(original_string)
                self.view.replace(edit, region, new_string)

    def get_method(self, encode_type):
        if 'encode' == encode_type:
            return codec_hex.encode_hex
        elif 'decode' == encode_type:
            return codec_hex.decode_hex
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))

class HexAsciiCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='encode'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                new_string = method(original_string)
                self.view.replace(edit, region, new_string)

    def get_method(self, encode_type):
        if 'encode' == encode_type:
            return codec_hex.encode_hex_ascii
        elif 'decode' == encode_type:
            return codec_hex.decode_hex_ascii
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))

class IdnCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='punycode_encode'):
        method = self.get_method(encode_type)

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                new_string = method(original_string)
                self.view.replace(edit, region, new_string)

    def get_method(self, encode_type):
        if 'punycode_encode' == encode_type:
            return codec_idn.punycode_encode
        elif 'punycode_decode' == encode_type:
            return codec_idn.punycode_decode
        elif 'idna_encode' == encode_type:
            return codec_idn.idna_encode
        elif 'idna_decode' == encode_type:
            return codec_idn.idna_decode
        elif 'idna2008_encode' == encode_type:
            return codec_idn.idna2008_encode
        elif 'idna2008_decode' == encode_type:
            return codec_idn.idna2008_decode
        elif 'idna2008uts46_encode' == encode_type:
            return codec_idn.idna2008uts46_encode
        elif 'idna2008uts46_decode' == encode_type:
            return codec_idn.idna2008uts46_decode
        elif 'idna2008transitional_encode' == encode_type:
            return codec_idn.idna2008transitional_encode
        elif 'idna2008transitional_decode' == encode_type:
            return codec_idn.idna2008transitional_decode
        else:
            raise NotImplementedError("unknown encoding type %s" % (str(encode_type),))

"""
Sublime Text 3 Base62 Codec
"""
class Base62EncodeCommand(sublime_plugin.TextCommand):

    def run(self, edit, encode_type='b62encode'):

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                if 'b62encode_int' == encode_type:
                    encoded_string = codec_base62.b62encode_int(original_string.encode("UTF-8"))
                elif 'b62decode_int' == encode_type:
                    encoded_string = codec_base62.b62decode_int(original_string.encode("UTF-8"))
                elif 'b62encode_inv_int' == encode_type:
                    encoded_string = codec_base62.b62encode_inv_int(original_string.encode("UTF-8"))
                elif 'b62decode_inv_int' == encode_type:
                    encoded_string = codec_base62.b62decode_inv_int(original_string.encode("UTF-8"))
                elif 'b62encode_hex' == encode_type:
                    encoded_string = codec_base62.b62encode_hex(original_string.encode("UTF-8"))
                elif 'b62decode_hex' == encode_type:
                    encoded_string = codec_base62.b62decode_hex(original_string.encode("UTF-8"))
                elif 'b62encode_inv_hex' == encode_type:
                    encoded_string = codec_base62.b62encode_inv_hex(original_string.encode("UTF-8"))
                elif 'b62decode_inv_hex' == encode_type:
                    encoded_string = codec_base62.b62decode_inv_hex(original_string.encode("UTF-8"))
                else:
                    print("unsupported operation %s" % (encode_type,))
                    break

                self.view.replace(edit, region, encoded_string.decode("UTF-8"))
