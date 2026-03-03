
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method.")
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=str, value=str, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        if self.tag is None:
            return f"{self.value}"
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag=str, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children if children is not None else [], props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children to convert to HTML.")
        props_html = self.props_to_html()
        opening_tag = f"<{self.tag} {props_html}>" if props_html else f"<{self.tag}>"
        children_html = ''.join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"