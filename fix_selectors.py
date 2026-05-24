import glob
import re

html_files = glob.glob('*.html')
if 'index.html' in html_files:
    html_files.remove('index.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'const CARD_SELECTORS = ' in content:
        content = re.sub(
            r"const CARD_SELECTORS = '[^']+';", 
            "const CARD_SELECTORS = 'section, .data-card, .step, .insight-panel, .habit, .testimonial, .cta-card, .meal-row, .monthly-panel, .analysis-card, .safety-card, .recommend-card, .chart-label';", 
            content
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
