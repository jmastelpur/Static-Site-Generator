from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest


class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        props_html = node.props_to_html()
        self.assertIn('href="https://www.google.com"', props_html)
        self.assertIn('target="_blank"', props_html)
    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph")
        repr_str = repr(node)
        self.assertIn("HTMLNode(tag=p", repr_str)
        self.assertIn("value=Paragraph", repr_str)
    

class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        leaf = LeafNode(tag="span", value="Leaf", props={"style": "color:red;"})
        self.assertEqual(leaf.tag, "span")
        self.assertEqual(leaf.value, "Leaf")
        self.assertEqual(leaf.children, [])
        self.assertEqual(leaf.props, {"style": "color:red;"})

    def test_to_html_with_props(self):
        leaf = LeafNode(tag="a", value="Link", props={"href": "https://www.example.com"})
        html = leaf.to_html()
        self.assertEqual(html, '<a href="https://www.example.com">Link</a>')

    def test_to_html_without_props(self):
        leaf = LeafNode(tag="p", value="Paragraph")
        html = leaf.to_html()
        self.assertEqual(html, '<p>Paragraph</p>')

    def test_to_html_no_tag(self):
        leaf = LeafNode(tag=None, value="Just text")
        html = leaf.to_html()
        self.assertEqual(html, 'Just text')

    def test_repr(self):
        leaf = LeafNode(tag="div", value="Content")
        repr_str = repr(leaf)
        self.assertIn("LeafNode(tag=div", repr_str)
        self.assertIn("value=Content", repr_str)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("h1", "Title")
        child2 = LeafNode("p", "Paragraph")
        parent_node = ParentNode("section", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<section><h1>Title</h1><p>Paragraph</p></section>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    def test_repr(self):
        child_node = LeafNode("i", "italic")
        parent_node = ParentNode("p", [child_node])
        repr_str = repr(parent_node)
        self.assertIn("ParentNode(tag=p", repr_str)
        self.assertIn("children=[LeafNode(tag=i", repr_str)