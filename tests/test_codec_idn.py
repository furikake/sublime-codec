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
        expected = 'München'
        s = 'Mnchen-3ya'

        self.assertEqual(expected, codec_idn.punycode_decode(s))

class TestIdna(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        expected = 'xn--mnchen-3ya'
        s = 'München'

        self.assertEquals(expected, codec_idn.idna_encode(s))

    def test_decode(self):
        expected = 'münchen'
        s = 'xn--mnchen-3ya'

        self.assertEqual(expected, codec_idn.idna_decode(s))
