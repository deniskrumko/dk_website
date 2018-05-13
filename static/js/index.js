jQuery(document).ready(function( $ ) {

  var scroll_navbar = 130;

  if ($(window).scrollTop() > scroll_navbar) {
    $('.uk-navbar-container').css('opacity', 0);
  } else {
    $('.uk-navbar-container').css('opacity', 1);
  }

  // Header fixed and Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > scroll_navbar) {
      $('.uk-navbar-container').css('opacity', 0);
    } else {
      $('.uk-navbar-container').css('opacity', 1);
    }
  });

});
