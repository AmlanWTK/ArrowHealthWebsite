import os
import glob

# Read the footer from index.html
with open('d:/carehub/arrow_health_website/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract arrow-footer
# We need the first matching arrow-footer that is not a modal footer
# Search for <footer class="arrow-footer">
start_idx = idx_content.find('<footer class="arrow-footer">')
if start_idx != -1:
    end_idx = idx_content.find('</footer>', start_idx) + len('</footer>')
    footer_html = idx_content[start_idx:end_idx]
    
    files_to_update = glob.glob('d:/carehub/arrow_health_website/*.html')
    for file in files_to_update:
        if 'index.html' in file:
            continue
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'class="arrow-footer"' not in content:
            # Insert before </body>
            body_end_idx = content.find('</body>')
            if body_end_idx != -1:
                new_content = content[:body_end_idx] + '\n  ' + footer_html + '\n' + content[body_end_idx:]
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added footer to {os.path.basename(file)}")
else:
    print("Could not find footer in index.html")
