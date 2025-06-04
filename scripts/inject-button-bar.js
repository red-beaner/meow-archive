document.addEventListener('DOMContentLoaded', () => {
  // Create the custom button bar
  const bar = document.createElement('div');
  bar.id = 'custom-button-bar';
  bar.innerHTML = `
    <button onclick="togglePanel('settings')">Settings</button>
    <button onclick="togglePanel('contact')">Contact</button>
    <button onclick="togglePanel('updates')">Update Notes</button>
    <button onclick="togglePanel('nav')">Navigation</button>

    <div id="settings-panel" style="display:none">
      <h2>Settings</h2>
      <label><input type="checkbox" id="toggle-dark"> Dark Mode</label>
      <label><input type="checkbox" id="toggle-bg"> Remove Background</label>
      <button onclick="closePanel('settings')">Close</button>
    </div>

    <div id="contact-panel" style="display:none">
      <h2>Contact</h2>
      <p>Discord User: redbeans._.</p>
      <p>Email: meowarchive@example.com</p>
      <p>Server <a href="https://discord.gg/N7ypkN85Rk">Join Link</a> , join our community!.</p>
      <p>To message me, join the server and then you'll be able to dm me.</p>
      <p>Main page <a href="https://red-beaner.github.io/meow-archive/">link</a></p>
      <button onclick="closePanel('contact')">Close</button>
    </div>

    <div id="updates-panel" style="display:none">
      <h2>Update Notes</h2>
      <p>Version 25.0603 includes the new welcome screen, improved dark mode, and updated navigation.</p>
      <button onclick="closePanel('updates')">Close</button>
    </div>

    <div id="navigation-panel" style="display:none">
      <h2>Navigation</h2>
      <p>#memes</p>
      <buton onclick="closePanel('nav')">Close</button>
    </div>
  `;
  document.body.appendChild(bar);

  // Event listeners
  document.getElementById('toggle-dark').addEventListener('change', (e) => {
    document.body.classList.toggle('dark-mode', e.target.checked);
  });

  document.getElementById('toggle-bg').addEventListener('change', (e) => {
    document.body.classList.toggle('no-bg', e.target.checked);
  });

  // Add your background here
  document.body.style.backgroundImage = 'url("https://yourdomain.com/background.jpg")';
});

function togglePanel(panel) {
  document.getElementById('settings-panel').style.display = 'none';
  document.getElementById('contact-panel').style.display = 'none';
  document.getElementById('updates-panel').style.display = 'none';
  document.getElementById(`${panel}-panel`).style.display = 'block';
}

function closePanel(panel) {
  document.getElementById(`${panel}-panel`).style.display = 'none';
}
