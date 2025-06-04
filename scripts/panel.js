// document.addEventListener('DOMContentLoaded', () => {
//   const darkToggle = document.getElementById('darkToggle');
//   const bgToggle = document.getElementById('bgToggle');
//   const openSettings = document.getElementById('openSettings');
//   const settingsModal = document.getElementById('settingsModal');
//   const closeSettings = document.getElementById('closeSettings');
//   const body = document.body;

//   // Dark Mode toggle
//   darkToggle.addEventListener('click', () => {
//     body.classList.toggle('dark-mode');
//     darkToggle.setAttribute('aria-pressed', body.classList.contains('dark-mode'));
//   });

//   // Background toggle
//   bgToggle.addEventListener('click', () => {
//     body.classList.toggle('no-background');
//     bgToggle.setAttribute('aria-pressed', !body.classList.contains('no-background'));
//   });

//   // Open settings modal
//   openSettings.addEventListener('click', () => {
//     settingsModal.style.display = 'flex';
//     settingsModal.focus();
//   });

//   // Close settings modal
//   closeSettings.addEventListener('click', () => {
//     settingsModal.style.display = 'none';
//     openSettings.focus();
//   });

//   // Close modal on clicking outside modal-content or pressing ESC
//   settingsModal.addEventListener('click', (e) => {
//     if (e.target === settingsModal) {
//       settingsModal.style.display = 'none';
//       openSettings.focus();
//     }
//   });

//   document.addEventListener('keydown', (e) => {
//     if (e.key === 'Escape' && settingsModal.style.display === 'flex') {
//       settingsModal.style.display = 'none';
//       openSettings.focus();
//     }
//   });
// });
