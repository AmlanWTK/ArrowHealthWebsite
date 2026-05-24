import glob
import re

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Change View Features to point to #bento (the actual features section)
    content = content.replace(
        '<a class="footer-btn secondary" href="index.html#features">View Features</a>',
        '<a class="footer-btn secondary" href="index.html#bento">View Features</a>'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Fixed View Features footer links to #bento.')
