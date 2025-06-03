import os

SETTINGS_HTML = """
<!-- SETTINGS START -->
<div id="settings-button" style="position:fixed;top:10px;right:10px;z-index:1000;">
  <button onclick="toggleSettings()" style="padding:8px 12px;border:none;border-radius:6px;background:#0077cc;color:white;cursor:pointer;">Settings</button>
</div>
<div id="settings-panel" style="display:none;position:fixed;top:50px;right:10px;background:white;color:black;padding:15px;border-radius:10px;box-shadow:0 2px 10px rgba(0,0,0,0.3);z-index:1000;">
  <label><input type="checkbox" id="darkModeToggle"> Dark Mode</label><br>
  <label><input type="checkbox" id="bgToggle"> Background Image</label>
</div>
<!-- SETTINGS END -->
"""

HEAD_SNIPPET = """
<link rel="stylesheet" href="style.css">
<script src="script.js" defer></script>
"""

def inject_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'SETTINGS START' in content:
        return

    if '<head>' in content:
        content = content.replace('<head>', f'<head>\n{HEAD_SNIPPET.strip()}')

    if '</body>' in content:
        content = content.replace('</body>', f'{SETTINGS_HTML.strip()}\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def inject_to_all_html(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                inject_html(os.path.join(root, file))

if __name__ == '__main__':
    target_dir = '.'
    inject_to_all_html(target_dir)
    print("✅ Settings injected into all HTML files.")