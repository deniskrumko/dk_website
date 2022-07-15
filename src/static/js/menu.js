function toggleMenu() {
  alert();
}

function scrollToTop(){
  var currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
  if (currentScroll > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo (0,currentScroll - (currentScroll/5));
  }
};
