from enum import Enum


def block_to_block_type(block):
    # unction that takes a single block of markdown text as input and returns the BlockType representing the type of block it is.
    # You can assume all leading and trailing whitespace were already stripped 
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    # Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
    # Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
    # Every line in an unordered list block must start with a - character, followed by a space.
    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    # If none of the above conditions are met, the block is a normal paragraph.
    
    def is_heading(b):
        if not b.startswith("#"):
            return False
        # count leading hashes
        i = 0
        while i < len(b) and b[i] == "#":
            i += 1
        if i == 0 or i > 6:
            return False
        # there must be at least one character after the hashes and it must be a space
        if i < len(b) and b[i] == " ":
            return True
        return False

    switch = {
        BlockType.Heading: is_heading(block),
        BlockType.Code: block.startswith("```") and block.endswith("```"),
        BlockType.Quote: all(line.startswith(">") for line in block.splitlines()),
        BlockType.Unordered_List: all(line.startswith("- ") for line in block.splitlines()),
        BlockType.Ordered_List: all(line.strip().startswith(f"{i}. ") for i, line in enumerate(block.splitlines(), start=1)),
    }
    for block_type, condition in switch.items():
        if condition:
            return block_type
    return BlockType.Paragraph 
    

class BlockType(Enum):
    Paragraph = "paragraph"
    Heading = "heading"
    Code = "code"
    Quote = "quote"
    Unordered_List = "unordered_list"
    Ordered_List = "ordered_list"

class Block:
    def __init__(self, block_type: BlockType, content: str):
        self.block_type = block_type
        self.content = content
    
    def __eq__(self, other):
        return self.block_type == other.block_type and self.content == other.content

    def __repr__(self):
        return f"Block({self.block_type.value}, {self.content})"