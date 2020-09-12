document.addEventListener("DOMContentLoaded", function(event) {
  // Add handler on textarea resize
  autosize(document.querySelector('textarea'));

  // Was entry changed or not?
  var was_changed = false;

  // Get all the objects by ID
  var entry = document.getElementById('text');
  var save_button = document.getElementById('save');
  var hidden_done_input = document.getElementById('done');
  var done_button = document.getElementById('is_ready');

  // If entry was changed - update `was_changed`
  entry.addEventListener('input', function (event) {
    was_changed = true;
  });

  // If save button is clicked - update `was_changed`
  save_button.addEventListener('click', function (event) {
    was_changed = false;
  });

  // If done button is clicked - update hidden input
  done_button.addEventListener('click', function (event) {
    was_changed = true;

    if (hidden_done_input.value == 'on') {
      hidden_done_input.value = '';
      done_button.classList.add('faded');
    } else {
      hidden_done_input.value = 'on';
      done_button.classList.remove('faded');
    }
  });

  // Set focus to entry
  entry.focus();

  // Handle click on tags
  document.addEventListener('click', function (event) {
  	if (!event.target.matches('.tag')) return;
  	event.preventDefault();

    was_changed = true;
    append_value = '';
    prefix = '#';

    if (entry.value) {
      prefix = '\n#';
    }
    if (event.target.innerText == '+ фото') {
      prefix = '';
      append_value = '<img src="ADD_LINK_HERE" class="diary-image"></img>';
    }
    else if (event.target.innerText != '#') {
      append_value = event.target.innerText + ' ';
    }

    entry.value = entry.value + prefix + append_value;
    var ta = document.querySelector('textarea');
    var evt = document.createEvent('Event');
    evt.initEvent('autosize:update', true, false);
    ta.dispatchEvent(evt);
  }, false);

  window.onbeforeunload = function(e) {
    if (was_changed) {
      return 'PLS SAVE ME!'
    } else {
      return
    }
  };
});
