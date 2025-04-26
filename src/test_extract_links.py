import unittest
from extract_links import extract_markdown_images, extract_markdown_links


class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and [another link](https://example.org)"
        )
        self.assertListEqual(
            [("link", "https://example.com"), ("another link", "https://example.org")],
            matches,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![image](https://example.com/image.png) and ![another image](https://example.org/another_image.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://example.com/image.png"),
                ("another image", "https://example.org/another_image.png"),
            ],
            matches,
        )
