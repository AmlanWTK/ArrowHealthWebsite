import os

script_path = 'd:/carehub/arrow_health_website/script.js'

with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()

# Check if scrollspy already exists
if 'ScrollSpy Logic' not in script_content:
    scrollspy_code = """
    // ScrollSpy Logic for Navbar
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = Array.from(navLinks).map(link => {
        const targetId = link.getAttribute('href').substring(1);
        return document.getElementById(targetId);
    }).filter(section => section !== null);

    const spyObserver = new IntersectionObserver((entries) => {
        let activeSectionId = null;

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                activeSectionId = entry.target.id;
            }
        });

        if (activeSectionId) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').substring(1) === activeSectionId) {
                    link.classList.add('active');
                }
            });
        }
    }, {
        rootMargin: '-50% 0px -50% 0px' // Trigger when section crosses the middle of the viewport
    });

    sections.forEach(section => spyObserver.observe(section));
"""
    with open(script_path, 'a', encoding='utf-8') as f:
        f.write('\n' + scrollspy_code)
    print("ScrollSpy logic added to script.js")
else:
    print("ScrollSpy logic already exists in script.js")
