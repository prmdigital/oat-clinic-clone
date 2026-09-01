/* OAT Clinic — ambient canvas layer.
   The subpage companion to the homepage's WebGL scene: soft glowing motes
   drifting over the dark brand surfaces, with a faint dotted route echoing
   the five-clinic path. Plain 2D canvas, no dependencies, a fraction of the
   cost of WebGL — cheap enough to run on every page header.

   Progressive enhancement: pages are complete without it. Honors
   prefers-reduced-motion (draws one static frame), pauses off-screen. */
(function () {
  'use strict';

  var hosts = document.querySelectorAll('[data-ambient]');
  if (!hosts.length) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  Array.prototype.forEach.call(hosts, function (host) {
    // Two palettes: bright glows for dark surfaces, deeper inks washed far
    // back for the light "morning mist" headers.
    var light = host.getAttribute('data-ambient') === 'light';
    var ROUTE = light ? '1,95,156' : '143,212,255';
    var NODE_COOL = light ? '1,95,156' : '143,212,255';
    var NODE_WARM = '244,127,32';
    var MOTE_COOL = light ? '1,95,156' : '191,227,255';
    var MOTE_WARM = light ? '224,116,15' : '255,176,103';
    var ROUTE_ALPHA = light ? 0.18 : 0.30;
    var NODE_ALPHA = light ? 0.35 : 0.55;
    var MOTE_ALPHA = light ? 0.10 : 0.22;

    var canvas = document.createElement('canvas');
    canvas.setAttribute('aria-hidden', 'true');
    host.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    var w = 0, h = 0;
    var motes = [];
    var COUNT = 34;

    function resize() {
      var r = host.getBoundingClientRect();
      w = Math.max(1, r.width);
      h = Math.max(1, r.height);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      canvas.style.width = w + 'px';
      canvas.style.height = h + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function seed() {
      motes = [];
      for (var i = 0; i < COUNT; i++) {
        var warm = Math.random() < 0.12; // an occasional brand-orange spark
        motes.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 2.2 + 0.8,
          vx: (Math.random() - 0.5) * 0.12,
          vy: -(Math.random() * 0.1 + 0.03),
          p: Math.random() * Math.PI * 2,
          warm: warm
        });
      }
    }

    function draw(t) {
      ctx.clearRect(0, 0, w, h);

      // The route: a faint dotted arc across the header, five brighter nodes.
      var y0 = h * 0.72;
      ctx.save();
      ctx.globalAlpha = ROUTE_ALPHA;
      ctx.strokeStyle = 'rgb(' + ROUTE + ')';
      ctx.lineWidth = 1.4;
      ctx.setLineDash([2, 11]);
      ctx.beginPath();
      for (var x = 0; x <= w; x += 8) {
        var y = y0 + Math.sin(x / w * Math.PI * 2 + 1) * h * 0.08;
        x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);
      for (var n = 0; n < 5; n++) {
        var nx = w * (0.08 + n * 0.21);
        var ny = y0 + Math.sin(nx / w * Math.PI * 2 + 1) * h * 0.08;
        var pulse = reduceMotion ? 0.5 : (Math.sin(t / 700 + n * 1.3) + 1) / 2;
        var g = ctx.createRadialGradient(nx, ny, 0, nx, ny, 9 + pulse * 5);
        var col = n === 0 ? NODE_WARM : NODE_COOL;
        g.addColorStop(0, 'rgba(' + col + ',.9)');
        g.addColorStop(1, 'rgba(' + col + ',0)');
        ctx.globalAlpha = NODE_ALPHA + pulse * 0.3;
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(nx, ny, 9 + pulse * 5, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();

      // Drifting motes.
      for (var i = 0; i < motes.length; i++) {
        var m = motes[i];
        if (!reduceMotion) {
          m.x += m.vx; m.y += m.vy;
          if (m.y < -6) { m.y = h + 6; m.x = Math.random() * w; }
          if (m.x < -6) m.x = w + 6;
          if (m.x > w + 6) m.x = -6;
        }
        var a = MOTE_ALPHA + ((Math.sin(t / 900 + m.p) + 1) / 2) * (MOTE_ALPHA + 0.08);
        var mg = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, m.r * 3);
        var mc = m.warm ? MOTE_WARM : MOTE_COOL;
        mg.addColorStop(0, 'rgba(' + mc + ',' + a + ')');
        mg.addColorStop(1, 'rgba(' + mc + ',0)');
        ctx.fillStyle = mg;
        ctx.beginPath();
        ctx.arc(m.x, m.y, m.r * 3, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    var running = false, rafId = 0;
    function loop(t) {
      rafId = requestAnimationFrame(loop);
      draw(t);
    }
    function start() {
      if (running || reduceMotion) return;
      running = true;
      rafId = requestAnimationFrame(loop);
    }
    function stop() {
      running = false;
      cancelAnimationFrame(rafId);
    }

    resize();
    seed();
    window.addEventListener('resize', function () { resize(); seed(); draw(0); });

    if (reduceMotion) {
      draw(0);
    } else if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries[0].isIntersecting ? start() : stop();
      }, { threshold: 0.02 }).observe(host);
      document.addEventListener('visibilitychange', function () {
        document.hidden ? stop() : start();
      });
    } else {
      start();
    }

    host.classList.add('is-ready');
  });
})();
