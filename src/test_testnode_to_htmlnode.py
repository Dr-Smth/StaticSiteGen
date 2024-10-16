import unittest
from textnode import TextNode, TextType
from htmlnode import *
from textnode_to_htmlnode import *

class Test_TextNode_to_HTMLNode(unittest.TestCase):

    def test_normal_conversion(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        result = text_node_to_html_node(text_node)
        
        self.assertIsNone(result.tag)
        self.assertEqual(result.value, "Normal text")
        self.assertIsNone(result.props)
    
    def test_bold_conversion(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        result = text_node_to_html_node(text_node)
        
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "Bold text")
        self.assertIsNone(result.props)

    def test_italic_conversion(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        result = text_node_to_html_node(text_node)
        
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "Italic text")
        self.assertIsNone(result.props)

    def test_code_conversion(self):
        text_node = TextNode("Code text", TextType.CODE)
        result = text_node_to_html_node(text_node)
        
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "Code text")
        self.assertIsNone(result.props)

    def test_link_conversion(self):
        text_node = TextNode("anchor text", TextType.LINK, "https://www.google.com")
        result = text_node_to_html_node(text_node)
        
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "anchor text")
        self.assertEqual(result.props, {"href": "https://www.google.com"})

    def test_image_conversion(self):
        text_node = TextNode("alt text", TextType.IMAGE, "https://www.google.com")
        result = text_node_to_html_node(text_node)
        
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")
        self.assertEqual(result.props, {"src": "https://www.google.com", "alt": "alt text"})