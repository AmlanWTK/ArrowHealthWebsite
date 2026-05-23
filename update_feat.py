import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    new_css = """    .feat-section {
      position: relative;
      overflow: hidden;
      border-radius: 0;
      padding: 96px 72px;
      background:
        linear-gradient(135deg, rgba(255, 255, 255, 0.82), rgba(248, 245, 239, 0.96)),
        url("appimages/feature_image.png") center / cover fixed;
      border: none;
      box-shadow: 0 40px 100px rgba(0,0,0,0.06);
      backdrop-filter: blur(18px);
      isolation: isolate;
    }"""
    
    text = re.sub(r'    \.feat-section \{[^}]+\}', new_css, text, flags=re.DOTALL)
    
    # Also update feature.html which uses .features-section
    new_css_html = new_css.replace('.feat-section', '.features-section')
    text = re.sub(r'    \.features-section \{[^}]+\}', new_css_html, text, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_file('style.css')
update_file('feature.html')
print("Updated successfully.")
