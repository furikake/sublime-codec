# -*- coding: utf-8 -*-
import codec_base62
import unittest

class TestBase62Padding(unittest.TestCase):

    def setUp(self):
        pass

    def test_b62encode_int(self):
        expected = 'base62'.encode('UTF-8')
        s = str(34441886726).encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62encode_int(s))

    def test_b62decode_int(self):
        expected= str(34441886726).encode('UTF-8')
        s = 'base62'.encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62decode_int(s))

    def test_b62encode_inv_int(self):
        expected = 'sugoibase62'.encode('UTF-8')
        s = str(23910073833777532558).encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62encode_inv_int(s))

    def test_b62decode_inv_int(self):
        expected = str(23910073833777532558).encode('UTF-8')
        s = 'sugoibase62'.encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62decode_inv_int(s))

    def test_b62encode_hex(self):
        expected = '1cqLN6AiTmAQbgVkTw7ElB'.encode('UTF-8')
        s = '35713dc184f34d098122952e5bec4a6d'.encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62encode_hex(s))

    def test_b62decode_hex(self):
        # don't care about case for hex
        expected = '35713dc184f34d098122952e5bec4a6d'.upper().encode('UTF-8')
        s = '1cqLN6AiTmAQbgVkTw7ElB'.encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62decode_hex(s).upper())

    def test_b62decode_inv_hex(self):
        # don't care about case for hex
        expected = '35713dc184f34d098122952e5bec4a6d'.upper().encode('UTF-8')
        s = '1CQln6aItMaqBGvKtW7eLb'.encode('UTF-8')

        self.assertEquals(expected, codec_base62.b62decode_inv_hex(s).upper())

    def test_hex_uuid_to_base62_to_integer_to_hex_uuid(self):

        expected_int = '71037065880782318858967682010007226989'.encode('UTF-8')
        expected_base62 = '1cqLN6AiTmAQbgVkTw7ElB'.encode('UTF-8')
        expected_base62_inv = '1CQln6aItMaqBGvKtW7eLb'.encode('UTF-8')
        uuid_hex = '35713dc184f34d098122952e5bec4a6d'.encode('UTF-8')

        # Base16 to Base62
        the_base62 = codec_base62.b62encode_hex(uuid_hex)
        # Base62 to Base10
        the_int = codec_base62.b62decode_int(the_base62)
        # Base10 to Base62
        the_base62_inv = codec_base62.b62encode_inv_int(the_int)
        # Base62 to Base16
        the_hex_inv = codec_base62.b62decode_inv_hex(the_base62_inv)

        self.assertEquals(expected_base62, the_base62)
        self.assertEquals(expected_int, the_int)
        self.assertEquals(expected_base62_inv, the_base62_inv)
        # ignore the case
        self.assertEquals(uuid_hex.upper(), the_hex_inv.upper())
