import split_delimiter
import unittest
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_one_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_delimiter.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    def test_invalid_markdown(self):
        node = TextNode("This is text with an unmatched `code block word", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_delimiter.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Invalid Markdown syntax: unmatched delimiter '`'", str(context.exception))
    def test_multiple_splits(self):
        node = TextNode("Here is `code1` and here is `code2`.", TextType.TEXT)
        new_nodes = split_delimiter.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and here is ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    def test_no_splits(self):
        node = TextNode("This is plain text without delimiters.", TextType.TEXT)
        new_nodes = split_delimiter.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is plain text without delimiters.", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)
    def test_italics(self):
        node = TextNode("This is *italic* text.", TextType.TEXT)
        new_nodes = split_delimiter.split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    