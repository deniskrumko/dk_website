function get_track(track_id) {
  return $('#' + track_id).get(0);
}

function stop_track(track) {
  track.pause();
  track.currentTime = 0;
}

function getPosition(el) {
    return el.getBoundingClientRect().left;
}

function playButtonAsPlay(playButton) {
  playButton.removeClass('active');
  playButton.text('Play');
}

function playButtonAsPause(playButton) {
  playButton.addClass('active');
  playButton.text('Pause');
}

function updatePlayButton(track) {
  var playButton = $('#play-' + track.id);
  if (track.paused) {
    playButtonAsPlay(playButton);
  } else {
    playButtonAsPause(playButton);
  }
}

function disablePlayer(track) {
  $(track).parent().removeClass('active');
  playButtonAsPlay($('#play-' + track.id));
  var pos = $(track).next().get(0);
  $(pos).width(0);
  var time_block = $(track).next().next().get(0);
  $(time_block).css('opacity', 0);
}

function enablePlayer(track) {
  $(track).parent().addClass('active');
}

function formatTime(seconds) {
    minutes = Math.floor(seconds / 60);
    minutes = (minutes >= 10) ? minutes : "0" + minutes;
    seconds = Math.floor(seconds % 60);
    seconds = (seconds >= 10) ? seconds : "0" + seconds;
    return minutes + ":" + seconds;
  }

jQuery(document).ready(function($) {

  var current_track = false;

  function timeUpdate() {
    percent = current_track.currentTime * 100 / current_track.duration;

    var pos = $(current_track).next().get(0);
    $(pos).width(percent + '%');

    var time_block = $(current_track).next().next().get(0);
    $(time_block).css('opacity', 1);
    var t1 = formatTime(current_track.currentTime);
    var t2 = formatTime(current_track.duration);

    $(time_block).text(t1 + ' / ' + t2);
  }

  // Play track on "Play" click
  $('.dk-play-button').click(function(event) {
    var track_id = $(this).data('track');
    var track = get_track(track_id);

    // If there is no current track - set it
    if (!current_track) {
      current_track = track;
      enablePlayer(current_track);
    }

    // If current track is not clicked track - stop current track
    if (current_track != track) {
      stop_track(current_track);
      current_track.removeEventListener("timeupdate", timeUpdate, false);
      disablePlayer(current_track);

      current_track = track;
      enablePlayer(current_track);
    }

    // Play or pause track
    if (current_track.paused) {
      current_track.play();
    } else {
      current_track.pause();
    }

    updatePlayButton(current_track);

    current_track.addEventListener("timeupdate", timeUpdate, false);

  });

  $('.dk-player-timeline').mousedown(function() {
    current_track.removeEventListener("timeupdate", timeUpdate, false);
    console.log('down');
  });

  $('.dk-player-timeline').mouseup(function(event) {
      console.log('up');
      var position = event.pageX - $(this).offset().left;
      var obj_width = $(this).width();
      var percent = (position * 100 / obj_width);

      if (current_track) {
        current_track.currentTime = current_track.duration / 100 * percent;
        console.log(current_track.duration);
        console.log(current_track.currentTime);
      }

      current_track.addEventListener("timeupdate", timeUpdate, false);
  });


});
