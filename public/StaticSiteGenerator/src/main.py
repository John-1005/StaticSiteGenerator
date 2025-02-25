import os
import shutil

from generate_page import extract_title, generate_pages_recursive

def copy_recursive(src, dst):
    print(f"Copying from {src} to {dst}")


    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {item}")
        else:
            os.mkdir(dst_path)
            print(f"Created directory {item}")

            copy_recursive(src_path, dst_path)

def copy_static():
    static_dir = "static"
    public_dir = "public"

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    os.mkdir(public_dir)
    copy_recursive(static_dir, public_dir)

def main():
    copy_static()
    generate_pages_recursive(
        dir_path_content = "content",
        template_path = "template.html",
        dest_dir_path = "public"
    )

if __name__ == "__main__":
    main()


