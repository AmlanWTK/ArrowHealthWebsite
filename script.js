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
            insight: 'Your glucose remained stable after your 20-minute walk.',
            graphPath: 'M 0,20 C 15,18 25,23 40,15 C 55,8 70,22 85,17 L 100,16'
        },
        meal: { 
            color: '#6F8B63', 
            title: 'Meal Est.', 
            score: '450', 
            unit: 'kcal • Lunch',
            insight: 'Your lunch today was perfectly balanced in macronutrients.',
            graphPath: 'M 0,25 C 20,25 35,22 45,10 C 55,2 65,12 80,18 L 100,20'
        },
        heart: { 
            color: '#B75D69', 
            title: 'Heart Rate Avg', 
            score: '68', 
            unit: 'bpm • Resting',
            insight: 'Your resting heart rate dropped by 2 bpm this week.',
            graphPath: 'M 0,18 C 10,18 20,18 25,18 C 28,18 30,5 33,28 C 35,25 37,18 40,18 C 50,18 60,18 65,18 C 68,18 70,5 73,28 C 75,25 77,18 80,18 L 100,18'
        },
        activity: { 
            color: '#B87942', 
            title: 'Daily Steps', 
            score: '8.4k', 
            unit: 'steps • Goal met',
            insight: 'Your sleep was better on days your activity stayed above 7,000 steps.',
            graphPath: 'M 0,25 C 20,23 45,16 60,12 C 75,6 90,4 100,2'
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
        const activeToggle = document.querySelector(`[data-service="${serviceKey}"]`);
        if (activeToggle) activeToggle.classList.add('active');

        // Update Text & Colors
        if (heroBrandHighlight) heroBrandHighlight.style.color = data.color;
        if (dynamicCardScore) dynamicCardScore.style.color = data.color;

        // Update Phone Data
        if (dynamicCardTitle) dynamicCardTitle.textContent = data.title;
        if (dynamicCardScore) dynamicCardScore.textContent = data.score;
        if (dynamicCardUnit) dynamicCardUnit.textContent = data.unit;
        
        // Update Insight
        if(dynamicInsightText) {
            dynamicInsightText.textContent = data.insight;
        }

        // Update Graph Path and Trigger Animation
        const linePath = document.querySelector('.graph-line-path');
        const fillPath = document.querySelector('.graph-fill-path');
        if (linePath && fillPath) {
            // Momentarily disable transitions to reset the stroke dashoffset instantly
            linePath.style.transition = 'none';
            fillPath.style.transition = 'none';
            
            // Reset stroke dashoffset (out of view)
            linePath.style.strokeDashoffset = '220';
            fillPath.style.opacity = '0';
            
            // Force reflow
            linePath.getBoundingClientRect();
            
            // Set new paths
            linePath.setAttribute('d', data.graphPath);
            fillPath.setAttribute('d', data.graphPath + ' L 100,30 L 0,30 Z');
            
            // Re-apply transitions
            linePath.style.transition = 'stroke-dashoffset 0.8s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.5s ease, d 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
            fillPath.style.transition = 'opacity 0.8s ease, fill 0.5s ease, d 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
            
            // Animate to fully drawn and faded in
            linePath.style.strokeDashoffset = '0';
            fillPath.style.opacity = '1';
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

    // Coded Glucose Today Interactive Chart Animation
    const interactiveScreen = document.querySelector('.glucose-app-screen');
    const interactiveLinePath = document.querySelector('.interactive-line-path');
    const interactiveFillPath = document.querySelector('.interactive-fill-path');
    const scanningGroup = document.querySelector('.scanning-group');
    const liveGlucoseVal = document.getElementById('liveGlucoseVal');
    const liveGlucoseStatus = document.getElementById('liveGlucoseStatus');
    const liveGlucoseTime = document.getElementById('liveGlucoseTime');
    const liveGlucosePeriod = document.getElementById('liveGlucosePeriod');
    const liveChartTooltip = document.getElementById('liveChartTooltip');
    const tooltipTime = liveChartTooltip ? liveChartTooltip.querySelector('.tooltip-time') : null;
    const tooltipVal = liveChartTooltip ? liveChartTooltip.querySelector('.tooltip-val') : null;

    if (interactiveScreen && interactiveLinePath && interactiveFillPath && scanningGroup) {
        // Initialize fill path
        const dAttr = interactiveLinePath.getAttribute('d');
        interactiveFillPath.setAttribute('d', dAttr + ' L 300,120 L 0,120 Z');

        let animationFrameId = null;
        let progress = 0;
        const totalLength = interactiveLinePath.getTotalLength();
        
        // Timeline array for realistic period/time mappings
        const timeline = [
            { xPct: 0.0, time: '10:45 AM', period: 'Before Breakfast' },
            { xPct: 0.15, time: '11:30 AM', period: 'After Breakfast' },
            { xPct: 0.35, time: '1:15 PM', period: 'Before Lunch' },
            { xPct: 0.55, time: '2:45 PM', period: 'After Lunch' },
            { xPct: 0.75, time: '7:30 PM', period: 'Before Dinner' },
            { xPct: 0.9, time: '9:23 PM', period: 'After Dinner' },
            { xPct: 1.0, time: '11:45 PM', period: 'Bedtime' }
        ];

        function getTimelineData(x) {
            const xPct = x / 300;
            for (let i = 0; i < timeline.length - 1; i++) {
                const current = timeline[i];
                const next = timeline[i+1];
                if (xPct >= current.xPct && xPct <= next.xPct) {
                    const distCurrent = xPct - current.xPct;
                    const distNext = next.xPct - xPct;
                    const closest = distCurrent < distNext ? current : next;
                    return closest;
                }
            }
            return timeline[timeline.length - 1];
        }

        function updateScanner() {
            progress += 0.0012; // slow sweeping speed
            if (progress > 1) {
                progress = 0;
            }

            const point = interactiveLinePath.getPointAtLength(progress * totalLength);
            
            // 1. Position scanning dot
            scanningGroup.setAttribute('transform', `translate(${point.x}, ${point.y})`);
            
            // 2. Position Tooltip
            const pctX = (point.x / 300) * 100;
            const pctY = (point.y / 120) * 100;
            if (liveChartTooltip) {
                liveChartTooltip.style.left = `${pctX}%`;
                liveChartTooltip.style.top = `${pctY}%`;
            }

            // 3. Map point.y to Glucose reading (viewBox Y=20 maps 10.0 and Y=100 maps 3.0)
            let val = 10.0 - ((point.y - 20) / 80) * 7.0;
            val = Math.max(2.5, Math.min(11.5, val)); // Clamp between safe biological bounds

            // 4. Update large value text
            if (liveGlucoseVal) {
                liveGlucoseVal.textContent = val.toFixed(1);
            }

            // 5. Update status pill
            if (liveGlucoseStatus) {
                if (val > 7.8) {
                    liveGlucoseStatus.textContent = 'High';
                    liveGlucoseStatus.className = 'status-pill red';
                } else if (val < 3.9) {
                    liveGlucoseStatus.textContent = 'Low';
                    liveGlucoseStatus.className = 'status-pill yellow';
                } else {
                    liveGlucoseStatus.textContent = 'Normal';
                    liveGlucoseStatus.className = 'status-pill green';
                }
            }

            // 6. Update period and time text from timeline
            const tData = getTimelineData(point.x);
            if (liveGlucoseTime) liveGlucoseTime.textContent = tData.time;
            if (liveGlucosePeriod) liveGlucosePeriod.textContent = tData.period;
            
            // 7. Update tooltip content
            if (tooltipTime) tooltipTime.textContent = tData.time;
            if (tooltipVal) tooltipVal.textContent = `${val.toFixed(1)} mmol/L`;

            animationFrameId = requestAnimationFrame(updateScanner);
        }

        // Setup Intersection Observer to animate only when visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (!animationFrameId) {
                        animationFrameId = requestAnimationFrame(updateScanner);
                    }
                } else {
                    if (animationFrameId) {
                        cancelAnimationFrame(animationFrameId);
                        animationFrameId = null;
                    }
                }
            });
        }, { threshold: 0.1 });

        observer.observe(interactiveScreen);
    }
});
