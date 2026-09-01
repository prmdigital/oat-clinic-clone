/* OAT Clinic hero scene: the ribbon.
   A wide translucent silk ribbon flows diagonally through the hero in true
   3D, lit softly, its colour graded from brand blue into dawn peach. A few
   frosted glass spheres drift at different depths for parallax. The mood
   stays calm; the dimensionality is unmistakable.

   Progressive enhancement only. If WebGL, the CDN, or JS is unavailable the
   hero keeps its CSS gradient and content. Honors prefers-reduced-motion,
   pauses off-screen and on hidden tabs, clamps DPR for mobile GPUs. */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

(function () {
  'use strict';

  var host = document.querySelector('[data-hero-3d]');
  if (!host) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
  } catch (e) {
    return; // no WebGL, the CSS fallback stays
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.domElement.setAttribute('aria-hidden', 'true');
  host.appendChild(renderer.domElement);

  var scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0xfdfcf9, 30, 78);

  var camera = new THREE.PerspectiveCamera(42, 1, 0.1, 200);
  camera.position.set(0, 0, 30);
  camera.lookAt(0, 0, 0);

  /* ---------- Soft studio light ---------- */
  scene.add(new THREE.HemisphereLight(0xdceffb, 0xffffff, 1.1));
  var key = new THREE.DirectionalLight(0xffffff, 1.2);
  key.position.set(6, 9, 7);
  scene.add(key);
  var warm = new THREE.DirectionalLight(0xffe3c4, 0.35);
  warm.position.set(-7, -3, 5);
  scene.add(warm);

  /* ---------- The ribbon: silk in slow motion ---------- */
  var SEG_X = 180, SEG_Y = 10;
  var ribbonGeo = new THREE.PlaneGeometry(72, 6.5, SEG_X, SEG_Y);
  var base = ribbonGeo.attributes.position.array.slice();

  // Colour grades along the length: blue, into mist, into dawn peach.
  var cA = new THREE.Color(0x8fc1e3);
  var cB = new THREE.Color(0xe8f2f8);
  var cC = new THREE.Color(0xf6c99a);
  var colors = new Float32Array(ribbonGeo.attributes.position.count * 3);
  var tmp = new THREE.Color();
  for (var i = 0; i < ribbonGeo.attributes.position.count; i++) {
    var u = (base[i * 3] + 36) / 72;
    if (u < 0.55) tmp.copy(cA).lerp(cB, u / 0.55);
    else tmp.copy(cB).lerp(cC, (u - 0.55) / 0.45);
    colors[i * 3] = tmp.r; colors[i * 3 + 1] = tmp.g; colors[i * 3 + 2] = tmp.b;
  }
  ribbonGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  var ribbon = new THREE.Mesh(ribbonGeo, new THREE.MeshPhongMaterial({
    vertexColors: true,
    transparent: true,
    opacity: 0.62,
    side: THREE.DoubleSide,
    shininess: 90,
    specular: new THREE.Color(0xffffff),
    depthWrite: false
  }));
  ribbon.position.set(2, -3.4, -7);
  ribbon.rotation.set(-0.38, 0.08, -0.16);
  scene.add(ribbon);

  function deformRibbon(t) {
    var pos = ribbonGeo.attributes.position.array;
    for (var i = 0; i < ribbonGeo.attributes.position.count; i++) {
      var x = base[i * 3], y = base[i * 3 + 1];
      pos[i * 3 + 2] =
        Math.sin(x * 0.16 + t * 0.45) * 1.7 +
        Math.sin(x * 0.07 - t * 0.28) * 1.1 +
        Math.cos(y * 0.7 + t * 0.5) * 0.35;
      pos[i * 3 + 1] = y + Math.sin(x * 0.05 + t * 0.2) * 0.8;
    }
    ribbonGeo.attributes.position.needsUpdate = true;
    ribbonGeo.computeVertexNormals();
  }

  /* ---------- Frosted spheres at different depths ---------- */
  var SPHERES = [
    { x: -20, y: 9.0, z: -15, r: 1.4, c: 0xbcdcf0, bob: 0.9, ph: 0.0 },
    { x: -21, y: -6.5, z: -8, r: 0.8, c: 0xfae4cd, bob: 0.7, ph: 1.6 },
    { x: 17, y: 8.2, z: -11, r: 1.0, c: 0xfae0c4, bob: 0.8, ph: 3.1 },
    { x: 19, y: -4.0, z: -4, r: 0.65, c: 0xa9cfe8, bob: 0.6, ph: 4.4 },
    { x: 8, y: -7.5, z: -12, r: 1.9, c: 0xd8ebf5, bob: 1.0, ph: 5.2 },
    { x: -6, y: 8.4, z: -18, r: 1.2, c: 0xcfe4f2, bob: 0.8, ph: 2.3 }
  ];
  var sphereGeo = new THREE.SphereGeometry(1, 40, 40); // hero objects: smooth
  var spheres = SPHERES.map(function (S) {
    var m = new THREE.Mesh(sphereGeo, new THREE.MeshStandardMaterial({
      color: S.c, roughness: 0.3, metalness: 0.05,
      transparent: true, opacity: 0.9
    }));
    m.position.set(S.x, S.y, S.z);
    m.scale.setScalar(S.r);
    scene.add(m);
    return { mesh: m, S: S };
  });

  /* ---------- Soft parallax, heavily damped ---------- */
  var targetX = 0, targetY = 0, curX = 0, curY = 0;
  if (!reduceMotion) {
    window.addEventListener('pointermove', function (e) {
      var r = host.getBoundingClientRect();
      if (r.bottom < 0) return;
      targetX = (e.clientX / window.innerWidth - 0.5) * 2;
      targetY = (e.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });
  }

  function resize() {
    var w = host.clientWidth, h = host.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  function drawScene(t) {
    deformRibbon(t);
    for (var i = 0; i < spheres.length; i++) {
      var s = spheres[i];
      s.mesh.position.y = s.S.y + Math.sin(t * 0.4 + s.S.ph) * s.S.bob;
      s.mesh.position.x = s.S.x + Math.cos(t * 0.3 + s.S.ph) * 0.5;
    }
    renderer.render(scene, camera);
  }

  var running = false, rafId = 0, t0 = performance.now();

  function frame(now) {
    rafId = requestAnimationFrame(frame);
    var t = Math.max(0, (now - t0) / 1000);
    curX += (targetX - curX) * 0.025;
    curY += (targetY - curY) * 0.025;
    camera.position.x = curX * 1.6;
    camera.position.y = -curY * 0.8;
    camera.lookAt(0, 0, 0);
    drawScene(t);
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
    drawScene(2.2);
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
})();
