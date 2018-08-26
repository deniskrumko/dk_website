jQuery(document).ready(function($) {

  $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
  });

  $('.dk-like').click(function(event) {
    var url = $(this).data('like');
    var obj = $(this);
    $.ajax({
        url: url,
        method: 'POST',
        data: {
          'username': '1'
        },
        dataType: 'json',
        success: function (data) {
          if (data.result != '') {
            $(obj).find('.dk-like-text').text(data.result);
          } else {
            alert('Почему-то не работает...')
          }
        }
      });
  });
});
