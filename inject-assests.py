import sys
import os
import re

def remove_old_ui(html_content):
    # This pattern matches the entire <script> block that loads parts dynamically (old UI)
    pattern = re.compile(
        r'<script>.*?async function loadNextPart\(\).*?window\.addEventListener\("scroll",.*?</script>',
        re.DOTALL
    )
    new_content, count = pattern.subn('', html_content)
    return new_content, count > 0

def main(folder):
    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a valid directory.")
        return

    html_files = [f for f in os.listdir(folder) if f.endswith('.html') and f.lower() != 'index.html']

    if not html_files:
        print("No HTML files found (excluding index.html).")
        return

    print(f"Processing {len(html_files)} files in '{folder}'...")

    for filename in html_files:
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changed = remove_old_ui(content)

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filename}")
        else:
            print(f"No changes: {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fix_old_ui.py <folder_path>")
    else:
        main(sys.argv[1])
