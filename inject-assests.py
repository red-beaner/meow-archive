from bs4 import BeautifulSoup # type: ignore
import os

# === CONFIG ===
HTML_FOLDER = 'C:\\Users\\j\\Documents\\GitHub\\meow-archive\\meow-archive'  # Change this to your HTML directory path
BACKGROUND_URL = 'https://drive.diggy.network/api/public/dl/HztOunHx?inline=true'  # Change this to your custom background image URL

BUTTONS_AND_MODALS_HTML = '''
<div class="button-container">
  <button id="contactBtn">Contact</button>
  <button id="settingsBtn">Settings</button>
  <button id="updateBtn">Update Notes</button>
</div>

<!-- Settings Modal -->
<div id="settingsModal" class="modal">
  <div class="modal-content">
    <h2>Settings</h2>
    <label><input type="checkbox" id="darkModeToggle" /> Dark Mode</label><br />
    <label><input type="checkbox" id="noBackgroundToggle" /> Remove Background</label><br />
    <button id="settingsCloseBtn">Close</button>
  </div>
</div>

<!-- Contact Modal -->
<div id="contactModal" class="modal">
  <div class="modal-content">
    <h2>Contact</h2>
    <p>Email: meowarchive@example.com</p>
    <button id="contactCloseBtn">Close</button>
  </div>
</div>

<!-- Update Notes Modal -->
<div id="updateModal" class="modal">
  <div class="modal-content">
    <h2>Update Notes</h2>
    <p>Version 25.0603 includes the new welcome screen, improved dark mode, and updated navigation.</p>
    <button id="updateCloseBtn">Close</button>
  </div>
</div>
'''

CUSTOM_BG_STYLE = f'''
<style>
  body {{
    background: url('{BACKGROUND_URL}') no-repeat center center fixed !important;
    background-size: cover !important;
    margin: 0; padding: 0;
  }}

  #page-wrapper {{
    max-width: 960px;
    margin: 40px auto;
    padding: 20px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
  }}

  body.dark-mode #page-wrapper {{
    background: rgba(30, 30, 30, 0.85);
    color: white;
  }}
</style>
'''

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Add <link rel="stylesheet" href="style.css"> in <head>
    head = soup.head
    if head:
        if not soup.find('link', href='style.css'):
            new_link = soup.new_tag('link', rel='stylesheet', href='style.css')
            head.append(new_link)
        # Inject custom background style if not present
        if not head.find('style', string=lambda text: text and BACKGROUND_URL in text):
            style_tag = BeautifulSoup(CUSTOM_BG_STYLE, 'html.parser')
            head.append(style_tag)
    else:
        # create <head> with style and link
        new_head = soup.new_tag('head')
        new_link = soup.new_tag('link', rel='stylesheet', href='style.css')
        new_head.append(new_link)
        style_tag = BeautifulSoup(CUSTOM_BG_STYLE, 'html.parser')
        new_head.append(style_tag)
        if soup.html:
            soup.html.insert(0, new_head)
        else:
            soup.insert(0, new_head)

    body = soup.body
    if body:
        # Add <script src="scripts.js" defer></script> before </body>
        if not soup.find('script', src='scripts.js'):
            new_script = soup.new_tag('script', src='scripts/inject-button-bar.js', defer=True)
            body.append(new_script)

        # Inject buttons + modals if not already there
        if not soup.find('div', class_='button-container'):
            buttons_soup = BeautifulSoup(BUTTONS_AND_MODALS_HTML, 'html.parser')
            for element in reversed(buttons_soup.contents):
                body.insert(0, element)

        # Wrap all existing content (except buttons/modals) inside #page-wrapper
        to_wrap = []
        for child in list(body.children):
            # Skip buttons container and modals
            if getattr(child, 'get', lambda x: None)('class'):
                classes = child.get('class')
                if 'button-container' in classes or 'modal' in classes:
                    continue
            if str(child).strip() == '':
                continue
            to_wrap.append(child)

        if to_wrap:
            wrapper_div = soup.new_tag('div', id='page-wrapper')
            for element in to_wrap:
                wrapper_div.append(element.extract())
            body.append(wrapper_div)

    else:
        # No body tag — create one
        new_body = soup.new_tag('body')
        new_link = soup.new_tag('link', rel='stylesheet', href='style.css')
        new_body.append(new_link)
        style_tag = BeautifulSoup(CUSTOM_BG_STYLE, 'html.parser')
        new_body.append(style_tag)
        buttons_soup = BeautifulSoup(BUTTONS_AND_MODALS_HTML, 'html.parser')
        for element in buttons_soup.contents:
            new_body.append(element)
        new_script = soup.new_tag('script', src='scripts/inject-button-bar.js', defer=True)
        new_body.append(new_script)
        soup.append(new_body)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Updated {filepath}")

def main():
    for root, dirs, files in os.walk(HTML_FOLDER):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                update_html_file(path)

if __name__ == '__main__':
    main()
