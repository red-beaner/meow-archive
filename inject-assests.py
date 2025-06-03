import os
import re

HTML_FOLDER = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive'  # Adjust to your path

def clean_html_content(content):
    original = content

    # Only remove <label><input type="checkbox"> Dark Mode or Remove Background</label>
    content = re.sub(
        r'<label[^>]*>\s*<input[^>]*type="checkbox"[^>]*>\s*(Dark Mode|Remove Background)\s*</label>\s*<br>',
        '',
        content,
        flags=re.IGNORECASE
    )

    # Remove old script blocks that reference known toggles
    content = re.sub(
        r'<script[^>]*>.*?(darkModeToggle|noBackgroundToggle|toggleDarkMode).*?</script>',
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
        print(f"✅ Cleaned: {path}")
    else:
        print(f"⏭️ No changes: {path}")

def run_cleanup(folder):
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return

    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.html'):
                clean_file(os.path.join(root, file))

if __name__ == "__main__":
    run_cleanup(HTML_FOLDER)
    print("\n🎉 Cleanup complete — safely.")
