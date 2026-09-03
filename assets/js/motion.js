/* OAT Clinic motion layer. GSAP + ScrollTrigger choreography following the
   ui-ux-pro-max presets: subtle scroll fades (y 8-16px, power1.out), standard
   child staggers (0.08s, power2.out, capped), and a grid wave (back.out(1.4),
   grid:'auto') for card grids.

   Progressive enhancement: if GSAP fails to load, or the visitor prefers
   reduced motion, the existing CSS reveal system keeps working untouched.
   Only once GSAP is confirmed does <html> get .gsap-motion, which hands
   the reveal work over to this file. */
(function () {
  'use strict';

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!window.gsap || !window.ScrollTrigger) return;

  var gsap = window.gsap;
  gsap.registerPlugin(window.ScrollTrigger);

  // Hand reveal duty over from the CSS system before any tween runs.
  document.documentElement.classList.add('gsap-motion');

  var GRID_SELECTORS = '.grid-3, .tiles, .places, .hero-stats, .steps';

  function inHero(el) {
    return !!el.closest('.hero-3d');
  }

  /* ---------- Hero entrance: one deliberate timeline ---------- */
  var hero = document.querySelector('.hero-3d');
  if (hero) {
    var tl = gsap.timeline({ defaults: { ease: 'power2.out' } });
    var eyebrow = hero.querySelector('.hero-eyebrow');
    var h1 = hero.querySelector('h1');
    var lede = hero.querySelector('.lede');
    var btns = hero.querySelectorAll('.btn-row .btn');
    var note = hero.querySelector('.hero-note');
    var card = hero.querySelector('.hero-card');
    var stats = hero.querySelectorAll('.hero-stat');

    if (eyebrow) tl.from(eyebrow, { opacity: 0, y: 14, duration: 0.45 });
    if (h1) tl.from(h1, { opacity: 0, y: 22, duration: 0.6 }, '-=0.2');
    if (lede) tl.from(lede, { opacity: 0, y: 16, duration: 0.5 }, '-=0.35');
    if (btns.length) tl.from(btns, { opacity: 0, y: 14, duration: 0.4, stagger: 0.08 }, '-=0.3');
    if (note) tl.from(note, { opacity: 0, duration: 0.4 }, '-=0.2');
    if (card) tl.from(card, { opacity: 0, y: 26, scale: 0.965, duration: 0.7 }, 0.25);
    if (stats.length) {
      tl.from(stats, {
        opacity: 0, scale: 0.92, y: 16, duration: 0.4,
        stagger: { each: 0.06, from: 'start', grid: 'auto' },
        ease: 'back.out(1.4)'
      }, '-=0.25');
    }
  }

  /* ---------- Page-header entrance: every interior page opens with it ---------- */
  var pagehead = document.querySelector('.pagehead');
  if (pagehead) {
    var ptl = gsap.timeline({ defaults: { ease: 'power2.out' } });
    var crumbs = pagehead.querySelector('.crumbs');
    var ph1 = pagehead.querySelector('h1');
    var plede = pagehead.querySelector('.pagehead-body .lede');
    var pbtns = pagehead.querySelectorAll('.btn-row .btn');
    var pphoto = pagehead.querySelector('.pagehead-photo');
    var ppill = pagehead.querySelector('.pill');

    if (crumbs) ptl.from(crumbs, { opacity: 0, y: 10, duration: 0.35 });
    if (ppill) ptl.from(ppill, { opacity: 0, y: 10, duration: 0.35 }, '-=0.15');
    if (ph1) ptl.from(ph1, { opacity: 0, y: 26, duration: 0.6 }, '-=0.15');
    if (plede) ptl.from(plede, { opacity: 0, y: 18, duration: 0.5 }, '-=0.35');
    if (pbtns.length) ptl.from(pbtns, { opacity: 0, y: 14, duration: 0.4, stagger: 0.08 }, '-=0.3');
    if (pphoto) ptl.from(pphoto, { opacity: 0, x: 44, scale: 0.965, duration: 0.75 }, 0.2);
  }

  /* ---------- Scroll reveals for everything else ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.reveal.stagger'), function (el) {
    if (inHero(el)) return;
    var kids = Array.prototype.slice.call(el.children, 0, 8); // cap per preset
    if (!kids.length) return;
    if (el.matches(GRID_SELECTORS)) {
      gsap.from(kids, {
        opacity: 0, scale: 0.92, y: 16, duration: 0.4,
        stagger: { each: 0.06, from: 'start', grid: 'auto' },
        ease: 'back.out(1.4)',
        scrollTrigger: { trigger: el, start: 'top 85%', once: true }
      });
    } else {
      gsap.from(kids, {
        opacity: 0, y: 24, duration: 0.5, stagger: 0.08, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 85%', once: true }
      });
    }
  });

  Array.prototype.forEach.call(document.querySelectorAll('.reveal:not(.stagger)'), function (el) {
    if (inHero(el)) return;
    gsap.from(el, {
      opacity: 0, y: 20, duration: 0.5, ease: 'power2.out',
      scrollTrigger: { trigger: el, start: 'top 88%', once: true }
    });
  });

  /* ---------- Photography: slow parallax drift inside its frame ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.photo-figure, .pagehead-photo'), function (el) {
    if (inHero(el) || el.closest('.pagehead')) return;
    var img = el.querySelector('img');
    if (!img) return;
    gsap.set(img, { scale: 1.12 }); // headroom so the drift never shows edges
    gsap.fromTo(img, { yPercent: -5 }, {
      yPercent: 5, ease: 'none',
      scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: 0.6 }
    });
  });

  /* ---------- Programme rows walk in one by one ---------- */
  var rows = document.querySelectorAll('.rows .row-link');
  if (rows.length) {
    gsap.from(rows, {
      opacity: 0, x: -22, duration: 0.45, stagger: 0.09, ease: 'power2.out',
      scrollTrigger: { trigger: rows[0].parentNode, start: 'top 85%', once: true }
    });
  }

  /* ---------- Checklists tick in ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.keypoints ul'), function (ul) {
    gsap.from(ul.children, {
      opacity: 0, x: 14, duration: 0.35, stagger: 0.07, ease: 'power1.out',
      scrollTrigger: { trigger: ul, start: 'top 88%', once: true }
    });
  });

  /* ---------- Clinic cards rise where not already staggered ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.places'), function (el) {
    if (el.classList.contains('reveal')) return; // homepage handled above
    gsap.from(el.children, {
      opacity: 0, y: 18, duration: 0.4, stagger: 0.07, ease: 'power2.out',
      scrollTrigger: { trigger: el, start: 'top 85%', once: true }
    });
  });

  /* ---------- Location facts tick in ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.loc-facts'), function (el) {
    gsap.from(el.children, {
      opacity: 0, y: 10, duration: 0.35, stagger: 0.06, ease: 'power1.out',
      scrollTrigger: { trigger: el, start: 'top 92%', once: true }
    });
  });

  /* ---------- Journey dot: travels the how-it-works line ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.steps-3'), function (steps) {
    var items = steps.querySelectorAll('.step');
    if (items.length !== 3) return; // only the three-stage journey

    var dot = document.createElement('span');
    dot.className = 'journey-dot';
    dot.setAttribute('aria-hidden', 'true');
    steps.appendChild(dot);

    var tl;
    function build() {
      if (tl) tl.kill();
      // Columns on desktop, stacked on mobile; the dot follows either way.
      var horizontal = Math.abs(items[1].offsetTop - items[0].offsetTop) < 10;
      var stops = Array.prototype.map.call(items, function (st) {
        return horizontal
          ? { x: st.offsetLeft + 2, y: 0 }
          : { x: st.offsetLeft + 2, y: st.offsetTop };
      });
      tl = gsap.timeline({
        repeat: -1,
        repeatDelay: 1.2,
        scrollTrigger: {
          trigger: steps,
          start: 'top 90%',
          toggleActions: 'play pause resume pause'
        }
      });
      tl.set(dot, { x: stops[0].x, y: stops[0].y, opacity: 0 })
        .to(dot, { opacity: 1, duration: 0.4 })
        .to(dot, { x: stops[1].x, y: stops[1].y, duration: 1.4, ease: 'power1.inOut' }, '+=0.9')
        .to(dot, { x: stops[2].x, y: stops[2].y, duration: 1.4, ease: 'power1.inOut' }, '+=0.9')
        .to(dot, { opacity: 0, duration: 0.5 }, '+=0.9');
    }
    build();
    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(build, 200);
    });
  });

  /* ---------- Section heads rise gently ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.sec-head'), function (el) {
    if (inHero(el) || el.closest('.reveal')) return;
    if (el.classList.contains('reveal')) return; // already handled
    gsap.from(el, {
      opacity: 0, y: 12, duration: 0.35, ease: 'power1.out',
      scrollTrigger: { trigger: el, start: 'top 90%', once: true }
    });
  });
})();
