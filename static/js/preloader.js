window.onload = function () {
  window.setTimeout(function () {
    document.getElementById('preloader-box').classList.add('fade');
  }, 300);
  window.setTimeout(function () {
    document.getElementById('preloader-box').classList.add('hide');
    document.getElementById('preloader-animation').remove();
  }, 600);
}

window.onclick = function(event) {
  if (event.target.href) {
    document.getElementById('preloader-box').classList.remove('hide');
    window.setTimeout(function () {
      document.getElementById('preloader-box').classList.remove('fade');
    }, 300);
  }
}
