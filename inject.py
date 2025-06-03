import os

BUTTON_PLACEHOLDER = '<div id="button-bar-placeholder"></div>'
SCRIPT_TAG = '<script src="/scripts/inject-button-bar.js"></script>'

def should_skip(filename):
    # Skip index.html and non-.html files
    return (
        filename == 'index.html'
        or not filename.endswith('.html')
        or os.path.isdir(filename)
    )

def is_main_html_file(filename):
    # Only top-level .html files, not inside any folders
    return (
        os.path.isfile(filename)
        and filename.endswith('.html')
        and not filename.endswith('_Files.html')
        and not filename.startswith('.')  # Ignore hidden files
    )

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if BUTTON_PLACEHOLDER not in content:
        if '<body>' in content:
            content = content.replace('<body>', f'<body>\n{BUTTON_PLACEHOLDER}', 1)
        else:
            content = f'{BUTTON_PLACEHOLDER}\n' + content
        changed = True

    if SCRIPT_TAG not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{SCRIPT_TAG}\n</body>', 1)
        else:
            content += '\n' + SCRIPT_TAG
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ Injected: {filepath}')
    else:
        print(f'⏭️ Already has elements: {filepath}')

def main():
    for filename in os.listdir('.'):
        if should_skip(filename):
            continue
        if is_main_html_file(filename):
            process_html_file(filename)

if __name__ == '__main__':
    main()
