"""
This module contains unit tests for the TextNode class.

"""

import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    """
    Test case for the TextNode class.
    """

    def test_eq(self):
        """
        Test the equality of two TextNode instances.
        """
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq(self):
        """
        Test the inequality of two TextNode instances.
        """
        node3 = TextNode("This is a text node", "italic", None)
        node4 = TextNode("This is a text node", "Bold", None)
        self.assertNotEqual(node3, node4)

    def test_eq_url(self):
        """
        Test the equality of two TextNode instances with URLs.
        """
        node5 = TextNode("This is a text node", "bold", "https://www.google.com")
        node6 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node5, node6)

    def test_repr(self):
        """
        Test the string representation of a TextNode instance.
        """
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_text_node_to_html_node_text(self):
        """
        Test the conversion of a text node to an HTML node for text type.
        """
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(value="This is a text node")
        self.assertEqual(repr(html_node), repr(expected_html_node))

    def test_text_node_to_html_node_link(self):
        """
        Test the conversion of a text node to an HTML node for link type.
        """
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(
            tag="a",
            value="This is a text node",
            props={"href": "https://www.google.com"},
        )
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_bold(self):
        """
        Test the conversion of a text node to an HTML node for bold type.
        """
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(tag="b", value="This is a text node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_italic(self):
        """
        Test the conversion of a text node to an HTML node for italic type.
        """
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(tag="i", value="This is a text node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_code(self):
        """
        Test the conversion of a text node to an HTML node for code type.
        """
        node = TextNode("This is a text node", TextType.CODE)
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(tag="code", value="This is a text node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_image(self):
        """
        Test the conversion of a text node to an HTML node for image type.
        """
        node = TextNode(
            "This is a text node", TextType.IMAGE, "https://www.example.com/image.jpg"
        )
        html_node = node.text_node_to_html_node()
        expected_html_node = LeafNode(
            tag="img", value="", props={"src": "https://www.example.com/image.jpg"}
        )
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_invalid_type(self):
        """
        Test the conversion of a text node to an HTML node for an invalid type.
        """
        node = TextNode("This is a text node", "invalid_type")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()
