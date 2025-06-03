const placeholder = document.getElementById("button-bar-placeholder");

if (placeholder) {
  placeholder.innerHTML = `
    <div class="button-bar">
      <a href="index.html" class="nav-button">🏠 Home</a>
      <a href="shared.html" class="nav-button">🔗 Shared</a>
      <a href="clipsandlinks.html" class="nav-button">🎞️ Clips</a>
    </div>
  `;
}
