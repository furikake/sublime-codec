import codec_xml
import unittest

class TestXmlEncoding(unittest.TestCase):

    def setUp(self):
        pass

    def test_escape(self):
        expected = '&lt;hello&gt;T&apos;was a dark &amp; &quot;stormy&quot; night&lt;/hello&gt;'
        input = '<hello>T\'was a dark & "stormy" night</hello>'
        self.assertEquals(expected, codec_xml.escape(input))

    def test_escape_additional_entities(self):
        expected = '&lt;hello&gt;T&apos;was&nbsp;a&nbsp;dark&nbsp;&amp;&nbsp;&quot;stormy&quot;&nbsp;night&lt;/hello&gt;'
        input = '<hello>T\'was a dark & "stormy" night</hello>'
        self.assertEquals(expected, codec_xml.escape(input, {' ': '&nbsp;'}))

    def test_escape_override_entities(self):
        expected = '&lt;hello&gt;T&blah;was a dark &amp; &quot;stormy&quot; night&lt;/hello&gt;'
        input = '<hello>T\'was a dark & "stormy" night</hello>'
        self.assertEquals(expected, codec_xml.escape(input, {"'": "&blah;"}))

    def test_unescape(self):
        expected = '<hello>T\'was a dark & "stormy" night</hello>'
        input = '&lt;hello&gt;T&apos;was a dark &amp; &quot;stormy&quot; night&lt;/hello&gt;'
        self.assertEquals(expected, codec_xml.unescape(input))

    def test_unescape_additional_entities(self):
        expected = '<hello>T\'was a dark & "stormy" night</hello>'
        input = '&lt;hello&gt;T&apos;was&nbsp;a&nbsp;dark&nbsp;&amp;&nbsp;&quot;stormy&quot;&nbsp;night&lt;/hello&gt;'
        self.assertEquals(expected, codec_xml.unescape(input, {'&nbsp;': ' '}))

    def test_unescape_override_entities(self):
        expected = '<hello>T\'was a dark & "stormy" night</hello>'
        input = '&lt;hello&gt;T&blah;was a dark &amp; &quot;stormy&quot; night&lt;/hello&gt;'
        self.assertEquals(expected, codec_xml.unescape(input, {"&blah;": "'"}))
