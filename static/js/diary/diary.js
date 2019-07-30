window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  var element = document.getElementById("diary-tags");
  if (currentScrollPos > 250) {
    document.getElementById("diary-top").style.top = "0px";
  } else {
    document.getElementById("diary-top").style.top = "-280px";
  }
}
