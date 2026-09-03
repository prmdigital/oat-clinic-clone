/* OAT Clinic section backdrop: drift.
   A minimal 3D layer for content sections: a handful of frosted pastel
   spheres drifting at different depths over the page's own background
   (alpha canvas, no clear color). Background-tier geometry only.

   Progressive enhancement. Honors prefers-reduced-motion, pauses
   off-screen and on hidden tabs, clamps DPR. */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

(function () {
  'use strict';

  var hosts = document.querySelectorAll('[data-3d-bg]');
  if (!hosts.length) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  Array.prototype.forEach.call(hosts, function (host) {
    var renderer;
    try {
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
    } catch (e) {
      return; // section simply keeps its CSS background
    }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    renderer.domElement.setAttribute('aria-hidden', 'true');
    host.appendChild(renderer.domElement);

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
    camera.position.set(0, 0, 26);

    scene.add(new THREE.HemisphereLight(0xdceffb, 0xffffff, 1.15));
    var key = new THREE.DirectionalLight(0xffffff, 0.9);
    key.position.set(5, 8, 6);
    scene.add(key);

    // Background tier: 16 segments is plenty at these sizes and opacities.
    var geo = new THREE.SphereGeometry(1, 16, 16);
    var SPHERES = [
      { x: -17, y: 6, z: -12, r: 1.6, c: 0xbcdcf0, bob: 0.8, ph: 0.0 },
      { x: -13, y: -6.5, z: -6, r: 0.7, c: 0xfae4cd, bob: 0.6, ph: 1.7 },
      { x: 15, y: 7, z: -9, r: 1.0, c: 0xd8ebf5, bob: 0.7, ph: 3.2 },
      { x: 18, y: -5, z: -13, r: 2.1, c: 0xcfe4f2, bob: 0.9, ph: 4.5 },
      { x: 2, y: 9, z: -16, r: 1.2, c: 0xfae0c4, bob: 0.7, ph: 2.4 }
    ];
    var spheres = SPHERES.map(function (S) {
      var m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({
        color: S.c, roughness: 0.35, metalness: 0.05,
        transparent: true, opacity: 0.55
      }));
      m.position.set(S.x, S.y, S.z);
      m.scale.setScalar(S.r);
      scene.add(m);
      return { mesh: m, S: S };
    });

    function resize() {
      var w = host.clientWidth, h = host.clientHeight;
      if (!w || !h) return;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    }
    resize();
    window.addEventListener('resize', resize);

    function draw(t) {
      for (var i = 0; i < spheres.length; i++) {
        var s = spheres[i];
        s.mesh.position.y = s.S.y + Math.sin(t * 0.35 + s.S.ph) * s.S.bob;
        s.mesh.position.x = s.S.x + Math.cos(t * 0.25 + s.S.ph) * 0.6;
      }
      renderer.render(scene, camera);
    }

    var running = false, rafId = 0, t0 = performance.now();
    function frame(now) {
      rafId = requestAnimationFrame(frame);
      draw(Math.max(0, (now - t0) / 1000));
    }
    function start() {
      if (running || reduceMotion) return;
      running = true;
      t0 = performance.now() - 1;
      rafId = requestAnimationFrame(frame);
    }
    function stop() {
      running = false;
      cancelAnimationFrame(rafId);
    }

    if (reduceMotion) {
      draw(2);
    } else {
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entries) {
          entries[0].isIntersecting ? start() : stop();
        }, { threshold: 0.02 }).observe(host);
      } else {
        start();
      }
      document.addEventListener('visibilitychange', function () {
        document.hidden ? stop() : start();
      });
    }

    host.classList.add('is-ready');
  });
})();
