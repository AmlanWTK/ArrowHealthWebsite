import glob
import re

html_files = glob.glob('*.html')
if 'index.html' in html_files:
    html_files.remove('index.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove inline initScrollReveal IIFE
    content = re.sub(r'\(function\s*\(\)\s*\{\s*const CARD_SELECTORS[\s\S]*?initScrollReveal\(\);\s*\}\)\(\);', '', content)
    # Also remove any initScrollReveal function declaration just in case
    content = re.sub(r'function initScrollReveal\(\)[\s\S]*?document\.addEventListener\([^\)]+\);', '', content)
    
    # 2. Add scroll-reveal.css to head if not present
    if 'scroll-reveal.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="scroll-reveal.css">\n</head>')

    # 3. Add scroll-reveal.js to body if not present
    if 'scroll-reveal.js' not in content:
        content = content.replace('</body>', '  <script src="scroll-reveal.js"></script>\n</body>')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Processed {f}')
