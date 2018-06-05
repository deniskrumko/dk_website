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

  // Warning before leaving the page (back button, or outgoinglink)
  window.onbeforeunload = function(e) {
    if (was_changed) {
      return '123'
    } else {
      return
    }
  };
});
