"""
This module defines the TextNode class and the TextType enum.


"""

from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    """
    Enum representing different types of text.
    """

    TEXT = "text"
    LINK = "link"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"


class TextNode:
    """
    Represents a node in a text-based document.

    Attributes:
        text (str): The text content of the node.
        text_type (TextType): The type of the text node.
        url (str, optional): The URL associated with the node.
            Only applicable for link and image types.
    """

    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        """
        Converts the text node to an HTML node.

        Returns:
            LeafNode: The HTML node representation of the text node.

        Raises:
            ValueError: If the text type is invalid.
        """
        if self.text_type == TextType.TEXT:
            return LeafNode(value=self.text)
        if self.text_type == TextType.LINK:
            return LeafNode(tag="a", value=self.text, props={"href": self.url})
        if self.text_type == TextType.BOLD:
            return LeafNode(tag="b", value=self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode(tag="i", value=self.text)
        if self.text_type == TextType.CODE:
            return LeafNode(tag="code", value=self.text)
        if self.text_type == TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": self.url})
        else:
            raise ValueError("Invalid text type")
