import re

# Read activity.html to extract the close button and footer styles/HTML
with open('activity.html', 'r', encoding='utf-8') as f:
    activity_content = f.read()

# Extract close-btn CSS
close_css_match = re.search(r'/\*\s*───\s*Close Button\s*───\s*\*/.*?(?=/\*|\Z)', activity_content, re.DOTALL)
close_css = close_css_match.group(0) if close_css_match else ""

# Extract footer CSS
footer_css_match = re.search(r'/\*\s*───\s*Footer\s*───\s*\*/.*?(?=\Z|</style>)', activity_content, re.DOTALL)
footer_css = footer_css_match.group(0) if footer_css_match else ""
# Let's clean up the footer_css so it doesn't include the </style> if matched accidentally
footer_css = re.sub(r'</style>.*', '', footer_css, flags=re.DOTALL)

# Extract close-btn HTML
close_html_match = re.search(r'<a href="index\.html" class="close-btn".*?</a>', activity_content, re.DOTALL)
close_html = close_html_match.group(0) if close_html_match else ""

# Extract footer HTML
footer_html_match = re.search(r'<footer class="arrow-footer">.*?</footer>', activity_content, re.DOTALL)
footer_html = footer_html_match.group(0) if footer_html_match else ""

files_to_process = {
    'new_glucose.html': 'glucose.html',
    'newai.html': 'ai_wellness.html',
    'new_meal.html': 'meal_estimation.html'
}

for new_file, target_file in files_to_process.items():
    try:
        with open(new_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add CSS
        if '.close-btn {' not in content:
            content = content.replace('</style>', f'\n{close_css}\n</style>')
        if '.arrow-footer {' not in content:
            content = content.replace('</style>', f'\n{footer_css}\n</style>')
            
        # Add HTML
        if 'class="close-btn"' not in content:
            # Add after noise div or body
            if '<div class="noise"></div>' in content:
                content = content.replace('<div class="noise"></div>', f'<div class="noise"></div>\n\n  <!-- Animated Close Button -->\n  {close_html}')
            elif '<body>' in content:
                content = content.replace('<body>', f'<body>\n\n  <!-- Animated Close Button -->\n  {close_html}')
                
        if 'class="arrow-footer"' not in content:
            # Add before body end
            content = content.replace('</body>', f'\n  <!-- Footer -->\n  {footer_html}\n\n</body>')
            
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Successfully processed {new_file} -> {target_file}')
    except Exception as e:
        print(f'Error processing {new_file}: {e}')
