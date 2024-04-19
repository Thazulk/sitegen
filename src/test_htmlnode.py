"""
This module contains unit tests for the HTMLNode class.

"""

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    """Test case for the HTMLNode class."""

    def test_repr(self):
        """Test the repr method of HTMLNode."""
        node = HTMLNode("p", "This is a text node")
        self.assertEqual(repr(node), "HTMLNode(p, This is a text node, None, None)")

    def test_repr_props(self):
        """Test the repr method of HTMLNode with properties."""
        node = HTMLNode(
            "a", "This is a text link", None, {"href": "www.link.uuu", "class": "text"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(a, This is a text link, None, {'href': 'www.link.uuu', 'class': 'text'})",
        )


class TestLeafNode(unittest.TestCase):
    """Test case for the LeafNode class."""

    def test_to_html(self):
        """Test the to_html method of LeafNode."""
        node = LeafNode("p", "This is a text node")
        self.assertEqual(node.to_html(), "<p>This is a text node</p>")

    def test_to_html_props(self):
        """Test the to_html method of LeafNode with properties."""
        node = LeafNode(
            "a", "This is a text link", None, {"href": "www.link.uuu", "class": "text"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="www.link.uuu" class="text">This is a text link</a>',
        )


class TestParentNode(unittest.TestCase):
    """Test case for the ParentNode class."""

    def test_to_html(self):
        """Test the to_html method of ParentNode."""
        node = ParentNode("div", [LeafNode("p", "This is a text node")])
        self.assertEqual(node.to_html(), "<div><p>This is a text node</p></div>")

    def test_to_html_props(self):
        """Test the to_html method of ParentNode with properties."""
        node = ParentNode(
            "div",
            [
                LeafNode(
                    "a",
                    "This is a text link",
                    None,
                    {"href": "www.link.uuu", "class": "text"},
                ),
                ParentNode("div", [LeafNode("p", "This is a nested text node")]),
            ],
            {"class": "container row"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container row"><a href="www.link.uuu" class="text">This is a text link</a><div><p>This is a nested text node</p></div></div>',
        )


if __name__ == "__main__":
    unittest.main()
