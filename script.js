function setCookie(name, value, days = 365) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie = name + "=" + encodeURIComponent(value) + "; expires=" + expires + "; path=/";
}

function getCookie(name) {
  return document.cookie.split("; ").reduce((r, v) => {
    const parts = v.split("=");
    return parts[0] === name ? decodeURIComponent(parts[1]) : r
  }, "");
}

function applySettingsFromCookies() {
  if (getCookie("darkMode") === "true") {
    document.body.classList.add("dark-mode");
    const darkToggle = document.getElementById("darkModeToggle");
    if (darkToggle) darkToggle.checked = true;
  }

  if (getCookie("bgImage") === "false") {
    document.body.classList.add("no-bg");
    const bgToggle = document.getElementById("bgToggle");
    if (bgToggle) bgToggle.checked = false;
  }
}

function toggleSettings() {
  const panel = document.getElementById("settings-panel");
  if (panel) panel.style.display = panel.style.display === "none" ? "block" : "none";
}

document.addEventListener("DOMContentLoaded", () => {
  applySettingsFromCookies();

  const darkToggle = document.getElementById("darkModeToggle");
  const bgToggle = document.getElementById("bgToggle");

  if (darkToggle) {
    darkToggle.addEventListener("change", () => {
      const enabled = darkToggle.checked;
      document.body.classList.toggle("dark-mode", enabled);
      setCookie("darkMode", enabled ? "true" : "false");
    });
  }

  if (bgToggle) {
    bgToggle.addEventListener("change", () => {
      const enabled = bgToggle.checked;
      document.body.classList.toggle("no-bg", !enabled);
      setCookie("bgImage", enabled ? "true" : "false");
    });
  }
});