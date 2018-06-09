jQuery(document).ready(function( $ ) {

  var scroll_navbar = 80;
  var navbar_hidden = true;

  if ($(window).scrollTop() > scroll_navbar) {
    $('.uk-navbar-container').css('z-index', -1);
    $('.uk-navbar-container').css('opacity', 0);
    navbar_hidden = true;
  } else {
    $('.uk-navbar-container').css('opacity', 1);
    navbar_hidden = false;
  }

  $(window).scroll(function() {
    if ($(this).scrollTop() > scroll_navbar) {
      if (!navbar_hidden) {
        $('.uk-navbar-container').css('opacity', 0);
        $('.uk-navbar-container').delay(1000).css('z-index', -1);
        navbar_hidden = true;
      }
    } else {
      if (navbar_hidden) {
        $('.uk-navbar-container').css('z-index', 100);
        $('.uk-navbar-container').css('opacity', 1);
        navbar_hidden = false;
      }
    }
  });

});
