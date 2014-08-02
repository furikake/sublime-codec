# -*- coding: utf-8 -*-
import codec_quopri
import unittest

class TestQuopriEncoding(unittest.TestCase):

    def setUp(self):
        pass

    def test_encodestring(self):
        expected = """If you believe that truth=3Dbeauty, then surely mathematics is the most bea=
utiful branch of philosophy."""
        input = """If you believe that truth=beauty, then surely mathematics is the most beautiful branch of philosophy."""
        self.assertEquals(expected, codec_quopri.encodestring(input))

    def test_decodestring(self):
        expected = """If you believe that truth=beauty, then surely mathematics is the most beautiful branch of philosophy."""
        input = """If you believe that truth=3Dbeauty, then surely mathematics is the most bea=
utiful branch of philosophy."""
        self.assertEquals(expected, codec_quopri.decodestring(input))

    def test_encodestring_unicode(self):
        expected = """This is a really long line to test whether "quoted-printable" works correct=
ly when using =E6=97=A5=E6=9C=AC=E8=AA=9E and =E8=8B=B1=E8=AA=9E"""
        input = """This is a really long line to test whether "quoted-printable" works correctly when using 日本語 and 英語"""
        self.assertEquals(expected, codec_quopri.encodestring(input))

    def test_decodestring_unicode(self):
        expected = """This is a really long line to test whether "quoted-printable" works correctly when using 日本語 and 英語"""
        input = """This is a really long line to test whether "quoted-printable" works correct=
ly when using =E6=97=A5=E6=9C=AC=E8=AA=9E and =E8=8B=B1=E8=AA=9E"""
        self.assertEquals(expected, codec_quopri.decodestring(input))
