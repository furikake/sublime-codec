import sublime, sublime_plugin
import base64
import hashlib

from urllib import parse

"""
Sublime Text 3 Base64 Codec
Assumes UTF-8 encoding

日本語 encodes to base64 as 5pel5pys6Kqe
subjects?abcd encodes to url safe base64 as c3ViamVjdHM_YWJjZA==

>>> view.run_command('base64_encode', {'encode_type': 'b64encode'})

"""
class Base64EncodeCommand(sublime_plugin.TextCommand):

    ENCODE_TYPE = {
        'b64encode': base64.b64encode,
        'b64decode': base64.b64decode,
        'urlsafe_b64encode': base64.urlsafe_b64encode,
        'urlsafe_b64decode': base64.urlsafe_b64decode,
        'b32encode': base64.b32encode,
        'b32decode': base64.b32decode,
        'b16encode': base64.b16encode,
        'b16decode': base64.b16decode
    }

    def run(self, edit, encode_type='b64encode'):

        base64_method = Base64EncodeCommand.ENCODE_TYPE[encode_type]
        # print("using base64 method: " + str(base64_method))

        for region in self.view.sel():
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                encoded_string = base64_method(original_string.encode("UTF-8"))
                # print("string encoded: " + str(encoded_string.decode("UTF-8")))
                self.view.replace(edit, region, encoded_string.decode("UTF-8"))

"""
Sublime Text 3 URL Encoding (Percentage Encoding) Codec 

日本語 encodes to %E6%97%A5%E6%9C%AC%E8%AA%9E
"something with a space" encodes to "something%20with%20a%20space"

>>> view.run_command('url_encode', {'encode_type': 'quote'})

"""
class UrlEncodeCommand(sublime_plugin.TextCommand):

    ENCODE_TYPE = {
        'quote': parse.quote,
        'unquote': parse.unquote,
        'quote_plus': parse.quote_plus,
        'unquote_plus': parse.unquote_plus
    }

    def run(self, edit, encode_type='quote'):
        urlencode_method = UrlEncodeCommand.ENCODE_TYPE[encode_type]
        # print("using url encode method: " + str(urlencode_method))

        for region in self.view.sel():
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                encoded_string = urlencode_method(original_string)
                # print("string encoded: " + encoded_string)
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
        'sha512': 'sha512',
    }

    def run(self, edit, secure_hash_type='sha256'):
        secure_hash_type = SecureHashCommand.SECURE_HASH_TYPE[secure_hash_type]
        # print("using secure hash algorithm: " + secure_hash_type)

        for region in self.view.sel():
            if not region.empty():
                original_string = self.view.substr(region)
                # print("string: " + original_string)
                hash_obj = hashlib.new(secure_hash_type)
                hash_obj.update(original_string.encode("UTF-8"))
                encoded_string = hash_obj.hexdigest()
                # print("string encoded: " + str(encoded_string))
                self.view.replace(edit, region, str(encoded_string))
