import re

# 1. Read feature.html
with open('feature.html', 'r', encoding='utf-8') as f:
    feature_content = f.read()

# 2. Extract CSS
css_match = re.search(r'<style>(.*?)</style>', feature_content, re.DOTALL)
if css_match:
    css = css_match.group(1)
    # Remove :root, *, body from css to avoid conflicts
    css = re.sub(r':root\s*\{[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\*\s*\{\s*box-sizing[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'body\s*\{[^}]*\}', '', css, flags=re.DOTALL)
    
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n/* --- Features Section --- */\n')
        f.write(css)

# 3. Extract HTML Section
html_match = re.search(r'<section class="features-section" id="features">.*?</section>', feature_content, re.DOTALL)
if html_match:
    feature_html = html_match.group(0)
    
    # 4. Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 5. Insert feature HTML before consult-section
    consult_idx = index_content.find('<section class="consult-section" id="consultation">')
    if consult_idx != -1:
        # Wrap it in a div or something if needed, but <section> is fine. We might need some spacing.
        wrapper = f'\n  <!-- Features Section -->\n  <div style="width: min(1500px, calc(100% - 48px)); margin: 0 auto; padding: 72px 0 90px;">\n    {feature_html}\n  </div>\n\n  '
        index_content = index_content[:consult_idx] + wrapper + index_content[consult_idx:]
    
    # 6. Insert link in navbar
    # Find <a href="#services">Services</a>
    nav_link = '<a href="#services">Services</a>'
    if nav_link in index_content:
        index_content = index_content.replace(nav_link, nav_link + '\n      <a href="#features">Features</a>')
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print('Successfully injected features section into index.html and style.css')
else:
    print('Could not find features section in feature.html')
