import re

with open('feature.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css = css_match.group(1)

css = re.sub(r':root\s*\{[^}]*\}', '', css, flags=re.DOTALL)
css = re.sub(r'\*\s*\{\s*box-sizing[^}]*\}', '', css, flags=re.DOTALL)
css = re.sub(r'body\s*\{[^}]*\}', '', css, flags=re.DOTALL)

replacements = {
    '.features-section': '.feat-section',
    '.feature-card': '.feat-card',
    '.feature-icon': '.feat-icon',
    '.feature-grid': '.feat-grid',
    '.feature-intro': '.feat-intro',
    '.preview-wrap': '.feat-preview-wrap',
    '.bar {': '.feat-bar {',
    '.bar span {': '.feat-bar span {',
    '.bar.animate': '.feat-bar.animate',
    'h2 {': '#features h2 {',
    '.accent {': '#features .accent {',
    '.lead {': '#features .lead {',
    '.kicker {': '#features .kicker {',
    '.kicker-dot {': '#features .kicker-dot {',
    '.section-inner {': '#features .section-inner {',
    '.story-collage {': '#features .story-collage {',
    '.story-image {': '#features .story-image {',
    '.story-pill {': '#features .story-pill {',
    '.story-pulse {': '#features .story-pulse {',
    '.mini-proof {': '#features .mini-proof {',
    '.proof-card {': '#features .proof-card {',
    '.proof-card:hover {': '#features .proof-card:hover {',
    '.proof-card strong {': '#features .proof-card strong {',
    '.proof-card span {': '#features .proof-card span {',
    '.report-preview {': '#features .report-preview {',
    '.report-preview small {': '#features .report-preview small {',
    '.report-preview strong {': '#features .report-preview strong {',
    '.risk-meter {': '#features .risk-meter {',
    '.risk-meter span {': '#features .risk-meter span {',
    '.wide-card {': '#features .wide-card {',
    '.wide-card h3 {': '#features .wide-card h3 {',
    '.connected-line {': '#features .connected-line {',
    '.connection-row {': '#features .connection-row {',
    '.connection-icon {': '#features .connection-icon {',
    '.connection-status {': '#features .connection-status {',
    '.card-sparkline {': '#features .card-sparkline {',
    '.spark-path {': '#features .spark-path {',
    '.ambient-ring {': '#features .ambient-ring {',
    '.ambient-ring::before,': '#features .ambient-ring::before,',
    '.ambient-ring::after {': '#features .ambient-ring::after {',
    '.memory-orbit {': '#features .memory-orbit {',
    '.memory-orbit::before,': '#features .memory-orbit::before,',
    '.memory-orbit::after {': '#features .memory-orbit::after {',
    '.floating-orb {': '#features .floating-orb {',
    '.orb-1 {': '#features .orb-1 {',
    '.orb-2 {': '#features .orb-2 {',
    '.orb-3 {': '#features .orb-3 {',
}

for k, v in replacements.items():
    css = css.replace(k, v)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n/* --- Features Section --- */\n')
    f.write(css)

html_match = re.search(r'<section class="features-section" id="features">.*?</section>', content, re.DOTALL)
html = html_match.group(0)

html = html.replace('features-section', 'feat-section')
html = html.replace('feature-card', 'feat-card')
html = html.replace('feature-icon', 'feat-icon')
html = html.replace('feature-grid', 'feat-grid')
html = html.replace('feature-intro', 'feat-intro')
html = html.replace('class="bar"', 'class="feat-bar"')

html = f'<div id="features" class="feat-preview-wrap" style="width: min(1500px, calc(100% - 48px)); margin: 0 auto; padding: 24px 0 32px;">\n{html}\n</div>'

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

consult_idx = index_html.find('<section class="consult-section" id="consultation">')
index_html = index_html[:consult_idx] + html + '\n\n  ' + index_html[consult_idx:]

nav_link = '<a href="#services">Services</a>'
if nav_link in index_html:
    index_html = index_html.replace(nav_link, nav_link + '\n      <a href="#features">Features</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("done")
