
def extract_title(markdown_text):
    # It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    # If there is no h1 header, raise an exception.
    # extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
    if '#' not in markdown_text:
        raise ValueError("No h1 header found in the markdown text.")
    lines = markdown_text.strip().splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found in the markdown text.")