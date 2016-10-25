# -*- coding: utf-8
import codec_hex
import unittest

class TestHex(unittest.TestCase):

    def assert_decode(self, encoded, expected):
        actual = codec_hex.decode_hex(encoded)
        self.assertEqual(expected, actual)

    def assert_encode(self, string, expected):
        actual = codec_hex.encode_hex(string)
        self.assertEqual(expected, actual)

    def test_ascii(self):
        self.assert_decode('\\x20\\x6C', ' l')
        self.assert_encode('~hello!', '\\x7e\\x68\\x65\\x6c\\x6c\\x6f\\x21')

    def test_nonprintable(self):
        self.assert_decode('\\x00\\x01', '\x00\x01')
        self.assert_encode('\x00\x01\xff', '\\x00\\x01\\xff')

    def test_unicode(self):
        """
        For now, unicode is not supported, but if you want to later
        support unicode, change this test.
        """
        self.assert_encode(u'€', u'€')
        self.assert_decode(u'€', u'€')


