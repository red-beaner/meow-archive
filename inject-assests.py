import os
import re

HTML_FOLDER = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive'  # Update this as needed

def clean_html_content(content):
    original = content

    # Remove specific old UI components without affecting functional ones
    # 1. Remove old dark mode and background toggles only if they're inside settings modal
    content = re.sub(
        r'<label[^>]*>\s*<input[^>]*type="checkbox"[^>]*>\s*(Dark Mode|Remove Background)\s*</label>\s*<br>',
        '',
        content,
        flags=re.IGNORECASE
    )

    # 2. Remove entire old divs by class or id heuristics (e.g., controls/settings-panel/legacy-ui)
    content = re.sub(
        r'<div[^>]+(id|class)="[^"]*(legacy|settings-panel|old-ui|toggle-controls)[^"]*"[^>]*>.*?</div>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 3. Remove old inline script blocks related to dark mode or background toggling
    content = re.sub(
        r'<script[^>]*>.*?(darkModeToggle|noBackgroundToggle|toggleDarkMode).*?</script>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # IMPORTANT: Do NOT remove any button with id="welcomeCloseBtn"
    # and skip <button>Close</button> patterns to prevent wiping functional modals

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
    print("\n🎉 Cleanup complete!")
