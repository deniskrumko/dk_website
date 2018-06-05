jQuery(document).ready(function($) {

  // Current playing track
  var current_track = false;

  // HELPER METHODS
  // =========================================================================

  // Get track object by track id
  function get_track(track_id) {
    return $('#' + track_id).get(0);
  }

  // Format seconds to "MM:SS"
  function formatTime(seconds) {
    minutes = Math.floor(seconds / 60);
    minutes = (minutes >= 10) ? minutes : "0" + minutes;
    seconds = Math.floor(seconds % 60);
    seconds = (seconds >= 10) ? seconds : "0" + seconds;
    return minutes + ":" + seconds;
  }

  // Method to show notification with provided message
  function showNotification(msg) {
    UIkit.notification({
      message: msg,
      timeout: 2000
    });
  }

  // Set "play-pause" button to "play" state
  function playButtonAsPlay() {
    $('#play-' + current_track.id).removeClass('active');
    $('#play-' + current_track.id).text('Play');
  }

  // Set "play-pause" button to "pause" state
  function playButtonAsPause() {
    $('#play-' + current_track.id).addClass('active');
    $('#play-' + current_track.id).text('Pause');
  }

  // Show notification about current playing track
  function showCurrentPlaying() {
    var artist = $(current_track).data('artist');
    var name = $(current_track).data('name');
    UIkit.notification({
      message: `<b>${artist}</b> — ${name}`,
      timeout: 2000
    });
  }

  // Method to play another provided track
  function playAnotherTrack(track) {
    disablePlayer(current_track);
    current_track = track;
    enablePlayer();
    toggleCurrentTrack();
  }

  // Method to play next/previous track
  function playNextPrevTrack(type) {
    if (current_track) {
      // Get "next" or "prev" track
      var nearby_track_id = $(current_track).data(type);

      if (nearby_track_id) {
        // If nearby track exists - play it!
        var track = get_track(nearby_track_id);
        playAnotherTrack(track)
        showCurrentPlaying();
      } else {
        // Otherwise - show notification that there is nothing to play
        if (type == 'next') {
          if (current_track.paused) {
            showNotification('Был прослушан последний трек');
          } else {
            showNotification('Вы слушаете последний трек');
          }
        } else {
          showNotification('Вы слушаете самый первый трек');
        }
      }
    }
  }

  // Method to play next track in playlist
  function playNextTrack() {
    playNextPrevTrack('next');
  }

  // Method to play previous track in playlist
  function playPrevTrack() {
    playNextPrevTrack('prev');
  }

  // Method to play/pause current track
  function toggleCurrentTrack() {
    if (current_track.paused) {
      current_track.play();
      playButtonAsPause();
      $(current_track).next().addClass('active');
    } else {
      current_track.pause();
      playButtonAsPlay();
      $(current_track).next().removeClass('active');
    }
  }

  // Method to set timeline position (from 0% to 100%)
  function setTimelinePosition(percent) {
    $(current_track).next().width(percent + '%');
  }

  // Method to set time block opacity (from 0 to 1)
  function setTimeblockOpacity(opacity) {
    var time_block = $(current_track).next().next().get(0);
    $(time_block).css('opacity', opacity);
  }

  // Method to add all event listeners to current track
  function addAllEventListeners() {
    current_track.addEventListener("timeupdate", timeUpdate, false);
    current_track.addEventListener("timeupdate", autoPlayNextTrack, false);
  }

  // Method to remove all event listeners from current track
  function removeAllEventListeners() {
    current_track.removeEventListener("timeupdate", timeUpdate, false);
    current_track.removeEventListener("timeupdate", autoPlayNextTrack, false);
  }

  // Method to enable player for current track
  function enablePlayer() {
    $(current_track).parent().addClass('active');
    setTimeblockOpacity(1);
    addAllEventListeners();
  }

  // Method to disable player for current track
  function disablePlayer() {
    current_track.pause();
    current_track.currentTime = 0;
    removeAllEventListeners();

    $(current_track).parent().removeClass('active');
    playButtonAsPlay();
    setTimelinePosition(0);
    setTimeblockOpacity(0);
  }

  // Initalize player with provided track (or first track)
  function initalizePlayer(track) {
    if (!current_track) {
      if (!track) {
        // If there are no `track` - use first and show notification
        track = get_track("track-1");
        current_track = track;
        showCurrentPlaying();
      } else {
        // Otherwise - use provided `track`
        current_track = track;
      }
      enablePlayer();
    }
  }

  // TASKS
  // =========================================================================

  // Task to update timeline of time block on track playing
  function timeUpdate() {
    percent = current_track.currentTime * 100 / current_track.duration;
    setTimelinePosition(percent);

    var time_block = $(current_track).next().next().get(0);
    var t1 = formatTime(current_track.currentTime);
    var t2 = formatTime(current_track.duration);
    $(time_block).text(t1 + ' / ' + t2);
  }

  // Task to autoplay next track if current track ended
  function autoPlayNextTrack() {
    if (current_track.currentTime == current_track.duration) {
      playNextTrack();
    }
  }

  // EVENT HANDLING
  // =========================================================================

  // Play or pause track on "play/pause" button click
  $('.dk-play-button').click(function(event) {
    var track_id = $(this).data('track');
    var track = get_track(track_id);

    // If there is no current track - initalize player
    initalizePlayer(track);

    if (current_track != track) {
      // If current track is not clicked track - play another track
      playAnotherTrack(track)
    } else {
      // Otherwise - play/pause current track
      toggleCurrentTrack();
    }

  });

  // On mouse down on timeline - remove all event listeners
  $('.dk-player-timeline').mousedown(function() {
    current_track.removeEventListener("timeupdate", timeUpdate, false);
  });

  // On mouse up on timeline - change current track position
  $('.dk-player-timeline').mouseup(function(event) {
    var position = event.pageX - $(this).offset().left;
    var obj_width = $(this).width();
    var percent = (position * 100 / obj_width);

    if (current_track) {
      current_track.currentTime = current_track.duration / 100 * percent;
    }

    current_track.addEventListener("timeupdate", timeUpdate, false);
  });

  // Player controls from keyboard
  $(document).keydown(function(e) {

    // Spacebar - play/pause current track
    if (e.keyCode == 32) {
      e.preventDefault();
      initalizePlayer();
      toggleCurrentTrack();
    }

    // Right arrow - play next track
    if (e.keyCode == 39) {
      playNextTrack();
    }

    // Left arrow - play previous track
    if (e.keyCode == 37) {
      playPrevTrack();
    }
  });

});
