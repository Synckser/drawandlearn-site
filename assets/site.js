// Draw & Learn site: video controls + scroll reveal. No tracking, no external code.
(function () {
  // Click-to-play videos with sound. Only one plays at a time.
  var players = document.querySelectorAll('[data-player]');
  function stopOthers(except) {
    players.forEach(function (p) {
      if (p !== except) {
        var v = p.querySelector('video');
        if (!v.paused) { v.pause(); }
        p.classList.remove('playing');
      }
    });
  }
  players.forEach(function (p) {
    var v = p.querySelector('video');
    var btn = p.querySelector('.play');
    function toggle() {
      if (v.paused) {
        stopOthers(p);
        v.muted = false;
        v.play().then(function () { p.classList.add('playing'); }).catch(function () {});
      } else {
        v.pause(); p.classList.remove('playing');
      }
    }
    if (btn) btn.addEventListener('click', toggle);
    v.addEventListener('click', toggle);
    v.addEventListener('ended', function () { p.classList.remove('playing'); v.currentTime = 0; });
  });

  // Hero: muted autoplay loop; button unmutes and restarts.
  var hero = document.querySelector('[data-hero]');
  if (hero) {
    var hv = hero.querySelector('video');
    var hb = hero.querySelector('.sound');
    hb.addEventListener('click', function () {
      if (hv.muted) {
        stopOthers(null);
        hv.muted = false; hv.currentTime = 0; hv.play();
        hb.textContent = '🔇 Mute'; hb.classList.add('on');
      } else {
        hv.muted = true; hb.textContent = '🔊 Hear Bob'; hb.classList.remove('on');
      }
    });
    hv.addEventListener('click', function () { hb.click(); });
  }

  // Scroll reveal.
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -10% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }
})();
