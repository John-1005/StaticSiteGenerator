from markdown_blocks import markdown_to_html_node
import os
from textnode import TextNode


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            heading = line[2:]
            return heading.strip()
    else:
        raise Exception("No valid h1 header found")



def generate_page(from_path, template_path, dest_path):

    print(f"Generate page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as view_markdown:
        markdown = view_markdown.read()


    with open(template_path) as view_template:
        template = view_template.read()

    title = extract_title(markdown)

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as output_file:
        output_file.write(final_html)


    return final_html




def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    print(f"Found these items: {contents}")
    for item in contents:
        full_path = os.path.join(dir_path_content, item)
        if os.path.isfile(full_path):
            if full_path.endswith('.md'):
                relative_path = os.path.relpath(full_path, dir_path_content)
                html_path = os.path.splitext(relative_path)[0] + '.html'
                dest_path = os.path.join(dest_dir_path, html_path)
                html = generate_page(full_path, template_path, dest_path)
                

        else:
            new_dest_dir = os.path.join(dest_dir_path, item)
            os.makedirs(new_dest_dir, exist_ok=True)

            generate_pages_recursive(full_path, template_path, new_dest_dir)

