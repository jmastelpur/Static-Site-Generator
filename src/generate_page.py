import os 
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath="/"):
    # Print a message like "Generating page from from_path to dest_path using template_path".
    # Read the markdown file at from_path and store the contents in a variable.
    # Read the template file at template_path and store the contents in a variable.
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    # Use the extract_title function to grab the title of the page.
    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    # n generate_page, after you replace the {{ Title }} and {{ Content }}, replace any instances of: href="/ with href="{basepath}, src="/ with src="{basepath}
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as f:
        template_content = f.read()
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    # Replace href and src attributes with the basepath
    full_html = full_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    # Crawl every entry in the content directory
    # For each markdown file found, generate a new .html file using the same template.html. 
    # The generated pages should be written to the public directory in the same directory structure.
    # Change your main function to use generate_pages_recursive instead of generate_page. 
    # You should generate a page for every markdown file in the content directory and write the results to the public directory.
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path.replace('.md', '.html'))
                generate_page(from_path, template_path, dest_path, basepath)