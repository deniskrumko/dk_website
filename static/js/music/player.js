var current_track = false;
var current_track_src = false;
var current_track_obj = false;

function playPauseTrack() {
  // Toggle playing current track

  var e = current_track_obj;
  if (current_track.paused) {
    current_track.play();
    e.classList.add("active");
    e.classList.remove("paused");
  } else {
    current_track.pause();
    e.classList.add("paused");
    e.classList.remove("active");
  }
}

function initTrack(e) {
  // Initialize track

  var clicked_src = e.dataset.src;
  current_track = new Audio(clicked_src);
  current_track_src = clicked_src;
  current_track_obj = e;

  current_track.onended = function() {
    playTrack(current_track_obj.nextElementSibling);
  };
}

function playTrack(e) {
  // Play track on click or spacebar press

  var clicked_src = e.dataset.src;

  if (clicked_src == current_track_src) {
    playPauseTrack();
  } else {
    if (current_track) {
      current_track.pause();
      current_track.onended = false;
      current_track_obj.classList.remove("paused");
      current_track_obj.classList.remove("active");
    }
    initTrack(e);
    current_track.play();
    e.classList.add("active");
  }
}

document.addEventListener('keydown', function(e) {
  // Spacebar - play/pause track
  if (e.keyCode == 32) {
    e.preventDefault();
    playPauseTrack();
  }

  // Right arrow - plus 10 sec
  if (e.keyCode == 39) {
    if (current_track) {
      var time = current_track.currentTime;
      current_track.currentTime = time + 10;
    }
  }

  // Left arrow - minus 10 sec
  if (e.keyCode == 37) {
    if (current_track) {
      var time = current_track.currentTime;
      current_track.currentTime = time - 10;
    }
  }
});

document.addEventListener("DOMContentLoaded", function(event) {
  initTrack(document.getElementsByClassName('track')[0]);
});
