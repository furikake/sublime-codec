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

class TestIdna2008(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        expected = 'xn--fa-hia.de'
        s = 'faß.de'

        self.assertEquals(expected, codec_idn.idna2008_encode(s))

    def test_decode(self):
        expected = 'faß.de'
        s = 'xn--fa-hia.de'

        self.assertEquals(expected, codec_idn.idna2008_decode(s))

class TestIdna2008Uts46(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        expected = 'xn--bb-eka.at'
        s = 'ÖBB.at'

        self.assertEquals(expected, codec_idn.idna2008uts46_encode(s))

    def test_decode(self):
        expected = 'ÖBB.at'
        s = 'xn--bb-eka.at'

        self.assertEquals(expected, codec_idn.idna2008uts46_decode(s))

class TestIdna2008Transitional(unittest.TestCase):

    def setUp(self):
        pass

    def test_encode(self):
        expected = 'xn--wgv71a119e.jp'
        s = '日本語。ＪＰ'

        self.assertEquals(expected, codec_idn.idna2008transitional_encode(s))

    def test_decode(self):
        expected = '日本語.jp'
        s = 'xn--wgv71a119e.jp'

        self.assertEquals(expected, codec_idn.idna2008transitional_decode(s))
