document.addEventListener('DOMContentLoaded', () => {
  // Create the custom button bar
  const bar = document.createElement('div');
  bar.id = 'custom-button-bar';
  bar.innerHTML = `
    <button onclick="togglePanel('settings')">Settings</button>
    <button onclick="togglePanel('contact')">Contact</button>
    <button onclick="togglePanel('updates')">Update Notes</button>
    <button onclick="togglePanel('navigation')">Navigation</button>

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
      // <p><a href="https://red-beaner.github.io/meow-archive/memes.html">#memes</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/quotes.html">#quotes</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/intros.html">#introductions</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/positivity.html">#positivity-place</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/distractedbf.html">#distracted-bf</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/art.html">#art</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/diary.html">#diary</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/dream.html">#dream</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/confess.html">#confessions</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/donnydump-path.html">#dony-dump</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/caughtin4k.html">#caught-in-4k</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/kitastare.html">#kita-stare</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/maddiespussies.html">#maddie's-pussies</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/onewordstory.html">#one-word-story</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/xscream2.html">#xscrem2</a></p>
      // <p><a href="https://red-beaner.github.io/meow-archive/finishthesong.html">#finish-the-song</a></p>
        <p>
          <a href="#" aria-haspopup="true" aria-expanded="false">#special-files ▼</a>
              <div class="dropdown-content" role="menu" aria-label="Special files submenu">
                <a href="donnydump-path.html" role="menuitem">donydump</a>
                <a href="caughtin4k.html" role="menuitem">caught in 4k</a>
                <a href="kitastare.html" role="menuitem">kitastare</a>
                <a href="maddiespussies.html" role="menuitem">maddie's pussies</a>
                <a href="onewordstory.html" role="menuitem">one word story</a>
                <a href="xscream2.html" role="menuitem">xscream2</a>
                <a href="finishthesong.html" role="menuitem">finish the song</a>
              </div>
        </p>

      <buton onclick="closePanel('navigation')">Close</button>
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
  document.getElementById('navigation-panel').style.display = 'none';
  document.getElementById(`${panel}-panel`).style.display = 'block';
}

function closePanel(panel) {
  document.getElementById(`${panel}-panel`).style.display = 'none';
}
