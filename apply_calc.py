import re

with open('activity.html', 'r', encoding='utf-8') as f:
    activity_content = f.read()

close_css_match = re.search(r'/\*\s*───\s*Close Button\s*───\s*\*/.*?(?=/\*|\Z)', activity_content, re.DOTALL)
close_css = close_css_match.group(0) if close_css_match else ''
footer_css_match = re.search(r'/\*\s*───\s*Footer\s*───\s*\*/.*?(?=\Z|</style>)', activity_content, re.DOTALL)
footer_css = footer_css_match.group(0) if footer_css_match else ''
footer_css = re.sub(r'</style>.*', '', footer_css, flags=re.DOTALL)

close_html_match = re.search(r'<a href="index\.html" class="close-btn".*?</a>', activity_content, re.DOTALL)
close_html = close_html_match.group(0) if close_html_match else ''
footer_html_match = re.search(r'<footer class="arrow-footer">.*?</footer>', activity_content, re.DOTALL)
footer_html = footer_html_match.group(0) if footer_html_match else ''

with open('new_calculator.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '.close-btn {' not in content:
    content = content.replace('</style>', f'\n{close_css}\n</style>')
if '.arrow-footer {' not in content:
    content = content.replace('</style>', f'\n{footer_css}\n</style>')
if 'class="close-btn"' not in content:
    if '<div class="noise"></div>' in content:
        content = content.replace('<div class="noise"></div>', f'<div class="noise"></div>\n\n  <!-- Animated Close Button -->\n  {close_html}')
    elif '<body>' in content:
        content = content.replace('<body>', f'<body>\n\n  <!-- Animated Close Button -->\n  {close_html}')
if 'class="arrow-footer"' not in content:
    content = content.replace('</body>', f'\n  <!-- Footer -->\n  {footer_html}\n\n</body>')

with open('calculators.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Processed new_calculator.html to calculators.html')
