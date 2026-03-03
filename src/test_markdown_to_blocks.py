import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
            def test_markdown_to_blocks(self):
                md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
                blocks = markdown_to_blocks(md)
                self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
            def test_empty_markdown(self):
                md = ""
                blocks = markdown_to_blocks(md)
                self.assertEqual(blocks, [])
            def test_markdown_with_only_newlines(self):
                md = "\n\n\n"
                blocks = markdown_to_blocks(md)
                self.assertEqual(blocks, [])
            def test_markdown_with_leading_trailing_newlines(self):
                md = "\n\nThis is a paragraph\n\n"
                blocks = markdown_to_blocks(md)
                self.assertEqual(blocks, ["This is a paragraph"])
        