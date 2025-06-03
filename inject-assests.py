import os
import re

HTML_FOLDER = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive'  # Update as needed

def clean_html_content(content):
    original = content

    # Remove checkboxes and their labels for "Dark Mode" or "Remove Background"
    content = re.sub(r'<input[^>]*checkbox[^>]*>\s*(Dark Mode|Remove Background)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<label[^>]*>(.*?)</label>', '', content, flags=re.IGNORECASE)

    # Remove leftover "Close" buttons (from old modals or popups)
    content = re.sub(r'<button[^>]*>\s*Close\s*</button>', '', content, flags=re.IGNORECASE)

    # Remove inline <script> blocks related to old dark mode logic
    content = re.sub(
        r'<script[^>]*>.*?(dark|background).*?</script>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Remove old floating UI divs (heuristically named things like "settings", "controls", "toggle")
    content = re.sub(
        r'<div[^>]*(id|class)="[^"]*(settings|controls|toggle)[^"]*"[^>]*>.*?</div>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    return content if content != original else None

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned = clean_html_content(content)

    if cleaned:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(cleaned)
        print(f"Cleaned: {path}")
    else:
        print(f"No old UI found: {path}")

def run_cleanup(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                clean_file(os.path.join(root, file))

if __name__ == "__main__":
    run_cleanup(HTML_FOLDER)
    print("\n✅ Old controls and UI cleaned up!")
