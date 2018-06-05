jQuery(document).ready(function( $ ) {

  var scroll_quote = 500;
  var quote_stage = 1;
  var update = false;

  $(window).scroll(function() {

    if ($(this).scrollTop() > scroll_quote) {
      if (quote_stage == 1) {
        $('#dk-quote-text').text('Умная цитата все еще в разработке...');
      }
      if (quote_stage == 2) {
        $('#dk-quote-text').text('Зачем Вы так часто листаете страницу?');
      }
      if (quote_stage == 3) {
        $('#dk-quote-text').text('Вы сейчас сломаете веб-сайт!');
      }
      if (quote_stage == 4) {
        $('#dk-quote-text').text('404: Website not found');
        $('#dk-quote-author').text('— Fatal error');
      }
      if (quote_stage > 4) {
        $('#dk-quote-text').text('404: Website not found ('+(quote_stage-3)+')');
      }

      if (quote_stage < 9) {
        update = true;
      } else {
        $('.dk-quote').hide();
      }

    } else {
      if (update) {
        quote_stage += 1;
        update = false;
      }
    }
  });

});
