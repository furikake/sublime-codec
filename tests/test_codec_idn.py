# -*- coding: utf-8 -*-
import codec_idn
import unittest

class TestPunycode(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        # the wikipedia example
        expected = 'Mnchen-3ya'
        s = 'München'

        self.assertEquals(expected, codec_idn.punycode_encode(s))

    def test_decode(self):
        # make sure 2 equals gets added
        expected = 'München'
        s = 'Mnchen-3ya'

        self.assertEqual(expected, codec_idn.punycode_decode(s))

