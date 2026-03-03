from textnode import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from BlockType import block_to_block_type, BlockType, Block
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    # Split the markdown into blocks (you already have a function for this)
    # Loop over each block:
    # Determine the type of block (you already have a function for this)
    # Based on the type of block, create a new HTMLNode with the proper data
    # Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. 
    # It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
    # The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. 
    # Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

    def text_to_children(text):
        # use text_to_textnodes to split inline markdown into TextNode objects,
        # then convert each TextNode into an HTMLNode (LeafNode or similar)
        nodes_list = text_to_textnodes(text)  # returns a list-of-lists
        if not nodes_list:
            return []
        textnodes = nodes_list[0]
        children = [text_node_to_html_node(n) for n in textnodes]
        return children

    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.Heading:
            # count leading hashes to determine heading level
            i = 0
            while i < len(block) and block[i] == "#":
                i += 1
            heading_level = i
            heading_text = block[i+1:].strip()  # skip the space after hashes
            children = text_to_children(heading_text)
            block_nodes.append(ParentNode(tag=f"h{heading_level}", children=children)) 
        elif block_type == BlockType.Code:
            content = block[3:-3]
            content = content[1:] if content.startswith("\n") else content
            block_nodes.append(ParentNode(tag="pre", children=[LeafNode(tag="code", value=content)]))
        elif block_type == BlockType.Quote:
            lines = block.splitlines()
            quote_text = " ".join(line[1:].strip() for line in lines)
            children = text_to_children(quote_text)
            block_nodes.append(ParentNode(tag="blockquote", children=children))
        elif block_type == BlockType.Unordered_List:
            items = [line[2:].strip() for line in block.splitlines()]
            item_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            block_nodes.append(ParentNode(tag="ul", children=item_nodes))
        elif block_type == BlockType.Ordered_List:
            items = [line[line.find(". ")+2:].strip() for line in block.splitlines()]
            item_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            block_nodes.append(ParentNode(tag="ol", children=item_nodes))
        else:  # Paragraph
            lines = block.splitlines()
            paragraph_text = " ".join(lines)
            children = text_to_children(paragraph_text)
            block_nodes.append(ParentNode(tag="p", children=children))
    return ParentNode(tag="div", children=block_nodes)
