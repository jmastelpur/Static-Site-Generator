
def markdown_to_blocks(markdown):
    # It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.
    # when you’re building current_block, detect “this line is a heading” and “current_block already has something”, 
    # then flush the current block and start a new one (also treat each heading line as a single-line block).

    lines = markdown.split("\n")
    blocks = []
    current_block = []
    for line in lines:
        if line.startswith("#") and current_block:
            blocks.append("\n".join(current_block))
            current_block = []
            blocks.append(line)  # add the heading as its own block
        elif line.strip() == "":
             if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append("\n".join(current_block))
    return blocks