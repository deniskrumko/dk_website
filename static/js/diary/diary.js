function expandPage(e) {
  // Expand page on button click
  var page = document.getElementById('page');
  page.classList.remove('collapsed-page');
  e.style.display = 'none';
}
