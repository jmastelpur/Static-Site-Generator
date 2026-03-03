import re 
from textnode import TextNode, TextType


def extract_markdown_images(text):
    # use regex to find all occurrences of ![alt text](url) in the text and return a list of tuples (alt_text, url)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    # use regex to find all occurrences of [anchor text](url) in the text and return a list of tuples (anchor_text, url)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    # to create TextNodes from raw markdown strings, specifically for images
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None:
            continue
        parts = extract_markdown_images(node.text)
        if not parts:
            new_nodes.append(node)
            continue
        last_index = 0
        for alt_text, url in parts:
            start_index = node.text.find(f"![{alt_text}]({url})", last_index)
            if start_index == -1:
                continue
            if start_index > last_index:
                new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = start_index + len(f"![{alt_text}]({url})")
        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
    return new_nodes

        

def split_nodes_link(old_nodes):
    # to create TextNodes from raw markdown strings, specifically for links
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None:
            continue

        parts = extract_markdown_links(node.text)
        if not parts:
            new_nodes.append(node)
            continue
        last_index = 0
        for link_text, url in parts:
            start_index = node.text.find(f"[{link_text}]({url})", last_index)
            if start_index == -1:
                continue
            if start_index > last_index:
                new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            last_index = start_index + len(f"[{link_text}]({url})")
        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
    return new_nodes
