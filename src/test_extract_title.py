import unittest
from extract_title import extract_title



class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_h1(self):
        markdown_text = "# Hello World\nThis is a test."
        title = extract_title(markdown_text)
        self.assertEqual(title, "Hello World")

    def test_extract_title_with_no_h1(self):
        markdown_text = "This is a test.\nNo h1 header here."
        with self.assertRaises(ValueError):
            extract_title(markdown_text)

    def test_extract_title_with_multiple_h1(self):
        markdown_text = "# First Title\n# Second Title\nThis is a test."
        title = extract_title(markdown_text)
        self.assertEqual(title, "First Title")

    def test_extract_title_with_whitespace(self):
        markdown_text = "   #   Hello World   \nThis is a test."
        title = extract_title(markdown_text)
        self.assertEqual(title, "Hello World")