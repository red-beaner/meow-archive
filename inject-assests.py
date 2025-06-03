import os
import re

HTML_FOLDER = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive'  # Update as needed

def clean_html_content(content):
    original = content

    # 1. Remove checkbox inputs for "Dark Mode" or "Remove Background" *and* their immediate following labels only
    # Use a pattern that captures input + label together for safety
    content = re.sub(
        r'<input[^>]*type=["\']?checkbox["\']?[^>]*>\s*<label[^>]*>\s*(Dark Mode|Remove Background)\s*</label>',
        '',
        content,
        flags=re.IGNORECASE
    )

    # 2. Remove *only* old UI Close buttons inside old UI containers (e.g., a div with class/id "old-ui" or similar)
    # Since we don't have exact old UI container IDs, let's only remove buttons named "Close" if they appear inside a div with class/id "old-ui"
    # First, find and remove <button>Close</button> inside <div id="old-ui">...</div>
    # If you don't have a wrapping div, remove this block and I'll adapt later
    def remove_old_ui_close_buttons(match):
        inner_html = match.group(1)
        cleaned_inner = re.sub(r'<button[^>]*>\s*Close\s*</button>', '', inner_html, flags=re.IGNORECASE)
        return f'<div id="old-ui">{cleaned_inner}</div>'

    content = re.sub(
        r'<div[^>]*id=["\']old-ui["\'][^>]*>(.*?)</div>',
        remove_old_ui_close_buttons,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # If you don't have an "old-ui" container, remove the above and just comment it out for now.

    # 3. Remove inline <script> blocks related to old dark mode or background logic (non-greedy)
    content = re.sub(
        r'<script[^>]*>.*?(dark|background).*?</script>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 4. Remove old floating UI divs with exact IDs/classes, non-greedy
    # Instead of broad matching, target exact ids/classes from your old UI if you know them.
    # Example: only remove divs with id="old-settings" or class="old-controls"
    # If you don't have exact names, here is a safer heuristic: 
    # Remove divs where the id/class contains exactly "old-settings", "old-controls", or "old-toggle" (not any div containing "settings")
    content = re.sub(
        r'<div[^>]*(id|class)=["\'](old-settings|old-controls|old-toggle)["\'][^>]*>.*?</div>',
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
