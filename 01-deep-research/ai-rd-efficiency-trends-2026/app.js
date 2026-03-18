/* AI × 研发效能：2026 — 交互脚本 */
(function () {
    'use strict';

    /* Tab switching */
    const btns = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.tab-panel');

    btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            btns.forEach(function (b) { b.classList.remove('active'); });
            btn.classList.add('active');
            panels.forEach(function (p) { p.classList.remove('active'); });
            var target = document.getElementById(btn.dataset.tab);
            if (target) target.classList.add('active');
        });
    });

    /* Collapsible sections */
    document.querySelectorAll('.collapsible-toggle').forEach(function (toggle) {
        toggle.addEventListener('click', function () {
            var body = toggle.nextElementSibling;
            var arrow = toggle.querySelector('.coll-arrow');
            if (body.style.maxHeight) {
                body.style.maxHeight = null;
                if (arrow) arrow.textContent = '▶';
            } else {
                body.style.maxHeight = body.scrollHeight + 'px';
                if (arrow) arrow.textContent = '▼';
            }
        });
    });

    /* Animate stat numbers on scroll */
    var observed = false;
    var observer = new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting && !observed) {
            observed = true;
            document.querySelectorAll('.stat-value[data-target]').forEach(function (el) {
                animateValue(el, el.dataset.target, el.dataset.suffix || '');
            });
        }
    }, { threshold: 0.3 });

    var statsGrid = document.querySelector('.stats-grid');
    if (statsGrid) observer.observe(statsGrid);

    function animateValue(el, target, suffix) {
        var start = 0;
        var end = parseInt(target, 10);
        var duration = 800;
        var startTime = null;
        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            var progress = Math.min((timestamp - startTime) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(eased * end) + suffix;
            if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }
})();
