import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_neq(self):    
        node3 = TextNode("This is a text node", "italic", None)
        node4 = TextNode("This is a text node", "Bold", None)
        self.assertNotEqual(node3, node4)

    def test_eq_url(self):    
        node5 = TextNode("This is a text node", "bold", "https://www.google.com")
        node6 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node5, node6)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

if __name__ == "__main__":
    unittest.main()
