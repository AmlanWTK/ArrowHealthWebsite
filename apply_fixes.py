import re
import os

files = ['glucose.html', 'meal_estimation.html', 'medicine.html', 'ai_wellness.html', 'calculators.html', 'activity.html']

css_to_add = """
    .btn-primary:hover {
      background: linear-gradient(135deg, var(--hero-active-color), var(--brand-primary)) !important;
      color: #fff !important;
    }
    .nav-links a { transition: color 0.3s; }
    .nav-links a.active {
      color: var(--brand-primary) !important;
      font-weight: 800 !important;
    }
"""

js_to_add = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = Array.from(navLinks).map(link => {
        const href = link.getAttribute('href');
        if(!href || !href.startsWith('#') || href === '#') return null;
        const targetId = href.substring(1);
        return document.getElementById(targetId);
    }).filter(section => section !== null);

    const spyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + entry.target.id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, { rootMargin: '-20% 0px -80% 0px' }); // triggers when section hits top 20%

    sections.forEach(section => spyObserver.observe(section));
});
</script>
"""

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add CSS
    if '.btn-primary:hover' not in content:
        content = content.replace('</style>', css_to_add + '\n  </style>')
    
    # 2. Add JS
    if 'spyObserver' not in content:
        content = content.replace('</body>', js_to_add + '\n</body>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
