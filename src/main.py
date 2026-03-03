import os
import shutil
from generate_page import generate_pages_recursive

def main():
    # Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    # It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    # It should copy all files and subdirectories, nested files, etc.
    # I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
    # no shutil.copytree() allowed, you must write the recursive function yourself using os and shutil modules.
    
    source_dir = "static"
    dest_dir = "public"
    # Delete all contents of the destination directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    # Recursive function to copy contents
    def copy_contents(src, dst):
        for item in os.listdir(src):
            src_item = os.path.join(src, item)
            dst_item = os.path.join(dst, item)
            if os.path.isdir(src_item):
                os.makedirs(dst_item)
                copy_contents(src_item, dst_item)
            else:
                shutil.copy2(src_item, dst_item)
                print(f"Copied: {src_item} to {dst_item}")
    # Start copying from source to destination
    copy_contents(source_dir, dest_dir)

    # after copying files from static to public, it should generate a page from content using template.html and write it to public.
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()