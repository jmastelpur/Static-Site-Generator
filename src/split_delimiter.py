from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #  to create TextNodes from raw markdown strings
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: unmatched delimiter '{delimiter}'")
        # If a matching closing delimiter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
        for i, part in enumerate(parts):
            if part:
                new_nodes.append(TextNode(part, TextType.TEXT if i % 2 == 0 else text_type))
            if i < len(parts) - 1:
                # Add the delimiter as a separate node if needed
                pass  # Delimiter is not added as a separate node in this implementation
    return new_nodes



    