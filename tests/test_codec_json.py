# -*- coding: utf-8 -*-
import codec_json
import unittest

class TestJsonEncoding(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        # 日本 = \xe6\x97\xa5\xe6\x9c\xac
        expected = "\"T'was a dark & \\\"stormy\\\" night in 日本\\n\\nblah blah!\""
        input = "T'was a dark & \"stormy\" night in 日本\n\nblah blah!"
        self.assertEquals(expected, codec_json.encode(input))

    def test_encode_ensure_ascii(self):
        expected = "\"T'was a dark & \\\"stormy\\\" night in \\u65e5\\u672c\\n\\nblah blah!\""
        input = "T'was a dark & \"stormy\" night in 日本\n\nblah blah!"
        self.assertEquals(expected, codec_json.encode_ensure_ascii(input))

    def test_decode(self):
        expected = "T'was a dark & \"stormy\" night in 日本\n\nblah blah!".decode("UTF-8")
        input = "\"T'was a dark & \\\"stormy\\\" night in 日本\\n\\nblah blah!\""
        self.assertEquals(expected, codec_json.decode(input))


