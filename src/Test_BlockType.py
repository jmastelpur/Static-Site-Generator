import unittest
from BlockType import BlockType, Block

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# Heading 1"
        self.assertEqual(BlockType.Heading, block_to_block_type(block))
    def test_block_to_block_type_code(self):
        block = "```\nCode block\n```"
        self.assertEqual(BlockType.Code, block_to_block_type(block))
    def test_block_to_block_type_quote(self):
        block = "> Quote line 1\n> Quote line 2"
        self.assertEqual(BlockType.Quote, block_to_block_type(block))
    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2"
        self.assertEqual(BlockType.Unordered_List, block_to_block_type(block))
    def test_block_to_block_type_ordered_list(self):
        block = "1. Item 1\n2. Item 2"
        self.assertEqual(BlockType.Ordered_List, block_to_block_type(block))
    def test_block_to_block_type_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))
    def test_block_to_block_type_invalid_heading(self):
        block = "####### Invalid Heading"
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))
    def test_block_to_block_type_invalid_code(self):
        block = "```\nUnclosed code block"
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))
    def test_block_to_block_type_invalid_quote(self):
        block = "> Quote line 1\nNot a quote line"
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))
    def test_block_to_block_type_invalid_unordered_list(self):
        block = "- Item 1\nNot a list item"
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))
    def test_block_to_block_type_invalid_ordered_list(self):
        block = "1. Item 1\n2. Not a list item"
        self.assertEqual(BlockType.Paragraph, block_to_block_type(block))