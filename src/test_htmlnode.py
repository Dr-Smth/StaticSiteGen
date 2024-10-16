import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    #props to html check
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", props={"class": "greeting"})
        expected_repr = (
            "HTMLNode(\n"
            "\n"
            "Tag: p. \n"
            "\n"
            "Value: Hello, world!. \n"
            "\n"
            "Children: None. \n"
            "\n"
            "Props: {'class': 'greeting'})"
        )
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()