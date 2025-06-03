// save as remove-old-ui.js and run: node remove-old-ui.js ./path/to/html/folder

const fs = require('fs');
const path = require('path');

const targetDir = process.argv[2] || '.';

if (!fs.existsSync(targetDir) || !fs.statSync(targetDir).isDirectory()) {
  console.error('Please provide a valid directory path');
  process.exit(1);
}

const OLD_UI_PATTERN = /<div class="button-container">[\s\S]*?<div class="modal" id="settingsModal">[\s\S]*?<button id="updateCloseBtn">Close<\/button>\s*<\/div>\s*<\/div>/m;

function cleanFile(filePath) {
  const fileName = path.basename(filePath);
  if (fileName.toLowerCase() === 'index.html') {
    console.log(`Skipping ${fileName}`);
    return;
  }

  let content = fs.readFileSync(filePath, 'utf8');

  if (OLD_UI_PATTERN.test(content)) {
    console.log(`Cleaning old UI from ${fileName}...`);
    content = content.replace(OLD_UI_PATTERN, '');
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Done cleaning ${fileName}`);
  } else {
    console.log(`No old UI found in ${fileName}`);
  }
}

fs.readdirSync(targetDir).forEach(file => {
  if (file.endsWith('.html')) {
    const fullPath = path.join(targetDir, file);
    cleanFile(fullPath);
  }
});
