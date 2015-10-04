# -*- coding: utf-8
import codec_hex
import unittest

class TestHex(unittest.TestCase):

    def assertDecode(self, encoded, expected):
        actual = codec_hex.decodeHex(encoded)
        self.assertEqual(expected, actual)

    def assertEncode(self, string, expected):
        actual = codec_hex.encodeHex(string)
        self.assertEqual(expected, actual)

    def test_ascii(self):
        self.assertDecode('\\x20\\x6C', ' l')
        self.assertEncode('~hello!', '\\x7e\\x68\\x65\\x6c\\x6c\\x6f\\x21')

    def test_nonprintable(self):
        self.assertDecode('\\x00\\x01', '\x00\x01')
        self.assertEncode('\x00\x01\xff', '\\x00\\x01\\xff')

    def test_unicode(self):
        """
        For now, unicode is not supported, but if you want to later
        support unicode, change this test.
        """
        self.assertEncode(u'€', u'€')
        self.assertDecode(u'€', u'€')


