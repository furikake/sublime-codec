import codec_base64
import unittest

class TestBase64Padding(unittest.TestCase):

    def setUp(self):
        pass

    def test_b64decode_two_pads(self):
        # make sure 2 equals gets added
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg'

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_zero_pads(self):
        # make sure no pads are added
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_strip_string_then_pad(self):
        # padding should trim spaces and line breaks
        expected = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg=='
        bad_padded_s = '   YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg\n\n'

        self.assertEqual(expected, codec_base64.fix_base64_padding(bad_padded_s))

    def test_b64decode_bad_padding(self):
        # don't fix the padding
        bad_padded_s = 'YWJjZGVmZ2hpamtsbW5vcHJzdHV2d3h5eg'

        with self.assertRaises(TypeError):
            codec_base64.b64decode(bad_padded_s)

    def test_b64decode_correct_bad_padding(self):
        # fix the bad padding
        bad_padded_s = '   YWJjZGVmZ2g\n\n\n'

        self.assertEquals('abcdefgh', codec_base64.b64decode(bad_padded_s, add_padding=True))

    def test_urlsafe_b64decode(self):
        # a valid urlsafe base64 encoded message
        s = "c3ViamVjdHM_YWJjZA=="

        self.assertEquals('subjects?abcd', codec_base64.urlsafe_b64decode(s))

    def test_urlsafe_b64decode_correct_bad_padding(self):
        # fix the bad badding for URL safe Base64
        s = "c3ViamVjdHM_YWJjZA=\n"

        self.assertEquals('subjects?abcd', codec_base64.urlsafe_b64decode(s, add_padding=True))

    def test_b32decode_zero_pads(self):
        # don't fix properly padded base32
        expected_s = 'IFBEGRCFIY======'
        s = 'IFBEGRCFIY======'

        self.assertEqual(expected, codec_base64.fix_base32_padding(s))


