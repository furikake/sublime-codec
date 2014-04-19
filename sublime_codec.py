# -*- coding: utf-8 -*-
import base64
import hashlib
import sublime, sublime_plugin
import sys

PYTHON = sys.version_info[0]

if 3 == PYTHON:
    # Python 3 and ST3
    from urllib import parse
    from . import codec_base64
    from . import codec_xml
else:
    # Python 2 and ST2
    import urllib
    import codec_base64
    import codec_xml

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
                    encoded_string = base64.b16decode(original_string.encode("UTF-8"))
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
        urlencode_method = UrlEncodeCommand.ENCODE_TYPE[encode_type]
        # print("using url encode method: " + str(urlencode_method))

        for region in selected_regions(self.view):
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string.encode("UTF-8"))
                # print("string encoded: " + encoded_string)
                if 2 == PYTHON:
                    encoded_string = urlencode_method(original_string.encode("UTF-8"))
                    self.view.replace(edit, region, encoded_string.decode("UTF-8"))
                else:
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
