(function () {
  const CARD_SELECTORS = [
    'section',
    '.data-card',
    '.step',
    '.insight-panel',
    '.habit',
    '.testimonial',
    '.cta-card',
    '.meal-row',
    '.monthly-panel',
    '.analysis-card',
    '.safety-card',
    '.recommend-card',
    '.chart-label',
    '.chart-line',
    '.donut',
    '.month-chart'
  ].join(', ');

  function initScrollReveal(selector) {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const elements = document.querySelectorAll(selector || CARD_SELECTORS);
    if (!elements.length) return;

    if (reduceMotion) {
      elements.forEach((el) => {
        el.classList.add('scroll-reveal', 'is-visible');
      });
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const el = entry.target;

          if (entry.isIntersecting) {
            const delay = Number(el.dataset.revealDelay) || 0;
            window.setTimeout(() => el.classList.add('is-visible'), delay);
          } else {
            el.classList.remove('is-visible');
            el.classList.toggle('from-bottom', entry.boundingClientRect.top > window.innerHeight * 0.45);
            el.classList.toggle('from-top', entry.boundingClientRect.top <= window.innerHeight * 0.45);
          }
        });
      },
      { threshold: 0.08, rootMargin: '0px 0px -8% 0px' }
    );

    elements.forEach((el, index) => {
      el.classList.add('scroll-reveal');
      if (!el.dataset.revealDelay) {
        el.dataset.revealDelay = String((index % 4) * 100);
      }

      const top = el.getBoundingClientRect().top;
      el.classList.add(top > window.innerHeight * 0.85 ? 'from-bottom' : 'from-top');
      observer.observe(el);
    });
  }

  function boot() {
    initScrollReveal();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  window.initScrollReveal = initScrollReveal;
})();
