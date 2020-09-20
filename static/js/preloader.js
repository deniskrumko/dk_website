window.onload = function () {
  window.setTimeout(function () {
    document.getElementById('preloader-box').classList.add('hide');
  }, 300);
  window.setTimeout(function () {
    document.getElementById('preloader-box').remove();
  }, 600);
}
