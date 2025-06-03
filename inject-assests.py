from bs4 import BeautifulSoup
import os
import shutil

html_path = r'C:\Users\j\Documents\GitHub\meow-archive\meow-archive\index.html'
backup_path = html_path + '.bak'

# Backup original first
shutil.copyfile(html_path, backup_path)
print(f"Backup created at {backup_path}")

with open(html_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Remove only these specific elements:
for selector in ['.button-container', '.panel']:
    for elem in soup.select(selector):
        elem.decompose()
        print(f"Removed element with selector: {selector}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Cleanup complete for index.html")
