import sys

with open(r'd:\carehub\arrow_health_website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Desktop Nav link
target_desktop = '<a href="#premium">Plans</a>'
replacement_desktop = '<a href="#premium">Plans</a>\n      <a href="ramadan_calculator.html" style="display:flex; align-items:center; gap:6px;"><span style="font-size:16px;">🧮</span> Calculator</a>'

# Mobile Nav link
target_mobile = '<a href="#premium">Plans</a>\n    <a href="#" class="mobile-nav-cta">Join Waitlist</a>'
replacement_mobile = '<a href="#premium">Plans</a>\n    <a href="ramadan_calculator.html">🧮 Calculator</a>\n    <a href="#" class="mobile-nav-cta">Join Waitlist</a>'

new_content = content.replace(target_desktop, replacement_desktop)
new_content = new_content.replace(target_mobile, replacement_mobile)

with open(r'd:\carehub\arrow_health_website\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Calculator link to index.html navs!")
