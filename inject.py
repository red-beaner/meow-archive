import os
import re

# Put your shared HTML + buttons + scripts here exactly as you want them injected.
shared_content = """
<!-- START SHARED UI -->
<div class="button-container">
  <button id="contactBtn" title="Contact">Contact</button>
  <button id="settingsBtn" title="Settings">Settings</button>
  <button id="updateBtn" title="Update Notes">Update Notes</button>
</div>

<script>
  // Your modal open/close and dark mode toggle JS here
  // You can keep your existing JS from index.html, or reference an external shared JS file
</script>
<!-- END SHARED UI -->
"""

def looks_like_main_page(content):
    # Simple heuristic: presence of <body> or <html> means main page
    if re.search(r'<body[^>]*>', content, re.IGNORECASE) or re.search(r'<html[^>]*>', content, re.IGNORECASE):
        return True
    return False

def inject_shared_ui(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- START SHARED UI -->' in content:
        print(f"{file_path}: Shared UI already injected, skipping.")
        return

    if looks_like_main_page(content):
        # Try to insert before </body>
        if '</body>' in content.lower():
            # Case insensitive insert before </body>
            pattern = re.compile(r'</body>', re.IGNORECASE)
            new_content = pattern.sub(shared_content + '\n</body>', content, count=1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{file_path}: Injected shared UI before </body>.")
        else:
            # No </body> but looks like main page: append at end
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content + '\n' + shared_content)
            print(f"{file_path}: No </body> found, appended shared UI at end.")
    else:
        print(f"{file_path}: Looks like fragment (no <body>), skipping injection.")

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            inject_shared_ui(filename)

if __name__ == '__main__':
    main()
