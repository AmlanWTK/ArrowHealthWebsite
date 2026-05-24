import glob
import re

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix Logo link
    content = re.sub(r'<a class="brand" href="[^"]+">', '<a class="brand" href="index.html">', content)
    
    # Add pathLength to paths with stroke
    def add_path_length(match):
        tag = match.group(0)
        if 'pathLength=' not in tag and 'stroke=' in tag and 'none' in tag:
            return tag.replace('<path ', '<path pathLength="100" ')
        return tag
    content = re.sub(r'<path\s+[^>]+>', add_path_length, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Fixed logo links and path lengths.')
