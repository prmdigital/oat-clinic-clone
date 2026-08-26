/* OAT Clinic site behaviour. No dependencies. Progressive enhancement only:
   every page remains usable with this file blocked. */
(function () {
  'use strict';

  var doc = document;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Mobile drawer ---------- */
  var burger = doc.querySelector('.burger');
  var drawer = doc.getElementById('drawer');

  var FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea';

  function setDrawer(open) {
    if (!burger || !drawer) return;
    burger.setAttribute('aria-expanded', String(open));
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    doc.body.classList.toggle('no-scroll', open);
    if (open) {
      // focus() is a no-op while the element is still visibility:hidden.
      // Reading a layout property forces the style change to apply now, so the
      // focus call stays inside the user gesture that opened the drawer.
      void drawer.offsetHeight;
      var first = drawer.querySelector(FOCUSABLE);
      if (first) first.focus();
    } else {
      burger.focus();
    }
  }

  // Keep Tab inside the drawer while it is open, so keyboard users do not
  // wander into the page hidden behind it.
  function trapFocus(e) {
    if (e.key !== 'Tab' || !drawer.classList.contains('is-open')) return;
    var items = drawer.querySelectorAll(FOCUSABLE);
    if (!items.length) return;
    var first = items[0];
    var last = items[items.length - 1];
    if (e.shiftKey && doc.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && doc.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  if (burger && drawer) {
    burger.addEventListener('click', function () {
      setDrawer(burger.getAttribute('aria-expanded') !== 'true');
    });
    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a') || e.target.closest('[data-close]')) setDrawer(false);
    });
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) setDrawer(false);
      trapFocus(e);
    });
    // A resize past the breakpoint should not leave the drawer stranded open.
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1024 && drawer.classList.contains('is-open')) setDrawer(false);
    });
  }

  /* ---------- Desktop dropdown ---------- */
  Array.prototype.forEach.call(doc.querySelectorAll('.nav-item[data-dropdown]'), function (item) {
    var trigger = item.querySelector('.nav-link');
    var panel = item.querySelector('.nav-panel');
    if (!trigger || !panel) return;
    var closeTimer;

    function open() {
      window.clearTimeout(closeTimer);
      item.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
    }
    function close(delay) {
      window.clearTimeout(closeTimer);
      closeTimer = window.setTimeout(function () {
        item.classList.remove('is-open');
        trigger.setAttribute('aria-expanded', 'false');
      }, delay || 0);
    }

    item.addEventListener('mouseenter', open);
    item.addEventListener('mouseleave', function () { close(140); });
    item.addEventListener('focusin', open);
    item.addEventListener('focusout', function (e) {
      if (!item.contains(e.relatedTarget)) close(0);
    });
    trigger.addEventListener('click', function (e) {
      // The trigger also links to the index page, so only intercept the first
      // activation, which is what a keyboard or touch user needs to see it.
      if (!item.classList.contains('is-open')) { e.preventDefault(); open(); }
    });
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && item.classList.contains('is-open')) { close(0); trigger.focus(); }
    });
  });

  /* ---------- Scroll driven chrome ---------- */
  var masthead = doc.querySelector('.masthead');
  var callbar = doc.querySelector('.callbar');
  var hero = doc.querySelector('.hero');
  if (masthead || callbar) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        var y = window.scrollY;
        if (masthead) masthead.classList.toggle('is-stuck', y > 8);
        // The hero already shows both actions, so the sticky bar would just
        // repeat them. Bring it in once the hero has scrolled away.
        if (callbar) {
          var trigger = hero ? hero.offsetHeight * 0.62 : 320;
          callbar.classList.toggle('is-visible', y > trigger);
        }
        ticking = false;
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Accordion: one FAQ open at a time ---------- */
  Array.prototype.forEach.call(doc.querySelectorAll('.faq-list'), function (list) {
    var items = list.querySelectorAll('details.faq-item');
    Array.prototype.forEach.call(items, function (item) {
      item.addEventListener('toggle', function () {
        if (!item.open) return;
        Array.prototype.forEach.call(items, function (other) {
          if (other !== item) other.open = false;
        });
      });
    });
  });

  /* ---------- Scroll reveal ---------- */
  var revealables = doc.querySelectorAll('.reveal');
  if (revealables.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(revealables, function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
    }
  }

  /* ---------- Callback form ---------- */
  var form = doc.getElementById('callback-form');
  if (form) {
    var status = doc.getElementById('form-status');

    var digits = function (v) { return (v || '').replace(/[^0-9]/g, ''); };

    var rules = {
      name: function (v) {
        return v.trim().length >= 2 ? '' : 'Please enter a name we can use when we call.';
      },
      phone: function (v) {
        var d = digits(v);
        if (d.length === 11 && d.charAt(0) === '1') d = d.slice(1);
        return d.length === 10 ? '' : 'Please enter a 10 digit phone number, for example 604 555 0123.';
      },
      consent: function (v, field) {
        var box = field.querySelector('input[type="checkbox"]');
        return box && box.checked ? '' : 'Please confirm it is safe for us to call this number.';
      }
    };

    function validateField(field) {
      var input = field.querySelector('input, select, textarea');
      if (!input) return true;
      var rule = rules[input.getAttribute('data-rule')];
      if (!rule) return true;
      var message = rule(input.value, field);
      field.classList.toggle('is-invalid', Boolean(message));
      var err = field.querySelector('.err');
      if (err) err.textContent = message;
      input.setAttribute('aria-invalid', message ? 'true' : 'false');
      return !message;
    }

    Array.prototype.forEach.call(form.querySelectorAll('.field'), function (field) {
      var input = field.querySelector('input, select, textarea');
      if (!input || !input.getAttribute('data-rule')) return;
      input.addEventListener('blur', function () { validateField(field); });
      input.addEventListener('input', function () {
        if (field.classList.contains('is-invalid')) validateField(field);
      });
    });

    // Format the phone number as it is typed, but leave the value alone when
    // the visitor is editing mid string so the caret does not jump.
    var phone = form.querySelector('input[data-rule="phone"]');
    if (phone) {
      phone.addEventListener('input', function () {
        if (phone.selectionStart !== phone.value.length) return;
        var d = digits(phone.value).slice(0, 10);
        var out = d;
        if (d.length > 6) out = d.slice(0, 3) + ' ' + d.slice(3, 6) + ' ' + d.slice(6);
        else if (d.length > 3) out = d.slice(0, 3) + ' ' + d.slice(3);
        phone.value = out;
      });
    }

    function showStatus(kind, message) {
      if (!status) return;
      status.className = 'form-status is-visible ' + kind;
      status.textContent = message;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fields = form.querySelectorAll('.field');
      var firstBad = null;
      Array.prototype.forEach.call(fields, function (field) {
        if (!validateField(field) && !firstBad) firstBad = field;
      });
      if (firstBad) {
        var bad = firstBad.querySelector('input, select, textarea');
        if (bad) bad.focus();
        showStatus('bad', 'Please check the highlighted fields and try again.');
        return;
      }

      // No endpoint is wired yet. Until one is, fail toward the phone number
      // rather than silently pretending the request was received.
      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) {
        showStatus('bad', 'Online requests are not connected yet. Please call 604 670 6580 and we will help you right away.');
        return;
      }

      var button = form.querySelector('button[type="submit"]');
      if (button) { button.disabled = true; button.textContent = 'Sending'; }

      var payload = {};
      new FormData(form).forEach(function (value, key) { payload[key] = value; });

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (res) {
        if (!res.ok) throw new Error('Request failed');
        form.reset();
        showStatus('ok', 'Thank you. Our team will call you back the same business day.');
      })['catch'](function () {
        showStatus('bad', 'Something went wrong on our end. Please call 604 670 6580 so we can help you now.');
      })['finally'](function () {
        if (button) { button.disabled = false; button.textContent = 'Request a callback'; }
      });
    });
  }

  /* ---------- Current year ---------- */
  Array.prototype.forEach.call(doc.querySelectorAll('[data-year]'), function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
