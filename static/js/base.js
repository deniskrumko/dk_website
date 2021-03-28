function scrollToTop(){
  var currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
  if (currentScroll > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo (0,currentScroll - (currentScroll/5));
  }
};

function toggleMenu(e){
  e.classList.toggle("is-active");
  document.getElementById('menu-items-box').classList.toggle('active');
  document.getElementById('menu-items-box-inside').classList.toggle('active');
}
