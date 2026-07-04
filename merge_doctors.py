import sys
import re

# The 6 top doctors we need to insert first
top_doctors_html = """
          <!-- Dr. Indrajit Prosad -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/prof.-dr.-indrajit prasad-1.png');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Dr. Indrajit Prasad</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Dr. Farid Uddin -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/Dr. Farid Uddin.jpeg');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Mohammad Farid Uddin</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Prof. Dr. A K M Aminul Islam -->
          <div class="expert-card">
            <div class="expert-status secondary">Next slot: Tomorrow</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/Prof. Dr. A K M Aminul Islam.jpeg');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Prof. Dr. A K M Aminul Islam</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Faria Afsana -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Dr. Faria Afsana/Faria-Afsana.webp');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Dr. Faria Afsana</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Shahajada Selim -->
          <div class="expert-card">
            <div class="expert-status secondary">Next slot: Tomorrow</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Dr. Shahjada Selim/Shahjada-Selim.webp');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Dr. Shahjada Selim</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Prof Faruque Pathan -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Professor Md. Faruque Pathan/Faruq_pathan-removebg-preview_1711966760.png');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Md. Faruque Pathan</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>
"""

names_to_remove = [
    "Professor Dr. Indrajit Prasad",
    "Professor Mohammad Farid Uddin",
    "Prof. Dr. A K M Aminul Islam",
    "Dr. Faria Afsana",
    "Dr. Shahjada Selim",
    "Professor Md. Faruque Pathan"
]

# 1. Extract original doctors from index.html (git restored one)
with open(r'd:\carehub\arrow_health_website\index.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

start_str = '<div class="experts-grid">'
start_idx = orig_content.find(start_str)

if start_idx == -1:
    print("Could not find experts-grid in orig")
    sys.exit(1)

content_after_start = orig_content[start_idx + len(start_str):]
div_count = 1
i = 0
while i < len(content_after_start) and div_count > 0:
    if content_after_start[i:i+4] == '<div':
        div_count += 1
        i += 4
    elif content_after_start[i:i+6] == '</div>':
        div_count -= 1
        i += 6
    else:
        i += 1

orig_experts_html = orig_content[start_idx + len(start_str) : start_idx + len(start_str) + i - 6]

# 2. Parse out each doctor card and skip if they are in the names_to_remove
# A simple way to split cards is by '<!-- ' assuming each card has a comment, or by '<div class="expert-card">'
cards = []
current_card = ""
for line in orig_experts_html.split('\n'):
    if line.strip().startswith('<!-- ') and current_card.strip() != "":
        cards.append(current_card)
        current_card = ""
    current_card += line + "\n"
if current_card.strip() != "":
    cards.append(current_card)

filtered_cards = []
for card in cards:
    should_keep = True
    for name in names_to_remove:
        if name in card:
            should_keep = False
            break
    if should_keep and card.strip() != "":
        filtered_cards.append(card)

rest_of_doctors_html = "".join(filtered_cards)
final_experts_html = top_doctors_html + "\n" + rest_of_doctors_html

# 3. Replace the experts-grid in index_current.html
with open(r'd:\carehub\arrow_health_website\index_current.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

c_start_idx = current_html.find(start_str)
c_content_after_start = current_html[c_start_idx + len(start_str):]
div_count = 1
i = 0
while i < len(c_content_after_start) and div_count > 0:
    if c_content_after_start[i:i+4] == '<div':
        div_count += 1
        i += 4
    elif c_content_after_start[i:i+6] == '</div>':
        div_count -= 1
        i += 6
    else:
        i += 1

c_end_idx = c_start_idx + len(start_str) + i - 6

new_current_html = current_html[:c_start_idx + len(start_str)] + "\n" + final_experts_html + "\n        " + current_html[c_end_idx:]

with open(r'd:\carehub\arrow_health_website\index.html', 'w', encoding='utf-8') as f:
    f.write(new_current_html)

print("Merged correctly!")
