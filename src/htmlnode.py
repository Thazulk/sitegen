"""
This module provides a class for representing an HTML node.
"""


class HTMLNode:
    """
    Represents an HTML node.

    Attributes:
        tag (str): The HTML tag of the node.
        value (str): The value of the node.
        children (list): A list of child nodes.
        props (dict): A dictionary of properties for the node.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes a new instance of the HTMLNode class.

        Args:
            tag (str): The HTML tag of the node.
            value (str): The value of the node.
            children (list): A list of child nodes.
            props (dict): A dictionary of properties for the node.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Converts the HTML node to its corresponding HTML representation.

        This method should be implemented by subclasses.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError

    def props_to_html(self):
        """
        Converts the properties of the node to HTML attribute string.

        Returns:
            str: The HTML attribute string.
        """
        if not self.props:
            return ""
        else:

            return " " + " ".join(
                [f'{key}="{value}"' for key, value in self.props.items()]
            )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """
    Represents a leaf node in an HTML document.

    Args:
        tag (str): The HTML tag for the node.
        value (str): The value/content of the node.
        children (list): List of child nodes.
        props (dict): Dictionary of HTML attributes and their values.

    Attributes:
        tag (str): The HTML tag for the node.
        value (str): The value/content of the node.
        children (list): List of child nodes.
        props (dict): Dictionary of HTML attributes and their values.

    Methods:
        to_html: Converts the node to its HTML representation.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag=tag, value=value, children=children, props=props)

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return (
                self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
            )
        return False

    def to_html(self):
        """
        Converts the leaf node to its HTML representation.

        Returns:
            str: The HTML representation of the leaf node.

        Raises:
            ValueError: If the leaf node does not have a value.
        """
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    """
    Represents a parent HTML node that contains child nodes.

    Args:
        tag (str): The HTML tag of the parent node.
        children (list): A list of child nodes.
        props (dict, optional): Additional properties for the parent node.

    Attributes:
        tag (str): The HTML tag of the parent node.
        value (None): The value of the parent node (always None for parent nodes).
        children (list): A list of child nodes.
        props (dict): Additional properties for the parent node.

    Raises:
        ValueError: If the parent node is missing a tag or children.

    Methods:
        to_html: Converts the parent node and its children to an HTML string.
    """

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """
        Converts the parent node and its children to an HTML string.

        Returns:
            str: The HTML representation of the parent node and its children.

        Raises:
            ValueError: If the parent node is missing a tag or children.
        """
        if not self.tag:
            raise ValueError("All parent nodes require a tag")
        if not self.children:
            raise ValueError("All parent nodes require children")

        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"
