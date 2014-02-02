import sublime, sublime_plugin
import base64
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

