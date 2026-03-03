import unittest
from markdown_to_html import markdown_to_html_node
from BlockType import *
import htmlnode


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_quote(self):
        md = """> This is a quote line 1
> This is a quote line 2 with **bold** text
> This is a quote line 3 with _italic_ text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><blockquote>This is a quote line 1 This is a quote line 2 with <b>bold</b> text This is a quote line 3 with <i>italic</i> text</blockquote></div>",
        )
    def test_unordered_list(self):
        md = """- Item 1
- Item 2 with **bold** text
- Item 3 with _italic_ text 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b> text</li><li>Item 3 with <i>italic</i> text</li></ul></div>",
        )
    def test_ordered_list(self):
        md = """1. Item 1
2. Item 2 with **bold** text    
3. Item 3 with _italic_ text 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><ol><li>Item 1</li><li>Item 2 with <b>bold</b> text</li><li>Item 3 with <i>italic</i> text</li></ol></div>",
        )
    def test_heading(self):
        md = """# Heading 1
## Heading 2
### Heading 3 with **bold** text
#### Heading 4 with _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3 with <b>bold</b> text</h3><h4>Heading 4 with <i>italic</i> text</h4></div>",
        )