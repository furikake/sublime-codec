# -*- coding: utf-8 -*-
import codec_base64
import unittest

class TestBase64Padding(unittest.TestCase):

    def setUp(self):
        pass

    def test_b64decode_three_pads(self):
        # blindly add three padding equals to very badly encoded string
        expected = '!@#$%==='.encode('UTF-8')
        bad_encoded_s = '!@#$%'.encode('UTF-8')

        self.assertEquals(expected, codec_base64.fix_base64_padding(bad_encoded_s))

    def test_b64decode_two_pads(self):
        # make sure 2 equals gets added
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='.encode('UTF-8')
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg'.encode('UTF-8')

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_zero_pads(self):
        # make sure no pads are added
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='.encode('UTF-8')
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='.encode('UTF-8')

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_strip_string_then_pad(self):
        # padding should trim spaces and line breaks
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='.encode('UTF-8')
        bad_padded_s = '   YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg\n\n'.encode('UTF-8')

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_bad_padding(self):
        # don't fix the padding
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg'.encode('UTF-8')

        with self.assertRaises(Exception):
            codec_base64.b64decode(bad_padded_s)

    def test_b64decode_correct_bad_padding(self):
        # fix the bad padding
        bad_padded_s = '   YWJjZGVmZ2g\n\n\n'.encode('UTF-8')
        expected = 'abcdefgh'.encode('UTF-8')

        self.assertEquals(expected, codec_base64.b64decode(bad_padded_s, add_padding=True))

    def test_urlsafe_b64decode(self):
        # a valid urlsafe base64 encoded message
        s = "c3ViamVjdHM_YWJjZA==".encode('UTF-8')
        expected = 'subjects?abcd'.encode('UTF-8')

        self.assertEquals(expected, codec_base64.urlsafe_b64decode(s))

    def test_urlsafe_b64decode_correct_bad_padding(self):
        # fix the bad badding for URL safe Base64
        s = "c3ViamVjdHM_YWJjZA=\n".encode('UTF-8')
        expected = 'subjects?abcd'.encode('UTF-8')

        self.assertEquals(expected, codec_base64.urlsafe_b64decode(s, add_padding=True))

    def test_b64decode_padding_is_none(self):
        # Pass None as the value for padding. The padding method should default back to None
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg'.encode('UTF-8')

        with self.assertRaises(Exception):
            codec_base64.b64decode(bad_padded_s, add_padding=None)

    def test_b32decode_zero_pads(self):
        # don't fix properly padded base32
        expected = 'IFBEGRCFIY======'.encode('UTF-8')
        s = 'IFBEGRCFIY======'.encode('UTF-8')

        self.assertEqual(expected, codec_base64.fix_base32_padding(s))

    def test_b32decode_six_pads(self):
        expected = 'ABCDEF'.encode('UTF-8')
        pad_padded_s = 'IFBEGRCFIY'.encode('UTF-8')

        self.assertEqual(expected, codec_base64.b32decode(pad_padded_s, add_padding=True))

    def test_b32decode_one_pad(self):
        expected = 'IFBEGRA='.encode('UTF-8')
        s = 'IFBEGRA'.encode('UTF-8')

        self.assertEqual(expected, codec_base64.fix_base32_padding(s))

    def test_b32decode_padding_is_false(self):
        # Don't fix the padding
        pad_padded_s = 'IFBEGRCFIY'.encode('UTF-8')

        with self.assertRaises(Exception):
            codec_base64.b32decode(pad_padded_s, add_padding=False)

