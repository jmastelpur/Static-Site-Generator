import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)
    def test_text_to_textnodes_no_formatting(self):
        text = "This is plain text without any formatting."
        expected = [
            [TextNode("This is plain text without any formatting.", TextType.TEXT)]
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)
    def test_text_to_textnodes_only_bold(self):
        text = "**Bold text only**"
        expected = [
            [
                TextNode("Bold text only", TextType.BOLD)
            ]
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)
    def test_text_to_textnodes_multiple_formats(self):
        text = "This is **bold** and _italic_ and `code`."
        expected = [
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(".", TextType.TEXT),
            ]
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)
    def test_text_to_textnodes_nested_formatting(self):
        text = "This is **bold and _italic_** text."
        expected = [
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold and _italic_", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ]
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)