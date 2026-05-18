document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Dynamic Hero Section Data (Premium Muted Colors)
    const services = {
        glucose: { 
            color: '#639898', 
            title: 'Latest Glucose', 
            score: '95', 
            unit: 'mg/dL • Normal',
            insight: 'Your glucose remained stable after your 20-minute walk.'
        },
        meal: { 
            color: '#6F8B63', 
            title: 'Meal Est.', 
            score: '450', 
            unit: 'kcal • Lunch',
            insight: 'Your lunch today was perfectly balanced in macronutrients.'
        },
        heart: { 
            color: '#B75D69', 
            title: 'Heart Rate Avg', 
            score: '68', 
            unit: 'bpm • Resting',
            insight: 'Your resting heart rate dropped by 2 bpm this week.'
        },
        activity: { 
            color: '#B87942', 
            title: 'Daily Steps', 
            score: '8.4k', 
            unit: 'steps • Goal met',
            insight: 'Your sleep was better on days your activity stayed above 7,000 steps.'
        }
    };

    const toggles = document.querySelectorAll('.service-toggle');
    const heroBrandHighlight = document.getElementById('heroBrandHighlight');
    const dynamicCardTitle = document.getElementById('dynamicCardTitle');
    const dynamicCardScore = document.getElementById('dynamicCardScore');
    const dynamicCardUnit = document.getElementById('dynamicCardUnit');
    const dynamicInsightText = document.getElementById('dynamicInsightText');
    
    let currentServiceIndex = 0;
    const serviceKeys = Object.keys(services);
    let autoRotateInterval;

    function setService(serviceKey) {
        const data = services[serviceKey];
        
        // Update CSS Variable for glow
        document.documentElement.style.setProperty('--hero-active-color', data.color);
        
        // Update Toggles
        toggles.forEach(t => t.classList.remove('active'));
        document.querySelector(`[data-service="${serviceKey}"]`).classList.add('active');

        // Update Text & Colors
        heroBrandHighlight.style.color = data.color;
        dynamicCardScore.style.color = data.color;

        // Update Phone Data
        dynamicCardTitle.textContent = data.title;
        dynamicCardScore.textContent = data.score;
        dynamicCardUnit.textContent = data.unit;
        
        // Update Insight
        if(dynamicInsightText) {
            dynamicInsightText.textContent = data.insight;
        }
    }

    function rotateService() {
        currentServiceIndex = (currentServiceIndex + 1) % serviceKeys.length;
        setService(serviceKeys[currentServiceIndex]);
    }

    // Start auto rotation
    function startRotation() {
        stopRotation(); // clear if existing
        autoRotateInterval = setInterval(rotateService, 5000);
    }

    function stopRotation() {
        if (autoRotateInterval) clearInterval(autoRotateInterval);
    }

    // Manual click handling
    toggles.forEach((toggle) => {
        toggle.addEventListener('click', () => {
            const serviceKey = toggle.getAttribute('data-service');
            currentServiceIndex = serviceKeys.indexOf(serviceKey);
            setService(serviceKey);
            
            // Stop and restart rotation on manual interaction
            startRotation();
        });
    });

    // Initialize first state
    setService('glucose');
    startRotation();

    // Why Arrow Health Modal Logic
    const whyBtn = document.querySelector('.floating-why-btn');
    const whyModal = document.getElementById('whyModal');
    const closeModalBtn = document.getElementById('closeModalBtn');

    if (whyBtn && whyModal && closeModalBtn) {
        whyBtn.addEventListener('click', () => {
            whyModal.classList.add('open');
            document.body.style.overflow = 'hidden'; // prevent background scrolling
        });

        closeModalBtn.addEventListener('click', () => {
            whyModal.classList.remove('open');
            document.body.style.overflow = '';
        });
    }

    // Bi-directional Scroll Animations
    const scrollSections = document.querySelectorAll('.why-section, .why-grid');
    
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Find all targets inside this section that need animation
            const animTargets = entry.target.classList.contains('why-section') 
                ? entry.target.querySelectorAll('.why-text, .app-mockup-wrapper, .iphone-frame-wrapper')
                : entry.target.querySelectorAll('.why-stat');

            if (entry.isIntersecting) {
                animTargets.forEach((t, index) => {
                    // Slight stagger for a premium feel
                    setTimeout(() => {
                        t.classList.add('is-visible');
                    }, index * 150);
                });
            } else {
                animTargets.forEach(t => {
                    t.classList.remove('is-visible');
                    
                    // Determine if it exited from top or bottom
                    if (entry.boundingClientRect.top > window.innerHeight / 2) {
                        t.classList.add('from-bottom');
                        t.classList.remove('from-top');
                    } else {
                        t.classList.add('from-top');
                        t.classList.remove('from-bottom');
                    }
                });
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    });

    scrollSections.forEach(section => {
        const animTargets = section.classList.contains('why-section') 
            ? section.querySelectorAll('.why-text, .app-mockup-wrapper, .iphone-frame-wrapper')
            : section.querySelectorAll('.why-stat');
            
        animTargets.forEach(t => {
            t.classList.add('scroll-reveal');
            // Initial setup: assume everything below fold is from-bottom
            if (section.getBoundingClientRect().top > window.innerHeight) {
                t.classList.add('from-bottom');
            } else {
                t.classList.add('from-top');
            }
        });
        scrollObserver.observe(section);
    });
});
