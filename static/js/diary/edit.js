jQuery(document).ready(function($) {
  autosize($('textarea'));

  $('textarea').focus();

  var was_changed = false;

  $('textarea').change(function(event) {
    was_changed = true;
  });

  $('#save').click(function(event) {
    was_changed = false;
  });

  $('.dk-insert-tag').click(function() {
    was_changed = true;

    current_value = $('textarea').val();
    button_value = $(this).text();
    append_value = '';
    prefix = '#';

    if (current_value) { prefix = '\n#'; }
    if (button_value != '#') { append_value = $(this).text() + ' '; }
    $('textarea').val(current_value + prefix + append_value);

    var ta = document.querySelector('textarea');
    var evt = document.createEvent('Event');
    evt.initEvent('autosize:update', true, false);
    ta.dispatchEvent(evt);
  });

  // Warning before leaving the page (back button, or outgoinglink)
  window.onbeforeunload = function(e) {
    if (was_changed) {
      return '123'
    } else {
      return
    }
  };
});
