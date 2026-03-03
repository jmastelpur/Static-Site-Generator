from enum import Enum
from htmlnode import HTMLNode, LeafNode


def text_node_to_html_node(text_node):
    # convert a TextNode into an HTMLNode (LeafNode or similar) based on its TextType
    switch = {
        TextType.TEXT: LeafNode(tag=None, value=text_node.text),
        TextType.BOLD: LeafNode(tag="b", value=text_node.text),
        TextType.ITALIC: LeafNode(tag="i", value=text_node.text),
        TextType.CODE: LeafNode(tag="code", value=text_node.text),
        TextType.LINK: LeafNode(tag="a", value=text_node.text, props={"href": text_node.url}),
        TextType.IMAGE: LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text}),
    }
    if switch.get(text_node.text_type) is None:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
    return switch.get(text_node.text_type, LeafNode(tag=None, value=text_node.text))

class TextType(Enum):
    TEXT = "text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"
class TextNode:
    def __init__(self, text: str, text_type: str, url: str = ""):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"

