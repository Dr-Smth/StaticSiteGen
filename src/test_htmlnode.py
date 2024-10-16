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

    #leafnode tests
    def test_leafnode_value_only(self):
        leaf = LeafNode(value="Just text")
        assert leaf.to_html() == "Just text"

    def test_leafnode_with_tag(self):
        leaf = LeafNode(tag="p", value="Paragraph content")
        assert leaf.to_html() == "<p>Paragraph content</p>"

    def test_leafnode_with_props(self):
        leaf = LeafNode(tag="a", value="Click here", props={"href": "https://example.com"})
        assert leaf.to_html() == '<a href="https://example.com">Click here</a>'

    def test_leafnode_with_no_value(self):
        try:
            leaf = LeafNode()
        except ValueError as e:
            assert str(e) == "LeafNode instances must have a 'value'."
    
    #parentnode tests
    def test_simple_single_depth(self):
        node = ParentNode("div", [LeafNode(None, "Simple Content")])
        result = node.to_html()
        expected = "<div>Simple Content</div>"
        self.assertEqual(result, expected, "Simple single depth test failed!")

    def test_nested_nodes(self):
        child_node = ParentNode("span", [LeafNode(None, "Nested Text")])
        parent_node = ParentNode("div", [child_node])
        result = parent_node.to_html()
        expected = "<div><span>Nested Text</span></div>"
        self.assertEqual(result, expected, "Nested nodes test failed!")

    def test_props_handling(self):
        node = ParentNode("div", [LeafNode(None, "Content")], props={"class": "example"})
        result = node.to_html()
        expected = '<div class="example">Content</div>'
        self.assertEqual(result, expected, "Props handling test failed!")

    def test_no_tag_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "Missing Tag")]).to_html()

    def test_empty_children_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()


if __name__ == "__main__":
    unittest.main()