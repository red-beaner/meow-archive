import os
import re

HTML_FOLDER = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive'  # Update this if needed

NEW_CSS_TAG = '<link rel="stylesheet" href="styles/inject-style.css">'
JS_TAG = '<script src="scripts/inject-button-bar.js" defer></script>'

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    original = content

    # Replace old CSS reference
    content = re.sub(
        r'<link[^>]*href=["\']?style\.css["\']?[^>]*>',
        NEW_CSS_TAG,
        content,
        flags=re.IGNORECASE
    )

    # Check if the JS tag is already present
    if JS_TAG not in content:
        # Try inserting JS tag before closing </body> if present
        if '</body>' in content.lower():
            content = re.sub(r'</body>', f'{JS_TAG}\n</body>', content, flags=re.IGNORECASE)
        else:
            # Else insert at end of file
            content += f'\n{JS_TAG}\n'

    # Only write if something changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def scan_directory(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file))

if __name__ == "__main__":
    scan_directory(HTML_FOLDER)
    print("\nAll HTML files updated.")
