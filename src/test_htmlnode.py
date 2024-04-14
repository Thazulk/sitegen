import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a text node")
        self.assertEqual(repr(node), "HTMLNode(p, This is a text node, None, None)")

    def test_repr_props(self):
        node = HTMLNode(
            "a", "This is a text link", None, {"href": "www.link.uuu", "class": "text"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(a, This is a text link, None, {'href': 'www.link.uuu', 'class': 'text'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a text node")
        self.assertEqual(node.to_html(), "<p>This is a text node</p>")

    def test_to_html_props(self):
        node = LeafNode(
            "a", "This is a text link", None, {"href": "www.link.uuu", "class": "text"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="www.link.uuu" class="text">This is a text link</a>',
        )


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "This is a text node")])
        self.assertEqual(node.to_html(), "<div><p>This is a text node</p></div>")

    def test_to_html_props(self):
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
