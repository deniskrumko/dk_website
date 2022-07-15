function toggleMenu() {
  var content = document.getElementById('mobile-menu');
  if (content.style.maxHeight){
    content.style.maxHeight = null;
  } else {
    content.style.maxHeight = content.scrollHeight + "px";
  }
}

function scrollToTop(){
  var currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
  if (currentScroll > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo (0,currentScroll - (currentScroll/5));
  }
};
