function setCookie(name, value, days) {
  const d = new Date();
  d.setTime(d.getTime() + (days*24*60*60*1000));
  let expires = "expires=" + d.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
  let cname = name + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(cname) === 0) {
      return c.substring(cname.length, c.length);
    }
  }
  return "";
}

function toggleSettingsMenu() {
  document.getElementById('settingsMenu').classList.toggle('hidden');
}

function toggleMode() {
  const isDark = document.getElementById('modeToggle').checked;
  document.body.classList.toggle('light-mode', !isDark);
  setCookie('darkmode', isDark ? '1' : '0', 365);
}

function toggleBackground() {
  const isEnabled = document.getElementById('bgToggle').checked;
  document.body.classList.toggle('bg-enabled', isEnabled);
  setCookie('background', isEnabled ? '1' : '0', 365);
}

window.onload = () => {
  const darkMode = getCookie('darkmode') === '1';
  const bgEnabled = getCookie('background') === '1';
  document.body.classList.toggle('light-mode', !darkMode);
  document.body.classList.toggle('bg-enabled', bgEnabled);
  document.getElementById('modeToggle').checked = darkMode;
  document.getElementById('bgToggle').checked = bgEnabled;
};