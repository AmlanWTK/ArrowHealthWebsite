import re

# 1. Read aisection.html
with open('aisection.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 2. Extract style
style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
style_css = style_match.group(1) if style_match else ""

# 3. Extract the section tag
section_match = re.search(r'<section class="wellness-guidance-hero" id="wellness-guidance">(.*?)</section>', html_content, re.DOTALL)
body_html = '<section class="wellness-guidance-hero" id="wellness-guidance">' + section_match.group(1) + '</section>' if section_match else ""

# 4. Classes to prefix
classes_to_prefix = [
    "page-wrap", "wellness-guidance-hero", "grain", "orbit-line", "section-inner", 
    "copy-side", "eyebrow", "eyebrow-icon", "gold", "hero-copy", "hero-btn", "arrow", 
    "trust-row", "trust-item", "trust-icon", "visual-side", "glass-card", "meal-card", 
    "card-title", "tiny-icon", "meal-photo", "balance-pill", "report-card", "score-row", 
    "score-number", "score-label", "score-up", "mini-chart", "chart-path", "progress-note", 
    "main-guidance-card", "guidance-icon-main", "suggestion-list", "suggestion-row", 
    "suggestion-icon", "status-ring", "private-note", "side-stack", "mini-image-card", 
    "mini-image-content", "bottom-toast", "toast-icon"
]

# Sort by length descending to avoid partial matches
classes_to_prefix.sort(key=len, reverse=True)

for cls in classes_to_prefix:
    style_css = style_css.replace(f".{cls}", f".ai-guidance-{cls}")
    body_html = re.sub(rf'\b{cls}\b', f'ai-guidance-{cls}', body_html)

# Scope tags
style_css = style_css.replace("h1 {", "#ai-tools h1 {")
style_css = style_css.replace("h1 .ai-guidance-gold", "#ai-tools h1 .ai-guidance-gold")

# Fix border-radius
style_css = style_css.replace("border-radius: 0 0 44px 44px;", "border-radius: 0;")
style_css = style_css.replace("border-radius: 30px;", "border-radius: 0;")

# 5. Modify texts in body_html to reflect "all AI tools"
body_html = body_html.replace('id="ai-guidance-wellness-guidance"', 'id="ai-tools"')

# Text Replacements
replacements = {
    "AI Wellness Guidance": "Complete AI Suite",
    "Wellness guidance,": "AI Health Tools,",
    "beautifully": "all",
    "personalized.": "in one place.",
    "Arrow Health AI learns from your data to offer smart, personalized suggestions for meals, activity, hydration, and more—so you can feel your best, every day.": "Arrow Health features advanced AI tools for glucose prediction, meal analysis, medicine scanning, and natural language health chat—so you have a personal health assistant, every day.",
    "Explore Your Insights": "Explore AI Tools",
    "Wellness guidance": "Your personal health AI",
    "Give personalized suggestions based on saved health data, from bedtime snacks and hydration to activity and doctor-ready follow-ups.": "From analyzing your meals to predicting glucose spikes, identifying medicines, and answering complex health questions, our AI suite is built to empower your daily decisions.",
    "Suggest lighter bedtime snack": "Analyze any meal instantly",
    "For better sleep quality": "With the Smart Camera",
    "Recommend short post-meal walk": "Understand your medications",
    "10–15 mins supports digestion": "Medicine Scan explains effects",
    "Hydration reminder generated": "Ask health questions naturally",
    "Stay on track with your goals": "AI Health Chat is ready 24/7"
}

for old, new in replacements.items():
    body_html = body_html.replace(old, new)

# 6. Read index.html and style.css
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

# Remove old AI section if present
old_ai_start = idx_content.find('<section class="ai-section" id="ai-services">')
if old_ai_start != -1:
    old_ai_end = idx_content.find('</section>', old_ai_start) + len('</section>')
    idx_content = idx_content[:old_ai_start] + idx_content[old_ai_end:]

# 7. Insert into index.html after consult-section
insert_idx = idx_content.find('<section class="premium-section"')
if insert_idx != -1:
    idx_content = idx_content[:insert_idx] + body_html + "\n\n  " + idx_content[insert_idx:]

# 8. Add links to Navbar
nav_idx = idx_content.find('class="nav-links">')
if nav_idx != -1:
    nav_end = idx_content.find('</div>', nav_idx)
    # Check if links already exist
    if 'href="#ai-tools"' not in idx_content[nav_idx:nav_end]:
        new_links = '\n      <a href="#ai-tools">AI Tools</a>\n      <a href="#consultation">Meet Experts</a>'
        idx_content = idx_content[:nav_end] + new_links + "\n    " + idx_content[nav_end:]

# Update footer links to point to #ai-tools instead of #ai-services
idx_content = idx_content.replace('href="#ai-services"', 'href="#ai-tools"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(style_content + "\n\n/* AI Tools Section Injected */\n" + style_css)

print("Injected successfully.")
